import pymysql
connection = pymysql.connect(host = "localhost", database = "BankingSystem", user = "root", passwd = "")
choice = int(input("Select Your Choice : \n Press 1 to create new account \n Press 2 for existing account \n1"))
mycursor = connection.cursor()
if choice == 1:
    from New.newaccount import NewAccount
    n = NewAccount.p1(0)
    f_n = NewAccount.p1(1)
    a_no = NewAccount.p1(2)
    p_no = NewAccount.p1(3)
    pi_no = NewAccount.p1(4)
    balance = NewAccount.p1(5)
    sql = "INSERT INTO newaccount(Name, Father_Name, Adhar_No, Pan_No, Pin_Code, balance) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, (n, f_n, a_no, p_no, pi_no, balance))
elif choice == 2:
    choice2 = int(input(" Press 1 For Account Information\n Press 2 To Withdraw Money\n Press 3 To Make A Deposit\n"))
    if choice2 == 1:
        ano = int(input("Enter Your Account Number : "))
        sql = "SELECT * FROM newaccount WHERE accno=%s"
        mycursor.execute(sql, (ano))
        myresult = mycursor.fetchall()
        print(myresult)
    elif choice2 == 2:
        ano = int(input("Enter Your Account Number : "))
        sql = "SELECT balance FROM newaccount WHERE accno=%s"
        mycursor.execute(sql, (ano,))
        myresult = mycursor.fetchall()
        bal = []
        for row in myresult:
            a = list(row)
            bal.append(a)
        bala = int(bal[0][0])
        amount = int(input("Enter The Amount You Wan't To Withdraw : "))
        if amount <= bala :
            print("-------THANKS FOR BANKING WITH US-------")
            new_bal = bala-amount
            print(f"Your Updated Baalance Is {new_bal}")
            sql = "UPDATE newaccount SET balance = %s WHERE accno=%s"
            mycursor.execute(sql, (new_bal, ano))
        else :
            print("You Don't Have Enough Balance")
    elif choice2 == 3:
        ano = int(input("Enter Your Account Number : "))
        deposit = int(input("Enter The Amount You Want To Deposit : "))
        sql = "SELECT balance FROM newaccount WHERE accno=%s"
        mycursor.execute(sql, (ano,))
        myresult = mycursor.fetchall()
        bal = []
        for row in myresult:
            a = list(row)
            bal.append(a)
        bala = bal[0][0]
        print("-------THANKS FOR BANKING WITH US-------")
        new_bal = bala+deposit
        print(f"Your Updated Baalance Is {new_bal}")
        sql = "UPDATE newaccount SET balance = %s WHERE accno=%s"
        mycursor.execute(sql, (new_bal, ano))
    else:
        pass
connection.commit()
connection.close()







