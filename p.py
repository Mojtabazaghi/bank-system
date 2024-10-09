from tkinter.tix import INCREASING


class Customer:
    def __init__(self,firstName,lastName,fatherName,balance,id):
        self.firstName=firstName
        self.lastName=lastName
        self.fatherName=fatherName
        self.balance=balance
        self.id=id

    def setfirstName(self,firstName):
        self.firstName=firstName
    def getfirstName(self):
        return self.firstName
    def setlastName(self,lastName):
        self.lastName=lastName
    def getlastName(self):
        return self.lastName

    def setFatherName(self,fatherName):
        self.fatherName=fatherName
    def getFatherName(self):
        return self.fatherName

    def setBalance(self,balance):
        self.balance=balance
    def getBalance(self):
        return self.balance

    def setId(self,id):
        self.id=id
    def getId(self):
        return self.id

    def printInfo(self):
        print(f" name {self.firstName} {self.fatherName} balance {self.balance} idNumber {self.id}")

    def increaseBalance(self,value):
        self.balance+=value


def isIdExist(customers,id):
    for customer in customers:
        if id==customer.getId():
            return True
    return False

def addCustomer(customers):
    firstName=input(" enter name: ")
    lastName=input('enter family ')
    fatherName=input(" enter father name: ")
    balance=int(input(" enter balance: "))
    while True:
        id=int(input(" enter id: "))
        if isIdExist(customers,id)==True:
            print("this id exist,try another one!")
        else:
            break
    sample=Customer(firstName,lastName,fatherName,balance,id)
    customers.append(sample)
    print("customer added")

def showCustomers(customers):
    if len(customers)==0:
        print("dont have Customer")
    else:
        for customer in customers:
            customer.printInfo()

def searchCustomer(customers):
    id=int(input("please enter id for search: "))
    for customer in customers:
        if customer.getId()==id:
            customer.printInfo()
            break
    else:
        print("----------------------we dont have customer with this id---------------------------")

def updateCustomer(customers):
    id=int(input("please enter id: "))
    for customer in customers:
        if customer.getId()==id:
            option=int(input("1-firstname\n2-lastname\n3-fatherName\n4-balance\n enter option: "))
            if option==1:
                newName = input("please enter new name: ")
                customer.setfirstName(newName)
            elif option==2:
                newlastName=input('enter last name ')
                customer.setlastName(newlastName)
            elif option==3:
                newFatherName=input("please enter new father Name: ")
                customer.setFatherName(newFatherName)
            elif option==4:
                newBalance=input("please enter new balance: ")
                customer.setBalance(newBalance)
            print(" info Updated")
            break
    else:
        print("this id not exist")



# function for delete Customers
def deleteCustomer(customers):
    id=int(input("please enter id: "))
    index=-1
    for i in range(0,len(customers)):
        if customers[i].getId()==id:
            index=i
            break

    if index != -1:
        del customers[index]
        print("------------------------customer deleted-----------------------")
    else:
        print("------------------customer doesn`t exist-----------------------")



def requestLoan(customers):
    id=int(input("please enter id: "))
    value=int(input("please enter loan value: "))
    for customer in customers:
        if customer.getId()==id and customer.getBalance()>value:
            customer.increaseBalance(value)
            print("can loan")
            break
    else:
        print("not found")

customers=[]
while True:
    print("1-add Customer\n2-show all Customers\n3-search Customer with id \n4-update Customer\n5-delete Customer\n6-request loan\n12-exit")
    opt=int(input("select option: "))
    if opt==1:
        addCustomer(customers)

    elif opt==2:
        showCustomers(customers)

    elif opt==3:
        searchCustomer(customers)

    elif opt==4:
        updateCustomer(customers)

    elif opt==5:
        deleteCustomer(customers)

    elif opt==6:
        requestLoan(customers)

    elif opt==12:
        break


class Employe(Customer):
    def __init__(self, firstName, lastName, fatherName, id, salary):
        super().__init__(firstName, lastName, fatherName,id)
        # self.salary=salary
    def setSalary(self,salary):
        self.salary=salary
    def  getSalary(self):
        return self.salary
    def printInfo(self):
        print(f" name {self.firstName} {self.fatherName} salary {self.salary} idNumber {self.id}")

    def increaseSalary(self,value):
        
        self.salary+=value
    def increase(emp):
        id=int(input("please enter id: "))
        value=int(input("enter amount : "))
        for emolo in emp:
            if emolo.getId()==id and emolo.getSalary()>value:
                return emolo.increaseSalary(value)
                
                break
        else:
            print("not found")
    
emp=[]
while True:
    print("1-add employe \n2-show all employe\n3-search employe with id \n4-update employe\n5-delete employe\n6-increase salary\n12-exit")
    opt=int(input("select option: "))
    if opt==1:
        addCustomer(emp)

    elif opt==2:
        showCustomers(emp)

    elif opt==3:
        searchCustomer(emp)

    elif opt==4:
        updateCustomer(emp)

    elif opt==5:
        deleteCustomer(emp)
    
    elif opt==6:
        pass
    

    

    elif opt==12:
        break

