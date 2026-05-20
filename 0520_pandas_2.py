# 0520_pandas_2.py

import pandas as pd

# ===== 使用「字典」建立 DataFrame =====
data_dict = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df_dict = pd.DataFrame(data_dict)

# ===== 使用「列表（子列表）」建立 DataFrame =====
data_list = [
    ["Apple", 30, 100],
    ["Banana", 20, 150],
    ["Orange", 25, 80],
    ["Mango", 60, 60],
    ["Grape", 45, 90],
    ["Guava", 35, 54]
]

df_list = pd.DataFrame(data_list, columns=["Product", "Price", "Sales"])

# ===== 顯示前5筆與後5筆 =====
print(df_dict.head())
print(df_dict.tail())

# ===== 資料基本資訊 =====
print(df_dict.shape)
print(df_dict.columns)

print(df_dict.dtypes)
print(df_dict.count())

# ===== 數值統計資訊 =====
stats = df_dict.describe()

# 四捨五入到小數2位
stats = stats.round(2)

print(stats)

# 存檔
stats.to_csv("0520_stock2.csv")