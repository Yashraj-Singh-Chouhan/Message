import os,time,msvcrt
def Friend():
    os.system("cls")
    Fri = open("C:\\Users\\RootUser\\Desktop\\det\\Friends.txt","r")
    print("Your Friend list :")
    Frir = Fri.readline()
    value = True
    while (Frir != ''):
        if(Frir[0:len(You)] == You):
            print(Frir[len(You):-1])
            value = False
        elif(Frir==''):
            break
        Frir = Fri.readline()
    del Frir
    Fri.close()
    if(value==True):
        print("\n\nNo Friends")
    print("\nTo Add Friends give his/her Username <casesensative> or Enter B for take Back :")
    ch = input("Choice : ")
    if ch == 'b' or ch=='B' or ch == You:
        Want()
    else:
        Mem = open("C:\\Users\\RootUser\\Desktop\\det\\Members.txt","r")
        value = True
        Memr = Mem.readline()
        while (Memr != ""):
            if (Memr[0:len(ch)] == ch):
                value = False
            Memr = Mem.readline()
        del Memr
        Mem.close()
        if(value==True):
            print(ch,"User not Found!")
            Friend()
        Fri = open("C:\\Users\\RootUser\\Desktop\\det\\Friends.txt","a")
        Fri.write(You+" "+ch+"\n")
        Fri.write(ch+" "+You+"\n")
        Fri.close()
        print(ch,"Added to Friend!")
        time.sleep(1)
        Friend()
def Members():
    os.system('cls')
    Mem = open("C:\\Users\\RootUser\\Desktop\\det\\Members.txt","r")
    mem = Mem.readline()
    while mem !='':
        print(mem)
        mem = Mem.readline()
    Mem.close()
    input("Press Enter to move Forward!")
    Want()

def Text(TXT):
    while True:
        Mess = open(TXT,"r+")
        Messr = Mess.readlines()
        pMessr= Messr[-20:]
        Mess.flush()
        if msvcrt.kbhit():
            s=input("TYPE YOUR MESSAGE or TYPE <b> FOR BACK: ")
            if(s=="<b>"or s == "<B>"):
                del Messr,pMessr
                return
            Mes = open(TXT,"a")
            Mes.write(You+" : "+s+"\n")
            Mes.flush()
        j=0
        while(j<=19):
            try:
                print(pMessr[j])
            except IndexError:
                break
            j+=1
        del Messr,pMessr
        print("press any key to type and wait for a second")
        time.sleep(2)
        os.system('cls')

def Message():
    os.system('cls')
    print("Send Message to ? or Press B for take Back\n\n")
    Fri = open("C:\\Users\\RootUser\\Desktop\\det\\Friends.txt","r")
    Frir = Fri.readline()
    value = True
    while (Frir != ''):
        if(Frir[0:len(You)] == You):
            print(Frir[len(You):-1])
            value = False
        elif(Frir==''):
            break
        Frir = Fri.readline()
    del Frir
    Fri.close()
    if(value==True):
        print("\n\nNo Friends\n\n")
        time.sleep(1)
        Want()
        return
    ch = input("\n\nName :")
    if(ch=='b'or ch=='B' or ch==You):
        Want()
    Fri = open("C:\\Users\\RootUser\\Desktop\\det\\Friends.txt","r")
    Frir = Fri.readline()
    value = True
    while (Frir != ""):
        if(Frir[0:len(You)] == You and ch == Frir[len(You)+1:-1]):
            value = False
            break
        Frir = Fri.readline()
    del Frir
    Fri.close()
    if(value==True):
        print("No user found")
        time.sleep(1)
        Message()
    if You[0]<ch[0]:
        TXT = "C:\\Users\\RootUser\\Desktop\\det\\Message\\"+You+ch+".txt"
    else:
        TXT = "C:\\Users\\RootUser\\Desktop\\det\\Message\\"+ch+You+".txt"
    Mess = open(TXT,"a+")
    Mess.close()
    time.sleep(1)
    os.system('cls')
    Text(TXT)
    Want()
        
def Want():
    os.system('cls')
    print("\t\t{**********Loged In!**********}\n\n")
    print("Hello,!",You,end="\n\n")
    print("Friends : F\tMembers : M\tSend Message : S\tLogout : L")
    ch=input()
    if ch=='f' or ch=='F':
        Friend()
    elif ch=='m'or ch=='M':
        Members()
    elif ch=='s' or ch=='S':
        Message()
    elif ch=='l' or ch=='L':
        print("Logout Successfully!")
        return 0
    else:
        print("Please Enter Valid choice!")
        time.sleep(1)
def Create():
    os.system('cls')
    Det = open('C:\\Users\\RootUser\\Desktop\\det\\det.txt','r+')
    Detr = Det.readlines()
    exist = True
    while(exist):
        Username = input("Enter New Username : ")
        for line in Detr:
            if Username == line[11:-1]:
                exist=True
                print("Username Exist!\n\t\tchoose another one")
                break
            exist=False
    Pass = input("Enter Password : ")
    Det.write("Username : "+Username)
    Det.write("\nPass : "+Pass+"\n")
    del Detr
    Det.close()
    Mem = open("C:\\Users\\RootUser\\Desktop\\det\\Members.txt","a+")
    Mem.write(Username+"\n")
    Mem.close()
    print("Account Created Successfully!!")
    time.sleep(1)

def Login():
    os.system('cls')
    print("\t\t|--------Login Here--------|\n")
    Username=input("\t\t    Username : ")
    Pass =input("\t\t    Password : ")
    print("\n\t\t|--------------------------|\n\n")
    Det = open('C:\\Users\\RootUser\\Desktop\\det\\det.txt','r')
    found = False
    while(found==False):
        Detr = Det.readline()
        if Username == Detr[11:-1]:
            Detr = Det.readline()
            if Pass == Detr[7:-1]:
                found=True
        elif Detr== '':
            break
        Detr = Det.readline()
    if(found==True):
        global You
        You = Username
        Want()
    else:
        print("Login Credentials Failed")
    del Detr
    Det.close()
    time.sleep(1)

while(1==1):
    os.system('cls')
    print("\t|================================================|")
    print("\t|\t\tYankee's Messenger\t\t |")
    print("\t|================================================|\n\n\n")
    print("Create Account : C\t\tLogin Account : L\t\tExit : E\n")
    ch = input("")
    if ch=='c' or ch == 'C':
        Create()
    if ch=='l' or ch=='L' :
        Login()
    if ch =='e' or ch == 'E':
        print("Exited")
        exit()