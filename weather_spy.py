from urllib.request import urlopen
from bs4 import BeautifulSoup


# 获取明天的天气预报
# 101020800 上海青浦
# 101010100 北京
def getWeather():
    result = dict()
    # resp = urlopen('http://www.weather.com.cn/weather/101020800.shtml')
    resp = urlopen('http://www.weather.com.cn/weather1d/101010100.shtml')
    soup = BeautifulSoup(resp, 'html.parser').find('ul', class_="t clearfix").find('li', class_="sky skyid lv1")
    dates = soup.h1.string

    tagToday = soup.find('p', class_="tem")
    try:
        highTemp = tagToday.span.string
    except AttributeError as e:
        highTemp = tagToday.find_next('p', class_="tem").span.string

    lowTemp = tagToday.i.string
    weather = soup.find('p', class_="wea").string

    tagWind = soup.find('p', class_="win")
    windLevel = tagWind.i.string

    result["date"] = dates
    result["windL"] = windLevel
    result["lowT"] = lowTemp
    result["highT"] = highTemp
    result["weather"] = weather

    return result
