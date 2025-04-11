import os
import shutil
import zipfileF

zipF = ""
zipFN = ""
root, dirs, files = next(os.walk("./"))
for file in files:
    if ((file.endswith(".nvz") == True) and (file.startswith("OLD_") == False)):
        zipF = os.path.join(root, file)
        zipFN = file[0:-4]
        break
        
if (zipF != ""):
    if (os.path.exists("translation.txt") == False):
        thing = zipfileF.ZipFileRW(zipF)
        f = thing.open("index.xml")
        r = f.read()
        f.close()
        temp = open("index.xml", "wb")
        temp.write(r)
        temp.close()
        t = open("index.xml", "rt")
        lines = list(t.read().split("\n"))
        t.close()
        thing.close()
        os.remove("index.xml")

        new = open("translation.txt", "wt")
        new.close()
        new = open("translation.txt", "at")

        count = 0
        for l in lines:
            if ((l.strip().startswith('<Action type="say"') == True) or (l.strip().startswith('<Option phrase="') == True)):
                count = count + 1
                try:
                    new.write("O" + str(count).zfill(4) + ": " + l.strip() + "\n")
                except:
                    print(lines.index(l))
                new.write("T" + str(count).zfill(4) + ": " + l.strip() + "\n")
                new.write("\n")
            elif ((l.strip().startswith('<Page name="') == True) or (l.strip().startswith('<Action type="goto"') == True)):
                new.write("~" + l.strip() + "~" + "\n\n")
        new.close()
    else:
        if (os.path.exists("OLD_" + zipFN + ".nvz") == False):
            shutil.copyfile(zipFN + ".nvz", "OLD_" + zipFN + ".nvz")
            
        thing = zipfileF.ZipFileRW("OLD_" + zipFN + ".nvz")
        f = thing.open("index.xml")
        r = f.read()
        f.close()
        temp = open("index.xml", "wb")
        temp.write(r)
        temp.close()
        t = open("index.xml", "rt")
        whole = t.read()
        t.close()
        thing.close()
        os.remove("index.xml")

        f = open("translation.txt", "rt")
        lines = list(f.read().split("\n"))
        f.close()
        
        pairs = []
        for l in lines:
            if (l.startswith("O") == True):
                for l2 in lines:
                    if (l2.startswith("T" + l[1:5]) == True):
                        pairs.append([l.split(": ")[1], l2.split(": ")[1]])
                        break
        for p in pairs:
            whole = whole.replace(p[0], p[1])

        res = zipfileF.ZipFileRW(zipFN + ".nvz", mode = "a")
        res.delete("index.xml")
        res.writestr("index.xml", whole)
        res.close()