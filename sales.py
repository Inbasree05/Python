import openpyxl as xl
wb=xl.load_workbook('sales.xlsx')
sheet=wb['Sheet1']
sheet.cell(1,4).value='Total Sales'
sheet.cell(1,5).value='level'
for row in range(2,sheet.max_row+1):
    total_sales=sheet.cell(row,2).value*sheet.cell(row,3).value
    sheet.cell(row,4).value=total_sales
    if total_sales>300:
        sheet.cell(row,5).value='High Sales'
    else:
        sheet.cell(row,5).value='Low Sales'
    print("The total sales is : ",total_sales)
    print("The Level of Sales is : ",sheet.cell(row,5).value)
wb.save('Sales_result.xlsx')

    
