from bs4 import BeautifulSoup 
import urllib.request as req
from datetime import datetime
import codecs
import subprocess
import csv
from reppy.robots import Robots

now = datetime.now().strftime("%Y/%m/%d %H:%M")

print("ユーザーIDを入力してください。")
userid = input()

url ='https://twitter.com/'

home = url
target = home + userid
userAgent = 'MyCralwer'
robotsUrl = Robots.robots_url(home)
robots = Robots.fetch(robotsUrl)
result = robots.allowed(target, userAgent)
print(result)
delay = robots.agent(userAgent).delay
print(delay)

res = req.urlopen(url+userid)

soup = BeautifulSoup(res, "lxml")

username = soup.find(class_='ProfileHeaderCard-name')

tweets = soup.find(class_='ProfileNav-item--tweets').find(class_='ProfileNav-value').string

following = soup.find(class_='ProfileNav-item--following').find(class_='ProfileNav-value').string

followers = soup.find(class_='ProfileNav-item--followers').find(class_='ProfileNav-value').string

favorite = soup.find(class_='ProfileNav-item--favorites').find(class_='ProfileNav-value').string

filename = "twitter-output/twitter-" +userid + ".text"

dataList = [(tweets.strip(),10),(following,10),(followers,10),(favorite,10)]

subprocess.call(['mkdir','twitter-output'])

print(	'【' + str(now) +'】\n'
		+" ユーザー名：" + username.text.strip() + " (@" + userid + ")" +'\n'
		+" ツイート数：" + tweets.strip() +'\n'
		+" フォロー　：" + following +'\n'
		+" フォロワー：" + followers +'\n'
		+" いいね数　：" + favorite  +'\n\n',file=codecs.open(filename, 'a', 'utf-8')
	)

<<<<<<< HEAD
# subprocess.call(['mkdir','twitter-output'])
# subprocess.call(['mv',filename,'./twitter-output/'+filename])
=======

subprocess.call(['mkdir','twitter-output'])
subprocess.call(['mv',filename,'./twitter-output/'+filename])
>>>>>>> master
