### Pythonのデコレータを理解するためのコード

## 函数内の同じ処理を行なっている部分をくくり出す。
## ---> ついに「デコレータ」を導入する！！

# デコレータ処理（函数）の定義（outerをそのまま流用する。）
def outer(func):
    # 函数内函数の定義
    def inner():
        print('==前処理を行います。==')

        # 被デコレート函数の処理
        func()

        print('==後処理を行います。==')

    # 入力の函数（引数func）に処理を追加した別の函数を返す！
    return inner


# メインの処理をする函数（デコレータをつける）
@outer
def operation():
    print('メインの処理を行います。')

@outer
def operation_2():
    print('２つ目の処理を行います。')


if __name__ == "__main__":
    # デコレータを利用したことで、普通の函数呼び出しと同じにできる！
    # 実際に実行されるのは、outer()の戻り値である函数inner()となる。
    operation()
    print()
    operation_2()
