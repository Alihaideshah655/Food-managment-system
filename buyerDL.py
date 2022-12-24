import buyerBL

class buyerDL:
    buyer=[]
    def addbuyerInSystem(client):
        buyerDL.buyer.append(client)
        
    def delBuyer(client):
        buyerDL.buyer.remove(client)
          
    def login(userN,passW):
        a=False
        for m in buyerDL.buyer:
            if(m.email == userN and m.password == passW ):
                a=True
            else:
                a=False
        return a  
    def printData():
        for m in buyerDL.buyer:
            print(m.email)