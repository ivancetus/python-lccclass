#開啟專案時，專案名稱不可以為中文
#開新python file時，可以使用中文檔名，但別讓其他老師看到
#人孔蓋：manholecover 專有名詞翻譯困難，可以用就用吧！
# '#'為註解說明，程式不執行
#在業界中，印出 hello world, 代表專案完成了一半
#底下的輸出視窗：日誌(log)除錯用的(debug)
#debug是程式設計師的天職
#師：直接改學生寫錯的code的老師會下地獄，話說的真重
# "字串" 直接打出來
# print(5/2.5)會做四則運算

print((100+2)/2)

'''
#為單行註解
多行註解 

資料格式 :
　　1. 字串
　　2. 數字
        a. 整數
        b. 小數
傳統語言 :(更優?)
    3/2 = 1 (整數/整數 = 整數)
    3/2.0 = 1.5 (整數/小數 = 小數)
Python :
    3/2 = 1.5 自動轉小數
'''
# //計算其商值
print(4/2)
print(4//2)

#輸入第三方套件
import math
print(math.sin(45*math.pi/180))
#弧度(徑度) pi/180 * 角度

#指數(冪次方)
print(10**3)
print(2**10)

#10開根號
print(10**0.5)
print(9**0.5)