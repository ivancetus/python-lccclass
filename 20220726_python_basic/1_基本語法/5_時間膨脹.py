c=299_792_458 # 光速 _作為千分位用 299.792.458 m/s 或 3e8 m/s = 3e5 km/s = 3e5*3600 km/hr
v=eval(input("請輸入速度(公里/小時): "))
# 可輸入 2e8 : 2*10^8
v=v*1000/3600 #由km/hr 轉 m/s
r=1/((1-v*v/(c*c))**0.5) # r=倍率, v<c, v不可超過光速, 會變虛數(根號裡為負數)
print(f"時間膨脹倍率: {r}")