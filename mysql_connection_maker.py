import mysql.connector as msc
mycon=msc.connect(host='localhost',user='root',passwd='root',database='library')
mycur=mycon.cursor()
mycur.execute('use library')
if mycon.is_connected():
    print('Connection made')
else:
    print('Connection Break')
