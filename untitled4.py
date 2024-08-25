# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:08:36 2024

@author: ASUS
"""

N = int(input("nhập số nguyên dương có hai chữ số: "))
if 10 <= N <= 99:
    tong = (N//10)+ (N%10)
    print("Tổng các chữ số của N là: ", tong)