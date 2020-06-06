import pandas as pd


def get_index():
	active=[]
	df=pd.read_csv('total_state_data.csv')
	i=0
	while(i<len(df)):
		
	
		active.append(i)
		i+=1


	df['index']=active


	df.to_csv('total_state_data.csv',index=False)

get_index()
