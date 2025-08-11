### Pythonのデコレータを理解するためのコード

## 函数内の同じ処理を行なっている部分をくくり出す。
## ---> 函数を引数とする函数を導入する！

# メインの処理をする函数
def operation():
    print('メインの処理を行います。')

def operation_2():
    print('２つ目の処理を行います。')


# 函数を引数に取る函数を定義して、同じ処理をくくり出す！
def outer_process(func):
    print('==前処理を行います。==')

    func()

    print('==後処理を行います。==')


if __name__ == "__main__":
    outer_process(operation)
    outer_process(operation_2)
