import os

os.chdir('C:/Users/John Rhee/Desktop/Practice')
files = os.listdir()

for f in files:
    f_name, f_ext = os.path.splitext(f)
    f_name = f_name.strip().zfill(3)

    newName = "{}{}".format(f_name,f_ext)

    os.rename(f, newName)
