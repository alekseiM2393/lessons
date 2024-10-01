from random import randint
n = int(randint(3,20))
def password_true(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password


result = password_true(n)
print('пароль для:',n, result)
