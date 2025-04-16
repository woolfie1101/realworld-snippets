# 📦 대용량 데이터 엑셀/CSV 다운로드 최적화 예제

웹 애플리케이션에서 수십만~백만 건 이상의 데이터를 효율적으로 엑셀 또는 CSV로 내보내는 방법을 정리한 실전 예제입니다.

> ✅ 실무에서 발생한 문제를 일반화하여 공유용 코드로 재구성했습니다.

---

## 🚀 주요 기능

- ✅ `openpyxl`로 Excel(.xlsx) 다운로드
- ⚡ `xlsxwriter`로 빠른 Excel 다운로드
- ⚡⚡ `csv`로 초고속 데이터 다운로드
- 📦 일정 건수 초과 시 자동 분할 저장
- 📂 여러 파일을 ZIP으로 묶어 반환
- ⏱ 각 방식별 소요 시간 로그 출력

---

## 📂 디렉토리 구조
```plaintext
📁 large-export-optimizer/
┣ 📜 openpyxl_export.py
┣ 📜 xlsxwriter_export.py
┣ 📜 csv_export.py
┣ 📜 README.en.md
┗ 📜 README.ko.md
```
---

## 📄 파일 설명

### `openpyxl_export.py`
- 전통적인 Excel export 방식
- 속도는 느리지만 Excel 포맷을 쓰고 싶을 때 유용

### `xlsxwriter_export.py`
- openpyxl보다 훨씬 빠른 Excel export
- 대용량에 최적화된 방식

### `csv_export.py`
- 가장 빠른 export 방식
- Excel 스타일이 필요 없는 경우에 추천

---

## 🧪 성능 측정 (1,025,731건 기준)

| 방식         | 소요 시간  | 형식  | 설명       |
|--------------|------------|--------|-------------|
| openpyxl     | 약 7분     | .xlsx | 느림         |
| xlsxwriter   | 약 2분     | .xlsx | 추천         |
| csv          | 약 1분     | .csv  | 가장 빠름    |

![openpyxl](/img/python/excel-export-optimization/01.png)

![xlsxwriter](/img/python/excel-export-optimization/02.png)

![csv](/img/python/excel-export-optimization/03.png)

> 💡 Django에서 제너레이터 기반으로 테스트한 결과입니다.

---

## 🔧 커스터마이징

```python
CHUNK_SIZE = 100_000
```

값을 조절하거나, 더미 데이터를 실제 DB 쿼리로 교체해 사용하세요.
