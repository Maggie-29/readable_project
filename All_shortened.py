import Utility

while True:
    a = int(Utility.mainMenu())
    
    if a == 1:            #录入书名与UID
        print(Utility.recordBooks())
        continue
   
    if a == 2:             #录入人名和UID
        print(Utility.recordUsers())
        continue
    
    if a == 3:             #借书流程
        print(Utility.borrowBooks())
        continue
    
    if a == 4:             #还书流程
        print(Utility.returnBooks())
        continue

    if a == 5:             #退出系统
        print('You have exited the system.')
        break
