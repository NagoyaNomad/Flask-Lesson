### 2-2 ルーティング/ 2-2-3 動的ルーティングとは pp.064 - 067
## リスト2.9に基づく。
from flask import Flask

# flaskインスタンスの生成
app = Flask(__name__)

## ルーティング
# コンバータなし
@app.route('/dynamic/<value>')
def dynamic_default(value):

    # 受け取った値のコンソールへの表示
    print(f'型：{type(value)}、値：{value}')

    # ルーティング函数の戻り値はブラウザに表示される。
    return f'<h2>渡された値は「{value}」です。</h2>'

# コンバータあり
@app.route('/dynamic2/<int:number>')
def dynamic_converter(number):
    print(f'型：{type(number)}、値：{number}')

    if number % 2 == 0:
        return f'<h2>渡された値{number}は偶数です。</h2>'
    else:
        return f'<h2>渡された値{number}は奇数です。</h2>'

# コンバータあり、複数値渡し
@app.route('/dynamic3/<value>/<int:number>')
def dynamic_converter_mutiple(value, number):
    print(f'型：{type(value)}、値：{value}')
    print(f'型：{type(number)}、値：{number}')
    return f'<h2>渡された値は「{value}と{number}」です。</h2>'


if __name__ == "__main__":
    app.run(debug = True)
