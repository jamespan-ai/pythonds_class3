import pandas as pd
import numpy as np
sessions=pd.read_csv('data/raw/sessions.csv')
mobile=pd.read_csv('data/raw/Automobile.csv')

def column_health_report(df,table_name=''):
    '''產生一張欄位健康報表'''
    report=pd.DataFrame({
        '欄位':'coding',
        '型別':'coding',
        '非空數':'coding',
        '缺失數':'coding',
        '缺失率':'coding',
        '不重覆值':'coding'
    })
    ##標註風險等級
    report['風險']='低'
    report.loc[report['缺失率']>10,'風險']='中'
    report.loc[report['缺失率']>30,'風險']='高'
    print(f'\n=={table_name} 欄位健康報告 =====')
    print(report.to_string(index=False))
    report.to_csv('health.csv')
    return report
health=column_health_report(sessions,'sessions')
# 1.查看 mobile 工作表的欄位名稱


# 2.將欄位名稱有 -(減號) 全改為 _(底線) 


# 3.查看 mobile 工作表的欄位名稱


# 4.將 mobile 工作表的 ? 全部轉為 NaN 值


# 5.將 mobile 輸出為 mobile1.csv


# 6.查看資料結構


# 7.將 price,horse_power,peak_rpm 更為類型為int


# 8.查看資料結構

# 9.呼叫 column_health_report 函式

