#產生一個隨機整數1~100(不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小
import random
r = random.randint(1, 100)
i = 0
while True:
    i = i + 1
    num = int (input('請輸入一個隨機整數1~100:'))
    if num == r:
        print('恭喜猜對了!')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('目前已猜次數為：', i)

