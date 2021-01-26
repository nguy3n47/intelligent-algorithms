"""
Created on PyCharm IDE
@author:    Nguy3n
@facebook:  https://www.facebook.com/nguyen.fit.hcmus
@github:    https://github.com/nguy3n47

"""


import math


# ------------------------ Exercise 1 ------------------------
def heron(a, b, c):
    return 0.25 * math.sqrt((a + b + c) * (a + b - c) * (b + c - a) * (c + a - b))


def isTriangle(a, b, c):
    p = a + b + c
    s = heron(a, b, c)
    if a < b + c and b < a + c and c < a + b:
        if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
            s = 0.5 * a * b
            print("Đây là tam giác vuông")
            print("Chu vi: ", p)
            print("Diện tích: ", s)
        elif a == b and b == c:
            p = a * 3
            s = a * a * math.sqrt(3) / 4
            print("Đây là tam giác đều")
            print("Chu vi: ", p)
            print("Diện tích: ", s)
        elif ((a * a == b * b + c * c and b == c) or (b * b == a * a + c * c and a == c) or
              (c * c == a * a + b * b and a == b)):
            p = a * 2 + c
            s = 0.5 * a * a
            print("Đây là tam giác vuông cân")
            print("Chu vi: ", p)
            print("Diện tích: ", s)
        elif a == b or a == c or b == c:
            p = a * 2 + c
            print("Đây là tam giác đều")
            print("Chu vi: ", p)
            print("Diện tích: ", s)
        else:
            print("Đây là tam giác thường")
            print("Chu vi: ", p)
            print("Diện tích: ", s)

    else:
        print("Ba cạnh a, b, c không phải là ba cạnh của một tam giác")


def exercise1():
    a = float(input("Nhập số nguyên dương a = "))
    b = float(input("Nhập số nguyên dương b = "))
    c = float(input("Nhập số nguyên dương c = "))
    isTriangle(a, b, c)


# ------------------------ Exercise 2 ------------------------
def electricityBill(money):
    if money < 0:
        return -1
    elif money <= 50:
        return money * 1.678 * 1.1
    elif 51 <= money <= 100:
        return money * 1.734 * 1.1
    elif 101 <= money <= 200:
        return money * 2.014 * 1.1
    elif 201 <= money <= 300:
        return money * 2.536 * 1.1
    elif 301 <= money <= 400:
        return money * 2.834 * 1.1
    elif money >= 401:
        return money * 2.927 * 1.1


def exercise2():
    a = int(input("Nhập chỉ số điện tháng trước = "))
    b = int(input("Nhập chỉ số điện tháng này = "))
    print("Tiền điện phải trả là: ", electricityBill(b - a))


# ------------------------ Exercise 3 ------------------------
def isPrimeNumber(n):
    # Số nguyên n < 2 không phải là số nguyên tố
    if n < 2:
        return False

    # Kiểm tra số nguyên tố khi n >= 2
    square_root = int(math.sqrt(n))
    for i in range(2, square_root + 1):
        if n % i == 0:
            return False
    return True


def exercise3():
    n = int(input("Nhập n = "))
    print("Dãy số nguyên tố bé hơn", n, ":", end=' ')
    for i in range(1, n - 1):
        if isPrimeNumber(i):
            print(i, end=' ')


# -------------------------- Menu --------------------------
print("18600187 - BTTH TUẦN 01")
print("1. Kiểm tra tam giác")
print("2. Tính tiền điện")
print("3. Số nguyên tố bé hơn n")
while True:
    choose = int(input("Chọn: "))
    if choose == -1:
        break
    if choose == 1:
        exercise1()
    elif choose == 2:
        exercise2()
    elif choose == 3:
        exercise3()
    else:
        print("Không hợp lệ!!")
    print("\nNhập -1 để thoát")
