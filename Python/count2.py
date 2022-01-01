import ctypes
import numpy as np
import matplotlib.pyplot as plt
#bignumber = ctypes.CDLL("counter")
#bignumber.add.restype = ctypes.c_char_p
#str1 = ctypes.c_char_p(bytes("223", 'utf-8'))
#str2 = ctypes.c_char_p(bytes("2234234", 'utf-8'))
#a = bignumber.out_minus(str1, str2)
'''with open("./data.txt", 'r') as f:
    print(f.read())'''

def Pi():
    return np.pi
def E():
    return np.e
class BigNumber:
    _bignumber = ctypes.CDLL("counter")
    def __init__(self, num):
        self.num = str(num)
    def __str__(self):
        return self.num
    def __repr__(self):
        return self.num
    def check(self):  # 检查num是否是字符串格式
        if type(self.num) != str:
            try:
                self.num = str(self.num)
            except BaseException as fault:
                print(f"出现错误:{fault}，无法转化字符串")
            return self.num
        else:
            return self.num
    def __add__(self, other):  # 重载加法
        self._bignumber.out_add(ctypes.c_char_p(bytes((self.check()), 'utf-8')), ctypes.c_char_p(bytes((other.check()), 'utf-8')))
        try:
            with open("./data.txt", 'r') as file:
                answer1 = file.read()
        except BaseException as fault1:
            print(f"答案读取失败,出现错误:{fault1}\n正在尝试重新生成答案...")
        try:
            answer2 = str(eval(self.num + "+" + other.num))
        except BaseException as fault2:
            print(f"生成答案失败,出现错误:{fault2}")
        answer = BigNumber(answer1 if answer1 == answer2 else answer2)
        return answer
    def __sub__(self, other):  # 重载减法
        self._bignumber.out_minus(ctypes.c_char_p(bytes((self.check()), 'utf-8')), ctypes.c_char_p(bytes((other.check()), 'utf-8')))
        try:
            with open("./data.txt", 'r') as file:
                answer1 = file.read()
        except BaseException as fault1:
            answer1 = 0
            print(f"答案读取失败,出现错误:{fault1}\n正在尝试重新生成答案...")
        try:
            answer2 = str(eval(self.num + "-" + other.num))
        except BaseException as fault2:
            answer2 = 0
            print(f"生成答案失败,出现错误:{fault2}")
        answer = BigNumber(answer1 if answer1 == answer2 else answer2)
        return answer
    def __mul__(self, other):  # 重载乘法
        self._bignumber.out_times(ctypes.c_char_p(bytes((self.check()), 'utf-8')), ctypes.c_char_p(bytes((other.check()), 'utf-8')))
        try:
            with open("./data.txt", 'r') as file:
                answer1 = file.read()
        except BaseException as fault1:
            answer1 = 0
            print(f"答案读取失败,出现错误:{fault1}\n正在尝试重新生成答案...")
        try:
            answer2 = str(eval(self.num + "*" + other.num))
        except BaseException as fault2:
            answer2 = 0
            print(f"生成答案失败,出现错误:{fault2}")
        answer = BigNumber(answer1 if answer1 == answer2 else answer2)
        return answer
    def __truediv__(self, other):  # 重载实数除法
        self._bignumber.out_div(ctypes.c_char_p(bytes((self.check()), 'utf-8')), ctypes.c_char_p(bytes((other.check()), 'utf-8')))
        try:
            with open("./data.txt", 'r') as file:
                answer1 = file.read()
        except BaseException as fault1:
            answer1 = 0
            print(f"答案读取失败,出现错误:{fault1}\n正在尝试重新生成答案...")
        try:
            answer2 = str(round(eval(self.num + "/" + other.num), 4))
        except BaseException as fault2:
            answer2 = 0
            print(f"生成答案失败,出现错误:{fault2}")
        answer = BigNumber(answer1 if answer1 == answer2 else answer2)
        return answer

    def __pow__(self, power):
        self._bignumber.out_pow(ctypes.c_char_p(bytes((self.check()), 'utf-8')), ctypes.c_int(int(power.num)))
        try:
            with open("./data.txt", 'r') as file:
                answer1 = file.read()
        except BaseException as fault1:
            answer1 = 0
            print(f"答案读取失败,出现错误:{fault1}\n正在尝试重新生成答案...")
        try:
            answer2 = str(round(eval(self.num + "**" + str(power)), 4))
        except BaseException as fault2:
            answer2 = 0
            print(f"生成答案失败,出现错误:{fault2}")
        answer = BigNumber(answer1 if answer1 == answer2 else answer2)
        return answer
def tan(x):
    return BigNumber(str(np.tan(eval(x.num))))
def sin(x):
    return BigNumber(str(np.sin(eval(x.num))))
def cos(x):
    return BigNumber(str(np.cos(eval(x.num))))
def ln(x):
    return BigNumber(str(np.log(eval(x.num))))
def sqrt(x):
    return BigNumber(str(np.sqrt(eval(x.num))))

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
        if len(kh) == 0:  # 判断有没有右括号
            return "存在括号不匹配！"
        elif kh[len(string) - 1] == -1:  # 判断在存在右括号的前提下，最后一位有没有括号不匹配的情况
            return "存在括号不匹配！"
        else:
            return len(string) - 1,kh[len(string) - 1]
    except BaseException as fault:
        return fault

def chuli(string):
    formula = []
    num = ""
    string += '@'
    for i in range(len(string)):
        if ord(string[i]) <= ord('9') and ord(string[i]) >= ord('0'):
            num += string[i]
        else:
            if len(num) > 0:
                formula.append('BigNumber(' + num + ')')
                num = ""
            if string[i] == '×':
                formula.append('*')
            elif string[i] == '^':
                formula.append('**')
            elif string[i] == '÷':
                formula.append('/')
            elif string[i] == 'e':
                formula.append('BigNumber(' + str(E()) + ')')
            elif string[i] == 'π':
                formula.append('BigNumber(' + str(Pi()) + ')')
            else:
                formula.append(string[i])
    return ''.join(formula[0:-1])

def Fun(string):
    answer = eval(chuli(string))
    answer = '0' if abs(eval(answer.num)) < 1e-8 else answer
    return string, answer

def chuli2(string):
    string = string.replace('^','**').replace('π',str(Pi())).replace('×','*').replace('÷','/').replace('e',str(E()))
    return string

def drow(string):
    plt.clf()
    plt.grid()
    x = np.arange(-2*Pi(),2*Pi(), 0.1)
    try:
        y = eval(chuli2(string))
    except BaseException as falut:
        return f"表达式发生错误{falut}，请确保输入正确！" 
    try:
        if type(y) == int or type(y) == float or type(y) == type(sqrt(BigNumber(21))):  # 判断输入的表达式是不是常数表达式
            plt.plot(x, np.array([y for i in x]))
        else:
            plt.plot(x,y)
    except BaseException as falut:
        return f"绘图发生错误{falut}，请确保输入正确表达式！" 

if __name__ == "__main__":
    print('tan(123)+345÷345-123123×890 + π + 2^3=', Fun("tan(123)+345÷345-123123×890+π+2^3"))
    print(type(Fun("tan(123)+345÷345-123123×890+π")[1]))
    pass
