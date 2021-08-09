import random
start = input('請輸入要數字範圍初始值')
end = input('請輸入數字範圍結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
print(r)
count = 0
while True:
    x = input('猜數字(二位數): ')
    x = int(x)
    count += 1
    if x == r:
    	print('終於猜對了!')
    	break
    elif x < r:
    	print('比答案小')
    elif x > r:
    	print('比答案大')
print('總共猜了', count, '次')
