i = 0
x = 3
while i<3:
    i = i + 1
    password = input('請輸入密碼(最多三次)： ')
    if password == 'a123456':
        print('登入成功')
        break
    else:
        x = x - 1
        print('"密碼錯誤!還有', x, '次機會"')