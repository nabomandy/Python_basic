# 날짜데이터
import pandas as pd

dates = pd.date_range('20210101', periods=6)
dates

df = pd.DataFrame({ "count1" : [10,2,3,1,5,1 ], 
                    "count2" : [1,2,4,6,7,8 ],  
                     # "date" : dates  })
                  },  index = dates )
df

df.index

df.columns

df['20210102' : '20210104']

df.loc['20210102':'20210104',['count1']]