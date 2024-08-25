# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:12:52 2024

@author: ASUS
"""

a = float(input("nhập giá trị của a: "))
b = float(input("nhập giá trị của b: "))
A = ((a**(1/2)-b**(a/2))/(a**(1/4)-b**(1/4)))-((a**(1/2)+(a*b)**(1/4)+b**(1/4)))
print("phương trình có giá trị là: ", A)
print("kết quả: ", b**(1/4))