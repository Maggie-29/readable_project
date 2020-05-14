import sqlite3
import os
# import pandas as pd
import datetime as dt 
import BOOKNAME

#添加表格 & 修改列名
def changeAll():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE allData             
         (ID  INTEGER PRIMARY KEY AUTOINCREMENT,
          TIME       TimeStamp NOT NULL DEFAULT (datetime('now','localtime')),
          PERSONUID       TEXT     NOT NULL,
          PERSONNAME      TEXT     NOT NULL,
          BOOKUID         TEXT     NOT NULL,
          BOOKNAME        TEXT     NOT NULL,
          FLAG            INT      NOT NULL,
          AUTHOR          TEXT     NULL,
          REFERRAL        TEXT     NULL);''')       #如果改变表格列名则需要修改
    conn.commit()
    conn.close()
    return("Table created/changed successfully")

#增加表格列
def increaseColumn():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("Alter Table allData ADD COLUMN REFERRAL    TEXT    NULL")
    conn.commit()
    conn.close()
    return('Completed')

def updateUsers():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("INSERT into allData(REFERRAL) select REFERRAL from Books")
    conn.commit()
    conn.close()
    return ('Successfully updated all users.')


#借书流程
def borrowBooks(userInfo,bookInfo): 
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("INSERT INTO allData (PERSONUID,PERSONNAME,BOOKUID,BOOKNAME,AUTHOR,REFERRAL,FLAG) values (?,?,?,?,?,?,?)", (userInfo[1],userInfo[2],bookInfo[1],bookInfo[2],bookInfo[3],bookInfo[4],1))
    conn.commit()
    print ("Records created successfully")
    cursor = c.execute("SELECT * from allData where PERSONUID=:useruid and BOOKUID=:bookuid and FLAG=1 order by ID desc", {"useruid": userInfo[1], "bookuid": bookInfo[1]})    #如果改变表格列名则需要修改
    result = cursor.fetchone()
    conn.close()
    # return (userInfo[2],bookInfo[2])
    return(result)

#还书流程
def returnBooks(userInfo,bookInfo): 
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("INSERT INTO allData (PERSONUID,PERSONNAME,BOOKUID,BOOKNAME,AUTHOR,REFERRAL,FLAG) values (?,?,?,?,?,?,?)", (userInfo[1],userInfo[2],bookInfo[1],bookInfo[2],bookInfo[3],bookInfo[4],0))
    conn.commit()
    print ("Records created successfully")
    cursor = c.execute("SELECT * from allData where PERSONUID=:useruid and BOOKUID=:bookuid and FLAG=0 order by ID desc", {"useruid": userInfo[1], "bookuid": bookInfo[1]})    #如果改变表格列名则需要修改
    result = cursor.fetchone()
    conn.close()
    # return (userInfo[2],bookInfo[2])
    return(result)

#删除指定借书记录
def deleteRecord(userInfo,bookInfo):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DELETE * from allData where PERSONUID=:useruid and BOOKUID=:bookuid", {"useruid": userInfo[1], "bookuid": bookInfo[1]})        #需要在all里定义username这个变量
    conn.commit()
    conn.close()
    return ('Successfully deleted the record')


#清空该表格所有数据
def clearAll():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DELETE from allData")
    conn.commit()
    conn.close()
    return ('Successfully deleted all data in table allData.')

#删除该表格
def dropTable():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DROP table allData")
    conn.commit()
    conn.close()
    return ('Successfully deleted table Users.')

# 查询表中是否有uid
# def check(uid):
    # c.execute("select isnull((select top(1) 1 from Books where uid), 0)")


#def export():
    #table = 'allData'
    #now_time = dt.datetime.now().strftime('%F %T').replace(':','-').replace(' ','-')
    #os.system('sqlite3 -header -csv Library.db "select * from allData;" >{0}_{1}.csv'.format(table,now_time))
    #print('Do you want to check the table you exported? Type yes or no to continue.')
    #answer = input('yes or no: ')
    #while True:
        #if answer == 'yes':
            #df = pd.read_csv('{0}_{1}.csv'.format(table,now_time))
            #print(df)
            #break
        #else:
            #break
    #return('Export completed.')

# a = dropTable()
# print(a)

# b = changeAll()
# print(b)

def updateValue(input):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("SELECT AUTHOR from Books where BOOKNAME=:input", {"input": input})
    author = cursor.fetchone()
    print(author)
    cursor = c.execute("UPDATE allData SET AUTHOR=:author where BOOKNAME=:input", {"author":author[0],"input": input})
    conn.commit()
    conn.close()
    return('Completed')

def Days(record):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("SELECT * from allData where PERSONUID=:useruid and BOOKUID=:bookuid and FLAG=0 order by ID desc", {"useruid": record[2], "bookuid": record[4]})
    returnRecord = cursor.fetchone()
    returnTime = dt.datetime.strptime(returnRecord[1], '%Y-%m-%d %H:%M:%S')
    cursor = c.execute("SELECT * from allData where PERSONUID=:useruid and BOOKUID=:bookuid and FLAG=1 order by ID desc", {"useruid": record[2], "bookuid": record[4]})
    borrowRecord = cursor.fetchone()
    borrowTime = dt.datetime.strptime(borrowRecord[1], '%Y-%m-%d %H:%M:%S')
    delta = returnTime - borrowTime
    return delta.days
    

# b = updateValue('创新者的窘境')
# print(b)
# a = export()
# print(a)