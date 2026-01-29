Name = input("Full Name: ")
Email = input("Email: ")
Mobile = input("Mobile: ")
Age = int(input("Age: "))
if Name[0]!=" " and Name[len(Name)-1]!=" " and " " in Name and\
       "@" in Email and "." in Email and Email[0] != "@" and \
        Mobile[0]!=0 and len(Mobile)==10 and Mobile.isdigit() and \
        18<=Age<=60:
    print("User profile is VALID")
else:
    print("User Profile is INVALID")