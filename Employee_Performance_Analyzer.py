import openpyxl as xl
wb=xl.load_workbook('employee_performance_scores.xlsx')
sheet=wb['Sheet1']
sheet.cell(1,5).value='Total'
sheet.cell(1,6).value='Average'
sheet.cell(1,7).value='Performance'
for row in range(2,sheet.max_row+1):
    total=sheet.cell(row,2).value + sheet.cell(row,3).value + sheet.cell(row,4).value
    avg=total/3
    sheet.cell(row,5).value=total
    sheet.cell(row,6).value=round(avg,2)
    if round(avg,2)>=90:
        sheet.cell(row,7).value="Excellent"
    elif round(avg,2)>=75 and round(avg,2)<90:
        sheet.cell(row,7).value="Good"
    elif round(avg,2)>=60 and round(avg,2)<75:
        sheet.cell(row,7).value="Average"
    else:
        sheet.cell(row,7).value="Need Improvement"
    print("The total value is : ",total)
    print("The average value is : ",round(avg,2))
    print("The performance of the employee is : ",sheet.cell(row,7).value)
wb.save('Performance_Result.xlsx')
