'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import supp_key_member_count
sep="-"*40
conn = Connect('dcris.txt')
cursor = conn.cursor
print("Test supp_key_member_count")
print()
r = supp_key_member_count(cursor)
print(r)
r = supp_key_member_count(cursor, member_id=42)
print(r)
r = supp_key_member_count(cursor, member_id=999)
print(r)
print(sep)