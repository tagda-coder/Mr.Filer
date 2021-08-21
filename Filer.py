import os 
import time 

import random

# Don't Copy This Code I have been given this code to modifier ....
#So you can exactly improve this But Give Credit 

# Code Start
os.system("rm File.py")
os.system("clear")
#os.system("cowsay | figlet | fortune")

colour = ["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m"]
Colour=random.choice(colour)



print(Colour)


print("      \033[31m""███████╗██╗██╗     ███████╗")
print("      \033[32m""██╔════╝██║██║     ██╔════╝")
print("      \033[33m""█████╗  ██║██║     █████╗  ")
print("      \033[34m""██╔══╝  ██║██║     ██╔══╝  ")
print("      \033[35m""██║     ██║███████╗███████╗")
print("      \033[36m""╚═╝     ╚═╝╚══════╝╚══════╝\033[32mVersion 2.0")
                           
                           
                           
                        


print("\033[38;5;209m|""\033[93m-------------------------------------------\033[31m|\033[0m")

print("\033[38;5;209m|""\033[93m-------------------------------------------\033[31m|\033[0m")

# Heading Design 


print()
print("         \033[38;5;229m""[1]. \033[38;5;209mCreate \033[38;5;85m\033[4mFolder\033[0m")

print("         \033[38;5;229m""[2]. \033[38;5;209mCreate \033[38;5;85m\033[4mFile\033[0m")

#print("         \033[38;5;229m""[3]. \033[38;5;209mRemove \033[38;5;85m\033[4mFolder\033[0m")

print("         \033[38;5;229m""[3]. \033[38;5;209mUpdate \033[35;5;85m\033[4mScript\033[0m")
print("         \033[38;5;229m""[4]. \033[38;5;209mCall   \033[33mSomeone")



print("         \033[38;5;229m""[5].\033[32m   ▶Exit◀")
print("                                                                         \033[41m\033[93m ▶Coded By M4ND33P🔙 \033[0m")

print("\033[38;5;229m|""\033[93m-------------------------------------------\033[31m|\033[0m")
print("\033[38;5;229m|""\033[93m-------------------------------------------\033[31m|\033[0m")
print()

option = int(input("\033[38;5;219m""       >[ Enter Your Choice ]> \033[38;5;14m"))
print()

if option == 1:
    Folder_Name = str(input("\033[32m""     :- Enter Your \033[33mFolder Name -:  \033[34m"))
    print("\033[36m""   Where Do You want to Create your \033[38;5;223mFolder ")
    print()
    print("\033[38;5;225m        1.In \033[32mHome Directory.")
    print("\033[38;5;225m        2.In \033[32mPresent Directory")
    print("\033[38;5;225m.       3.In \033[32mInternal Storage")
    print()
    choice = int(input("\033[93m""      Enter Your Choice : -  \033[47m\033[0m"))
    if choice == 1:
        os.system("mkdir " + Folder_Name )
        os.system("mv " + Folder_Name + " /data/data/com.termux/files/home")
        
        print()
        print("\033[34m"">>>[ Your \033[35mFolder \033[34mhas been Created Succesfully ]<<\033[0m")
        
    elif choice == 2:
        os.system("mkdir " + Folder_Name)
        print()
        print("\033[34m"">>>[ Your \033[35mFolder \033[34mhas been Created Succesfully ]<<\033[0m")
    elif choice == 3:
        os.system("mkdir " + Folder_Name)
        os.system("mv -f " + Folder_Name + " /sdcard")
        
        os.system("clear")
        print()
        print()
        print("\033[32m    )>>>>[ \033[31mSuccessfully Created !\033[32m ]<<<( \033[0m")
        print()
        print()
        print()

    else:
        print()
        print("\033[38;5;209m"' ------------[ Invalid Option ]-----------')
        print()
        os.system("termux-tts-speak Restarting sir")
        print("\033[33m"'     ........\033[31mRestarting\033[33m.......!')
        time.sleep(3)
        os.system('python File.py')




#Part 2 
if option == 2:
    File_Name = str(input("\033[32m""     :- Enter Your \033[31mFile Name -:  \033[34m"))
    print("\033[36m""   Where Do You want to Create your \033[38;5;223mFolder ")
    print()
    print("\033[38;5;225m        1.In \033[32mHome Directory.")
    print("\033[38;5;225m        2.In \033[32mPresent Directory")
    print()
    choice2 = int(input("\033[38;5;229m""      Enter Your Choice : -  \033[47m\033[0m"))
    if choice2 == 1:
        os.system("touch " + File_Name)
        os.system("mv " + File_Name + " /data/data/com.termux/files/home")
        #decoration bacha hai



    elif choice2 == 2:
        os.system("touch " + File_Name)
        #decoeation bacha hai






#part3
if option == 3:
    os.system("bash upd.sh")





else:
    print()

if option == 4:
    num=str(input("    >>[ \033[38;5;209mEnter The Phone Number\033[36m ]>> : \033[32m"))
    os.system("termux-tts-speak Sir I am Calling on this Same Number ")
    os.system("termux-telephony-call " + num)
    



    
