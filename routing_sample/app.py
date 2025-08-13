### 2-2 ルーティング/ 2-2-2 ルーティングとは pp.060 - 063
## リスト2.8に基づく。
from flask import Flask

# flaskインスタンスの生成
app = Flask(__name__)

## ルーティング
# URLアドレスと実行する関数との紐付けを実行処理の分だけ実装する。

# TOPページ
@app.route('/')
def index():
    return '<h1>トップページ</h1>'

# 一覧ページ
@app.route('/list')
def item_list():
    return '<h1>商品一覧ページ</h1>'

# 商品の詳細ページ
@app.route('/detail')
def item_detail():
    return '<h1>商品詳細ページ</h1>'


# 動作テスト
if __name__ == "__main__":
    # オプションで"debug"をTrueにすると、
    # デバッグモードとなり、コードの変更がサーバに反映される。
    app.run(debug = True)
