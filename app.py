from flask import Flask
app = Flask(__name__) # 建立 Flask 物件

# 建立路徑"/"的回應方式
@app.route('/')
def index(): # 回應函式
    return 'Hello, World!' # 回傳網站首頁內容

# 建立路徑"/data"的回應方式
@app.route('/data')
def data():
    return 'Data Page'

# 動態路由:建立路徑 /user/使用者名稱 的回應方式
@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return 'Hello, admin'
    else:
        return '你好, {}'.format(name)

# 啟動網站伺服器，可設定port參數
app.run(port=3000)