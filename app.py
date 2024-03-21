from flask import Flask, request, redirect, url_for, render_template
import json
# 建立 Flask 物件
app = Flask(
    __name__,
    static_folder="public", # 靜態檔案資料夾
    static_url_path="/" # 靜態檔案網址路徑
)
# 所有在 public 資料夾內的檔案，都可以透過 / 網址路徑存取

# 建立路徑"/"的回應方式
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page')
def page():
    return render_template("page.html")
# # 建立路徑"/getSum"的回應方式
# # Query String 提供彈性 : /getSum?max=最大數字&min=最小數字
# @app.route('/getSum' )
# def getSum(): # min+(min+1)+(min+2)+...+max
#     min = int(request.args.get("min" , 1))
#     max = int(request.args.get("max" , 100))
#     result = 0
#     for n in range(min, max+1):
#         result += n
#     return "結果"+str(result)

# # 建立路徑"/"的回應方式
# @app.route('/')
# def index(): # 回應函式
#     # return redirect("/data") # 重新導向到 /data 路徑


#     # print("請求方法", request.method) # 取得請求方法(GET/POST/PUT/DELETE)
#     # print("請求網址", request.url) # 取得請求網址
#     # print("網址路徑", request.path) # 取得網址路徑
#     # print("主機名稱", request.host) # 取得主機名稱
#     # print("通訊協定", request.scheme) # 取得通訊協定
#     # print("瀏覽器作業系統", request.user_agent.platform) # 取得瀏覽器作業系統
#     # print("語言", request.headers.get("accept-language")) # 取得語言
#     # print("瀏覽器", request.user_agent.browser)
#     # print("瀏覽器版本", request.user_agent.version)
#     # print("引薦網址", request.referrer) # 取得引薦網址


#     # language = request.headers.get("accept-language")
#     # print("語言", language)
#     # if language.startswith("zh"):
#     #     return redirect("/zh")
#     # else:
#     #     return redirect("/en")
    
#     return render_template("index", name="Flask")
#     # 回傳網站首頁內容
        
# # 建立路徑"/zh"的回應方式
# @app.route('/zh')
# def zh():
#     return '歡迎來到網站'

# # 建立路徑"/en"的回應方式
# @app.route('/en')
# def en():
#     return 'Welcome to the website'


# # 建立路徑"/data"的回應方式
# @app.route('/data')
# def data():
#     return 'Data Page'

# # 動態路由:建立路徑 /user/使用者名稱 的回應方式
# @app.route('/user/<name>')
# def user(name):
#     if name == 'admin':
#         return 'Hello, admin'
#     else:
#         return '你好, {}'.format(name)

# 啟動網站伺服器，可設定port參數
app.run(port=3000)