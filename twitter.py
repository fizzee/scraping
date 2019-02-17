# coding: utf-8
from bs4 import BeautifulSoup 
import urllib.request as req
from datetime import datetime
import codecs
import subprocess
import csv
import glob
import datetime
import pytz

tmp = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))

weekday = weekday(tmp.year,tmp.month,tmp.day)

# [０ , １  , ２  , ３]
# [年 , 月 , 日 , 時間]
timedate = [tmp.year,tmp.month,tmp.day,tmp.hour]

columns = ['ユーザー名','取得日時' , 'ツイート数','フォロー数', 'フォロワー数', 'ファボ数']

dateList = []

print("ユーザーIDを入力してください。")
userid = "atk420t"

url ='https://twitter.com/'

res = req.urlopen(url+userid)

soup = BeautifulSoup(res, "lxml")

username = soup.find(class_='ProfileHeaderCard-name')

userdate = username.text.strip() + " (@" + userid + ")" 
dateList.append(userdate)

dateList.append(str(timedate[0]) + "年" + str(timedate[1]) + "月" + str(timedate[2]) + "日"+ str(timedate[3]) + "時")

tweets = soup.find(class_='ProfileNav-item--tweets').find(class_='ProfileNav-value').string
dateList.append(str(tweets))

following = soup.find(class_='ProfileNav-item--following').find(class_='ProfileNav-value').string
dateList.append(str(following))

followers = soup.find(class_='ProfileNav-item--followers').find(class_='ProfileNav-value').string
dateList.append(str(followers))

favorite = soup.find(class_='ProfileNav-item--favorites').find(class_='ProfileNav-value').string
dateList.append(str(favorite))

filename = userid + '.csv'
files = glob.glob("./*.csv") 

if "./"+ filename in files:
	f = open(filename, 'a')
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(dateList)
else :
	f = open(filename, 'a')
	writer = csv.writer(f, lineterminator='\n')
	writer.writerow(columns)
	writer.writerow(dateList)

f = open("tmp.csv", 'a')
writer = csv.writer(f, lineterminator='\n')
writer.writerow(dateList[2:6])

#1日の平均
if timedate[3] == 23:
	cmd = "Python3 week_average.py"
	subprocess.Popen(cmd.split())

#週の平均
if weekday == 0:
	cmd = "Python3 week_average.py"
	subprocess.Popen(cmd.split())