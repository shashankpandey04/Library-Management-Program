#Database Creator Python Program
import sys
import mysql.connector as msc
mycon=msc.connect(host='localhost',user='root',passwd='root')
mycur=mycon.cursor()
mycur.execute('create database library')
print('Database Created As *LIBRARY*')
mycur.execute('use library')
mycur.execute('create table data (bookuid int primary key, bookname varchar(50), issueuid varchar(50));')
print('Table created named as "DATA"')
if mycon.is_connected():
    print('Connection made')
else:
    print('Connection Break')
print('Now you can close this program')
sys.exit()
