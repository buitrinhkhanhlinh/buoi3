# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 07:39:51 2024

@author: ASUS
"""

a = int(input("nhập số thứ nhất:"))
b = int(input("nhập số thứ hai:"))
Tổng = a + b
print("Tổng của hai số là: ", Tổng)
if a > b:
    h = a - b
    print("Hiệu của a, b là:", h)
else:
    h = b - a
    print("Hiệu của b, a là:", h)
T = a/b
print("Thương của hai số là: ", round(T, 3))
CD = a % b
print("chia lấy dư của hai số là: ", CD)
CN = a//b
print("chia lấy nguyên hai số là: ", CN)

    


