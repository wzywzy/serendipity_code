import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='serendipity',
        charset='utf8',
        )
cursor=connection.cursor()


s1=set()
s1=set()

cursor.execute("select author1,author2,early_year from wzy_c;")
results=cursor.fetchall()
for result in results:

	s1.clear()

	cursor.execute("select normalizedPN from Papers_C join PaperAuthorAffiliations_C on Papers_C.paperID=PaperAuthorAffiliations_C.paperID where authorId=%s and paperPY<%s;",(result[0],result[2]))

	pn1s=cursor.fetchall()
	for pn1 in pn1s:
		s1.add(pn1)
	
	final1="#".join(list(s1))



	s2.clear()

	cursor.execute("select normalizedPN from Papers_C join PaperAuthorAffiliations_C on Papers_C.paperID=PaperAuthorAffiliations_C.paperID where authorId=%s and paperPY<%s;",(result[1],result[2]))

	pn2s=cursor.fetchall()
	for pn2 in pn2s:
		s2.add(pn2)
	
	final2="#".join(list(s2))
	

	sql = 'INSERT INTO wzy_c (titles_before_colla1, titles_before_colla2) where author1=%s and author2=%s VALUES (%s, %s)'
        cursor.execute(sql, (final1,final2,result[0],result[1]));


connection.commit()
