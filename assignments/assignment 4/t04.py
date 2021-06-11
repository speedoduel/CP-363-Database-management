'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import foreign_key_info
sep="-"*40
conn = Connect('dcris.txt')
cursor = conn.cursor
print("Test foreign_key_info")
print()
ronn = foreign_key_info(cursor)
print(ronn)
ronn = foreign_key_info( member_id=42)
print(ronn)
ronn = foreign_key_info(cursor, member_id=999)
print(ronn)
print(sep)