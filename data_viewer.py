def allcheck():
    query="select * from data"
    mycur.execute(query)
    data=mycur.fetchall()
    if data!=None:
        print(data)
    else:
        print("No data!")
