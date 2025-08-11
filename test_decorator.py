### Pythonのデコレータを理解するためのコード

## デコレータ適用前の函数とその実行

def operation():
    print('前処理を行います。')

    print('メインの処理を行います。')

    print('後処理を行います。')

def operation_2():
    print('前処理を行います。')

    print('２つ目の処理を行います。')

    print('後処理を行います。')


if __name__ == "__main__":
    operation()
    operation_2()
