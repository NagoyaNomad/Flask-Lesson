### Pythonのデコレータを理解するためのコード

## 函数内の同じ処理を行なっている部分をくくり出す。
## ---> 函数内函数を導入する！！

# メインの処理をする函数
def operation():
    print('メインの処理を行います。')

def operation_2():
    print('２つ目の処理を行います。')


# 函数を引数に取る函数を定義して、同じ処理をくくり出す！
def outer(func):
    # 函数内函数の定義
    def inner():
        print('==前処理を行います。==')

        # 実際の処理（これも函数内函数であることに注意！）
        func()

        print('==後処理を行います。==')

    # 入力の函数（引数func）に処理を追加した別の函数を返す！
    return inner


if __name__ == "__main__":
    # デコレータ処理を手動で行う。
    # Flask本ではなぜこのリストがあるのかわからなかったが、
    # 「入門Python3、O'Rilley」のデコレータの説明を読んで判った！
    result = outer(operation)
    result()

    result_2 = outer(operation_2)
    result_2()
