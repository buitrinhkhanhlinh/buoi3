import math

def tinh_bieu_thuc(a, b):
    
    can_a = math.sqrt(a)
    can_b = math.sqrt(b)
    canbon_a = math.sqrt(math.sqrt(a))
    canbon_b = math.sqrt(math.sqrt(b))
    
   
    tu1 = can_a - can_b
    mau1 =  canbon_a - canbon_b
    
    tu2 = can_a + math.pow(a * b, 1/4)
    mau2 = canbon_a +  canbon_b

    ket_qua = (tu1 / mau1) - (tu2 / mau2)
    
    return ket_qua

a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
ket_qua = tinh_bieu_thuc(a, b)
print (ket_qua)