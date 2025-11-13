import os
#1
path='C:/Users/user/Desktop/programs/c'
os.makedirs(path,exist_ok=True)
print(f'התיקיה{path}נוצרה בהצלחה או כבר קימת')

#2
path='C:/Users/user/Desktop/programs/c'
if os.path.exists(path):
    if not os.listdir(path):
            os.rmdir(path)
print(f'התיקיה{path}נמחקה בהצלחה או לא קימת')

#3
file=open("C:/Users/user/Desktop/programs/b/new_file.txt","w")
file.close()

#4
file=open("C:/Users/user/Desktop/programs/b/new_file.txt","w")
file.write("i write in the file")
file.close()

#5
path='C:/Users/user/Desktop/programs/b/new_file.txt'
if os.path.exists(path):
            os.remove(path)

#6
path='C:/Users/user/Desktop/programs/b'
print(os.listdir(path))

#7
directory=os.getcwd()
print(f'{directory}is a directory')





