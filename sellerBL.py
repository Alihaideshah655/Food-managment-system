class sellerBL:
    firstName=""
    lastName=""
    email=""
    password=""
    confirmPassword=""
    
    companyName=""
    address=""
    foodType=""
    quantity=""
    postalAddress=""
    productDescription=""
    
    def __init__(self ,fName ,lName ,email ,password ,confirmPassword ,companyName ,address ,foodType ,quantity ,postalAddress ,productDescription ):
        self.firstName=fName
        self.lastName=lName
        self.email=email
        self.password=password
        self.confirmPassword=confirmPassword
        self.companyName=companyName
        self.address=address
        self.foodType=foodType
        self.quantity=quantity
        self.postalAddress=postalAddress
        self.productDescription=productDescription
        