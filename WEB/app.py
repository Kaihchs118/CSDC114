from flask import Flask, request
 
app = Flask(__name__) # __name__ 參數通常設為當前模組的名稱
 
@app.route('/')  # 進到 '/' 時則執行 index 函式
def index():
    return "Hello, World!"  # Hello World'

@app.post('/hello') # POST 方法
def postHello():
    data = request.get_json() # 取得 POST 資料，並轉換為 JSON 格式
    return "Hello, " + data['name'] + "!"

@app.get('/hello/<name>/<message>') # 帶參數的路由
def helloName(name,message):
    return "Hello, " + name + "!"+ message
 
if __name__ == '__main__':  # 直接呼叫這個檔案時才執行
    app.run(debug=True)  # 啟動 Flask 伺服器，開啟 debug 模式方便除錯
    


