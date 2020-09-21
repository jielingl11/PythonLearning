# 定義函式
# 函式內部的程式碼，若沒有呼叫函式，就不會執行
def multiply(n1, n2):
   # print (n1*n2)
    return n1*n2

# 呼叫函式
value= multiply (3,4)+ multiply (10,12)
print (value)
# multiply (3,4)
# multiply (10,12)

# 程式的包裝：同樣的邏輯，可以重複利用
def calculate(max):
    sum=0
    for i in range(1, max+1):
       sum = sum + i
    print(sum)

calculate(10)
calculate(20)

