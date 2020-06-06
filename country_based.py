import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os


def country_wide_var():
	df=pd.read_csv('covid_19_india.csv', index_col=0)
	df.sort_values('Date')
	
	df=df.drop(['State/UnionTerritory','Time','ConfirmedIndianNational','ConfirmedForeignNational'],axis=1)


	text=open('total_country.csv','w')
	text.write('Date,Cured,Confirmed,Deaths\n')
	text.close()


	dates=df['Date'].unique()
	text=open('total_country.csv','a')
	for date in dates:
		df_temp=df[df['Date']==date]
		cured=df_temp['Cured'].sum()
		confirmed=df_temp['Confirmed'].sum()
		Deaths=df_temp['Deaths'].sum()		

		text.write(date+','+str(cured)+','+str(confirmed)+','+str(Deaths)+'\n')

	text.close()
	df=pd.read_csv('total_country.csv',index_col=0)
	df.sort_values('Date')
	
	df.to_csv('total_country.csv',index=False)


def plot():
	df=pd.read_csv('total_country.csv',index_col=0)
	
	ax1=plt.subplot2grid((4,1), (0,0), rowspan=5, colspan=1)

	ax1.plot(df.index, df['Cured'], label="cured")
	ax1.plot(df.index, df['Confirmed'], label="Confirmed")
	ax1.plot(df.index, df['Deaths'], label="Deaths")
	plt.legend(loc="upper left")
	plt.xticks(rotation=90)

	plt.show()

def plot_corr():
	df=pd.read_csv('total_country.csv',index_col=0)
	df=df.T
	df_corr=df.corr()

	print(df_corr.head())

	data=df_corr.values
	fig=plt.figure()
	ax=fig.add_subplot(1,1,1)


	heatmap=ax.pcolor(data, cmap=plt.cm.RdYlGn)

	
	fig.colorbar(heatmap)

	

	ax.set_xticks(np.arange(data.shape[0])+ 0.5, minor=False)
	ax.set_yticks(np.arange(data.shape[1])+ 0.5, minor=False)

	ax.invert_yaxis()
	ax.xaxis.tick_top()

	
	columns_labels=df_corr.columns

	row_labels=df_corr.index



	ax.set_xticklabels(columns_labels)
	ax.set_yticklabels(row_labels)

	
	plt.xticks(rotation=90)

	heatmap.set_clim(0.85,1)
	

	plt.tight_layout()
	plt.show()


	fig=plt.figure()
	ax=fig.add_subplot(1,1,1)


	
plot_corr()
