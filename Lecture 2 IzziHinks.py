# -*- coding: utf-8 -*-
"""
calculates monthly average price of conventional gas prices 
in the New York Harbor from Jan 1987 to December 2016 using
data from EIA.gov
"""

import xlrd
import xlsxwriter
import numpy as np

file_location = '/Users/ihinks/Desktop/ENEC490/NY_Harbor_Gas_Prices_FOB.xls'
workbook = xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(1) 

start = 0
yearly_average = []
yearly_data = []

#grabs prices from Jan 1987 to Dec 2016 and adds them into yearly_data
for i in range(10, 369):
    value = sheet.cell_value(i, 1)
    yearly_data.append(value)
    
#finds the average for each year
#increments start to begin at the next january date
for i in range(0, 30):
    avg = np.mean(yearly_data[start:start+12])
    yearly_average = np.append(yearly_average,avg)
    #worksheet1.write('A1', yearly_average[i])
    start += 12

# making a matrix with years and each monthly average per year
final_data = np.zeros((30, 2))
final_data[0:30, 0]=1987+np.arange(30)
final_data[0:30, 1]=yearly_average

#new workbook to add the years and monthly averages to a new file
workbook2 = xlsxwriter.Workbook('monthly_average_price.xlsx')
worksheet1 = workbook2.add_worksheet()

row=1
col=0

worksheet1.write(col,0, 'Year')
worksheet1.write(col,0,'Monthly Average Price')

for item, price in (final_data):
    worksheet1.write(row, col, item)
    worksheet1.write(row, col+1, price)
    row+=1
    
workbook2.close()

