#主页面显示的内容
import RFIDread
import BOOKNAME
import PERSONNAME
import allData
import printer

def mainMenu():
    print('''What do you want to print? 

type 1 if you want to put a book into the system, 
type 2 if you want to get a user card, 
type 3 if you want to borrow a book,
type 4 if you want to return a book
type 5 if you want to exit the system''')   
    a = input('please input numbers from 1-5: ')
    return a


#如果删除了db文件，就重新运行以下代码创建表格
def recreateTable():
    a = BOOKNAME.changeBooks()
    print(a)
    b = PERSONNAME.changeUsers()
    print(b)
    c = allData.changeAll()
    print(c)
    return(a,b,c)


#录入书名人名的函数  for 1 & 2
def recordBooks():
    while True:
        print("Please scan a book sticker first. Please finish in 15 seconds or you will go back to the main menu.")
        bookuid = RFIDread.read()
        if bookuid == -1:
            returnValue = 'You have quitted.'
            break
        whetherInUsers = PERSONNAME.checkRepetition(bookuid)
        if whetherInUsers > 0:
            print("Sorry, please don't scan a user card.")
            continue
        count = BOOKNAME.checkRepetition(bookuid)
        if count > 0:
            print('Sorry, the book has already been imported.')
            continue
        if count == 0:
            bookname = input('Please enter the name of the book: ')
            author = input('Who is the author? ')
            source = input('Where did you hear about this book? ')
            bookinfo = BOOKNAME.importBooks(bookuid,bookname,author,source)
            print(bookinfo)
            returnValue = 'You have successfully recorded a book.'
            answer = input("Do you want to add another one? Type 'yes' or 'no' to continue: ")
            if answer == 'yes':
                returnValue = 'You have successfully recorded those books.'
                continue
            else:
                break
    return returnValue


def recordUsers():
    while True:
        print("Please scan a user card first. Please finish in 15 seconds or you will go back to the main menu.")
        useruid = RFIDread.read()
        if useruid == '-1':
            returnValue = 'You have quitted.'
            break
        whetherInBooks = BOOKNAME.checkRepetition(useruid)
        if whetherInBooks > 0:
            print("Sorry, please don't scan a book sticker.")
            continue
        count = PERSONNAME.checkRepetition(useruid)
        if count > 0:
            print('Sorry, the user card has already been registered..')
            continue
        if count == 0:
            personname = input('And then please enter your name: ')
            userinfo = PERSONNAME.importPeople(useruid,personname)
            print(userinfo)
            returnValue = 'You have successfully recorded a user.'
            answer = input("Do you want to add another one? Type 'yes' or 'no' to continue: ")
            if answer == 'yes':
                continue
            else:
                break
    return returnValue

#借书流程
def borrowBooks():
    while True:
        print("Please scan your user card first. Please finish in 15 seconds or you will go back to the main menu.")
        useruid = RFIDread.read()
        if useruid == -1:
            returnValue = 'You have quitted.'
            break
        userInfo = PERSONNAME.seeUser(useruid)
        if userInfo == 0:
            print('Sorry, it is not a properly registered user card.')
            continue
        else:
            print('This is your user information: ' + str(userInfo))
            break
    while True:
        print("Scan the sticker of the book you want to borrow. Please finish in 15 seconds or you will go back to the main menu.")
        bookuid = RFIDread.read()
        if bookuid == -1:
            returnValue = 'You have quitted.'
            break
        bookInfo = BOOKNAME.seeBook(bookuid)
        if bookInfo == 0:
            print('Sorry, it is not an available book.')
            continue
        else:
            flag = int(BOOKNAME.selectFlag(bookuid))
            if flag == 1:
                print('Sorry, the book has already been borrowed.')
                answer = input("Do you want to borrow another book? Type 'yes' or 'no' to continue: ")
                record = 0
                if answer == 'yes':
                    continue
                else:
                    break
            if flag == 0:
                flag = 1
                print(BOOKNAME.changeFlag(bookuid,flag))
                record = allData.borrowBooks(userInfo,bookInfo)
                returnValue = 'You have successfully borrowed a book.'
                print(str(record))
                printer.printLine(record,flag)
                answer = input("Do you want to borrow another book? Type 'yes' or 'no' to continue: ")
                if answer == 'yes':
                    continue
                else:
                    break
    return returnValue


#还书流程
def returnBooks():
    while True:
        print("Please scan your user card first. Please finish in 15 seconds or you will go back to the main menu.")
        useruid = RFIDread.read()
        if useruid == -1:
            returnValue = 'You have quitted.'
            break
        userInfo = PERSONNAME.seeUser(useruid)
        if userInfo == 0:
            print('Sorry, it is not a properly registered user card.')
            continue
        else:
            print('This is your user information: ' + str(userInfo))
            break
    while True:
        print("Scan the sticker of the book you want to return. Please finish in 15 seconds or you will go back to the main menu.")
        bookuid = RFIDread.read()
        if bookuid == -1:
            returnValue = 'You have quitted.'
            break
        bookInfo = BOOKNAME.seeBook(bookuid)
        if bookInfo == 0:
            print('Sorry, it is not an available book.')
            continue
        else:
            flag = int(BOOKNAME.selectFlag(bookuid))
            if flag == 0:
                print('Sorry, the book has already been returned. ')
                answer = input("Do you want to return another book? Type 'yes' or 'no' to continue: ")
                if answer == 'yes':
                    continue
                else:
                    break
            if flag ==1:
                flag = 0
                print(BOOKNAME.changeFlag(bookuid,flag))
                record = allData.returnBooks(userInfo,bookInfo)
                print(str(record))
                deltatime = allData.Days(record)
                printer.printLine(record,flag,deltatime=deltatime)
                answer = input("Do you want to return another book? Type 'yes' or 'no' to continue: ")
                returnValue = 'You have successfully returned the book.'
                if answer == 'yes':
                    continue
                else:
                    break
    return returnValue


#显示最新的十条记录
    #  select * from (select ROW_NUMBER()over(order by TIME desc) rowId,* 
    #   from auto_AuctionRecords where Uid=353) as AuctionRecords

