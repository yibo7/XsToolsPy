# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_index.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(855, 645)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txtFilePath = QLineEdit(self.tab_2)
        self.txtFilePath.setObjectName(u"txtFilePath")

        self.horizontalLayout_3.addWidget(self.txtFilePath)

        self.btnSelFile = QPushButton(self.tab_2)
        self.btnSelFile.setObjectName(u"btnSelFile")

        self.horizontalLayout_3.addWidget(self.btnSelFile)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.txtSoure = QTextEdit(self.tab_2)
        self.txtSoure.setObjectName(u"txtSoure")
        self.txtSoure.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.txtSoure)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.txtRz = QTextEdit(self.tab_2)
        self.txtRz.setObjectName(u"txtRz")

        self.horizontalLayout.addWidget(self.txtRz)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.btnClear = QPushButton(self.tab_2)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btnClear)

        self.btnMake = QPushButton(self.tab_2)
        self.btnMake.setObjectName(u"btnMake")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMake.sizePolicy().hasHeightForWidth())
        self.btnMake.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.btnMake)

        self.btnCopy = QPushButton(self.tab_2)
        self.btnCopy.setObjectName(u"btnCopy")
        sizePolicy.setHeightForWidth(self.btnCopy.sizePolicy().hasHeightForWidth())
        self.btnCopy.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.btnCopy)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_7 = QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txtLangSoure = QTextEdit(self.tab)
        self.txtLangSoure.setObjectName(u"txtLangSoure")
        self.txtLangSoure.setAcceptRichText(False)

        self.horizontalLayout_7.addWidget(self.txtLangSoure)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btcToCn = QPushButton(self.tab)
        self.btcToCn.setObjectName(u"btcToCn")
        sizePolicy.setHeightForWidth(self.btcToCn.sizePolicy().hasHeightForWidth())
        self.btcToCn.setSizePolicy(sizePolicy)
        self.btcToCn.setMinimumSize(QSize(130, 35))

        self.verticalLayout_5.addWidget(self.btcToCn)

        self.btnEnToCn = QPushButton(self.tab)
        self.btnEnToCn.setObjectName(u"btnEnToCn")
        sizePolicy.setHeightForWidth(self.btnEnToCn.sizePolicy().hasHeightForWidth())
        self.btnEnToCn.setSizePolicy(sizePolicy)
        self.btnEnToCn.setMinimumSize(QSize(130, 35))

        self.verticalLayout_5.addWidget(self.btnEnToCn)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.txtLangRz = QTextEdit(self.tab)
        self.txtLangRz.setObjectName(u"txtLangRz")

        self.horizontalLayout_7.addWidget(self.txtLangRz)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab, "")
        self.tbCreactQr = QWidget()
        self.tbCreactQr.setObjectName(u"tbCreactQr")
        self.horizontalLayout_6 = QHBoxLayout(self.tbCreactQr)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.tbCreactQr)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.btnMakeQr = QPushButton(self.tbCreactQr)
        self.btnMakeQr.setObjectName(u"btnMakeQr")
        sizePolicy.setHeightForWidth(self.btnMakeQr.sizePolicy().hasHeightForWidth())
        self.btnMakeQr.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.btnMakeQr)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.txtQrContent = QTextEdit(self.tbCreactQr)
        self.txtQrContent.setObjectName(u"txtQrContent")
        self.txtQrContent.setAcceptRichText(False)

        self.verticalLayout_4.addWidget(self.txtQrContent)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.groupBox = QGroupBox(self.tbCreactQr)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(300, 150))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 12, 281, 301))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbQrcode = QLabel(self.layoutWidget)
        self.lbQrcode.setObjectName(u"lbQrcode")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbQrcode.sizePolicy().hasHeightForWidth())
        self.lbQrcode.setSizePolicy(sizePolicy3)
        self.lbQrcode.setMinimumSize(QSize(0, 0))
        self.lbQrcode.setMaximumSize(QSize(300, 300))

        self.verticalLayout_6.addWidget(self.lbQrcode)

        self.btnClearQr = QPushButton(self.layoutWidget)
        self.btnClearQr.setObjectName(u"btnClearQr")
        self.btnClearQr.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btnClearQr.sizePolicy().hasHeightForWidth())
        self.btnClearQr.setSizePolicy(sizePolicy)
        self.btnClearQr.setCheckable(False)

        self.verticalLayout_6.addWidget(self.btnClearQr)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_5.addWidget(self.groupBox)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tbCreactQr, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 855, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.btnMake.clicked.connect(MainWindow.make_toc)
        self.btnSelFile.clicked.connect(MainWindow.sel_file)
        self.btnClear.clicked.connect(self.txtSoure.clear)
        self.btnClear.clicked.connect(self.txtRz.clear)
        self.btnCopy.clicked.connect(self.txtRz.selectAll)
        self.btnCopy.clicked.connect(self.txtRz.copy)
        self.btnMakeQr.clicked.connect(MainWindow.make_qrcode)
        self.btnClearQr.clicked.connect(MainWindow.click_clear_qr)
        self.btcToCn.clicked.connect(MainWindow.click_changetocn)
        self.btnEnToCn.clicked.connect(MainWindow.click_entocn)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5e38\u7528\u5de5\u5177\u96c6", None))
        self.btnSelFile.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.txtSoure.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u9700\u8981\u8f6c\u6362\u7684markdown\u5185\u5bb9\uff0c\u6216\u70b9\u51fb\u4e0a\u9762\u52a0\u8f7d\u6587\u4ef6", None))
        self.txtRz.setDocumentTitle("")
        self.txtRz.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u751f\u6210\u540e\u5c06\u8f93\u51fa\u7ed3\u679c\u5728\u8fd9\u91cc", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6240\u6709", None))
        self.btnMake.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210", None))
        self.btnCopy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u751f\u6210MarkDown\u6807\u9898", None))
        self.txtLangSoure.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u7ffb\u8bd1\u7684\u5185\u5bb9", None))
        self.btcToCn.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u8bed\u8a00\u7ffb\u8bd1\u6210\u4e2d\u6587", None))
        self.btnEnToCn.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u8bed\u8a00\u7ffb\u8bd1\u6210\u82f1\u6587", None))
        self.txtLangRz.setDocumentTitle("")
        self.txtLangRz.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ffb\u8bd1\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8c37\u6b4c\u7ffb\u8bd1", None))
#if QT_CONFIG(tooltip)
        self.tbCreactQr.setToolTip(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u4e8c\u7ef4\u7801", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u751f\u6210\u7684\u4e8c\u7ef4\u7801\u5185\u5bb9\uff0c\u7136\u540e\u70b9\u51fb\u751f\u6210\u4e8c\u7ef4\u7801", None))
        self.btnMakeQr.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u4e8c\u7ef4\u7801", None))
        self.txtQrContent.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u9700\u8981\u8f6c\u6362\u7684markdown\u5185\u5bb9\uff0c\u6216\u70b9\u51fb\u4e0a\u9762\u52a0\u8f7d\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ef4\u751f\u6210\u7ed3\u679c", None))
        self.lbQrcode.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ef4\u7801", None))
        self.btnClearQr.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6570\u636e", None))
        self.label_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tbCreactQr), QCoreApplication.translate("MainWindow", u"\u751f\u6210\u4e8c\u7ef4\u7801", None))
    # retranslateUi

