#--------------------------------------------------
# ToolName   : HidLink
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2024
# Language   : Python
#--------------------------------------------------


import os, time, sys

os.system('clear')




# Установка зависсимсот


print(f'\33]0; HidLink - Установка...\a',
                  end='', flush=True)

  

# зависимости


os.system('clear')

filename = "/data/data/com.termux/files/home/HidLink/tg_SYPEXHACK"

if os.path.exists(filename):
    
    os.system('clear')


else:
      
    print ('[~] Установка зависимостей... \n')
    time.sleep(2)
    os.system('clear')
       
    #colorama
    print ('[~] Установка colorama... \n')
    time.sleep(1.5)
    os.system('pip install colorama')
    os.system('clear')
      
    #питон

    from colorama import Fore, Style
    
    print ('\n')
    def res():
        print(Style.RESET_ALL)

    os.system('clear')
    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка lolcat...")
    res()
    time.sleep(1.5)
    os.system('pip install lolcat')
    os.system('clear')

    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка wget...")
    res()
    time.sleep(1.5)
    os.system('pkg install wget -y')
    os.system('clear')

    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python2...")
    res()
    time.sleep(1.5)
    os.system('pkg install python2 -y')
    os.system('clear')

    print(Fore.WHITE+'', Style.BRIGHT)
    os.system('clear')
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка python3...")
    res()
    time.sleep(1.5)
    os.system('pkg install python3 -y')

    #запуск на installer
    os.system("""sed -i '/alias installer="cd ~\/HidLink && python HidLink.py/d' ~/.bashrc""")
    os.system("""sed -i '/printf "\\33\]0; Telegram > @SYPEXHACK\\a"/d' ~/.bashrc""")

  
    os.system('rm -fr tg_SYPEXHACK')
    os.chdir('/data/data/com.termux/files/home/HidLink')
  
    os.system('clear')



from colorama import Fore, Style

#mef

def res():
        print(Style.RESET_ALL)
  
def baner():
    os.system('clear')
    os.system("""lolcat \n _   _ _     _     _            _     _       _ \n | | | (_) __| | __| | ___ _ __ | |   (_)_ __ | | \n | |_| | |/ _  |/ _  |/ _ \ '_ \| |   | | '_ \| |/ / \n  |  _  | | (_| | (_| |  __/ | | | |___| | | | |   < \n |_| |_|_|\__,_|\__,_|\___|_| |_|_____|_|_| |_|_|\_\""")







# легкий запуск


os.system('clear')

filename = "/data/data/com.termux/files/home/HidLink/tg_SYPEXHACK"

if os.path.exists(filename):
    
    os.system('clear')


else:
  
    os.system("""echo 'printf "\33]0; Telegram > @SYPEXHACK\a"' >> ~/.bashrc""")
    os.system("""alias HidLink="cd ~/HidLink && python HidLink.py" """)
    os.system("""echo 'alias HidLink="cd ~/HidLink && python HidLink.py"' >> ~/.bashrc""")



#доступ к файлам

os.system('clear')

filename = "/data/data/com.termux/files/home/storage"

if os.path.exists(filename):
  
    os.system('clear')


else:
  
    print ('\n')
    def res():
        print(Style.RESET_ALL)
        
    os.system('clear')
    baner()
    print(Fore.WHITE+'', Style.BRIGHT)
    print (Fore.YELLOW+" ["+Fore.CYAN+"!"+Fore.YELLOW+"] Разрешите доступ к файлам устройства")
    os.system('termux-setup-storage')
    time.sleep(1)
    print(Fore.WHITE+'', Style.BRIGHT)
    tsu = input(' [Нажмите Enter чтобы продолжить]')
    os.system('clear')



# удаление мусора


os.system('rm -fr /data/data/com.termux/files/home/installer/README.md')





print(Style.RESET_ALL)
os.system('clear')
print(Fore.WHITE+'', Style.BRIGHT)
print("[+]═════════════════════════════════════════════════[+]")
print("")
print("Этот инструмент создан с целью обучения и повышения")
print("квалификации в области безопасности. Важно помнить,")
print("что не все скрытые ссылки являются безопасными.")
print("")
print("[+]═════════════════════════════════════════════════[+]")
print("")
time.sleep(5)


os.chdir('/data/data/com.termux/files/home/HidLink')




baner()




#--------------------------------------------------
# ToolName   : HidLink
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2024
# Language   : Python
#--------------------------------------------------
