'''
-------------------------------------------------------
Author:  Ronak Arora
ID:      193156510
Email:   aror6510@mylaurier.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
'''
def keyword_table(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the keyword table.
    Use: rows = keyword_table(cursor)
    Use: rows = keyword_table(cursor, keyword_id=v)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with the contents of the keyword table;
        the entire table if keyword_id is None, else the row
        matching keyword_id (list of ?)
    -------------------------------------------------------
    """
        #Selects all matching the keyword_id
    if (keyword_id != None):
        sql = "SELECT * FROM keyword WHERE keyword_id = %s"
        #editable parameters are kept separate to stop SQL injection
        params = [keyword_id]
        #execute sql and parameters
        cursor.execute(sql,params)
    #Selects all in keyword table
    else:
        sql = "SELECT * FROM keyword"
        cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
    
    
    
def pub_table(cursor, member_id=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub table.
    Use: rows = pub_table(cursor)
    Use: rows = pub_table(cursor, member_id=v1)
    Use: rows = pub_table(cursor, pub_type_id=v2)
    Use: rows = pub_table(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with the contents of the pub table;
        the entire table if member_id and pub_type_id are None,
        else rows matching member_id and pub_type_id
        if given (list of ?)
    -------------------------------------------------------
    """    
    if ((member_id != None) and (pub_type_id!=None)):
        sql = "SELECT * FROM pub WHERE member_id = %s AND pub_type_id=%s"
        #editable parameters are kept separate to stop SQL injection
        params = [member_id,pub_type_id]
        #execute sql and parameters
        cursor.execute(sql,params)
    #Selects all in keyword table
    else:
        sql = "SELECT * FROM pub"
        cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def member_expertise(cursor, member_id=None, keyword_id=None):
    """
    -------------------------------------------------------
    Queries the v_member_keyword view.
    Use: rows = member_expertise(cursor)
    Use: rows = member_expertise(cursor, member_id=v1)
    Use: rows = member_expertise(cursor, keyword_id=v2)
    Use: rows = member_expertise(cursor, member_id=v1, keyword_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with the last name, first name, and keyword
            description of the v_member_keyword view:
        the entire view if member_id and keyword_id are None,
            sorted by last name, first name, keyword description
        rows matching member_id if keyword_id is None:
            sorted by last name, first name, keyword description
        rows matching keyword_id if member_id is None:
            sorted by keyword description, last name, first name
        otherwise rows unsorted
        if given (list of ?)
    -------------------------------------------------------
    """
    if ((member_id != None) and (keyword_id!=None)):
        sql = """SELECT first_name, last_name,k_desc FROM v_member_keyword 
        WHERE member_id = %s AND keyword_id=%s
        ORDER BY last_name,first_name,k_desc"""
        #editable parameters are kept separate to stop SQL injection
        params = [member_id,keyword_id]
        #execute sql and parameters
        cursor.execute(sql,params)
    #Selects all in keyword table
    elif((member_id == None) and (keyword_id!=None)): 
        sql = "SELECT * FROM v_member_keyword WHERE keyword_id=%s ORDER BY last_name,first_name,k_desc"
        #editable parameters are kept separate to stop SQL injection
        params = [keyword_id]
        #execute sql and parameters
        cursor.execute(sql,params)
    #Selects all in keyword table   
    elif(member_id != None): 
        sql = "SELECT * FROM v_member_keyword WHERE member_id=%s ORDER BY last_name,first_name,k_desc"
        #editable parameters are kept separate to stop SQL injection
        params = [member_id]
        #execute sql and parameters
        cursor.execute(sql,params)
    #Selects all in keyword table 
    else:
        sql = "SELECT * FROM v_member_keyword ORDER BY last_name,first_name,k_desc"
        cursor.execute(sql)
    rows = cursor.fetchall()
    return rows
    
def expertise(cursor, keyword=None, supp_key=None):
    """
    -------------------------------------------------------
    Queries the v_keyword_supp_key view.
    Use: rows = expertise(cursor)
    Use: rows = expertise(cursor, keyword=v1)
    Use: rows = expertise(cursor, supp_key=v2)
    Use: rows = expertise(cursor, keyword=v1, supp_key=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword - a partial keyword description (str)
        supp_key - a partial supplementary description (str)
    Returns:
        rows - a list with the keyword and supplementary keyword descriptions
            of the v_keyword_supp_key view:
        the entire view if keyword and supp_key are None,
            sorted by keyword description, supplementary keyword description
        rows containing keyword if supp_key is None:
            sorted by keyword description, supplementary keyword description
        rows matching supp_key if keyword is None:
            sorted by supplementary keyword description, keyword description
        otherwise rows
            sorted by keyword description, supplementary keyword description
    -------------------------------------------------------
    """ 
    if keyword is None and supp_key is None:
        sql = """SELECT k_desc, sk_desc FROM v_keyword_supp_key
        ORDER BY k_desc, sk_desc"""
        cursor.execute(sql)
    elif keyword is None:
        sql = """SELECT k_desc, sk_desc FROM v_keyword_supp_key
        WHERE sk_desc LIKE %s ORDER BY sk_desc, k_desc"""
        params =[supp_key]
        cursor.execute(sql, params)
    elif supp_key is None:
        sql = """SELECT k_desc, sk_desc FROM v_keyword_supp_key
        WHERE k_desc LIKE %s ORDER BY k_desc, sk_desc"""
        params = [keyword]
        cursor.execute(sql, params)
    else:
        sql = """SELECT k_desc, sk_desc FROM v_keyword_supp_key
        WHERE k_desc LIKE %s AND sk_desc LIKE %s
        ORDER BY k_desc, sk_desc"""
        params = [keyword,supp_key]
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows   

def publications(cursor, title=None, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = publications(cursor)
    Use: rows = publications(cursor, title=v1)
    Use: rows = publications(cursor, pub_type_id=v2)
    Use: rows = publications(cursor, title=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        title - a partial title (str)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
            name, the title of a publication, and the full publication
            type (i.e. 'article' rather than 'a')
        If title and pub_type_id are None
            returns the entire table
        If partial title and/or pub_type are given
            returns only matching results
        Rows sorted by last name, first name, title
        (list of ?)
    -------------------------------------------------------
    """
    if title is None and pub_type_id is None:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
        FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
        JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
        ORDER BY last_name, first_name, p_title"""
        cursor.execute(sql)
    elif title is None:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
        FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
        JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
        WHERE p.pub_type_id = %s
        ORDER BY last_name, first_name, p_title"""
        params = ("%{}%".format(pub_type_id),)
        cursor.execute(sql, params)
    elif pub_type_id is None:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
        FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
        JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
        WHERE p_title LIKE %s
        ORDER BY last_name, first_name, p_title"""
        params = ("%{}%".format(title),)
        cursor.execute(sql, params)
    else:
        sql = """SELECT last_name, first_name, p_title, pt.pt_desc
        FROM member AS m JOIN pub AS p ON p.member_id = m.member_id
        JOIN pub_type AS pt ON p.pub_type_id = pt.pub_type_id
        WHERE p.pub_type_id = %s AND p_title LIKE %s
        ORDER BY last_name, first_name, p_title"""
        params = (pub_type_id, "%{}%".format(title),)
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows
def pub_counts(cursor, member_id, pub_type_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor, member_id=v1)
    Use: rows = pub_counts(cursor, member_id=v1, pub_type_id=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
        pub_type_id - a publication type (str)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the number of publications of type pub_type
        If pub_type_id is None
            returns the count of all their publications
        otherwise
            returns the count of publications of type pub_type_id
        (list of ?)
    -------------------------------------------------------
    """
    if pub_type_id is None:
        sql = """SELECT last_name, first_name, COUNT(pub_type_id) AS count
        FROM member AS m LEFT OUTER JOIN pub AS p ON p.member_id = m.member_id
        WHERE m.member_id = %s
        GROUP BY m.member_ID"""
        params = (member_id,)
        cursor.execute(sql, params)
    else:
        sql = """SELECT last_name, first_name, COUNT(pub_type_id) AS count
        FROM member AS m LEFT OUTER JOIN pub AS p ON p.member_id = m.member_id
        AND pub_type_id = %s
        WHERE m.member_id = %s
        GROUP BY m.member_ID"""
        params = (pub_type_id, member_id)
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows
def member_expertise_count(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member and keyword tables.
    Use: rows = member_expertise_count(cursor)
    Use: rows = member_expertise_count(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the count of the number of expertises (i.e. keywords)
            they hold 
        If member_id is None
            returns the keyword count for all members
        otherwise
            returns the keyword count for the member matching member_id
        Sorted by last name, first name
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT last_name, first_name, COUNT(keyword_id) AS count
        FROM member AS m LEFT OUTER JOIN member_keyword AS mk
        ON m.member_id  = mk.member_id
        GROUP BY m.member_ID"""
        cursor.execute(sql)
    else:
        sql = """SELECT last_name, first_name, COUNT(keyword_id) AS count
        FROM member AS m LEFT OUTER JOIN member_keyword AS mk
        ON m.member_id  = mk.member_id
        WHERE m.member_id = %s
        GROUP BY m.member_ID
        ORDER BY last_name, first_name"""
        params = (member_id, )
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows
def all_expertise(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the member, keyword, and supp_key tables
    Use: rows = all_expertise(cursor)
    Use: rows = all_expertise(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, a keyword description, and a supplementary keyword description
        If member_id is None
            returns descriptions for all members
        Otherwise
            returns descriptions for the member matching member_id
        Sorted by last_name, first_name, keyword description, supplementary
                keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT last_name, first_name, k_desc, sk_desc
        FROM member AS m LEFT OUTER JOIN member_supp_key AS msk ON m.member_id  = msk.member_id
        JOIN supp_key as sk ON sk.supp_key_id = msk.supp_key_id
        JOIN keyword AS k ON k.keyword_id = sk.keyword_id
        ORDER BY last_name, first_name, k_desc, sk_desc"""
        cursor.execute(sql)
    else:
        sql = """SELECT last_name, first_name, k_desc, sk_desc
        FROM member AS m LEFT OUTER JOIN member_supp_key AS msk ON m.member_id  = msk.member_id
        JOIN supp_key as sk ON sk.supp_key_id = msk.supp_key_id
        JOIN keyword AS k ON k.keyword_id = sk.keyword_id
        WHERE m.member_id = %s
        ORDER BY last_name, first_name, k_desc, sk_desc"""
        params = (member_id, )
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows

def pub_counts_all(cursor, member_id=None):
    """
    -------------------------------------------------------
    Queries the pub and member tables.
    Use: rows = pub_counts(cursor)
    Use: rows = pub_counts(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the numbers of publications of each type. Name these
            three fields "articles", "papers", and "books".
        If member_id is None
            returns numbers of publications for all members
        Otherwise
            returns numbers of publications for the member matching member_id
        Sorted by last_name, first_name
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT last_name, first_name,
        (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
        AND pub_type_id = 'a') AS articles,
        (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
        AND pub_type_id = 'p') AS papers,
        (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
        AND pub_type_id = 'b') AS books
        FROM member AS m ORDER BY last_name, first_name"""
        cursor.execute(sql)
    else:
        sql = """SELECT last_name, first_name,
        (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
        AND pub_type_id = 'a') AS articles,
        (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
        AND pub_type_id = 'p') AS papers,
        (SELECT COUNT(*) FROM pub AS p WHERE m.member_id = p.member_ID
        AND pub_type_id = 'b') AS books
        FROM member AS m
        WHERE member_id = %s"""
        params = (member_id,)
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows
    
def expertise_count(cursor, member_id=None):
    """
    -------------------------------------------------------
    Use: rows = expertise_count(cursor)
    Use: rows = expertise_count(cursor, member_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        member_id - a member ID number (int)
    Returns:
        rows - a list with a member's last name, a member's first
            name, and the number of keywords and supplementary keywords
            for the member. Name these fields "keywords" and "supp_keys".
        If member_id is None
            returns numbers of expertises for all members
        Otherwise
            returns numbers of expertises for the member matching member_id
        Sorted by last_name, first_name
        (list of ?)
    -------------------------------------------------------
    """
    if member_id is None:
        sql = """SELECT last_name, first_name,
        (SELECT COUNT(*) FROM member_keyword AS mk
        WHERE m.member_id = mk.member_ID) AS keywords,
        (SELECT COUNT(*) FROM member_supp_key AS msk
        WHERE m.member_id = msk.member_ID) AS supp_keys
        FROM member AS m ORDER BY last_name, first_name"""
        cursor.execute(sql)
    else:
        sql = """SELECT last_name, first_name,
        (SELECT COUNT(*) FROM member_keyword AS mk
        WHERE m.member_id = mk.member_ID) AS keywords,
        (SELECT COUNT(*) FROM member_supp_key AS msk
        WHERE m.member_id = msk.member_ID) AS supp_keys
        FROM member AS m
        WHERE member_id = %s"""
        params = (member_id,)
        cursor.execute(sql, params)
    rows = cursor.fetchall()
    return rows
def keyword_count(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_count(cursor)
    Use: rows = keyword_count(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword's description and the number of
            supplementary keywords that belong to it. Name the second field
            "supp_key_count".
        If keyword_id is None
            returns numbers of supplementary keywords for all keywords
        Otherwise
            returns numbers of supplementary keywords for the keyword matching
                keyword_id
        Sorted by keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if keyword_id is None:
        sql = """SELECT k_desc, COUNT(sk.supp_key_id) AS supp_key_count
        FROM keyword AS k LEFT OUTER JOIN supp_key AS sk
        ON k.keyword_id = sk.keyword_id
        GROUP BY k.keyword_id
        ORDER BY k_desc"""
        cursor.execute(sql)
    else:
        sql = """SELECT k_desc, COUNT(sk.supp_key_id) AS supp_key_count
        FROM keyword AS k LEFT OUTER JOIN supp_key AS sk
        ON k.keyword_id = sk.keyword_id
        WHERE k.keyword_id = %s
        GROUP BY k.keyword_id"""
        params = (keyword_id,)
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows
def keyword_member_count(cursor, keyword_id=None):
    """
    -------------------------------------------------------
    Use: rows = keyword_member_count(cursor)
    Use: rows = keyword_member_count(cursor, keyword_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        keyword_id - a keyword ID number (int)
    Returns:
        rows - a list with a keyword description and the number of members
            that have it. Name the second field "member_count".
        If keyword_id is None
            returns numbers of members for all keywords
        Otherwise
            returns numbers of members for the keyword matching keyword_id
        Sorted by keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if keyword_id is None:
        sql = """SELECT k_desc, COUNT(mk.keyword_id) AS member_count
        FROM keyword AS k LEFT OUTER JOIN member_keyword AS mk
        ON k.keyword_id = mk.keyword_id
        GROUP BY k.keyword_id
        ORDER BY k_desc"""
        cursor.execute(sql)
    else:
        sql = """SELECT k_desc, COUNT(mk.keyword_id) AS member_count
        FROM keyword AS k LEFT OUTER JOIN member_keyword AS mk
        ON k.keyword_id = mk.keyword_id
        WHERE k.keyword_id = %s
        GROUP BY k.keyword_id"""
        params = (keyword_id,)
        cursor.execute(sql, params)

    rows = cursor.fetchall()
    return rows
    
def supp_key_member_count(cursor, supp_key_id=None):
    """
    -------------------------------------------------------
    Use: rows = supp_key_member_count(cursor)
    Use: rows = supp_key_member_count(cursor, supp_key_id=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        supp_key_id - a supp_key ID number (int)
    Returns:
        rows - a list with a keyword's description, a supplementary
            keyword description, and the number of members that have that
            supplementary expertise. Name the last field "member_count".
        If supp_key_id is None
            returns numbers of members for all supplementary keywords
        Otherwise
            returns numbers of members for the supplementary keyword
            matching supp_key_id
        Sorted by keyword description and then supplementary keyword description
        (list of ?)
    -------------------------------------------------------
    """
    if supp_key_id is None:
        sql = """SELECT k_desc, sk_desc, COUNT(msk.member_id) AS member_count
        FROM keyword AS k JOIN supp_key AS sk
        ON k.keyword_id = sk.keyword_id
        LEFT OUTER JOIN member_supp_key AS msk
        ON sk.supp_key_id = msk.supp_key_id
        GROUP BY msk.supp_key_id
        ORDER BY k_desc, sk_desc"""
        cursor.execute(sql)
    else:
        sql = """SELECT k_desc, sk_desc, COUNT(msk.member_id) AS member_count
        FROM keyword AS k JOIN supp_key AS sk
        ON k.keyword_id = sk.keyword_id
        AND sk.supp_key_id = %s
        LEFT OUTER JOIN member_supp_key AS msk
        ON sk.supp_key_id = msk.supp_key_id
        GROUP BY msk.supp_key_id
        ORDER BY k_desc, sk_desc"""
        params = (supp_key_id,)
        cursor.execute(sql, params)      

    rows = cursor.fetchall()
    return rows

def table_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLES for metadata.
    Use: rows = table_info(cursor, table_schema)
    Use: rows = table_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, TABLE_TYPE, TABLE_ROWS,
            and TABLE_COMMENT fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, TABLE_TYPE
        (list of ?)
    -------------------------------------------------------
    """
    try:
        if table_name is None:
            sql=""" SELECT DISTINCT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
                    FROM information_schema.TABLES
                    ORDER BY TABLE_NAME ASC, TABLE_TYPE """
        else:
            sql=""" SELECT DISTINCT TABLE_NAME, TABLE_TYPE, TABLE_ROWS, TABLE_COMMENT
                    FROM information_schema.TABLES
                    WHERE table_name='{}'
                    ORDER BY TABLE_NAME ASC, TABLE_TYPE""".format(table_name)
        cursor.execute(sql) 
        result = cursor.fetchall()
    except Exception as e:
        result = str(e)               
    return result

def column_info(cursor, table_schema, table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.COLUMNS for metadata.
    Use: rows = column_info(cursor, table_schema)
    Use: rows = column_info(cursor, table_schema, table_name=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        table_name - a table name (str)
    Returns:
        rows - a list of data from the TABLE_NAME, COLUMN_NAME, IS_NULLABLE,
            and DATA_TYPE fields.
        If table_name is None
            returns data for all tables
        Otherwise
            returns data for table whose name matches table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """
    if table_name is None:
        sql="""SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
        FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA= %s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        params="%{}%".format(table_schema)
        cursor.execute(sql,params)
    else:
        sql="""
        SELECT TABLE_NAME, COLUMN_NAME, IS_NULLABLE, DATA_TYPE
        FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA= %s and TABLE_NAME=%s
        ORDER BY TABLE_NAME, COLUMN_NAME
        """
        params=(table_schema,table_name)
        cursor.execute(sql,params)
    rows=cursor.fetchall()
    return rows
        
def constraint_info(cursor, table_schema, constraint_type=None):
    """
    -------------------------------------------------------
    Queries information_schema.TABLE_CONSTRAINTS for metadata.
    Use: rows = constraint_info(cursor, table_schema)
    Use: rows = constraint_info(cursor, table_schema, constraint_type=v1)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        table_schema - the database table schema (str)
        constraint_type - a database constraint type (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME,
            and CONSTRAINT_TYPE fields.
        If constraint_type is None
            returns data for all constraints
        Otherwise
            returns data for constraint whose type matches constraint_type
        Sorted by CONSTRAINT_NAME, TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """
    if constraint_type is None:
        sql=""" SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA=%s 
        ORDER BY CONSTRAINT_NAME,TABLE_NAME"""
        params=(table_schema)
        cursor.execute(sql,params)
    else:
        sql="""SELECT CONSTRAINT_NAME, TABLE_NAME, CONSTRAINT_TYPE 
        FROM information_schema.TABLE_CONSTRAINTS
        WHERE TABLE_SCHEMA=%s AND CONSTRAINT_TYPE=%s
        ORDER BY CONSTRAINT_NAME,TABLE_NAME"""   
        params=(table_schema,constraint_type)
        cursor.execute(sql,params) 
    rows=cursor.fetchall()
    return rows
def foreign_key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.REFERENTIAL_CONSTRAINTS for metadata.
    Use: rows = foreign_key_info(cursor, constraint_schema)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = foreign_key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = foreign_key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, UPDATE_RULE, DELETE_RULE,
            TABLE_NAME, and REFERENCED_TABLE_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by CONSTRAINT_NAME, TABLE_NAME, REFERENCED_TABLE_NAME
        (list of ?)
    -------------------------------------------------------
    """
    try:
        if table_name is None and ref_table_name is None:
            sql="""SELECT DISTINCT CONSTRAINT_NAME,UPDATE_RULE,DELETE_RULE,TABLE_NAME,REFRENCED_TABLE_NAME
            FROM information_schema.REFRENTIAL_CONSTRAINTS
            ORDER BY CONSTRAINT_NAME,TABLE_NAME,REFRENCED_TABLE_NAME"""
        elif table_name is None and ref_table_name is not None:  
            sql="""SELECT DISTINCT CONSTRAINT_NAME,UPDATE_RULE,DELETE_RULE,TABLE_NAME,REFRENCED_TABLE_NAME
            FROM information_schema.REFRENTIAL_CONSTRAINTS
            WHERE REFRENCED_TABLE_NAME='{}'
            ORDER BY CONSTRAINT_NAME,TABLE_NAME,REFRENCED_TABLE_NAME""".format(ref_table_name)
        elif  table_name is not None and ref_table_name is None:
            sql="""SELECT DISTINCT CONSTRAINT_NAME,UPDATE_RULE,DELETE_RULE,TABLE_NAME,REFRENCED_TABLE_NAME
            FROM information_schema.REFRENTIAL_CONSTRAINTS
            WHERE TABLE_NAME='{}'
            ORDER BY CONSTRAINT_NAME,TABLE_NAME,REFRENCED_TABLE_NAME""".format(table_name) 
        else:
            sql="""SELECT DISTINCT CONSTRAINT_NAME,UPDATE_RULE,DELETE_RULE,TABLE_NAME,REFRENCED_TABLE_NAME
            FROM information_schema.REFRENTIAL_CONSTRAINTS
            WHERE REFRENCED_TABLE_NAME='{}' AND REFRENCED_TABLE_NAME='{}'
            ORDER BY CONSTRAINT_NAME,TABLE_NAME,REFRENCED_TABLE_NAME""".format(table_name,ref_table_name)
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as er:
        result =str(er)
    return result 
def key_info(cursor, constraint_schema, table_name=None, ref_table_name=None):
    """
    -------------------------------------------------------
    Queries information_schema.KEY_COLUMN_USAGE for metadata.
    Use: rows = key_info(cursor, constraint_schema)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1)
    Use: rows = key_info(cursor, constraint_schema, ref_table_name=v2)
    Use: rows = key_info(cursor, constraint_schema, table_name=v1, ref_table_name=v2)
    -------------------------------------------------------
    Parameters:
        cursor - a database cursor (cursor)
        constraint_schema - the database constraint schema (str)
        table_name - a table name (str)
        ref_table_name - a table name (str)
    Returns:
        rows - a list of data from the CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
            REFERENCED_TABLE_NAME, and REFERENCED_COLUMN_NAME fields.
        If table_name and ref_table_name are None
            returns data for all foreign keys
        If table_name is None
            returns data for foreign keys referencing only ref_table_name
        If ref_table_name is None
            returns data for foreign keys referencing only table_name
        Otherwise
            returns data for the foreign key for table_name and ref_table_name
        Sorted by TABLE_NAME, COLUMN_NAME
        (list of ?)
    -------------------------------------------------------
    """
    try:
        if table_name is None and ref_table_name is None:
            sql=""" SELECT DISTINCT CONSTRAINT_NAME, TABLE_NAME,COLUMN_NAME,REFRENCED_TABLE_NAME
                    FROM information_schema.KEY_COLUMN_USAGE
                    ORDER BY TABLE_NAME, COLUMN_NAME"""
        elif table_name is None and ref_table_name is not None:         
            sql=""" SELECT DISTINCT CONSTRAINT_NAME, TABLE_NAME,COLUMN_NAME,REFRENCED_TABLE_NAME
                    FROM information_schema.KEY_COLUMN_USAGE
                    WHERE REFRENCED_TABLE_NAME='{}'
                    ORDER BY TABLE_NAME, COLUMN_NAME""".format(ref_table_name)
        elif table_name is not None and ref_table_name is None:
            sql=""" SELECT DISTINCT CONSTRAINT_NAME, TABLE_NAME,COLUMN_NAME,REFRENCED_TABLE_NAME
                    FROM information_schema.KEY_COLUMN_USAGE
                    WHERE TABLE_NAME='{}'
                    ORDER BY TABLE_NAME, COLUMN_NAME""".format(table_name)
        else:
            sql=""" SELECT DISTINCT CONSTRAINT_NAME, TABLE_NAME,COLUMN_NAME,REFRENCED_TABLE_NAME
                    FROM information_schema.KEY_COLUMN_USAGE
                    WHERE TABLE_NAME='{}' AND REFRENCED_TABLE_NAME
                    ORDER BY TABLE_NAME, COLUMN_NAME""".format(table_name,ref_table_name)
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as er:
        result =str(er)
    return result            