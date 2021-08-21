#!/bin/bash
clear
apt update && apt upgrade -y
gem install lolcat -y


mkdir Update 
mv update.sh Update
clear 
echo -e "\e[33m.........[Welcome]......."
echo ''
echo -e ".........Git Installing......." | lolcat -as 100
pkg install git -y 
echo -e ".........Git Installed Successfully......." | lolcat -as 10
ls | lolcat -as 100
chmod +x File.py
echo -e ".........Python Installing......." | lolcat -as 100
pkg install python -y 
echo -e ".........Python  Installed Successfull......." | lolcat -as 100
clear
echo -e ".........Python2 Installing......." | lolcat -as 10
pkg install python2 -y 
echo -e ".........Python2 Installed Successfully......." | lolcat -as 100
clear 
echo -e "\033[33m"                              
echo -e "Make Sure that You Have already install\033[34m.   \n.        Termux-api \033[33m\n.       From Playstore\n\033[32mOtherwise Install it from \033[38;5;209m\033[4mplayStore \033[0m"                              
sleep 7                                       
termux-open-url https://play.google.com/store/apps/details?id=com.termux.api


