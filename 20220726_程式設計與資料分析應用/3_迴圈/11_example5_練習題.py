'''
1  2  3  4  5  6  7  8  9
2  ..
3  ..
4  ..
5  ..
6  ..
7  ..
8  16 24 32 40 48 56 ...
9  18 27 36 45 54 63 72 81
九九乘法表
'''
for i in range(1,10):
    for j in range(1,10):
        print(f"{i*j:2d} ",end="") #:2d印兩個字元，不足則加空格，向右對齊
    print()

