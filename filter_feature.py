import pandas as pd

def drop_date():
	active=[]
	df=pd.read_csv('total_state_data.csv')
	df=df.drop(['Date'],axis=1)

	df.to_csv('feature.csv',index=False)

drop_date()

