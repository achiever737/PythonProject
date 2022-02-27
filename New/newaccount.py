class NewAccount:
    def details(self, Name, Father_Name, Adhar_No, Pan_No, Pin_Code, Balance):
        self.Name = Name
        self.Father_Name = Father_Name
        self.Adhar_No = Adhar_No
        self.Pan_No = Pan_No
        self.Pin_Code = Pin_Code
        self.Balance = Balance
    def registered(self):
        return [self.Name, self.Father_Name, self.Adhar_No, self.Pan_No, self.Pin_Code, self.Balance]
    def p1(i):
        return p1[i]
new = NewAccount()
print('--------ENTER DETAILS TO CREATE A NEW ACCOUNT--------\n')
Name = input('Enter Your Name : ')
Father_Name = input('Enter Your Fathers Name : ')
Adhar_No = int(input('Enter Your Adhar Card Number : '))
Pan_No = input('Enter Your Pan Card Number : ')
Pin_Code = int(input('Enter Your Area Pin Code : '))
Balance = int(input('Deposite A Amount To Open A Account : '))
new.details(Name, Father_Name, Adhar_No, Pan_No, Pin_Code, Balance)
p1 = NewAccount.registered(new)




