import time
import io
import zipfile
import csv
from django.http import HttpResponse

def export_large_data_as_csv(request):
    CHUNK_SIZE = 100_000

    try:
        start_time = time.time()
        print("CSV export started")

        columns = [
            "ColumnA", "ColumnB", "ColumnC", "ColumnD", "ColumnE",
            "ColumnF", "ColumnG", "ColumnH", "ColumnI", "ColumnJ"
        ]

        def dummy_data_generator():
            for i in range(1_025_731):
                yield [f"Value{i}_{col}" for col in range(len(columns))]

        data_iterator = dummy_data_generator()
        zip_buffer = io.BytesIO()
        zip_file = zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED)

        row_count = 0
        file_index = 1
        current_buffer = io.StringIO()
        writer = csv.writer(current_buffer)
        writer.writerow(columns)

        for row in data_iterator:
            writer.writerow(row)
            row_count += 1

            if row_count >= CHUNK_SIZE:
                zip_file.writestr(f"export_csv_part_{file_index:02d}.csv", current_buffer.getvalue())
                print(f"create csv_{file_index:02d}")
                file_index += 1
                row_count = 0
                current_buffer = io.StringIO()
                writer = csv.writer(current_buffer)
                writer.writerow(columns)

        if row_count > 0:
            suffix = f"_{file_index:02d}" if file_index > 1 else ""
            zip_file.writestr(f"export_csv_part{suffix}.csv", current_buffer.getvalue())
            print(f"create csv{suffix}")

        zip_file.close()
        zip_buffer.seek(0)

        response = HttpResponse(zip_buffer, content_type="application/zip")
        response["Content-Disposition"] = "attachment; filename*=UTF-8''export_csv_files.zip"

        print(f"CSV export completed in {(time.time() - start_time):.2f} seconds")
        return response

    except Exception as e:
        print(f"[ERROR] CSV export failed: {e}")
        return HttpResponse("Internal Server Error", status=500)