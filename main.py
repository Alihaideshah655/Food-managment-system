import sys
from PyQt5 import QtWidgets,uic,QtCore,QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from buyerBL import buyerBL
from buyerDL import buyerDL
from sellerBL import sellerBL
from sellerDL import sellerDL
from StockBL import Product
from stockDL import productDL
import uuid
class login(QtWidgets.QMainWindow):

    def __init__(self):
        super(login,self).__init__()
        uic.loadUi('login.ui',self)
        self.pushButton_4.clicked.connect(self.selleropensignup)
        self.pushButton_5.clicked.connect(self.buyeropensignup)
        self.pushButton.clicked.connect(self.admincheck)
    
    
    def selleropensignup(self):
        
        uic.loadUi('signup.ui',self)
        self.pushButton.clicked.connect(self.storedata)
        self.pushButton_4.clicked.connect(self.loginUI)

        
    def buyeropensignup(self):
        
        uic.loadUi('buyersignupUI.ui',self)
        self.pushButton11.clicked.connect(self.storedata)
        self.pushButton_4.clicked.connect(self.loginUI)
        
    def loginUI(self):
        uic.loadUi('login.ui',self)
        self.pushButton_4.clicked.connect(self.selleropensignup)
        self.pushButton_5.clicked.connect(self.buyeropensignup)
        self.pushButton.clicked.connect(self.admincheck)
        
    def loadadmin(self):
        print('s')
        uic.loadUi('adminMenu.ui',self)
        self.pushButton_6.clicked.connect(self.addstock)
        self.pushButton_9.clicked.connect(self.updateStock)
        self.pushButton_8.clicked.connect(self.deleteStock)
        self.pushButton_7.clicked.connect(self.viewstock)
        self.pushButton_13.clicked.connect(self.deleteclient)
        self.pushButton_14.clicked.connect(self.viewclient)
        self.pushButton_15.clicked.connect(self.addorder)
    
    def updateStock(self):
        uic.loadUi('Updatestock.ui',self)  
        self.pushButton_91.clicked.connect(self.updatestock2)
        
    def updatestock2(self):
        uic.loadUi('Updatestock2.ui',self)  
        
    def deleteStock(self):
        uic.loadUi('deletestock.ui',self)
        self.pushButton_91.clicked.connect(self.deletestock2)
        
    def deletestock2(self):
        uic.loadUi('Deletestock2.ui',self)
        
        
    def addstock(self):
        uic.loadUi('addstock.ui',self)
        self.pushButton_9.clicked.connect(self.storeStock)
    
    def viewstock(self):
        uic.loadUi('stockview.ui',self)
        
    def deleteclient(self):
        uic.loadUi('deleteclient.ui',self)
        self.pushButton_91.clicked.connect(self.deleteclient2)
        
    def deleteclient2(self):
        uic.loadUi('deleteclient2.ui',self)
    
    def viewclient(self):
        uic.loadUi('viewClient.ui',self)
    
    def addorder(self):
        uic.loadUi('Addorder.ui',self)
    
    def storeStock(self):
        b=str(uuid.uuid4())[0:6]
        a=Product(b,self.lineEdit.text(),self.lineEdit_3.text(),self.lineEdit_2.text(),) 
        productDL.addProductIntoTheSystem(a)
        print("done")    
          
    def storedata(self):
        s=sellerBL(self.lineEdit.text() ,self.lineEdit_5.text(),self.lineEdit_2.text() ,
                          self.lineEdit_11.text() ,self.lineEdit_10.text(),self.lineEdit_3,
                          self.lineEdit_7.text(),self.comboBox_2.currentText(),
                          self.lineEdit_12.text(),
                          self.lineEdit_6.text() 
                          ,self.lineEdit_8.text(),)
        sellerDL.addSellerInSystem(s) 
        print("done")

    def storedata(self):
        s=buyerBL(self.lineEdit.text() ,self.lineEdit_5.text(),self.lineEdit_2.text() ,
                          self.lineEdit_11.text() ,self.lineEdit_10.text(),self.lineEdit_3,
                          self.lineEdit_7.text(),self.lineEdit_6.text() 
                          ,self.lineEdit_8.text(),)
        buyerDL.addbuyerInSystem(s)
        buyerDL.printData()
        print("done1")
    def admincheck(self):
        a=buyerDL.login(self.lineEdit.text(),self.lineEdit_2.text())
        s=sellerDL.loginS(self.lineEdit.text(),self.lineEdit_2.text())
        if(self.lineEdit.text()=='admin' and self.lineEdit_2.text()=='admin'):
            self.pushButton.clicked.connect(self.loadadmin)
            
        elif(a==True ):
            uic.loadUi('buyerMenu.ui',self)
        else:
            print("as")
if __name__=='__main__' :
    app=QtWidgets.QApplication(sys.argv)
    window=login()
    window.show()
    sys.exit(app.exec_())