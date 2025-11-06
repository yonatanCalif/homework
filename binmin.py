def binstring(num):
    res=""
    while(num>0):
        res=res+str(num%2)
        num=num//2
    res=res+"00"
    return res[::-1]
def minus(num):
    num1=num
    tmp="1"
    for i in range(len(num1)):

        if num1[i]=="0":
            num1=num1[0:i]+"1"+num1[i+1:]
        elif num1[i]=="1":
            num1 = num1[0:i] + "0" + num1[i + 1:]
    for i in range(len(num1)-1,1,-1):
        if(tmp=="1" and num1[i]=="0"):
            tmp="0"
            num1=num1[0:i]+"1"+num1[i+1:]


        elif(tmp=="1" and num1[i]=="1"):
            num1=num1[0:i]+"0"+num1[i+1:]

    return num1
def main():
    print(minus(binstring(int(input("number")))))
if __name__ == "__main__":
    main()