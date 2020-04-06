import pandas as pd
import numpy as np
raw1=pd.read_csv('BW_sales_2016_may_2017_april.csv',engine='python')
raw2=pd.read_csv("BW_sales_2017_may_2018_apr.csv",engine='python')
raw3=pd.read_csv("BW_sales_2018_may_2019_apr.csv",engine='python')

raw=pd.concat([raw1,raw2,raw3])
raw=raw[raw['TradeNonTrade']=='T']
raw=raw[(raw['Material Group']=='W001')|(raw['Material Group']=='W002')]
raw['Billing Date']=pd.to_datetime(raw['Billing Date'])

'''conditions = [
    (raw['Billing Date'].day >=1) & (raw['Billing Date']<=10),
    (raw['Billing Date'].day >=11) & (raw['Billing Date'].day <=21),
    (raw['Billing Date'].day >21)]
choices = [1,2,3]
raw['Period'] = np.select(conditions, choices)'''

#conditions=[(raw['Billing Date'])]
def Cat(x):
    if x in range(0,11):
        return 1
    elif x in range(11,21):
        return 2
    elif x in range(21,32):
        return 3

raw['Period'] = raw['Billing Date'].apply(lambda x:Cat(x.day))



