import io
import traceback

import qrcode
from PySide6 import QtGui
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import sys

from googletrans import Translator

from git_toc import detectHeadLines
from ui.ui_index import Ui_MainWindow


class IndexWindow(QMainWindow):

    def __init__(self):
        super(IndexWindow, self).__init__()
        self.ui = Ui_MainWindow()  # QUiLoader().load('index.ui') #Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbQrcode.setScaledContents(True)  # 设置二维码图像容器内部件缩放
        self.ui.btnClearQr.hide()

    def make_toc(self):
        txtS = self.ui.txtSoure.toPlainText()

        rzText = detectHeadLines(txtS)
        self.ui.txtRz.setText(rzText)

    def sel_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "open file dialog", "", "Txt files(*.md)")
        file = open(file_path, mode='r', encoding="utf8")
        data = file.read()
        self.ui.txtFilePath.setText(file_path)
        self.ui.txtSoure.setText(data)

    def click_clear_qr(self):
        self.ui.txtQrContent.setText('')
        self.ui.lbQrcode.hide()
        self.ui.btnClearQr.hide()

    def click_changetocn(self):
        """
            将其他语言翻译成中文
        """
        txt_lang = self.ui.txtLangSoure.toPlainText()
        if txt_lang.strip() == '':
            QMessageBox.warning(self, '操作提示', '内容不能为空', )
            return

        # 设置Google翻译服务地址
        translator = Translator(service_urls=[
            'translate.google.cn'
        ])

        translation = translator.translate(txt_lang, dest='zh-CN')
        self.ui.txtLangRz.setText(translation.text)

    def click_entocn(self):
        """
            将其他语言翻译成英文
        """
        txt_lang = self.ui.txtLangSoure.toPlainText()
        if txt_lang.strip() == '':
            QMessageBox.warning(self, '操作提示', '内容不能为空', )
            return

        # 设置Google翻译服务地址
        translator = Translator(service_urls=[
            'translate.google.cn'
        ])

        translation = translator.translate(txt_lang, dest='en')
        self.ui.txtLangRz.setText(translation.text)

    def make_qrcode(self):
        try:
            qr_text = self.ui.txtQrContent.toPlainText()  # 二维码内容值
            if qr_text.strip() == '':
                QMessageBox.warning(self, '操作提示', '内容不能为空',)
                return

            qr = qrcode.QRCode(
                version=5,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            qr.add_data(qr_text)

            qr.make(fit=True)
            img = qr.make_image()
            # filename = 'qrcode_dome.png'
            # img.save(filename)
            # img.show()

            fp = io.BytesIO()
            img.save(fp, "BMP")
            image = QtGui.QImage()
            image.loadFromData(fp.getvalue(), "BMP")
            qr_pixmap = QtGui.QPixmap.fromImage(image)
            self.ui.lbQrcode.setPixmap(qr_pixmap)
            self.ui.lbQrcode.show()
            self.ui.btnClearQr.show()
        except Exception as e:
            print(repr(e))
            print(traceback.print_exc())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('ui/logo.ico'))
    indexWin = IndexWindow()
    indexWin.show()

    sys.exit(app.exec())
