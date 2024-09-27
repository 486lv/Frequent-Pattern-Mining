import tkinter as tk
from tkinter import messagebox, font
from copy import deepcopy

def get_transactions(input_text):
    transactions = {}
    lines = input_text.strip().split('\n')
    for line in lines:
        try:
            transaction_id, items = line.split(":", 1)
            transaction_id = transaction_id.strip()
            items = [item.strip() for item in items.split(" ")]
            transactions[transaction_id] = items
        except ValueError:
            messagebox.showerror("输入错误", "输入格式错误，请重新输入。")
            return None
    return transactions

def get_unique(transactions):
    unique_item = set()
    for value_list in transactions.values():
        for item in value_list:
            unique_item.add(item)
    return unique_item

def my_Apriori(transactions, support_ratio, frequency):
    result = {}
    support = int(len(transactions) * support_ratio)
    uniquelist = get_unique(transactions)

    form = [[item] for item in uniquelist]
    form.sort(key=lambda x: x[0])

    for cnt in range(len(uniquelist)):
        reach_support = []
        for item in form:
            count = 0
            for itemset in transactions.values():
                if set(item).issubset(itemset):
                    count += 1
            if count >= support:
                reach_support.append((item, count))

        if len(reach_support):
            result[cnt + 1] = reach_support
            if frequency > 0 and cnt + 1 == frequency:
                return result

        support_len = len(reach_support)
        next_form = set()
        for i in range(support_len - 1):
            for j in range(i + 1, support_len):
                if reach_support[i][0][:-1] == reach_support[j][0][:-1]:
                    linked = deepcopy(reach_support[i][0][:-1])
                    a = reach_support[i][0][-1]
                    b = reach_support[j][0][-1]
                    if a < b:
                        linked += [a, b]
                    else:
                        linked += [b, a]
                    next_form.add(tuple(linked))

        if len(next_form) == 0:
            break

        if cnt == 0:
            form = [list(itemset) for itemset in next_form]
            continue

        form = []
        reach_support = [list(item[0]) for item in reach_support]
        for itemset in next_form:
            itemset = sorted(list(itemset))
            for item in itemset:
                temp = deepcopy(itemset)
                temp.remove(item)
                temp = tuple(temp)
                if temp not in reach_support:
                    break
            form.append(itemset)
        if len(form) == 0:
            break

    return result

def run_common_apriori():
    input_text = transactions_text.get("1.0", tk.END)
    transactions = get_transactions(input_text)
    if transactions is None:
        return

    try:
        support_ratio = float(support_entry.get())
        frequency = int(frequency_entry.get())
    except ValueError:
        messagebox.showerror("输入错误", "支持度和迭代次数必须是数字。")
        return

    result = my_Apriori(transactions, support_ratio, frequency)

    result_text.delete("1.0", tk.END)

    for key, value in result.items():
        one_patterns = []
        for itemset, count in value:
            one_patterns.append((itemset, count))
        one_patterns.sort(key=lambda x: x[1], reverse=True)
        result_text.insert(tk.END, f"频繁{key}项集：\n")
        for item, supports in one_patterns:
            result_text.insert(tk.END, f"{item},支持度：{supports}\n")

def run_sort_apriori():
    input_text = transactions_text.get("1.0", tk.END)
    transactions = get_transactions(input_text)
    if transactions is None:
        return

    try:
        support_ratio = float(support_entry.get())
        frequency = int(frequency_entry.get())
    except ValueError:
        messagebox.showerror("输入错误", "支持度和迭代次数必须是数字。")
        return

    result = my_Apriori(transactions, support_ratio, frequency)

    result_text.delete("1.0", tk.END)

    all_patterns = []
    for key, value in result.items():
        for itemset, count in value:
            all_patterns.append((itemset, count))

    all_patterns.sort(key=lambda x: x[1], reverse=True)

    for itemset, count in all_patterns:
        result_text.insert(tk.END, f"频繁项集：{itemset}，支持度：{count}\n")

def is_maximal(itemset, all_itemsets):
    for other_itemset in all_itemsets:
        if set(itemset).issubset(set(other_itemset)) and itemset != other_itemset:
            return False
    return True

def run_maximal_apriori():
    input_text = transactions_text.get("1.0", tk.END)
    transactions = get_transactions(input_text)
    if transactions is None:
        return

    try:
        support_ratio = float(support_entry.get())
        frequency = int(frequency_entry.get())
    except ValueError:
        messagebox.showerror("输入错误", "支持度和迭代次数必须是数字。")
        return

    result = my_Apriori(transactions, support_ratio, frequency)

    result_text.delete("1.0", tk.END)

    all_patterns = []
    for key, value in result.items():
        for itemset, count in value:
            all_patterns.append((itemset, count))

    maximal_patterns = [pattern for pattern in all_patterns if is_maximal(pattern[0], [p[0] for p in all_patterns])]
    maximal_patterns.sort(key=lambda x: x[1], reverse=True)

    for itemset, count in maximal_patterns:
        result_text.insert(tk.END, f"极大频繁项集：{itemset}，支持度：{count}\n")

def run_k_apriori():
    input_text = transactions_text.get("1.0", tk.END)
    transactions = get_transactions(input_text)

    if transactions is None:
        return

    try:
        support_ratio = float(support_entry.get())
        frequency = int(frequency_entry.get())
        k = int(knum.get())
    except ValueError:
        messagebox.showerror("输入错误", "支持度、迭代次数和k值必须是数字。")
        return

    result = my_Apriori(transactions, support_ratio, frequency)

    result_text.delete("1.0", tk.END)

    all_patterns = []
    for key, value in result.items():
        for itemset, count in value:
            all_patterns.append((itemset, count))

    all_patterns.sort(key=lambda x: x[1], reverse=True)

    for itemset, count in all_patterns[:k]:
        result_text.insert(tk.END, f"频繁项集：{itemset}，支持度：{count}\n")

# 创建主窗口
root = tk.Tk()
root.title("Apriori算法")

# 创建字体对象
bold_font = font.Font(weight="bold")

# 创建并展示加粗和部分文字变色的标签
text_widget = tk.Text(root, height=5, wrap="word")
text_widget.insert(tk.END, "输入事务集，每行一个事务，事务ID和事务项之间用")
text_widget.insert(tk.END, "冒号（英文:）", ("red",))
text_widget.insert(tk.END, "分隔，事务项之间用空格分隔。\n举例：1:I1 I2 I3\n2:面包 牛奶 鸡蛋\n3:りんご バナナ パイナップル")
text_widget.tag_configure("bold", font=bold_font)
text_widget.tag_configure("red", foreground="red")
text_widget.tag_add("bold", "5.0", "end")
text_widget.pack()

# 创建输入框和按钮
tk.Label(root, text="输入事务集：").pack()
transactions_text = tk.Text(root, height=10)
transactions_text.pack()

tk.Label(root, text="支持度阈值（0~1）：").pack()
support_entry = tk.Entry(root)
support_entry.pack()

tk.Label(root, text="迭代次数：").pack()
frequency_entry = tk.Entry(root)
frequency_entry.pack()

tk.Label(root, text="k：").pack()
knum = tk.Entry(root)
knum.pack()

tk.Button(root, text="运行Apriori算法,并按照频繁项集次序输出", command=run_common_apriori).pack()
tk.Button(root, text="运行Apriori算法,按支持度降序排列输出", command=run_sort_apriori).pack()
tk.Button(root, text="运行Apriori算法,输出极大频繁模式", command=run_maximal_apriori).pack()
tk.Button(root, text="运行Apriori算法,输出支持度最大的前k个频繁项集", command=run_k_apriori).pack()

tk.Label(root, text="结果：").pack()
result_text = tk.Text(root, height=10)
result_text.pack()

# 运行主循环
root.mainloop()
