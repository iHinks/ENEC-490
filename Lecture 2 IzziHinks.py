import csv
import xlwt
import openpyxl

'''
calculates monthly average price of conventional gas prices 
in the New York Harbor from Jan 1987 to December 2016 using
data from EIA.gov
'''
# calculating average price from file
with open('New_York_Harbor_Conventional_Gasoline_Regular_Spot_Price_FOB.csv', newline='') as f:
    reader = csv.reader(f)
    the_numbers = [float(row[1]) for row in reader]
    average = sum(the_numbers) / len(the_numbers)

# writing average to Excel file named monthly_average_price.xlsx
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws['A1'] = average
wb.save("monthly_average_price.xlsx")
