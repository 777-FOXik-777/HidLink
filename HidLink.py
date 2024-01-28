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
    print (Fore.YELLOW+"["+Fore.RED+"~"+Fore.YELLOW+"] Установка requests...")
    res()
    time.sleep(1.5)
    os.system('pip install requests')
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
    os.system("""sed -i '/alias HidLink="cd ~\/HidLink && python HidLink.py/d' ~/.bashrc""")
    os.system("""sed -i '/printf "\\33\]0; Telegram > @SYPEXHACK\\a"/d' ~/.bashrc""")

  
    os.system('rm -fr tg_SYPEXHACK')
    os.chdir('/data/data/com.termux/files/home/HidLink')
  
    os.system('clear')


else:
      
    os.system('clear')



import requests

from colorama import Fore, Style

#mef

def res():
        print(Style.RESET_ALL)
  



def baner():
    os.system('clear')
    os.system("lolcat ~/HidLink/baner.txt")
    print(Fore.WHITE+'', Style.BRIGHT)


# легкий запуск


os.system('clear')

filename = "/data/data/com.termux/files/home/HidLink/tg_SYPEXHACK"

if os.path.exists(filename):
    
    os.system("""echo 'printf "\33]0; Telegram > @SYPEXHACK\a"' >> ~/.bashrc""")
    os.system("""alias HidLink="cd ~/HidLink && python HidLink.py" """)
    os.system("""echo 'alias HidLink="cd ~/HidLink && python HidLink.py"' >> ~/.bashrc""")

else:
  
    os.system('clear')


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
print("Этот инструмент создан с целью обучения. Важно помнить,")
print("что не все замаскированные ссылки являются безопасными.")
print("")
print("[+]═════════════════════════════════════════════════[+]")
print("")
time.sleep(5)


os.chdir('/data/data/com.termux/files/home/HidLink')






url = 'https://www.google.com'

original_url = 'https://www.google.com'




def shorten_url(original_url):
    api_url = "https://is.gd/create.php"
    cleaned_url = original_url.rstrip('/') 
    params = {"format": "simple", "url": cleaned_url}

    try:
        response = requests.get(api_url, params=params)
        if response.status_code == 200:
            shortened_url = response.text.strip()
            return cleaned_url, shortened_url
        else:
            print(f"Ошибка! {response.status_code}: {response.text}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


shortened_url_result = shorten_url(url)




while True:
    baner()
    inp = input('\n Выбери пункт ➤ ')
    os.system('clear')
    


  
    if inp == '1':
      
        url = input('\n Ввведите url ➤ ')
        
        original_url = input('\n Ввведите org url ➤ ')
        
        
        if shortened_url_result:
            original_url, shortened_url = shortened_url_result  # Распаковка кортежа
            print(f"{original_url}@{shortened_url.replace('https://', '')}")



#--------------------------------------------------
# ToolName   : HidLink
# Author     : SYPEXHACK
# Github     : https://github.com/777-FOXik-777
# Contact    : https://t.me/SYPEXHACK
# 1st Commit : 2024
# Language   : Python
#--------------------------------------------------
