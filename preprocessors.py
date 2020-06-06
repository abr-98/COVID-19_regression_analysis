import os
import pandas as pd
import numpy as np


def inp_mortality_tot():
	df=pd.read_csv('total_country.csv')

	mortal_rate=[]
	cured_rate=[]

	i=0

	while(i<len(df)):
		res=df.iloc[i]['Deaths']/df.iloc[i]['Confirmed']
		res_2=df.iloc[i]['Cured']/df.iloc[i]['Confirmed']

		mortal_rate.append(res)
		cured_rate.append(res_2)

		i+=1


	df['mortal_rate']=mortal_rate
	df['cured_rate']=cured_rate

	df.to_csv('total_country_mod.csv',index=False)

def state_wise_process():

	files=os.listdir('details_state')

	for file in files:
		name='details_state/'+file
		df=pd.read_csv(name)

		mortal_rate=[]
		cured_rate=[]

		i=0

		while(i<len(df)):
			res=df.iloc[i]['Deaths']/df.iloc[i]['Confirmed']
			res_2=df.iloc[i]['Cured']/df.iloc[i]['Confirmed']

			mortal_rate.append(res)
			cured_rate.append(res_2)

			i+=1


		df['mortal_rate']=mortal_rate
		df['cured_rate']=cured_rate

		df.to_csv(name,index=False)

def mark_rate_tot():
	confirm_rate=[]
	rec_rate=[]
	df=pd.read_csv('total_country_mod.csv')
	i=0
	while(i<len(df)):
		if i==0:
			res=0
			res2=0
		else:
			res=(df.iloc[i]['Confirmed']-df.iloc[i-1]['Confirmed'])/(df.iloc[i]['Confirmed'])
			try:
				res2=(df.iloc[i]['Cured']-df.iloc[i-1]['Cured'])/(df.iloc[i]['Cured'])
			except:
				res2=0

		confirm_rate.append(res)
		rec_rate.append(res2)

		i+=1


	df['confirmation_increase_rate']=confirm_rate
	df['cured_increase_rate']=rec_rate

	df.to_csv('total_country_mod.csv',index=False)


mark_rate_tot()



