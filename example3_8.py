import pandas as pd
sessions=pd.read_csv('data/raw/sessions.csv')
def column_health_report(df,table_name=''):
    '''產生一張欄位健康報表'''
    report=pd.DataFrame({
        '欄位':df.columns,
        '型別':df.dtypes.values,
        '非空數':df.notna().sum().values,
        '缺失數':df.isna().sum().values,
        '缺失率':(df.isna().sum()/len(df)*100).round(2).values,
        '不重覆值':df.nunique().values
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
