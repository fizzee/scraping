import csv
import datetime
import pytz
import statistics
import math
import glob
import subprocess

userid = "atk420t"

tmp = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
seven_days_ago = tmp - datetime.timedelta(weeks=1)

# [０ , １  , ２  , ３]
# [年 , 月 , 日 , 時間]
timedate = [tmp.year,tmp.month,tmp.day,tmp.hour]

filename = userid + "[" + str(timedate[0]) + "年" + str(timedate[1]) + "月" + "]" 

columns = ['取得日時' , 'ツイート数','フォロー数', 'フォロワー数', 'ファボ数']

tweets = []
following = []
followers = []
favorite = []


with open("day_tmp.csv","r") as f:
	reader = csv.reader(f)
	for row in reader:
		tweets.append(int(row[0].replace('.', ""),10))
		following.append(int(row[1].replace('.', ""),10))
		followers.append(int(row[2].replace('.', ""),10))
		favorite.append(int(row[3].replace('.', ""),10))

dateList = [str(timedate[0]) + " " + str(seven_days_ago.month) + "/" + str(seven_days_ago.day) + "/~" + str(timedate[1]) + "/" + str(timedate[2])  ,  int(sum(tweets)/len(tweets)),int(sum(following)/len(following)),int(sum(followers)/len(followers)),int(sum(favorite)/len(favorite))]

files = glob.glob("./*.csv")

if "./" + filename + "_weekdate.csv" in files:
	f = open(filename  + "_weekdate.csv", 'a')
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(dateList)
else :
	f = open(filename + "_weekdate.csv", 'a')
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(columns)
	writer.writerow(dateList)

subprocess.call(["rm","day_tmp.csv"])