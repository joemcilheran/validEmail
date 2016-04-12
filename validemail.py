def validemailcheck():
    email = input("please enter email address \n")
    if (email[0].isalpha()) and (email.count(" ") == 0) and (email.count("@") == 1) and (email.endswith(".com") == True):
        print("Thank you")
    else:
        print("invalid email address")
validemailcheck()

            
    