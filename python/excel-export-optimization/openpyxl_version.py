import time
import io
import zipfile
import openpyxl
from django.http import HttpResponse

def large_excel_download(request):
    CHUNK_SIZE = 100_000  # rows per file

    try:
        start_time = time.time()
        print("Excel export started")

        # Dummy column headers
        columns = [
            "ColumnA", "ColumnB", "ColumnC", "ColumnD", "ColumnE",
            "ColumnF", "ColumnG", "ColumnH", "ColumnI", "ColumnJ"
        ]

        # Dummy data iterator (replace with your actual queryset or data source)
        def dummy_data_generator():
            for i in range(1_025_731):
                yield [f"Value{i}_{col}" for col in range(len(columns))]

        data_iterator = dummy_data_generator()

        zip_buffer = io.BytesIO()
        zip_file = zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED)

        row_count = 0
        file_index = 1

        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Data"
        ws.append(columns)

        for row in data_iterator:
            ws.append(row)
            row_count += 1

            if row_count >= CHUNK_SIZE:
                temp_buffer = io.BytesIO()
                wb.save(temp_buffer)
                zip_file.writestr(f"export_data_{file_index:02d}.xlsx", temp_buffer.getvalue())
                print(f"Saved chunk {file_index}")
                file_index += 1
                row_count = 0
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.title = "Data"
                ws.append(columns)

        # 마지막 파일 저장
        if row_count > 0:
            temp_buffer = io.BytesIO()
            wb.save(temp_buffer)
            zip_file.writestr(f"export_data_{file_index:02d}.xlsx", temp_buffer.getvalue())
            print(f"Saved final chunk {file_index}")

        zip_file.close()
        zip_buffer.seek(0)

        response = HttpResponse(zip_buffer, content_type="application/zip")
        response["Content-Disposition"] = "attachment; filename*=UTF-8''export_data_all.zip"

        print(f"Export completed in {time.time() - start_time:.2f} seconds")
        return response

    except Exception as e:
        print(f"[ERROR] Excel export failed: {e}")
        return HttpResponse("Internal Server Error", status=500)