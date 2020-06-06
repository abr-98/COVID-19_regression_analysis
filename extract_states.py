import os
import pandas as pd
import json


def record_dates():
	df=pd.read_csv('total_country_mod.csv')
	dates=df['Date'].unique()

	date_rec={}

	for date in dates:
		date_rec[date]={}

	with open("date_rec.json","w") as op:
		json.dump(date_rec,op)





def record_state_data():
	record_dates()

	with open('date_rec.json', 'r') as ip: 
		data = json.load(ip) 

	files=os.listdir('details_state')

	for file in files:
		name='details_state/'+file
		print(name)
		confirmed=[]
		death=[]
		recovered=[]
		df=pd.read_csv(name)

		i=0

		while i<len(df):
			data[df.iloc[i]['Date']][file[:-4]]={}
			data[df.iloc[i]['Date']][file[:-4]]['confirmed']=int(df.iloc[i]['Confirmed'])
			data[df.iloc[i]['Date']][file[:-4]]['death']=int(df.iloc[i]['Deaths'])
			data[df.iloc[i]['Date']][file[:-4]]['recovered']=int(df.iloc[i]['Cured'])

			i+=1
	print(data)
	with open("date_rec_mod.json","w") as op:
		json.dump(data,op)

record_state_data()