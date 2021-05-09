import urllib.request,json,time

data = urllib.request.urlopen("https://api.bilibili.com/x/web-interface/card?mid=286429414")
xinxi = data.read().decode('utf-8')
dict = json.loads(xinxi)
fans = dict['data']['card']['fans']
t = time.strftime('%m-%d', time.localtime())

add_info = t + ',' + str(fans) + '\n'

with open('data.csv','a') as f:
    f.write(add_info)
    

from pandas import read_csv
import matplotlib.pyplot as plt

series = read_csv('data.csv',header=0, index_col=0, parse_dates=True, squeeze=True)

series.plot()
plt.xlabel('Date')

plt.savefig('粉丝数趋势.jpg', bbox_inches='tight', dpi=360, pad_inches=0)
#输出图片并去除白边