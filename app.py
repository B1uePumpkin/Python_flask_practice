from flask import Flask, request
# 建立 Flask 物件
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案資料夾
    static_url_path="/" # 靜態檔案網址路徑
)
# 所ˇ有在 public 資料夾內的檔案，都可以透過 / 網址路徑存取

# 建立路徑"/"的回應方式
@app.route('/')
def index(): # 回應函式
    print("請求方法", request.method) # 取得請求方法(GET/POST/PUT/DELETE)
    print("請求網址", request.url) # 取得請求網址
    print("網址路徑", request.path) # 取得網址路徑
    print("主機名稱", request.host) # 取得主機名稱
    print("通訊協定", request.scheme) # 取得通訊協定
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