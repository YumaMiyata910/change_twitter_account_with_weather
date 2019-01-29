# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import emoji
import requests
import json
import os

CK = os.environ.get('CK')                          # Consumer Key
CS = os.environ.get('CS')                          # Consumer Secret
AT = os.environ.get('AT')                          # Access Token
AS = os.environ.get('AS')                          # Accesss Token Secert
WEATHER_APP_ID = os.environ.get('WEATHER_APP_ID')  # Open Weathre Map API Key

# アカウント名変更用のURL
TWITTER_API_URL = 'https://api.twitter.com/1.1/account/update_profile.json'
# OpenWeatherMapの天気取得APIのURL
WEATEHR_API_URL = 'http://api.openweathermap.org/data/2.5/weather?q=Tokyo&appid='

def set_account_name(account_name):
	"""
	Twitterのアカウント名を更新する。

	Parameters
	----------
	account_name: str
		更新するアカウント名
	"""

	emoji_icon = get_tokyo_weather()
	# アカウント名の後ろに天気の絵文字をくっつける
	account_name += emoji_icon

	# nameに変更する名前を設定
	params = {'name': account_name}

	# OAuth認証で POST method で投稿
	twitter = OAuth1Session(CK, CS, AT, AS)
	req = twitter.post(TWITTER_API_URL, params = params)

	# レスポンスを確認
	if req.status_code == 200:
		print ("Changed Account!!")
	else:
		print ("Error: %d" % req.status_code)

def get_tokyo_weather():
	"""
	東京の天気から絵文字を生成して返す。

	Returns
	-------
	emoji_icon: str
		東京の天気の絵文字。
	"""

	weather_url = WEATEHR_API_URL + WEATHER_APP_ID

	response = requests.get(weather_url)
	data = json.loads(response.text)

	weather_id = int(data['weather'][0]['id'])
	emoji_icon = ''

	clear_id = [800]
	sunny_id = [801]
	cloudy_id = [802]
	bloken_cloudy_id = [803, 804]
	light_rain_id = [500]
	rain_id = [501]
	heavy_rain_id = [502, 503, 504, 511, 520, 521, 522, 531]
	drizzle_id = [300, 301, 302, 310, 311, 312, 313, 314, 321]
	thunderstorm_id = [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]
	snow_id = [600, 601, 602, 611, 612, 615, 616, 620, 621, 622]
	atmosphere_id = [701, 711, 721, 731, 741, 751, 761, 762, 771, 781]

	# 快晴
	if weather_id in clear_id:
		sun = emoji.emojize(':sun:', use_aliases=True)
		emoji_icon = sun
	# 晴れ
	elif weather_id in sunny_id:
		sun = emoji.emojize(':sun:', use_aliases=True)
		cloud = emoji.emojize(':cloud:', use_aliases=True)
		emoji_icon = sun + cloud
	# 曇り
	elif weather_id in cloudy_id:
		cloud = emoji.emojize(':cloud:', use_aliases=True)
		emoji_icon = cloud
	# 曇天
	elif weather_id in bloken_cloudy_id:
		cloud = emoji.emojize(':cloud:', use_aliases=True)
		emoji_icon = cloud + cloud
	# 小雨
	elif weather_id in light_rain_id:
		cloud = emoji.emojize(':cloud:', use_aliases=True)
		rain = emoji.emojize(':umbrella:', use_aliases=True)
		emoji_icon = cloud + rain
	# 雨
	elif weather_id in rain_id:
		rain = emoji.emojize(':umbrella:', use_aliases=True)
		emoji_icon = rain
	# 豪雨
	elif weather_id in heavy_rain_id:
		rain = emoji.emojize(':umbrella:', use_aliases=True)
		emoji_icon = rain + rain
	# 雷雨
	elif weather_id in thunderstorm_id:
		thunder = emoji.emojize(':zap:', use_aliases=True)
		rain = emoji.emojize(':umbrella:', use_aliases=True)
		emoji_icon = thunder + rain
	# 雪
	elif weather_id in snow_id:
		snow = emoji.emojize(':snowman:', use_aliases=True)
		emoji_icon = snow
	# 霧
	elif weather_id in atmosphere_id:
		foggy = emoji.emojize(':foggy:', use_aliases=True)
		emoji_icon = foggy
	# 霧雨
	elif weather_id in drizzle_id:
		foggy = emoji.emojize(':foggy:', use_aliases=True)
		rain = emoji.emojize(':umbrella:', use_aliases=True)
		emoji_icon = foggy + rain
	# 該当なし
	else:
		question = emoji.emojize(':question:', use_aliases=True)
		emoji_icon = question

	return emoji_icon


def main():
	account_name = u'アカウント名'  # 任意のアカウントを指定
	set_account_name(account_name)

if __name__ == '__main__':
	main()