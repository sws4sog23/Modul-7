import os
print(os.getcwd())

for i in os.walk('.'):
    print(i)
os.path.join('.')
os.path.getmtime('.')
print(os.listdir())
files = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print('файлы',files)
print('директории',dirs)
# os.startfile(files[4])
print(os.stat(files[4]))
print(os.stat(files[4]).st_size)
print(os.stat(files[4]).st_mtime)
print(os.path.getmtime(r'.\products.txt'))
print(os.path.join(r'.','modul 7','products.txt'))
print(os.path.dirname('.\\modul 7\\products.txt'))
print(os.path.getsize('Mother Goose - Monday’s Child.txt'))
print(os.path.getmtime('products.txt'))
