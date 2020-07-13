import re


def join_equation(equation_list, operator_list):
    for index, item in enumerate(equation_list):
        if index == 0:
            equation = item
        elif index != 0:
            equation += operator_list[index - 1] + item
    return equation


def mul_div_operation(equation):
    value_list = re.split("[*/]", equation)  # 数值
    operator_list = re.findall("[*/]", equation)  # 符号
    res = 0
    for index, item in enumerate(value_list):
        if index == 0:
            res = float(item)
        else:
            if operator_list[index - 1] == '*':
                res *= float(item)
            elif operator_list[index - 1] == '/':
                res /= float(item)
    return res


def plus_miuns_operation(equation):
    value_list = re.split("[+-]", equation)  # 数值
    operator_list = re.findall("[+-]", equation)  # 符号
    res = 0
    for index, item in enumerate(value_list):
        if index == 0:
            res = float(item)
        else:
            if operator_list[index - 1] == '+':
                res += float(item)
            elif operator_list[index - 1] == '-':
                res -= float(item)
    return res


def deal_mulordiv_minus(equation):
    is_minus = re.search("[0-9]+[.]*[0-9]*[*|/][-][0-9]+[.]*[0-9]*", equation)  # 匹配/- 和*-

    while is_minus:
        old = is_minus.group()
        new = "-" + old.replace("-", "")
        equation = equation.replace(old, new)
        equation = deal_double_operator(equation)  # 符号移位后去双重符号
        is_minus = re.search("[0-9]+[.]*[0-9]*[*|/][-][0-9]+[.]*[0-9]*", equation)

    if equation[0] == '-':
        equation = '0' + equation
    if equation[0] == '+':
        equation = equation[1:]

    return equation


def deal_double_operator(equation):
    # 双加减符号处理
    equation = equation.replace(" ", "")
    equation = equation.replace("++", "+")
    equation = equation.replace("+-", "-")
    equation = equation.replace("-+", "-")
    equation = equation.replace("--", "+")
    return equation


def base_operation(equation):
    # 符号合并
    equation = deal_double_operator(equation)
    # 负号预处理
    equation = deal_mulordiv_minus(equation)

    mul_div_list = re.split("[+-]", equation)  # 分割出乘除
    operator_list = re.findall("[+-]", equation)  # 加减号
    for index, item in enumerate(mul_div_list):
        mul_div_list[index] = str(mul_div_operation(item))  # 乘除运算
    equation = join_equation(mul_div_list, operator_list)
    equation = plus_miuns_operation(equation)  # 加减运算
    return equation


def brackets_operation(equation):
    equation.replace(" ", "")
    is_brackets = re.search("\([^()]*\)", equation)  # 匹配最小括号
    while is_brackets:
        temp_equation = is_brackets.group().strip("()")  # 去除括号
        result = base_operation(temp_equation)  # 计算括号内式子
        equation = equation.replace(is_brackets.group(), str(result))
        is_brackets = re.search("\([^()]*\)", equation)
    equation = base_operation(equation)
    return equation


def main():
    string = input("请输入需要运算的字符串：")
    print("计算结果是：" + str(brackets_operation(string)))


if __name__ == '__main__':
    main()
