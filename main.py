import requests
s_city ="Moscow,RU"
appid ="5930f4c7fd9ece22ee82f1e6009c43dd"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   params={'q':s_city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print("видимость:", data['visibility'])
print("скорость ветра:", data['wind']['speed'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
for i in data['list']:
    print("Дата <", i['dt_txt'],"> \r\nскорость ветра<",'{0:+3.0f}'.format(i['wind']['speed']),"> \r\nвидимость <",i['visibility'],">")
    print("____________________________")