'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import table_info
conn = Connect('dcris.txt')
cursor = conn.cursor
row = table_info(cursor,table_schema=42)
print(row)
row = table_info(cursor, table_name='z', table_schema=42)
print(row)