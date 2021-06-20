# 產生一個隨機整數1~100（不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話 印出“終於猜對了！”
# 猜錯的話 要告訴他 比答案大/小

import random
start = input('請輸入起始數字')
end = input('請輸入結束數字')
start=int(start)
end=int(end)

r = random.randint(start, end)
count = 0

while True:
	count += 1 # count = count + 1
	n = input('請猜數字：')
	n = int(n) # number數字
	if n == r:
		print('終於猜對了！')
		print('這是你猜的第', count, '次')
		break
	elif r > n:
		print('再往上猜')
	elif r < n:
		print('再往下猜')
	print('這是你猜的第', count, '次')



