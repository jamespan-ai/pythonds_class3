import pandas as pd
sessions=pd.read_csv('data/raw/sessions.csv')
def lesson3(sessions)->None:
    print('Lesson 3:profiling,missing value,dtype,datetime')
    ## 1.查看所有欄位的型別
    
    print('='*30)
    ## 2.查看 campaign 欄的前五大類別
    

    print('='*30)
    ## 3.將 session_start 從字串轉為 datetime
    

    print('='*30)
    ## 4.印出資料覆蓋的時間範圍
    
lesson3(sessions)