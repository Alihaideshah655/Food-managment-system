class buyerBL:
    firstName=""
    lastName=""
    email=""
    password=""
    confirmPassword=""
    
    companyName=""
    address=""
    postalAddress=""
    contactNumber=""
    def __init__(self ,fName ,lName ,email ,password ,confirmPassword ,companyName ,address ,postalAddress,contactNumber):
        self.firstName=fName
        self.lastName=lName
        self.email=email
        self.password=password
        self.confirmPassword=confirmPassword
        self.companyName=companyName
        self.address=address
        self.postalAddress=postalAddress
        self.contactNumber=contactNumber