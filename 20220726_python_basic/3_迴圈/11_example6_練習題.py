'''
*
* *
* * *
* * * *
* * * * *
'''
for i in range(5):     #外迴圈決定第幾列
    for j in range(i+1): #內迴圈決定第幾行
        print("* ", end="")
    print()

#比較快的方法也更推薦使用，可以用單迴圈處理就用單迴圈，但因本次教學主題為巢狀迴圈，故題目皆使用巢狀迴圈來處理
for i in range(5):
    print("* "*i)
