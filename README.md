# Change Twitter Account With Weather Emoji!

### 前提
- Python3系
- pip3インストール済み

### 準備
以下コマンドで必要なモジュールをインストールしてください。
```bash
$ pip3 install emoji==0.5.0
$ pip3 install requests-oauthlib==0.8.0
```
また、APIに必要なトークンの取得してください。
- [Twitter API](https://developer.twitter.com/en.html)
- [OpenWeatherMap](https://openweathermap.org/)

### 利用方法
ソース上部のトークンを宣言している(XXXXXとなっている)部分に取得したAPIトークンを記載。
```python3
CK = 'XXXXXXXXXXXXXXXXXXXXXXXXX'                     # Consumer Key
CS = 'XXXXXXXXXXXXXXXXXXXXXXXXX'                     # Consumer Secret
AT = 'XXXXXXXXXXXXXXXXXXXXXXXXX'                     # Access Token
AS = 'XXXXXXXXXXXXXXXXXXXXXXXXX'                     # Accesss Token Secert
WEATHER_APP_ID = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Open Weathre Map API Key
```
main関数内のaccount_nameに任意のアカウント名を指定してください。  
``` python3
account_name = u'アカウント名'  # 任意のアカウントを指定
```
設定後、このファイルを実行することでアカウント名が変更されます。
```bash
$ python3 auto_change_name.py
```

### おまけ
AWS Lambdaなどを利用することで、  
定期的にアカウント名を変更することができます。
