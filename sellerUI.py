import sys
from PyQt5 import QtWidgets,uic,QtCore,QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from sellerBL import sellerBL
from sellerDL import sellerDL
class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login,self).__init__()
        uic.loadUi('login.ui',self)
    def __init__(self):
        super(login,self).__init__()
        uic.loadUi('signup.ui',self)
        self.pushButton.clicked.connect(self.storedata)

    def storedata(self):
        s=sellerBL(self.lineEdit.text() ,self.lineEdit_5.text(),self.lineEdit_2.text() ,
                          self.lineEdit_11.text() ,self.lineEdit_10.text(),self.lineEdit_3,
                          self.lineEdit_7.text(),self.comboBox_2.currentText(),
                          self.lineEdit_12.text(),
                          self.lineEdit_6.text() 
                          ,self.lineEdit_8.text(),self.comboBox3.currentText(),)
        sellerDL.addSellerInSystem(s)

if __name__=='__main__' :
    app=QtWidgets.QApplication(sys.argv)
    window=login()
    window.show()
    sys.exit(app.exec_())