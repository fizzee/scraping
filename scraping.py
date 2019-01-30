from bs4 import BeautifulSoup 
import urllib.request as req
from reppy.robots import Robots


# Trueが返されればスクレイピングしてもOK。
# ※利用規約に禁止が明記されている可能性でもTrueが返されてしまうことがある。
# Crawl_delayが設定されていない場合にはNoneが返される。	

print("確認したいURLを入力してください(https://以下)")
url = 'https://'
url += input()
print(url)
home = url
target = url
userAgent = 'MyCralwer'
robotsUrl = Robots.robots_url(home)
robots = Robots.fetch(robotsUrl)
result = robots.allowed(target, userAgent)
print(result)
delay = robots.agent(userAgent).delay
print(delay)