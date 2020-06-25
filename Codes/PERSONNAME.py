import sqlite3
import os
#import pandas as pd
import datetime as dt 


#添加表格 & 修改列名
def changeUsers():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE Users             
         (ID  INTEGER PRIMARY KEY AUTOINCREMENT,
          PERSONUID       TEXT     NOT NULL   UNIQUE,
          PERSONNAME      TEXT     NOT NULL);''') 
    conn.commit()
    conn.close()
    return("Table created/changed successfully")



#录入人名
def importPeople(uid,personname): 
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("INSERT INTO Users (PERSONUID,PERSONNAME) values ('{0}','{1}')".format(uid, personname))
    conn.commit()
    print ("Records created successfully")
    cursor = c.execute("SELECT * from Users where PERSONUID=:uid and PERSONNAME=:personname", {"uid": uid, "personname": personname}) 
    (personid1, personuid1, personname1) = cursor.fetchone()
    conn.close()
    return (personid1, personuid1, personname1)

#********************************************************
def checkRepetition(useruid):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("SELECT count(*) from Users where PERSONUID=:useruid", {"useruid": useruid})
    result = cursor.fetchone()
    count = int(result[0])
    return count

#显示user信息
def seeUser(useruid):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    count = checkRepetition(useruid)
    if count == 0:
        userInfo = 0
    if count > 0:
        cursor = c.execute("SELECT * from Users where PERSONUID=:useruid", {"useruid": useruid})
        userInfo = cursor.fetchone()
    conn.close()
    return userInfo


#删除指定User
def deleteUser(username):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DELETE * from Users where PERSONNAME=:username", {"username": username} )        #需要在all里定义username这个变量
    conn.commit()
    conn.close()
    return ('Successfully deleted user '+ username)


#清空该表格所有数据
def clearAll(Users):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DELETE from Users")
    conn.commit()
    conn.close()
    return ('Successfully deleted all data in table Users.')

#删除该表格
def dropTable(Users):
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    cursor = c.execute("DROP table Users")
    conn.commit()
    conn.close()
    return ('Successfully deleted table Users.')
    



'''
def export():
    table = 'Users'
    now_time = dt.datetime.now().strftime('%F %T').replace(':','-').replace(' ','-')
    os.system('sqlite3 -header -csv Library.db "select * from Users;" >{0}_{1}.csv'.format(table,now_time))
    return('Do you want to check the table you exported? Type yes or no to continue.')
    answer = input('yes or no: ')
    while True:
        if answer == 'yes':
            df = pd.read_csv('{0}_{1}.csv'.format(table,now_time))
            df
        else:
            break
    return('Export completed.')'''