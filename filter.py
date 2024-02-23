import os, shutil

path1 = input("Enter path - This where want it to copy FROM\t")
path2 = input("Enter path - This is where it should compare with\t")
merge = input("Enter destination folder\t")

if not (os.path.exists(merge)):
    os.umask(0)
    os.makedirs(merge, mode=0o777)

dirPath1 = os.listdir(path1)
dirPath2 = os.listdir(path2)
count = 0

p2FileList = list(map(lambda x: os.path.splitext(x)[0], dirPath2))

for i in dirPath1:
    file = os.path.splitext(i)[0]
    if file in p2FileList:
        filepath = os.path.join(path1, i)
        shutil.copy(f"{path1}\\{i}", merge)
        count += 1
    
print(f"{count} files copied to new folder: {merge}")
