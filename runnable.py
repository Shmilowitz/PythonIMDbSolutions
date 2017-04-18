import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, operator

df = pd.read_csv('movies.csv',quotechar='"',skipinitialspace=True, delimiter=',')
data = df.as_matrix()

def HistLen(df):
	# Histogram of Length
	dfLen = df['length'].value_counts()
	dfLen.sort_index(inplace=True)
	dfLen = dfLen.loc[dfLen.index < 180]
	print(dfLen)
	# Plotting Histogram of Length
	axLen = dfLen.plot(kind='bar')
	# Set x-ticks every 10th
	ticks = axLen.xaxis.get_ticklocs()
	ticklabels = [l.get_text() for l in axLen.xaxis.get_ticklabels()]
	axLen.xaxis.set_ticks(ticks[::10])
	axLen.xaxis.set_ticklabels(ticklabels[::10])
	axLen.set_xlabel("Length")
	axLen.set_ylabel("Count")
	axLen.figure.savefig('LengthHist.png', bbox_inches='tight')

def HistRat(df):
	dfRat = df['rating'].value_counts()
	dfRat.sort_index(inplace=True)
	print(dfRat)
	#Plotting Histogram of Rating
	axRat = dfRat.plot(kind='bar')
	#Set x-ticks every 10th
	ticks = axRat.xaxis.get_ticklocs()
	ticklabels = [l.get_text() for l in axRat.xaxis.get_ticklabels()]
	axRat.xaxis.set_ticks(ticks[::10])
	axRat.xaxis.set_ticklabels(ticklabels[::10])
	axRat.set_xlabel("Rating")
	axRat.set_ylabel("Count")
	axRat.figure.savefig('RatingHist.png', bbox_inches='tight')
	
def HistYear(df):
	dfYear = df['year'].value_counts()
	dfYear.sort_index(inplace=True)
	print(dfYear)
	#Plotting Histogram of Rating
	axYear = dfYear.plot(kind='bar')
	#Set x-ticks every 10th
	ticks = axYear.xaxis.get_ticklocs()
	ticklabels = [l.get_text() for l in axYear.xaxis.get_ticklabels()]
	axYear.xaxis.set_ticks(ticks[::10])
	axYear.xaxis.set_ticklabels(ticklabels[::10])
	axYear.set_xlabel("Year")
	axYear.set_ylabel("Count")
	#Red line creation - Sound film/Colored film
	axYear.axvline(x=35, color='r', linestyle='--', ymin=0.25)
	axYear.text(36,1500,'Sound/Colored Film',rotation=90)
	#Blue line creation - WW2
	axYear.axvline(x=49, color='blue', linestyle='--', ymin=0.25)
	axYear.text(50,1500,'World War 2',rotation=90)
	axYear.figure.savefig('YearHist.png', bbox_inches='tight')
# HistLen(df)
HistRat(df)
# HistYear(df)