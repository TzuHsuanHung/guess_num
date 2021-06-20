# 產生一個隨機整數1~100（不要印出來）
# 讓使用者重複輸入數字去猜
# 猜對的話 印出“終於猜對了！”
# 猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1, 100)
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
		print('你的回答比答案還小')
	elif r < n:
		print('你的回答比答案還大')
	print('這是你猜的第', count, '次')



