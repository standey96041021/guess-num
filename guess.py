#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小
import random
start_num = int(input('請輸入開始數值:'))
end_num = int(input('請輸入結束數值:'))
r = random.randint(start_num, end_num)
count = 0
while True:
    count += 1 # count = count + 1
    num = int (input('請輸入一個隨機整數'))
    if num == r:
        print('恭喜猜對了!')
        print('這是您猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是您猜的第', count, '次')

