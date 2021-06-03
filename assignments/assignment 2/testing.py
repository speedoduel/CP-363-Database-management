"""
-------------------------------------------------------
testing
Tests functions from asgn01.py
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-02-07"
-------------------------------------------------------
"""
from Connect import Connect
from asgn02 import publications, pub_counts, member_expertise_count, all_expertise

SEP = '-' * 40

conn = Connect('dcris.ini')
print(SEP)
print("Test publications")
print()
r = publications(conn)
print(r)
r = publications(conn, pub_type_id='a')
print(r)
r = publications(conn, pub_type_id='x')
print(r)
r = publications(conn, title='war')
print(r)
r = publications(conn, title='xxx')
print(r)
r = publications(conn, pub_type_id='a', title='war')
print(r)
r = publications(conn, pub_type_id='z', title='xxx')
print(r)
input("Next:")
print(SEP)
print("Test pub_counts")
print()
r = pub_counts(conn, member_id=42)
print(r)
r = pub_counts(conn, member_id=42, pub_type_id='b')
print(r)
r = pub_counts(conn, member_id=999, pub_type_id='z')
print(r)
print(SEP)
print("Test member_expertise_count")
print()
r = member_expertise_count(conn)
print(r)
r = member_expertise_count(conn, member_id=49)
print(r)
print(SEP)
print("Test expertise")
print()
r = all_expertise(conn)
print(r)
r = all_expertise(conn, member_id=42)
print(r)
r = all_expertise(conn, member_id=999)
print(r)
