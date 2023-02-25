def newbook():
    bookname=input('Enter book name- ')
    bookuid=int(input('Enter book ID- '))
    issueuid='Null'
    query="insert into data values({0},'{1}','{2}')".format(bookuid,bookname,issueuid)
    mycur.execute(query)
    mycon.commit()
    print('New Book Added')
    print('- - - - - - - - - -')
