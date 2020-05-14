
def main():
    print('''What do you want to print? 

type 1 if you want to put a book into the system, 
type 2 if you want to get a user card, 
type 3 if you want to borrow a book,
type 4 if you want to return a book
type 5 if you want to exit the system''')   

#如果删除了db文件，就重新运行以下代码创建表格
# from BOOKNAME import changeBooks
# a = changeBooks()
# print(a)
# from PERSONNAME import changeUsers
# b = changeUsers()
# print(b)

while True:
    main()
    a = int(input())

    #录入书名与UID
    if a == 1:
        while True:
            print('Please scan a sticker first and then enter the name of the book')
            from RFIDread import read
            uid = read()
            bookname = input()
            from BOOKNAME import importBooks
            (bookid, bookuid, bookname) = importBooks(uid,bookname)
            print(bookid, bookuid, bookname)
            print("Do you want to add another one? Type 'yes' or 'no' to continue")
            answer = input()
            if answer == 'yes':
                continue
            else:
                break
        continue

    #录入人名和UID
    if a == 2:
        while True:
            print('Please scan a sticker first and then enter your name')
            from RFIDread import read
            uid = read()
            personname = input()
            from PERSONNAME import importPeople
            (personid, personuid, personname) = importPeople(uid,personname)
            print(personid, personuid, personname)
            print("Do you want to add another one? Type 'yes' or 'no' to continue")
            answer = input()
            if answer == 'yes':
                continue
            else:
                break
        continue

    #借书流程
    if a == 3:
        print('Please scan your user card first.')
        from RFIDread import read
        useruid = read()
        from PERSONNAME import seeUser
        userInfo = seeUser(useruid)
        print('This is your user information: ' + str(userInfo))
        while True:
            print('Then scan the sticker of the book you want to borrow.')
            bookuid = read()
            from BOOKNAME import seeBook
            bookInfo = seeBook(bookuid)
            from allData import borrowBooks
            record = borrowBooks(userInfo,bookInfo)
            print(str(record) + "Do you want to borrow another book? Type 'yes' or 'no' to continue")
            answer = input()
            if answer == 'yes':
                continue
            else:
                break
        continue

    #借书流程
    if a == 4:
        print('Please scan your user card first.')
        from RFIDread import read
        useruid = read()
        from PERSONNAME import seeUser
        userInfo = seeUser(useruid)
        print('This is your user information: ' + str(userInfo))
        while True:
            print('Then scan the sticker of the book you want to return.')
            bookuid = read()
            from BOOKNAME import seeBook
            bookInfo = seeBook(bookuid)
            from allData import returnBooks
            record = returnBooks(userInfo,bookInfo)
            print(str(record) + "Do you want to return another book? Type 'yes' or 'no' to continue")
            answer = input()
            if answer == 'yes':
                continue
            else:
                break
        continue

    #退出系统
    if a == 5:
        print('You have exited the system.')
        break


#显示最新的十条记录
    #  select * from (select ROW_NUMBER()over(order by TIME desc) rowId,* 
    #   from auto_AuctionRecords where Uid=353) as AuctionRecords