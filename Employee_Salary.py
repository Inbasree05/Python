import openpyxl as xl
wb=xl.load_workbook('employee.xlsx')
sheet=wb['Sheet1']
sheet.cell(1,4).value='Gross Salary'
sheet.cell(1,5).value='Tax'
sheet.cell(1,6).value='Net Salary'
sheet.cell(1,7).value='Level'
for row in range(2,sheet.max_row+1):
    sheet.cell(row,4).value=sheet.cell(row,2).value+sheet.cell(row,3).value
    sheet.cell(row,5).value=sheet.cell(row,4).value*0.05
    sheet.cell(row,6).value=sheet.cell(row,4).value-sheet.cell(row,5).value
    if(sheet.cell(row,6).value>30000):
        sheet.cell(row,7).value='High Salary'
    else:
        sheet.cell(row,7).value='Low Salary'
wb.save('Employee_result.xlsx')


