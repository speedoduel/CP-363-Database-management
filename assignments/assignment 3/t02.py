'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import expertise_count
sep="-"*40
conn = Connect('dcris.txt')
cursor = conn.cursor
print("Test expertise_count")
print()
r = expertise_count(cursor)
print(r)
r = expertise_count(cursor, member_id=42)
print(r)
r = expertise_count(cursor, member_id=999)
print(r)
print(sep)