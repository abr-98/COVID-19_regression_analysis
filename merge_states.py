import pandas as pd
import numpy as np

import os
import json

def merge():

	df=pd.read_csv('covid_19_india.csv', index_col=0)

	s_names=df['State/UnionTerritory'].unique()

	df_2=pd.read_csv('total_country_mod.csv')

	df3=df_2

	df3.to_csv('total_state_data.csv',index=False)

	with open('date_rec_mod.json', 'r') as ip: 
		data = json.load(ip) 

	
	for name in s_names:
		print(name)
		df3=pd.read_csv('total_state_data.csv')
		i=0
		confirmed=[]
		death=[]
		rec=[]
		while i<len(df3):
			date=df3.iloc[i]['Date']
			print(date)
			if data[date].get(name) is None:
				confirmed.append(0)
				death.append(0)
				rec.append(0)

			else:
				confirmed.append(data[date][name]['confirmed'])
				death.append(data[date][name]['death'])
				rec.append(data[date][name]['recovered'])

			i+=1
		df3[name+'_con']=confirmed
		df3[name+'_death']=death
		df3[name+'_rec']=rec

		df3.to_csv('total_state_data.csv',index=False)

merge()
				






