# 有序可變動列表 List
grades=[99,85,77,63,15]

print(grades) # output:[99,85,77,63,15]

print(grades[3]) # output: 63

grades[0]=55 # 把55放到列表中的第一個位置 output:[55,85,77,63,15]
print(grades) 

print(grades[1:4]) # 取得列表中開頭不含結尾 output:[85,77,63]

grades[1:4]=[] # 連續刪除列表從編號1到3 output:[55,15]
print(grades)

grades=grades+[12,33] # 列表串接 output:[55,15,12,33]
print(grades)

print(len(grades)) # 取得列表的長度 len(列表資料)
length=len(grades)
print(length)

data=[[3,4,5],[6,7,8]] # 巢狀列表
print(data[0][2]) # 取得[第一層][第二層] output:5

data[0][0:2]=[5,5,5] #替換資料 output:[[5,5,5,5][6,7,8]]
print(data)

# 有序不可動列表 Tuple
weight=(52,47,84)
# weight[0]=42 錯誤！tuple的資料不可變動
print(weight) 
