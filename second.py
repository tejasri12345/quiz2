password = input("Enter password: ")
print(password)
length = len(password)
flag =0
for i in password:
    if length>=6 and length<=16:
        if (i>='a' or i<='z'):
            flag=1
        elif(i>='A' or i<='Z'):
            flag=1
        elif(i==0 or i==1 or i==2 or i==3 or i==4 or i==5 or i==6 or i==7 or i==8 or i==9):
            flag=1
        elif (i=='@' or i=='#' or i=='$'):
            flag=1



if(flag == 0):
    print("not valid")
else:
    print("valid")
