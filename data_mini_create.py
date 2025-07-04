import random

# 定义商品项
items = ['牛奶', '鸡蛋', '面包', '薯片', '爆米花', '啤酒', '黄油', '巧克力', '果汁', '奶酪']

# 随机生成交易数据
def generate_transactions(num_transactions, max_items):
    transactions = {}
    for i in range(1, num_transactions + 1):
        transaction_items = random.sample(items, random.randint(2, max_items))
        transactions[i] = transaction_items
    return transactions

# 打印数据集，格式类似1: 牛奶, 鸡蛋, 面包
def print_transactions(transactions):
    for key, value in transactions.items():
        print(f"{key}:{' '.join(value)}")

# 生成并打印交易数据集
num_transactions = 10000  # 设置交易数量
max_items = 10 # 设置每个交易的最大商品数量
transactions = generate_transactions(num_transactions, max_items)
print_transactions(transactions)

# 实现了新的功能 1
