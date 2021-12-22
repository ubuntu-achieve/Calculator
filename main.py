import sys
from GUI import Ui_Form
import count
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow



class Form(QWidget, Ui_Form):
    string = ''  # 用于存放给用户展示的字符串
    lineput = ''  # 用于存放计算用的字符串
    def __init__(self):
        super(Form, self).__init__()  # 继承父类的init方法
        self.setupUi(self)
    def pb_0(self):
        self.lineput += '0'
        self.string+='0'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_1(self):
        self.lineput += '1'
        self.string+='1'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_2(self):
        self.lineput += '2'
        self.string+='2'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_3(self):
        self.lineput += '3'
        self.string+='3'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_4(self):
        self.lineput += '4'
        self.string+='4'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_5(self):
        self.lineput += '5'
        self.string+='5'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_6(self):
        self.lineput += '6'
        self.string+='6'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_7(self):
        self.lineput += '7'
        self.string+='7'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_8(self):
        self.lineput += '8'
        self.string+='8'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)
    
    def pb_9(self):
        self.lineput += '9'
        self.string+='9'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_e(self):
        self.lineput += 'e'
        self.string+='e'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_pi(self):
        self.lineput += 'π'
        self.string+='π'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_dot(self):
        self.lineput += '.'
        self.string+='.'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_add(self):
        self.lineput += '+'
        self.string+='+'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_minus(self):
        self.lineput += '-'
        self.string+='-'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_times(self):
        self.lineput += '*'
        self.string+='×'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_kl(self):
        self.lineput += '('
        self.string+='('
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_kr(self):
        self.lineput += ')'
        self.string+=')'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_div(self):
        self.lineput += '/'
        self.string+='÷'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_sin(self):
        self.lineput = 'sin(' + self.lineput +')'
        self.string = self.lineput.replace('sqrt', '√')
        self.textBrowser.clear()
        self.textBrowser.append(self.string)
    
    def pb_cos(self):
        self.lineput = 'cos(' + self.lineput +')'
        self.string = self.lineput.replace('sqrt', '√')
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_tan(self):
        self.lineput = 'tan(' + self.lineput +')'
        self.string = self.lineput.replace('sqrt', '√')
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_ln(self):
        self.lineput = 'ln(' + self.lineput +')'
        self.string = self.lineput.replace('sqrt', '√')
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_sqrt(self):
        self.string = '√(' + self.string + ')'
        self.lineput = 'sqrt(' + self.lineput +')'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_cifang(self):
        self.lineput += '^'
        self.string+='^'
        self.textBrowser.clear()
        self.textBrowser.append(self.string)
    
    def pb_back(self):
        if len(self.string) == 0:  # 如果是空串就不执行退格操作
            pass
        elif self.string[-1] == ')':
            kh = count.kh(self.string)
            if type(kh) != type((1,2)):  # 判断返回的是否为字符串，若是则说明括号不匹配
                l = [i for i in self.string]
                l.pop()  # 若不匹配则只删去最后一个
                self.string = ''.join(l)
            else:  # 若不是字符串，则说明括号匹配
                l = [i for i in self.string]
                if len(self.string) >= 4 and self.string[kh[1] - 1] == 'n' and self.string[kh[1] - 2] == 'l':  # 判断要退格的函数是否为ln
                    l.pop();del l[kh[1] - 2:kh[1] + 1]
                elif len(self.string) >= 5 and self.string[kh[1] - 1] == 'n' or self.string[kh[1] - 1] == 's':  # 判断要退格的函数是否为sin、cos、tan
                    l.pop();del l[kh[1] - 3:kh[1] + 1]
                elif len(self.string) >= 3 and self.string[kh[1] - 1] == '√':  # 判断要退格的函数是否为根号
                    l.pop();del l[kh[1] - 1:kh[1] + 1]
                else:
                    l.pop()          
                self.string = ''.join(l)
                self.string.replace('tan','').replace('cos','').replace('sin','').replace('ln','').replace('√','')
        else:
            l = [i for i in self.string]
            l.pop()
            self.string = ''.join(l)
        self.lineput = self.string.replace('÷','/').replace('×','*').replace('√','sqrt')
        self.textBrowser.clear()
        self.textBrowser.append(self.string)
    
    def pb_clean(self):
        self.string = ''
        self.lineput = ''
        self.textBrowser.clear()
        self.textBrowser.append(self.string)

    def pb_equal(self):
        if len(self.lineput) == 0:
            pass
        else:
            print(self.lineput)
            with open('logging.txt','a') as f:
                try:
                    fun, answer = count.Fun(self.lineput)
                    self.string = self.string + '=' + str(answer)
                    f.write(f"{fun}={answer}\n")  # 存入每次计算的日志
                    self.textBrowser.clear()
                    self.textBrowser.append(self.string)
                    self.string = ''
                    self.lineput = ''
                except BaseException as fault:
                    print(1,fault)
                    self.textBrowser.clear()
                    self.textBrowser.append(f"出现错误：{fault},请确保输入正确的式子")
                    f.write(f"出现错误：{fault},请确保输入正确的式子")  # 存入每次报错的日志
                    self.string = ''
                    self.lineput = ''
                
                #print(f.readline())
        

app = QApplication(sys.argv)
window = Form()
window.pushButton_0.clicked.connect(window.pb_0)
window.pushButton_1.clicked.connect(window.pb_1)
window.pushButton_2.clicked.connect(window.pb_2)
window.pushButton_3.clicked.connect(window.pb_3)
window.pushButton_4.clicked.connect(window.pb_4)
window.pushButton_5.clicked.connect(window.pb_5)
window.pushButton_6.clicked.connect(window.pb_6)
window.pushButton_7.clicked.connect(window.pb_7)
window.pushButton_8.clicked.connect(window.pb_8)
window.pushButton_9.clicked.connect(window.pb_9)
window.pushButton_e.clicked.connect(window.pb_e)
window.pushButton_pi.clicked.connect(window.pb_pi)
window.pushButton_dot.clicked.connect(window.pb_dot)
window.pushButton_add.clicked.connect(window.pb_add)
window.pushButton_minus.clicked.connect(window.pb_minus)
window.pushButton_times.clicked.connect(window.pb_times)
window.pushButton_div.clicked.connect(window.pb_div)
window.pushButton_cifang.clicked.connect(window.pb_cifang)
window.pushButton_sin.clicked.connect(window.pb_sin)
window.pushButton_cos.clicked.connect(window.pb_cos)
window.pushButton_tan.clicked.connect(window.pb_tan)
window.pushButton_ln.clicked.connect(window.pb_ln)
window.pushButton_sqrt.clicked.connect(window.pb_sqrt)
window.pushButton_back.clicked.connect(window.pb_back)
window.pushButton_equal.clicked.connect(window.pb_equal)
window.pushButton_kuohao_l.clicked.connect(window.pb_kl)
window.pushButton_kuohao_r.clicked.connect(window.pb_kr)
window.pushButton_clear.clicked.connect(window.pb_clean)

window.show()
sys.exit(app.exec_())