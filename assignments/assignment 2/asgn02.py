"""
-------------------------------------------------------
CP363 Assignment 2.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-10-31"
-------------------------------------------------------
"""


def publications(conn, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = publications(conn)
    Use: rows = publications(conn, title=v1)
    Use: rows = publications(conn, pub_type_id=v2)
    Use: rows = publications(conn, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
                name, the title of a publication, and the full publication
                type (i.e. 'article' rather than 'a';
        the entire table if title and pub_type_id are None,
        else rows matching the partial title and pub_type_id
        if given
                sorted by last name, first name, title (list of ?)
    -------------------------------------------------------
    """
    if title is None and pub_type_id is None:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
ORDER BY last_name, first_name, p_title"""
        conn.cursor.execute(sql)
    elif title is None:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
WHERE p.pub_type_id = %s
ORDER BY last_name, first_name, p_title"""
        params = (pub_type_id,)
        conn.cursor.execute(sql, params)
    elif pub_type_id is None:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
WHERE p_title LIKE %s
ORDER BY last_name, first_name, p_title"""
        params = ("%{}%".format(title),)
        conn.cursor.execute(sql, params)
    else:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
WHERE p.pub_type_id = %s AND p_title LIKE %s
ORDER BY last_name, first_name, p_title"""
        params = (pub_type_id, "%{}%".format(title),)
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows


def pub_counts(conn, member_id, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_counts(conn, member_id=v1)
    Use: rows = pub_counts(conn, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the number of publications of type pub_type
        if given, if not, the number of all their publications (list of ?)
    -------------------------------------------------------
    """
    if pub_type_id is None:
        sql = """SELECT last_name, first_name, COUNT(pub_type_id) AS count
FROM member AS m LEFT OUTER JOIN pub AS p ON p.member_id = m.member_id
WHERE m.member_id = %s
GROUP BY m.member_ID"""
        params = (member_id,)
        conn.cursor.execute(sql, params)
    else:
        sql = """SELECT last_name, first_name, COUNT(pub_type_id) AS count
FROM member AS m LEFT OUTER JOIN pub AS p ON p.member_id = m.member_id
AND pub_type_id = %s
WHERE m.member_id = %s
GROUP BY m.member_ID"""
        params = (pub_type_id, member_id)
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows


def member_expertise_count(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = member_expertise_count(conn)
    Use: rows = member_expertise_count(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, and the count of the number of expertises they
            hold (i.e. keywords)
        all records member_id is None, sorted by last name, first name
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT last_name, first_name, COUNT(keyword_id) AS count
FROM member AS m LEFT OUTER JOIN member_keyword AS mk
ON m.member_id  = mk.member_id
GROUP BY m.member_ID"""
        conn.cursor.execute(sql)
    else:
        sql = """SELECT last_name, first_name, COUNT(keyword_id) AS count
FROM member AS m LEFT OUTER JOIN member_keyword AS mk
ON m.member_id  = mk.member_id
WHERE m.member_id = %s
GROUP BY m.member_ID
ORDER BY last_name, first_name"""
        params = (member_id, )
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows


def all_expertise(conn, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = all_expertise(conn)
    Use: rows = all_expertise(conn, member_id=v1)
    -------------------------------------------------------
    Parameters:
        conn - a database connection (Connect)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
        name, a keyword description, and a supplementary keyword description
        all records if member_id is None,
        sorted by last_name, first_name, keyword description, supplementary
                keyword description
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT last_name, first_name, k_desc, sk_desc
FROM member AS m LEFT OUTER JOIN member_supp_key AS msk ON m.member_id  = msk.member_id
JOIN supp_key as sk ON sk.supp_key_id = msk.supp_key_id
JOIN keyword AS k ON k.keyword_id = sk.keyword_id
ORDER BY last_name, first_name, k_desc, sk_desc"""
        conn.cursor.execute(sql)
    else:
        sql = """SELECT last_name, first_name, k_desc, sk_desc
FROM member AS m LEFT OUTER JOIN member_supp_key AS msk ON m.member_id  = msk.member_id
JOIN supp_key as sk ON sk.supp_key_id = msk.supp_key_id
JOIN keyword AS k ON k.keyword_id = sk.keyword_id
WHERE m.member_id = %s
ORDER BY last_name, first_name, k_desc, sk_desc"""
        params = (member_id, )
        conn.cursor.execute(sql, params)

    rows = conn.cursor.fetchall()
    return rows
