import pandas as pd
sessions=pd.read_csv('data/raw/sessions.csv')
## 資料型別轉
## 1. 查看 session_start 欄位的資料型態


## 2.將 session_start 欄位轉成日期時間格式


## 3.顯示記錄期間即開始至結束


## 4.讀入 order_items.csv 檔指定給 order_items 變數

print('='*20)
## 5.查看 DataFrame 所有欄位的資料型態

print('='*20)
## 6.單存查看 unit_price 與 quantity 二欄位的資料型態


## 7.將 sessions 工作表 的 device 欄位 強制轉為數值欄位,若無法轉換則填入 NaN


## 8.字串清理,利用.str 存取器
## 8-1 將 campaign 欄位的內容 去頭尾空白,輸出為 temp3.csv


## 8-2 將 campaign 欄位的內容 去頭尾空白,輸出為 temp3.csv


## 8-3 查詢 campaign 欄位是否有包含 retarget 的值 ,輸出為 temp3.csv


## 8-4 查詢 符合 campaign 為 retarget 的記錄,只看 campaign 與 device　二欄位



print('='*30)
## 8-5 檢查 campaign 欄位是否有異常的類別 利用 unique 方法

