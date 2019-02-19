import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import title, xlabel, ylabel
from pylab import axis
from pylab import plot,savefig
import glob
matplotlib.use('Agg')

follwer = []
time = []
files = glob.glob("./*.csv")

for file in files:
	time.clear()
	follwer.clear()
	with open(file,"r") as f:
		reader = csv.reader(f)
		print (reader)
		for row in reader:
			follwer.append(row[3])
			time.append(row[0])

	del follwer[0]
	del time[0]

	follwer = [int(i,10) for i in follwer]
	left = np.array(follwer)
	height = np.array(time)

	title("file")
	ylabel("follwer")
	xlabel("Time")
	plt.ylim([min(follwer)-5,max(follwer)+5])
	plt.plot(height,left, marker='o')
	plt.savefig("hoge"+'.png')

	print(time)
	print(follwer)



