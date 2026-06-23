def count_word(s):
    result = {
        '英文字母': 0,
        '数字': 0,
        '空格': 0,
        '其他符号': 0
    }

    for char in s:
        if char.isalpha():
            result['英文字母'] += 1
        elif char.isdigit():
            result['数字'] += 1
        elif char.isspace():
            result['空格'] += 1
        else:
            result['其他符号'] += 1

    return result


user_input = input("请输入一段任意字符串: ")


stats = count_word(user_input)
print("统计结果如下:")
for key, value in stats.items():
    print(f"{key}: {value}")

with open("result.txt", "w", encoding="utf-8") as f:
    f.write("字符串统计结果:\n")
    for key, value in stats.items():
        f.write(f"{key}: {value}\n")

print("统计结果已成功写入 result.txt 文件。")