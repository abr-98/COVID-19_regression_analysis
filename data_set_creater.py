import pandas as pd
import numpy as np
import os

def create_data_set():
	if not os.path.exists("details_state"):
		os.makedirs("details_state")

	df=pd.read_csv('covid_19_india.csv', index_col=0)

	s_names=df['State/UnionTerritory'].unique()
	print(s_names)


	for name in s_names:
				print(name)
		#if not os.path.exists('details_state/{}.csv'.format(name)):
			#try:
				df_k=df[df['State/UnionTerritory']==name]
				df_k.sort_values('Date')
				
				df_k=df_k.drop(['Time','ConfirmedIndianNational','ConfirmedForeignNational'],axis=1)
				print(df_k.head())
				df_k.to_csv('details_state/{}.csv'.format(name))
			#except:
			#	print("Error")
			#	continue


create_data_set()



