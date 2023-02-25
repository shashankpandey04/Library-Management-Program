def issue():
    bookuid=int(input('Enter book ID- '))
    query1="select bookuid from data where bookuid={0}".format(bookuid)
    mycur.execute(query1)
    data=mycur.fetchone()
    if data!=None:
        print("BOOK UID- ",data)
        issueuid=input('Enter Student ID- ')
        query="update data set issueuid={0} where bookuid={1}".format(issueuid,bookuid)
        mycur.execute(query)
        mycon.commit()
    else:
        print('Record not found')
