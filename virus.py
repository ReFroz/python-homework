import re
def remove_virus(sen:str):
    lst=re.split(":|,",sen)
    for i in lst:
        if not (re.search(r"anti?|not?",i)!=None or \
        re.search(r"virus?|danger?|warior?|malware?",i)==None):
            lst.remove(i)
    if len(lst)==1:
        print("Файлы на пк: Пусто")
        return("Файлы на пк: Пусто")
    
    print("Файлы на пк:"+" ,".join(lst[1:]))       
    return "Файлы на пк:"+" ,".join(lst[1:])
    
remove_virus("Файлы на пк:antivirus.exe,cat.exe,dangerdungeon.exe,\
notvirus.exe,virus.exe,happycat.exe, dege.jpg, asmalware.exe, slawe.exe")
remove_virus("Файлы на пк:dangeonslawe.exe,mister, happy")
remove_virus("")