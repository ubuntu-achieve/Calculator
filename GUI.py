# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo1sSIabI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"From")
        Form.resize(470, 450)
        Form.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(255,255,255)\n"
        "}"
        "TextBrowser {\n"
        "background-color:rgb();\n"
        "}\n"
        "QLineEdit {\n"
        "background-color:rgb();\n"
        "}\n"
        "QComboBox {\n"
        "background-color:rgb();\n"
        "}\n"
        "QLabel {\n"
        "background-color:rgb();\n"
        "}\n"
        "QPushButton {\n"
        "background-color:rgb();\n"
        "}")
        self.setWindowIcon(QtGui.QIcon('计算器.png'))
        self.setWindowTitle('计算器.png')
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 430, 371))
        self.gridLayoutWidget.setStyleSheet(u"")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_sqrt = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sqrt.setObjectName(u"pushButton_sqrt")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sqrt.sizePolicy().hasHeightForWidth())
        self.pushButton_sqrt.setSizePolicy(sizePolicy)
        self.pushButton_sqrt.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_sqrt, 3, 2, 1, 1)
        
        font = QtGui.QFont()
        font.setPointSize(15)

        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setFont(font)
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 2, 4)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)  # 隐藏
        self.textBrowser.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(210,210,212,58%);\n"
        "border-radius: 10px;\n"
        "}"
        )

        self.pushButton_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_div.setObjectName(u"pushButton_div")
        self.gridLayout.addWidget(self.pushButton_div, 5, 3, 1, 1)

        font1 = QtGui.QFont()
        font1.setPointSize(12)

        self.pushButton_back = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_back.setObjectName(u"pushButton_back")
        sizePolicy.setHeightForWidth(self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        self.pushButton_back.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_back, 10, 2, 1, 1)


        self.pushButton_kuohao_r = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_kuohao_r.setObjectName(u"pushButton_kuohao_r")
        sizePolicy.setHeightForWidth(self.pushButton_kuohao_r.sizePolicy().hasHeightForWidth())
        self.pushButton_kuohao_r.setSizePolicy(sizePolicy)
        self.pushButton_kuohao_r.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_kuohao_r, 3, 1, 1, 1)

        self.pushButton_kuohao_l = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_kuohao_l.setObjectName(u"pushButton_kuohao_l")
        sizePolicy.setHeightForWidth(self.pushButton_kuohao_l.sizePolicy().hasHeightForWidth())
        self.pushButton_kuohao_l.setSizePolicy(sizePolicy)
        self.pushButton_kuohao_l.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_kuohao_l, 3, 0, 1, 1)

        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_clear, 4, 0, 1, 1)

        self.pushButton_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setFont(font1)
        self.pushButton_0.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_0, 10, 1, 1, 1)

        self.pushButton_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setFont(font1)
        self.pushButton_1.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_1, 9, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_2, 9, 1, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_3, 9, 2, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_4, 8, 0, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"")
        self.pushButton_5.setIconSize(QtCore.QSize(16, 16))
        self.gridLayout.addWidget(self.pushButton_5, 8, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_6, 8, 2, 1, 1)
        
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_7, 7, 0, 1, 1)

        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_8, 7, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_9, 7, 2, 1, 1)

        self.pushButton_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        sizePolicy.setHeightForWidth(self.pushButton_dot.sizePolicy().hasHeightForWidth())
        self.pushButton_dot.setSizePolicy(sizePolicy)
        self.pushButton_dot.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_dot, 10, 0, 1, 1)

        self.pushButton_pi = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_pi.setObjectName(u"pushButton_pi")
        sizePolicy.setHeightForWidth(self.pushButton_pi.sizePolicy().hasHeightForWidth())
        self.pushButton_pi.setSizePolicy(sizePolicy)
        self.pushButton_pi.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_pi, 5, 0, 1, 1)

        self.pushButton_e = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_e.setObjectName(u"pushButton_e")
        sizePolicy.setHeightForWidth(self.pushButton_e.sizePolicy().hasHeightForWidth())
        self.pushButton_e.setSizePolicy(sizePolicy)
        self.pushButton_e.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_e, 5, 1, 1, 1)

        self.pushButton_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_add, 9, 3, 1, 1)

        self.pushButton_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus.setObjectName(u"pushButton_minus")
        sizePolicy.setHeightForWidth(self.pushButton_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_minus.setSizePolicy(sizePolicy)
        self.pushButton_minus.setFont(font1)
        self.pushButton_minus.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_minus, 8, 3, 1, 1)

        self.pushButton_times = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_times.setObjectName(u"pushButton_times")
        sizePolicy.setHeightForWidth(self.pushButton_times.sizePolicy().hasHeightForWidth())
        self.pushButton_times.setSizePolicy(sizePolicy)
        self.pushButton_times.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_times, 7, 3, 1, 1)

        self.pushButton_sin = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sin.setObjectName(u"pushButton_sin")
        sizePolicy.setHeightForWidth(self.pushButton_sin.sizePolicy().hasHeightForWidth())
        self.pushButton_sin.setSizePolicy(sizePolicy)
        self.pushButton_sin.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_sin, 4, 1, 1, 1)

        self.pushButton_cos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_cos.setObjectName(u"pushButton_cos")
        sizePolicy.setHeightForWidth(self.pushButton_cos.sizePolicy().hasHeightForWidth())
        self.pushButton_cos.setSizePolicy(sizePolicy)
        self.pushButton_cos.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_cos, 4, 2, 1, 1)

        self.pushButton_tan = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_tan.setObjectName(u"pushButton_tan")
        sizePolicy.setHeightForWidth(self.pushButton_tan.sizePolicy().hasHeightForWidth())
        self.pushButton_tan.setSizePolicy(sizePolicy)
        self.pushButton_tan.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_tan, 4, 3, 1, 1)

        self.pushButton_ln = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_ln.setObjectName(u"pushButton_ln")
        sizePolicy.setHeightForWidth(self.pushButton_ln.sizePolicy().hasHeightForWidth())
        self.pushButton_ln.setSizePolicy(sizePolicy)
        self.pushButton_ln.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_ln, 3, 3, 1, 1)

        self.pushButton_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_equal.setObjectName(u"pushButton_equal")
        sizePolicy.setHeightForWidth(self.pushButton_equal.sizePolicy().hasHeightForWidth())
        self.pushButton_equal.setSizePolicy(sizePolicy)
        self.pushButton_equal.setFont(font1)
        self.pushButton_equal.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_equal, 10, 3, 1, 1)

        self.pushButton_cifang = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_cifang.setObjectName(u"pushButton_cifang")
        sizePolicy.setHeightForWidth(self.pushButton_cifang.sizePolicy().hasHeightForWidth())
        self.pushButton_cifang.setSizePolicy(sizePolicy)
        self.pushButton_cifang.setStyleSheet(u"")
        self.gridLayout.addWidget(self.pushButton_cifang, 5, 2, 1, 1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        font2 = QtGui.QFont()
        font2.setPointSize(16)
        self.label.setFont(font2)
        self.label.setToolTipDuration(-2)
        #self.label.setStyleSheet(u"text-align:r;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.retranslateUi(Form)
        #style-----------------------------------
        self.pushButton_kuohao_l.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_kuohao_r.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_clear.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_ln.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_cos.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_sin.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_tan.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_sqrt.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_ln.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:28px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_back.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_cifang.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_e.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_pi.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_div.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_times.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_add.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_minus.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_equal.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(222,226,233,100%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_dot.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_0.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_1.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_2.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_3.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_4.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_5.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_6.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_7.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_8.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )
        self.pushButton_9.setStyleSheet(u"QWidget {\n"
        "background-color:rgb(231,223,220,70%);\n"
        "border-top-left-radius: 0px;\n"
        "border-top-right-radius: 0px;\n"
        "border-bottom-left-radius: 0px;\n"
        "border-bottom-right-radius: 0px;\n"
        "min-width:100px;\n"
        "min-height:36px;\n"
        "}QWidget:focus{outline: none;}\n"
        "QPushButton:hover{\n"
        "background-color:rgb(191,191,191,60%);\n"
        "}QPushButton:pressed{"
        "background-color:rgb(191,191,191,100%);}\n"
        )

        QtCore.QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtCore.QCoreApplication.translate("Form", u"计算器", None))
        self.pushButton_clear.setText(QtCore.QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.pushButton_0.setText(QtCore.QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1.setText(QtCore.QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QtCore.QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QtCore.QCoreApplication.translate("Form", u"3", None))
        self.pushButton_4.setText(QtCore.QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QtCore.QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QtCore.QCoreApplication.translate("Form", u"6", None))
        self.pushButton_7.setText(QtCore.QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QtCore.QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QtCore.QCoreApplication.translate("Form", u"9", None))
        self.pushButton_e.setText(QtCore.QCoreApplication.translate("Form", u"e", None))
        self.pushButton_pi.setText(QtCore.QCoreApplication.translate("Form", u"π", None))
        self.pushButton_dot.setText(QtCore.QCoreApplication.translate("Form", u".", None))
        self.pushButton_add.setText(QtCore.QCoreApplication.translate("Form", u"+", None))
        self.pushButton_minus.setText(QtCore.QCoreApplication.translate("Form", u"-", None))
        self.pushButton_times.setText(QtCore.QCoreApplication.translate("Form", u"×", None))
        self.pushButton_div.setText(QtCore.QCoreApplication.translate("Form", u"÷", None))
        self.pushButton_cifang.setText(QtCore.QCoreApplication.translate("Form", u"^", None))
        self.pushButton_kuohao_l.setText(QtCore.QCoreApplication.translate("Form", u"(", None))
        self.pushButton_kuohao_r.setText(QtCore.QCoreApplication.translate("Form", u")", None))
        self.pushButton_sqrt.setText(QtCore.QCoreApplication.translate("Form", u"√", None)) 
        self.pushButton_ln.setText(QtCore.QCoreApplication.translate("Form", u"ln", None))
        self.pushButton_sin.setText(QtCore.QCoreApplication.translate("Form", u"sin", None))
        self.pushButton_cos.setText(QtCore.QCoreApplication.translate("Form", u"cos", None))
        self.pushButton_tan.setText(QtCore.QCoreApplication.translate("Form", u"tan", None))
        self.pushButton_equal.setText(QtCore.QCoreApplication.translate("Form", u"=", None))
        self.pushButton_back.setText(QtCore.QCoreApplication.translate("Form", u"后退", None))
    # retranslateUi


class Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a = Form()
    a.show()
    sys.exit(app.exec_())