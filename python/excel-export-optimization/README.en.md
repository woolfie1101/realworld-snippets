# 📦 Large Dataset Export Optimizer

Exporting large datasets efficiently from web applications can be challenging — especially when dealing with Excel or CSV formats. This repository demonstrates three approaches to exporting over 1 million rows with better performance and user experience.

> 🔁 Real-world inspired — generalized for open sharing.

---

## 🚀 Features

- ✅ Export data as Excel using `openpyxl`
- ⚡ Export data as Excel using `xlsxwriter` (fast!)
- ⚡⚡ Export data as CSV (super fast!)
- 🧩 Automatically split into multiple files if data exceeds threshold
- 📦 Zip all files into a single downloadable response
- 📊 Logs time taken per method

---

## 📂 Directory Structure
```plaintext
📁 large-export-optimizer/
┣ 📜 openpyxl_export.py
┣ 📜 xlsxwriter_export.py
┣ 📜 csv_export.py
┣ 📜 README.en.md
┗ 📜 README.ko.md
```

---

## 📄 Code Overview

### `openpyxl_export.py`
- Standard Excel export using `openpyxl`
- Good for styled spreadsheets, but **slower** for large datasets

### `xlsxwriter_export.py`
- Optimized Excel export using `xlsxwriter`
- **2~3x faster** than `openpyxl` in large data use cases

### `csv_export.py`
- Fastest method using plain `csv`
- Ideal for raw data exports (e.g. analytics, logs)
- Automatically split into chunks if too large

---

## 🧪 Performance Example (1,025,731 rows)

| Method        | Duration   | Format | Notes         |
|---------------|------------|--------|---------------|
| openpyxl      | ~7 min     | .xlsx  | Slowest       |
| xlsxwriter    | ~2 min     | .xlsx  | Recommended   |
| csv           | ~1 min     | .csv   | Fastest       |

> 💡 Results based on local Django test with generator-based data

---

## 🔧 Customization

You can adjust:

```python
CHUNK_SIZE = 100_000
```

And replace the dummy_data_generator() with your real queryset or data source.
