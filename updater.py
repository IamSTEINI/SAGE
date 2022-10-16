
import subprocess
import sys
import shutil
import os
path = os.getcwd()
os.chdir(path)
print(path)
print("Cleaning up workspace")
os.system(f"rd /s /q {path}\\.git\\")
count = 0
for file in os.listdir(path):
    if not os.path.isdir(file):
        if not file.lower() == "updater.py":
            if not file.lower() == "launcher.bat":
                os.remove(path+"\\"+file)
                print(str(count) + "| Removing " + file)
                count += 1
for file in os.listdir(path+"\\data"):
    
    try:
        os.system(f"rd /s /q {path}\\data\\{file}")
    except:
        for files in os.listdir(path+"\\data\\"+file):
            os.remove(path+"\\data\\"+files+"\\"+file)
    os.system("del "+path+"\\data\\settings.cfg")
            
os.removedirs(path+"\\data")
        
        
print("\nInstalling in " + path)
os.chdir(path)
os.system(f"rd /s /q {path}\\.git\\")
os.system("git clone https://github.com/IamSTEINI/SAGE.git")
os.rename('SAGE', 'updated')
print("Extracting new files...")
count = 0
for file in os.listdir(path + "/updated"):
    print(str(count) + "| Moving " + file)
    count += 1
    shutil.move(path + "\\updated\\" + file, path)
print("Cleaning up update files...")
os.chdir(path)
os.system(f"rd /s /q {path}\\updated\\")
os.system(f"rd /s /q {path}\\.git\\")