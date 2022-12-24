import sellerBL

class sellerDL:
    seller=[]
    def addSellerInSystem(client):
        sellerDL.seller.append(client)
    def delSeller(client):
        sellerDL.seller.remove(client)
    def searchClientBYPasssword(passw):
        for m in sellerBL.Seller:
            if(m.password == passw):
                return m    
        return None    
    def loginS(userN,passW):
        a=False
        for m in sellerDL.seller:
            if(m.email == userN and m.password == passW ):
                a=True
            else:
                a=False
        return a  