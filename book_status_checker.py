def status():
    bookuid=int(input('Enter book ID- '))
    query="select issueuid from data where bookuid={0}".format(bookuid)
    mycur.execute(query)
    data=mycur.fetchone()
    if data!=None:
        print(data)
    else:
        print('Record not found')
