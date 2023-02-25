def unissue():
    bookuid=int(input('Enter book ID- '))
    issueid='Null'
    query="update data set issueuid={0} where bookuid={1}".format(issueid,bookuid)
    mycur.execute(query)
    mycon.commit()
