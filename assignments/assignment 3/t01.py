'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
from Connect import Connect
from functions import pub_counts_all
sep="-"*40
conn = Connect('dcris.txt')
cursor = conn.cursor
print("Test pub_counts_all")
print()
r = pub_counts_all(cursor)
print(r)
r = pub_counts_all(cursor, 42)
print(r)
r = pub_counts_all(cursor, 999)
print(r)
print(sep)