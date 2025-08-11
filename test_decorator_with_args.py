### Pythonのデコレータを理解するためのコード

## 函数内の同じ処理を行なっている部分をくくり出す。
## ---> 「デコレータ」を導入する！！

# デコレータ処理（函数）の定義（元の函数の引数を受け取るようにした）。
def outer(func):
    # 函数内函数の定義
    def inner(*args, **kwargs):
        print('==前処理を行います。==')

        # 被デコレート函数の処理
        func(*args, **kwargs)

        print('==後処理を行います。==')

    # 入力の函数（引数func）に処理を追加した別の函数を返す！
    return inner


# 処理をするデータ
nums = (10, 20, 30, 40)
user_dict = {'やまさん': 30, 'てっちゃん': 40, 'くまさん': 50}

# メインの処理をする函数（デコレータをつける）
@outer
def show_sum(nums):
    summary = 0
    for num in nums:
        summary += num

    print(f'{nums}の合計：{summary}')

@outer
def show_info(users):
    for name, age in users.items():
        print(f'名前：{name}、年齢：{age}')


if __name__ == "__main__":
    show_sum(nums)
    show_info(user_dict)
