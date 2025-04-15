import time
import io
import zipfile
import xlsxwriter
from django.http import HttpResponse

def export_large_data_as_excel(request):
    CHUNK_SIZE = 100_000

    try:
        start_time = time.time()
        print("xlsxwriter export started")

        # 예시 컬럼명
        columns = [
            "ColumnA", "ColumnB", "ColumnC", "ColumnD", "ColumnE",
            "ColumnF", "ColumnG", "ColumnH", "ColumnI", "ColumnJ"
        ]

        # 더미 데이터 생성 (실제 데이터로 대체)
        def dummy_data_generator():
            for i in range(1_025_731):
                yield [f"Value{i}_{col}" for col in range(len(columns))]

        data_iterator = dummy_data_generator()
        zip_buffer = io.BytesIO()
        zip_file = zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED)

        row_count = 0
        file_index = 1
        current_buffer = io.BytesIO()
        workbook = xlsxwriter.Workbook(current_buffer, {'in_memory': True})
        worksheet = workbook.add_worksheet("Data")

        for col_num, header in enumerate(columns):
            worksheet.write(0, col_num, header)

        current_row = 1

        for row in data_iterator:
            for col_num, cell in enumerate(row):
                worksheet.write(current_row, col_num, cell)
            current_row += 1
            row_count += 1

            if row_count >= CHUNK_SIZE:
                workbook.close()
                zip_file.writestr(f"export_excel_part_{file_index:02d}.xlsx", current_buffer.getvalue())
                print(f"create excel_{file_index:02d}")
                file_index += 1
                row_count = 0
                current_row = 1
                current_buffer = io.BytesIO()
                workbook = xlsxwriter.Workbook(current_buffer, {'in_memory': True})
                worksheet = workbook.add_worksheet("Data")
                for col_num, header in enumerate(columns):
                    worksheet.write(0, col_num, header)

        if row_count > 0:
            workbook.close()
            suffix = f"_{file_index:02d}" if file_index > 1 else ""
            zip_file.writestr(f"export_excel_part{suffix}.xlsx", current_buffer.getvalue())
            print(f"create excel{suffix}")

        zip_file.close()
        zip_buffer.seek(0)

        response = HttpResponse(zip_buffer, content_type="application/zip")
        response["Content-Disposition"] = "attachment; filename*=UTF-8''export_excel_files.zip"

        print(f"xlsxwriter export completed in {(time.time() - start_time):.2f} seconds")
        return response

    except Exception as e:
        print(f"[ERROR] Excel export failed: {e}")
        return HttpResponse("Internal Server Error", status=500)