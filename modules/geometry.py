# 在 geometry 模組中，定義集合運算功能
# 計算兩個點的距離
def distance (x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

# 計算線段的斜率
def slope (x1,y1,x2,y2):
    return (y1-y2)/(x1-x2)