import numpy as np

def Pi():
    return np.pi
def E():
    return np.e
def chuli(string):
    string = string.replace('^','**').replace('π',str(Pi())).replace('×','*').replace('÷','/').replace('e',str(E()))
    return string
def tan(x):
    return np.tan(x)
def sin(x):
    return np.sin(x)
def cos(x):
    return np.cos(x)
def ln(x):
    return np.log(x)
def sqrt(x):
    return np.sqrt(x)
def kh(string):
    kh = {}
    for i in range(len(string)):
        if string[i] == '(':
            num = 1
            for j in range(i + 1,len(string)):
                if string[j] == '(':
                    num += 1
                if string[j] == ')':
                    num -= 1
                if num == 0:
                    pivot = j
                    break
                else:
                    pivot = -1
            kh[pivot] = i
    try:
        if len(kh) == 0:  # 判断有没有右括号000
            return "存在括号不匹配！"
        elif kh[len(string) - 1] == -1:  # 判断在存在右括号的前提下，最后一位有没有括号不匹配的情况
            return "存在括号不匹配！"
        else:
            return len(string) - 1,kh[len(string) - 1]
    except BaseException as fault:
        return fault
def Fun(string):
    string = chuli(string)
    answer = eval(string)
    return string,answer

if __name__ == "__main__":
    print("请勿使用！")
