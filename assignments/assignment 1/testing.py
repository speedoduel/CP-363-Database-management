"""
-------------------------------------------------------
Tests functions from Assignment 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2020-10-19"
-------------------------------------------------------
"""
from Connect import Connect
from functions import keyword_table, pub_table, member_expertise, expertise

SEP = '-' * 40

conn = Connect('dcris.txt')
cursor = conn.cursor
print(SEP)
print("Test keyword_table")
print()
r = keyword_table(cursor)
print(r)
r = keyword_table(cursor, 12)
print(r)
r = keyword_table(cursor, 99)
print(r)
print(SEP)
print("Test pub_table")
print()
r = pub_table(cursor)
print(r)
r = pub_table(cursor, pub_type_id='b')
print(r)
r = pub_table(cursor, member_id=49)
print(r)
r = pub_table(cursor, member_id=49, pub_type_id='b')
print(r)
r = pub_table(cursor, member_id=99, pub_type_id='z')
print(r)
print(SEP)
print("Test member_expertise")
print()
r = member_expertise(cursor)
print(r)
r = member_expertise(cursor, member_id=49)
print(r)
r = member_expertise(cursor, member_id=999)
print(r)
r = member_expertise(cursor, keyword_id=12)
print(r)
r = member_expertise(cursor, keyword_id=999)
print(r)
r = member_expertise(cursor, member_id=49, keyword_id=12)
print(r)
r = member_expertise(cursor, member_id=999, keyword_id=999)
print(r)
print(SEP)
print("Test expertise")
print()
r = expertise(cursor)
print(r)
r = expertise(cursor, keyword="military")
print(r)
r = expertise(cursor, supp_key="war")
print(r)
r = expertise(cursor, keyword="military", supp_key="war")
print(r)
