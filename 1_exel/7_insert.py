from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# # ws.insert_rows(8) # 8번줄이 비워짐
# ws.insert_rows(8,5) # 8번줄에 5줄 삽입
# wb.save("sample_insert_rows.xlsx")

# ws.insert_cols(2)
ws.insert_cols(2,3) # B 번째 줄에 빈 컬럼 3개 삽입
wb.save("sample_insert_cols.xlsx")
