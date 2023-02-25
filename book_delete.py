def deletebook():
    bookuid=int(input('Enter Book ID- '))
    query="delete from data where bookuid={}".format(bookuid)
    mycur.execute(query)
    mycon.commit()
