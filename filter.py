import os, shutil

path1 = r'C:\Users\Asher\Documents\Code\Folder filter\test'
path2 = r'C:\Users\Asher\Documents\Code\Folder filter\test\T2'
merge = r'C:\Users\Asher\Documents\Code\Folder filter\Merged'

if not (os.path.exists(merge)):
    os.umask(0)
    os.makedirs(merge, mode=0o777)

dirPath1 = os.listdir(path1)
dirPath2 = os.listdir(path2)
count = 0

for i in dirPath1:
    if i in dirPath2:
        filepath = os.path.join(path1, i)
        shutil.copy(f"{path1}\\{i}", merge)
        count += 1
    
print(f"{count} files copied to new folder: {merge}")
