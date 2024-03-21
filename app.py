from flask import Flask
app = Flask(__name__) # 建立 Flask 物件

# 建立首頁回應方式
@app.route('/')
def index(): # 首頁回應函式
    return 'Hello, World!' # 回傳網站首頁內容

# 啟動網站伺服器，可設定port參數
app.run(port=3000)