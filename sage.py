import os
import time
from time import sleep
from urllib.request import Request, urlopen
import sys

#Check config file
config = open('./data/settings.cfg', 'r')
settings = config.readlines()
#Settings
installed = False
#Apply settings
for setting in settings:
    name = setting.split("=")[0]
    action = setting.split("=")[1]
    if action.lower() == "false":
        action = False
    else:
        action = True
        
    if name.lower() == "installed":
        installed = action

if not installed:
    print("Installing missing requirements...")
    sleep(1)
    require = ['colorama',"bs4"]
    for pk in require:
        os.system("cls")
        os.system("python -m pip install " + pk)


from datetime import date

from bs4 import BeautifulSoup
from colorama import Back, Fore, Style

#VARS
version_url = "https://pastebin.com/raw/mWtZRzY9"
version_url = Request(version_url)
version_url = urlopen(version_url)
client_version = "0.0.1"
today = date.today()
version_url = BeautifulSoup(version_url, "html.parser")
outdated = False
version_url = version_url.get_text()



import sys


def progressbar(it, prefix="", size=60, out=sys.stdout): # Python3.3+
    count = len(it)
    def show(j):
        x = int(size*j/count)
        print(Fore.LIGHTBLUE_EX+"{}[{}{}] {}/{}".format(Fore.CYAN+prefix, Fore.LIGHTGREEN_EX+"#"*x, Fore.CYAN+"."*(size-x)+Fore.CYAN, j, count)+Fore.CYAN, 
                end='\r'+Fore.CYAN, file=out, flush=True)
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    print("\n", flush=True, file=out)




class prefix:
    inputPrefix = Fore.LIGHTCYAN_EX + "[" + Fore.CYAN + "~" + Fore.LIGHTCYAN_EX+"] " + Fore.RESET
    errorPrefix = Fore.LIGHTCYAN_EX + "[" + Fore.LIGHTRED_EX + "~" + Fore.LIGHTCYAN_EX+"] " + Fore.RESET
    warningPrefix = Fore.LIGHTCYAN_EX + "[" + Fore.YELLOW + "!" + Fore.LIGHTCYAN_EX+"] " + Fore.RESET
    choicePrefix = Fore.LIGHTCYAN_EX + "[" + Fore.LIGHTMAGENTA_EX + "T/F" + Fore.LIGHTCYAN_EX+"] " + Fore.RESET
    successPrefix = Fore.LIGHTCYAN_EX + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.LIGHTCYAN_EX+"] " + Fore.RESET
    loadingPrefix = Fore.LIGHTCYAN_EX + "[" + Fore.LIGHTBLUE_EX + "#" + Fore.LIGHTCYAN_EX+"] " + Fore.RESET

#load tool files
files = [f for f in os.listdir("./data/commands/") if os.path.isfile(os.path.join("./data/commands/", f))]
for file in files:
    with open(f"./data/commands/{file}") as f:
        try:
            lines = f.readlines()
            if str(lines[0]) == "":
                print(f"{prefix.warningPrefix} File '{file}' is empty.")
            elif lines[0] == "#cmd@Sage":
                print(f"{prefix.successPrefix} File found: {file}")
            else:
                print(f"{prefix.warningPrefix} File '{file}' is no tool. Please consider adding the '#cmd@Sage' tag in the first line.")
                files.remove(file)
        except IndexError as e:
            print(f"{prefix.errorPrefix} Error while reading file '{file}'. Are there any contents in the file? ({e})")
            files.remove(file)
time.sleep(1)
    
    
def update():        
    os.system("cls")
    print(Fore.CYAN+"""
    ███████╗ █████╗  ██████╗ ███████╗
    ██╔════╝██╔══██╗██╔════╝ ██╔════╝
    ███████╗███████║██║  ███╗█████╗  
    ╚════██║██╔══██║██║   ██║██╔══╝              """+Fore.LIGHTMAGENTA_EX+""">>Made by Rafa#2804 & Stein#7722<< """+Fore.CYAN+f"""    DATE: {today}
    ███████║██║  ██║╚██████╔╝███████╗
    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
----Checking for updates-----------------------------------------------------------------------------------------------""")
    print("\n")
    print(prefix.loadingPrefix+Fore.LIGHTCYAN_EX+f"Downloading SAGE v{version_url} ...")
    path = os.getcwd()
    path = os.path.dirname(path)
    os.chdir(path)
    print(prefix.loadingPrefix+Fore.LIGHTCYAN_EX+f"Downloading in {path} ...")
    os.system("git clone https://github.com/IamSTEINI/SAGE.git")
    

def main():
    
        
    os.system("cls")
    os.system(f"title [~SAGE~] - MADE BY Rafa#2804 - Stein#7722 - - {today}")
    print(Fore.CYAN+"""
    ███████╗ █████╗  ██████╗ ███████╗
    ██╔════╝██╔══██╗██╔════╝ ██╔════╝
    ███████╗███████║██║  ███╗█████╗  
    ╚════██║██╔══██║██║   ██║██╔══╝              """+Fore.LIGHTMAGENTA_EX+""">>Made by Rafa#2804 & Stein#7722<< """+Fore.CYAN+f"""    DATE: {today}
    ███████║██║  ██║╚██████╔╝███████╗
    ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
------------------------------------------------------------------------------------------------------------------------""")
    print("")
    print(Fore.LIGHTRED_EX+     "    -[ reload ]- Reload Sage     "+"-[ clear ]- Clear the output "+"-[ help ]- Shows this menu   "+"-[ update ]-update SAGE      ")
    print(Fore.YELLOW+          "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.LIGHTGREEN_EX+   "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.GREEN+           "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.LIGHTCYAN_EX+    "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.CYAN+            "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.LIGHTBLUE_EX+    "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.BLUE+            "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.MAGENTA+         "    -[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        "+"-[ NAME ]-descripiton        ")
    print(Fore.CYAN+        "------------------------------------------------------------------------------------------------------------------------")
    if outdated:
        print(Fore.LIGHTBLUE_EX+f" | COPYRIGHT (C) SAGE | Stein#7722 / Rafa#2804 | Version: {client_version} (outdated) | TYPE 'Help' to get some help |------------")
        print(Fore.LIGHTGREEN_EX+" | -Type 'update' to install the newer version!"+Fore.LIGHTBLUE_EX)
    else:
        print(Fore.LIGHTBLUE_EX+f" | COPYRIGHT (C) SAGE | Stein#7722 / Rafa#2804 | Version: {client_version} | TYPE 'Help' to get some help |------------------------")
    print(" | ")
    print(" ᐯ This is your input, you can type something... ")
    while True:
        print("")
        userInput = input(f"{prefix.inputPrefix}").lower()
        known = 0
        match userInput:
            case "reload":
                known = 1
                os.system("python sage.py")
            case "prefix":
                known = 1
                print(prefix.inputPrefix)
                print(prefix.errorPrefix)
                print(prefix.warningPrefix)
                print(prefix.choicePrefix)
                print(prefix.successPrefix)
                print(prefix.loadingPrefix)
            case "":
                known = 1
            case "progressbar":
                known = 1
                for i in progressbar(range(15), "Loading: ", 40):
                    time.sleep(0.1)
            case "clear":
                known = 1
                os.system("cls")
            case "help":
                known = 1
                main()
            case "update":
                known = 1
                if not outdated:
                    print(prefix.errorPrefix+Fore.LIGHTRED_EX+"You are already on the newest version!")
                else:
                    update()
                        
                    
                    
                    
                    
                    
                    
        if known == 0:
            print(prefix.errorPrefix+"Unknown command, try 'help'")
    


if version_url != client_version:
    outdated = True
    os.system("cls")
    print("\n\n")
    print(prefix.errorPrefix+Fore.CYAN+"Update avaible! "+Fore.LIGHTCYAN_EX+"Your version: "+ client_version + " New version: " + version_url + "| Type '"+Fore.BLUE+"update"+Fore.LIGHTCYAN_EX+"' to update your SAGE client."+Fore.RESET)
    print("\n\n\n\n")
    for i in progressbar(range(3), "Continue in: ", 40):
        time.sleep(1)
main()