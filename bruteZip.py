from zipfile import ZipFile
from os import mkdir

line = "----------------------------------"
counter = 0
print('Наш телеграмчик: @Termuxtop')
print('''
▄▄▄   ▄▄▄· ▄▄▄  ▄▄▄▄· ▄▄▄  ▄• ▄▌▄▄▄▄▄▄▄▄ .
▀▄ █·▐█ ▀█ ▀▄ █·▐█ ▀█▪▀▄ █·█▪██▌•██  ▀▄.▀·
▐▀▀▄ ▄█▀▀█ ▐▀▀▄ ▐█▀▀█▄▐▀▀▄ █▌▐█▌ ▐█.▪▐▀▀▪▄
▐█•█▌▐█ ▪▐▌▐█•█▌██▄▪▐█▐█•█▌▐█▄█▌ ▐█▌·▐█▄▄▌
.▀  ▀ ▀  ▀ .▀  ▀·▀▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀  ▀▀▀
''')
dict = input('Dictionary name: ')
def generator(string):
    for word in string:
        passwd = word.replace('\n', '')
        archive.setpassword(passwd.encode())
        try:
            archive.extractall(directory)
        except:
            yield "[False]: " + passwd
        else:
            yield line + "\n[True]: " + passwd;
            return


directory = "Bruteforcing"
try:
    mkdir(directory)
except FileExistsError:
    pass

# counter = 0
print(line)
with open(dict, errors='ignore') as dictionary:
    with ZipFile(input('zip archive name: ')) as archive:
        print(line)
        for password in generator(dictionary):
            counter += 1
            print(str(counter) + '>> ', end="")
            print(password + '\n' + line)
print(line)
print('Разработчик: @sudoTulpa')
