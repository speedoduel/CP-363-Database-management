'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import keyword_member_count
sep="-"*54
conn = Connect('dcris.txt')
cursor = conn.cursor
print("Test keyword_member_count")
print()
r = keyword_member_count(cursor)
print(r)
r = keyword_member_count(cursor, keyword_id=12)
print(r)
r = keyword_member_count(cursor, keyword_id=999)
print(r)
print(sep)