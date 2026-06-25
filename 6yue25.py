gold = 100  # 全局变量

def show_gold():
    # 只读取全局变量
    print("当前金币：", gold)

def buy_sword():
    # 修改全局变量
    global gold
    gold -= 30
    print("购买宝剑后金币：", gold)

def test_local():
    # 局部变量
    gold = 999
    print("局部金币：", gold)

print("程序开始")

show_gold()      # 读取全局变量

test_local()     # 创建局部变量

print("全局金币仍然是：", gold)

buy_sword()      # 修改全局变量

print("最终金币：", gold)