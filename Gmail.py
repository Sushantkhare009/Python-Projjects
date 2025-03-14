gmail = input("Enter Your Gmail : ")  #Sushant@gmail.com 
k,j,d=0,0,0
if len(gmail)>=6:  #length
    if gmail[0].isalpha(): #first leter captital 
        if ("@"in gmail) and (gmail.count("@") == 1): #check @ 
            if (gmail[-4]==".") ^ (gmail[-3]=="."):# check . 
                for i in gmail:
                    if i==i .isspace():  #check space
                        k=1
                    elif i.isalpha(): #check uppercase
                        if i==i.upper():
                            j=1  
                    elif i.isdigit(): #check digit
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:    #any other symbol like #_&*or etc d=1 wron gmai
                        d=1

                if k==1 or j==1 or d==1:
                    print(" Wrong Gmail 5")    
            else:
                print(" Wrong Gmail 4 ")
        else:
            print(" Wrong Gmai 3")
    else:
        print(" Wrong Gmail 2 ")
else:
    print(" Wrong Gmail 1 ")