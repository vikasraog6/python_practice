sex = input("Enter sex (male, female, m, f ) :")
age = int(input("Enter age : "))

if (sex.lower() in ("female", "f")):

    if(age >= 18):
        print("Eligible For Marriage")
    else:
        print("Not Eligible For Marriage")

elif (sex.lower() in ("male", "m")):

    if (age >= 18):
        print("Eligible For Marriage")
    else:
        print("Not Eligible For Marriage")
else:
    print("We dont know")
