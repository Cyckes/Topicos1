# -*- coding: utf-8 -*-
#Ervis Alain [8-938-73]
#Daniella Ramos [8-938-1528]
#Harold Torres [8-943-2153]



from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(409, 674)
        MainWindow.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("30537.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ejecutar = QtWidgets.QPushButton(self.centralwidget)
        self.ejecutar.setGeometry(QtCore.QRect(150, 200, 101, 31))
        self.ejecutar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ejecutar.setStyleSheet("background-color:rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.ejecutar.setObjectName("ejecutar")
        self.txtentrada = QtWidgets.QTextEdit(self.centralwidget)
        self.txtentrada.setGeometry(QtCore.QRect(40, 140, 341, 51))
        self.txtentrada.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.txtentrada.setObjectName("txtentrada")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 411, 61))
        self.label.setStyleSheet("background-color: rgb(0, 120, 176);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 181, 21))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(110, 460, 201, 131))
        self.imagen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.imagen.setFrameShape(QtWidgets.QFrame.Box)
        self.imagen.setText("")
        self.imagen.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.imagen.setObjectName("imagen")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 430, 91, 21))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.txtestado = QtWidgets.QLabel(self.centralwidget)
        self.txtestado.setGeometry(QtCore.QRect(160, 610, 105, 31))
        self.txtestado.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.txtestado.setFrameShape(QtWidgets.QFrame.Box)
        self.txtestado.setObjectName("txtestado")
        self.txtsalida = QtWidgets.QTextEdit(self.centralwidget)
        self.txtsalida.setGeometry(QtCore.QRect(40, 290, 341, 121))
        self.txtsalida.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.txtsalida.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.txtsalida.setReadOnly(True)
        self.txtsalida.setObjectName("txtsalida")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 250, 201, 31))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setStatusBar(self.statusbar)
        
        ver="Apagado.png"
        pixmap = QtGui.QPixmap(ver) # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imagen.width(), self.imagen.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imagen.setPixmap(pixmap) # Set the pixmap onto the label
        self.imagen.setAlignment(QtCore.Qt.AlignCenter) # Align the label to cente



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Arranque"))
        self.ejecutar.setText(_translate("MainWindow", "Ejecutar"))
        self.txtentrada.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Sistema de Arranque de una </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Computadora</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Ingrese su solicitud</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Estado</span></p></body></html>"))
        self.txtestado.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.txtsalida.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Resultado del Proceso</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())