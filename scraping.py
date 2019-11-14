# scraping
Scraping_website


import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

name = []
shokusyu_list = []
cmp_list = []
pay_list = []

for page in range(1,3): #ここでページ数を設定。parameterの2個目を変更でページ数を増やす。今は1,2ページ目を読み込み
  url = "https://hw.workport.co.jp/search/area-24/job-1/?p=" + str(page)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  time.sleep(3) #とりあえずここで3秒のインターバル


  titles = soup.find_all('p', {'class' : 'title com_sp'})
  for title in titles:
    name.append(title.string)


  shokusyus = soup.find_all('h2', {'class' : 'shokusyu'})
  for shokusyu in shokusyus:
    shokusyu_list.append(shokusyu.string)


  cmp_names = soup.find_all('p', {'class' : 'cmp_name com_pc'})
  for cmp_name in cmp_names:
    cmp_list.append(cmp_name.string)

  i = 1
  pays = soup.find_all('dl', {'class' : 'pay'})
  for pay in pays:
    if i%2 != 0:
      pay_list.append(pay.dd)
    i += 1
  time.sleep(3) #上記のループの前に3秒のインターバル

df = pd.DataFrame({"Title":name, "Shokusyu":shokusyu_list, "Company":cmp_list, "Payment":pay_list})
df
