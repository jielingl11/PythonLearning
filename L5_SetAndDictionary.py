# 集合的運算
s1={3,4,5}
print(3 in s1) # 判斷資料是否在集合中 output: True
print(10 in s1) # output: False
print(10 not in s1) # output: True

s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 # 交集: 取兩個集合中，相同的資料
print(s3) # output: {4, 5}

s4=s1|s2 # 聯集: 取兩個集合中的所有資料，但不重複選。|符號在enter的上方 
print(s4) # output: {3, 4, 5, 6, 7}

s5=s1-s2 # 差集: 從s1中，減去和s2重疊的部分 output: {3}
print(s5)

s6=s1^s2 # 反交集: 取兩個集合中，不重疊的部分 output: {3, 6, 7}
print(s6) 

s=set("Hello") # set(字串) output: {'o', 'e', 'l', 'H'} 無順序
print(s)
print("H" in s) # output: True

# 字典的運算: Key-Value 的配對
dic={"apple":"蘋果","data":"資料"}
print(dic["apple"]) # output: 蘋果

dic["apple"]= "小蘋果" # 更改對應資料 output: 小蘋果
print(dic["apple"])

print("apple"in dic) # 判斷key是否存在

del dic["apple"] #刪除字典中的鍵值對
print(dic)

dic={x:x*2 for x in [3,4,5]} # 從列表的資料產生字典
print (dic)
