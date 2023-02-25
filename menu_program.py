#MENU
while True:
    print('''---------------------
New Book record-1
Delete book record-2
Check Issue Status-3
Issue a book-4
See all data-5
Un-issue the book-6
------------------------------''')
    opt=int(input('Enter option- '))
    if opt==1:
        newbook()
    elif opt==2:
        deletebook()
    elif opt==3:
        status()
    elif opt==4:
        issue()
    elif opt==5:
        allcheck()
    elif opt==6:
        unissue()
