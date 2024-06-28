from random import choice
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

import zhangchangpu
import mizhu
from dialogue import *
from list_themes import *


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('zhangchangpu.ui')
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.pushButton_2.clicked.connect(self.handleCalc2)
        self.ui.pushButton_3.clicked.connect(self.handleCalc3)
        self.ui.pushButton_4.clicked.connect(self.handleCalc4)
        self.ui.pushButton_5.clicked.connect(self.handleCalc5)
        self.ui.pushButton_6.clicked.connect(self.handleCalc6)
        self.ui.pushButton_7.clicked.connect(self.handleCalc7)
        self.ui.pushButton_8.clicked.connect(self.handleCalc8)
        self.ui.pushButton_9.clicked.connect(self.handleCalc9)
        self.ui.pushButton_10.clicked.connect(self.handleCalc10)
        self.ui.pushButton_11.clicked.connect(self.handleCalc11)
        self.ui.pushButton_12.clicked.connect(self.handleCalc12)
        self.ui.pushButton_13.clicked.connect(self.handleCalc13)
        self.ui.pushButton_14.clicked.connect(self.handleCalc14)
        self.ui.textEdit.returnPressed.connect(self.handleCalc14)  # 单行文本框回车消息
        self.ui.pushButton_15.clicked.connect(self.handleCalc15)

        self.ui.pushButton_16.clicked.connect(self.handleCalc16)
        self.ui.pushButton_17.clicked.connect(self.handleCalc17)
        self.ui.pushButton_18.clicked.connect(self.handleCalc18)
        self.ui.pushButton_19.clicked.connect(self.handleCalc19)
        self.ui.pushButton_20.clicked.connect(self.handleCalc20)
        self.ui.pushButton_21.clicked.connect(self.handleCalc21)
        self.ui.pushButton_22.clicked.connect(self.handleCalc22)
        self.ui.pushButton_23.clicked.connect(self.handleCalc23)
        self.ui.pushButton_24.clicked.connect(self.handleCalc24)
        self.ui.pushButton_25.clicked.connect(self.handleCalc25)
        self.ui.pushButton_26.clicked.connect(self.handleCalc26)
        self.ui.pushButton_27.clicked.connect(self.handleCalc27)
        self.ui.pushButton_28.clicked.connect(self.handleCalc28)
        self.ui.pushButton_29.clicked.connect(self.handleCalc29)
        self.ui.textEdit_2.returnPressed.connect(self.handleCalc29)  # 单行文本框回车消息
        self.ui.pushButton_30.clicked.connect(self.handleCalc30)

    # 张菖蒲
    def jqk(self, str):  # 输入JQK替换为数字字符
        str = str.replace('J', '11')
        str = str.replace('j', '11')
        str = str.replace('Q', '12')
        str = str.replace('q', '12')
        str = str.replace('K', '13')
        str = str.replace('k', '13')
        return str

    def reverse_jqk(self, str):  # 输出数字字符替换为JQK
        str = str.replace('11', 'J')
        str = str.replace('12', 'Q')
        str = str.replace('13', 'K')
        return str

    def handleCalc(self):  # 数字按钮对应文本框追加输入
        self.ui.textEdit.insert("1 ")

    def handleCalc2(self):
        self.ui.textEdit.insert("2 ")

    def handleCalc3(self):
        self.ui.textEdit.insert("3 ")

    def handleCalc4(self):
        self.ui.textEdit.insert("4 ")

    def handleCalc5(self):
        self.ui.textEdit.insert("5 ")

    def handleCalc6(self):
        self.ui.textEdit.insert("6 ")

    def handleCalc7(self):
        self.ui.textEdit.insert("7 ")

    def handleCalc8(self):
        self.ui.textEdit.insert("8 ")

    def handleCalc9(self):
        self.ui.textEdit.insert("9 ")

    def handleCalc10(self):
        self.ui.textEdit.insert("10 ")

    def handleCalc11(self):
        self.ui.textEdit.insert("J ")

    def handleCalc12(self):
        self.ui.textEdit.insert("Q ")

    def handleCalc13(self):
        self.ui.textEdit.insert("K ")

    def handleCalc14(self):  # ENTER按钮，将输入内容转换为int列表，传给cal计算
        str = self.ui.textEdit.text()
        str = self.jqk(str)
        # self.ui.textEdit.clear()
        # str = str.replace('\n', ' ')
        for i in range(1, 10):
            str = str.replace('  ', ' ')  # 清空多余空格
        str = str.strip(' ')  # 清空首尾空格
        list = []
        # print(str)
        for i in str.split(' '):
            list.append(int(i))
        # print(list)
        self.cal(list)

    def handleCalc15(self):  # DELETE按钮，将所有文本框清空，重置提示语为张菖蒲台词
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()
        self.ui.textEdit.setText("")
        dialogue = dialogue_zhangchangpu()
        str = choice(dialogue)  # 随机获取dialogue列表元素
        self.ui.textEdit.setPlaceholderText(str)
        self.ui.textBrowser.setPlaceholderText('')
        self.ui.textBrowser_2.setPlaceholderText('')

    def cal(self, list):  # 获取主功能函数结果：全部解，最优解，输入数，输出数
        p1, p2, length, longest = zhangchangpu.match(list)
        self.ui.textBrowser.clear()
        self.ui.textBrowser_2.clear()
        for i1 in p1:
            i1 = ("".join(i1))  # 将多个字符连接成一个字符串
            i1 = self.reverse_jqk(i1)
            self.ui.textBrowser.append(i1)
        for i2 in p2:
            i2 = ("".join(i2))
            i2 = self.reverse_jqk(i2)
            self.ui.textBrowser_2.append(i2)
        analysis = "输入" + str(length) + "个，" + "获得" + str(longest) + "个"
        self.ui.textBrowser_2.append(analysis)

    # 糜竺
    def handleCalc16(self):  # 数字按钮对应文本框追加输入
        self.ui.textEdit_2.insert("1 ")

    def handleCalc17(self):
        self.ui.textEdit_2.insert("2 ")

    def handleCalc18(self):
        self.ui.textEdit_2.insert("3 ")

    def handleCalc19(self):
        self.ui.textEdit_2.insert("4 ")

    def handleCalc20(self):
        self.ui.textEdit_2.insert("5 ")

    def handleCalc21(self):
        self.ui.textEdit_2.insert("6 ")

    def handleCalc22(self):
        self.ui.textEdit_2.insert("7 ")

    def handleCalc23(self):
        self.ui.textEdit_2.insert("8 ")

    def handleCalc24(self):
        self.ui.textEdit_2.insert("9 ")

    def handleCalc25(self):
        self.ui.textEdit_2.insert("10 ")

    def handleCalc26(self):
        self.ui.textEdit_2.insert("J ")

    def handleCalc27(self):
        self.ui.textEdit_2.insert("Q ")

    def handleCalc28(self):
        self.ui.textEdit_2.insert("K ")

    def handleCalc29(self):  # ENTER按钮，将输入内容转换为int列表，传给cal计算
        s1 = self.ui.textEdit_2.text()
        s1 = self.jqk(s1)
        # self.ui.textEdit_2.clear()
        # str = str.replace('\n', ' ')
        for i in range(1, 10):
            s1 = s1.replace('  ', ' ')  # 清空多余空格
        s1 = s1.strip(' ')  # 清空首尾空格
        list = []
        # print(str)
        for i in s1.split(' '):
            list.append(int(i))
        # print(list)
        self.cal_2(list)

    def handleCalc30(self):  # DELETE按钮，将所有文本框清空，重置提示语为张菖蒲台词
        self.ui.textBrowser_3.clear()
        self.ui.textEdit_2.setText("")
        dialogue = dialogue_mizhu()
        str = choice(dialogue)  # 随机获取dialogue列表元素
        self.ui.textEdit_2.setPlaceholderText(str)
        self.ui.textBrowser_3.setPlaceholderText('')

    def cal_2(self, list):  # 获取主功能函数结果：全部解，最优解，输入数，输出数
        p1 = mizhu.findNum(list, 13)
        self.ui.textBrowser_3.clear()
        if not p1:
            self.ui.textBrowser_3.append("这道题，冲儿解不出来")
        else:
            list_str = []
            for i in p1:
                s1 = ''
                for j in i: s1 = s1 + str(j) + '+'
                s1 = s1.strip('+')
                list_str.append(s1)
            # print(list_str)
            for i in list_str:
                i = ("".join(i))
                i = self.reverse_jqk(i)
                self.ui.textBrowser_3.append(i)
            list_str = []
            # analysis = "输入" + str(length) + "个，" + "获得" + str(longest) + "个"
            # self.ui.textBrowser_3.append(analysis)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[21], extra=extra, invert_secondary=True)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
