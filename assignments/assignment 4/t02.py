'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import column_info
conn = Connect('dcris.txt')
cursor = conn.cursor
row = column_info(cursor, table_schema=0 ,table_name='EVENTS')
print(row)
row = column_info(cursor, pub_type_id='z')
print(row)
row = column_info(cursor, title='xxx')
print(row)
row = column_info(cursor, title='war')
print(row)
row = column_info(cursor, pub_type_id='a', title='war')
print(row)
row = column_info(cursor, pub_type_id='z', title='xxx')
print(row)
