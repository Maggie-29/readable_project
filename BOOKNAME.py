import sqlite3
import os
#import pandas as pd
import datetime as dt 

#添加表格 & 修改列名
def changeBooks():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE Books            
         (ID  INTEGER PRIMARY KEY AUTOINCREMENT,
          BOOKUID       TEXT     NOT NULL    UNIQUE,
          BOOKNAME      TEXT     NOT NULL,
          AUTHOR        TEXT     NOT NULL,
          REFERRAL      TEXT     NOT NULL,
          FLAG          INT      NULL);''')       #如果改变表格列名则需要修改
    conn.commit()
    conn.close()
    return("Table created/changed successfully")

#增加表格列
def increaseColumn():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("Alter Table Books ADD COLUMN  FLAG    INT    NULL")
    conn.commit()
    conn.close()
    return('Completed')

#录入书籍
def importBooks(uid,bookname,author,source): 
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    flag = 0
    c.execute("INSERT INTO Books (BOOKUID,BOOKNAME,AUTHOR,REFERRAL,FLAG) values ('{0}','{1}','{2}','{3}','{4}')".format(uid,bookname,author,source,flag))  #如果改变表格列名则需要修改
    conn.commit()
    print ("Records created successfully")
    cursor = c.execute("SELECT * from Books where BOOKUID=:uid and BOOKNAME=:bookname and REFERRAL=:source", {"uid": uid, "bookname": bookname, "source":source})    #如果改变表格列名则需要修改
    bookInfo = cursor.fetchone()
    conn.close()
    return bookInfo

#**************************88
def checkRepetition(bookuid):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("SELECT count(*) from Books where BOOKUID=:bookuid", {"bookuid": bookuid})
    result = cursor.fetchone()
    count = int(result[0])
    return count

#显示书籍信息
def seeBook(bookuid):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    count = checkRepetition(bookuid)
    if count == 0:
        bookInfo = 0
    if count > 0:
        cursor = c.execute("SELECT * from Books where BOOKUID=:bookuid", {"bookuid": bookuid})
        bookInfo = cursor.fetchone()
    conn.close()
    return bookInfo

    

#删除指定书籍
def deleteBook(a):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    a = 'null'
    cursor = c.execute("DELETE * from Books where BOOKNAME=:bookname", {"bookname": a})         #需要在all里定义username这个变量
    conn.commit()
    conn.close()
    return ('Successfully deleted book '+ bookname)

#清空该表格所有数据
def clearAll(Books):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DELETE from Books")
    conn.commit()
    conn.close()
    return ('Successfully deleted all data in table Books.')

#删除该表格 
def dropTable():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DROP table Books")
    conn.commit()
    conn.close()
    return ('Successfully deleted table Books.')

# a = dropTable()
# print(a)
# b = changeBooks()
# print(b)

    # for row in c:
    #     print ("ID = ", row[0])
    #     print ("PERSONUID = ", row[1])
    #     print ("PERSONNAME= ", row[2]),"\n"
    #     conn.close()


# sql = "select * from TableName where "+条件+" order by "+排序+" limit "+要显示多少条记录+" offset "+跳过多少条记录;
# 如: select * from Students limit 15 offset 20     表示: 从Students表跳过20条记录选出15条记录

#导出为csv文件
'''
def export():
    table = 'Books'
    now_time = dt.datetime.now().strftime('%F %T').replace(':','-').replace(' ','-')
    os.system('sqlite3 -header -csv Library.db "select * from Books;" >{0}_{1}.csv'.format(table,now_time))
    print('Do you want to check the table you exported? Type yes or no to continue.')
    answer = input('yes or no: ')
    while True:
        if answer == 'yes':
            df = pd.read_csv('{0}_{1}.csv'.format(table,now_time))
            df
        else:
            break
    return('Export completed.')
'''


#将Books表格中的flag取出来
def selectFlag(bookuid):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("SELECT FLAG FROM Books where BOOKUID=:bookuid", {"bookuid": bookuid})
    FLAG = cursor.fetchone()
    print(FLAG)
    return(FLAG[0])



#将Books表格中的flag改为1/0
def changeFlag(bookuid,flag):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("UPDATE Books SET FLAG=:flag where BOOKUID=:bookuid", {"flag":flag, "bookuid": bookuid})
    conn.commit()
    conn.close()
    print('Flag Change Completed')

def printTable():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * from Books")
    list1 = cursor.fetchall()
    print(list1)
    conn.close()