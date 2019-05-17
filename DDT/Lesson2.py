import openpyxl

path = "C:/Users/khan/Desktop/QA/Data driven testing/Test2.xlsx"

workbook = openpyxl.load_workbook(path)

# First Method
sheet = workbook.active

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(row = r, column = c).value = "Welcome"
workbook.save(path)