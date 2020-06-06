import pandas as pd


def get_active_cases():
	active=[]
	df=pd.read_csv('total_state_data.csv')
	i=0
	while(i<len(df)):
		
	
		res=df.iloc[i]['Confirmed']-df.iloc[i]['Cured']-df.iloc[i]['Deaths']
		active.append(res)

		i+=1


	df['active_cases']=active


	df.to_csv('total_state_data.csv',index=False)

get_active_cases()
