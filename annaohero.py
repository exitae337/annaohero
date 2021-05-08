import os
import sys
import shutil

class Nishia:
    def __init__(self, path, files):
        self.path = path
        self.files = []
        for ad, dirs, fil in os.walk(path):
            for f in fil:
                self.files.append(f)

    def no_files_in_directory(self):
        if len(self.files) == 0:
            return 1
        else:
            return 0

    def compress_it(self):
        os.chdir(self.path)
        pop = open('sop.nosh', "wb+")
        num = bytes(str(len(self.files)), encoding='cp1251')
        pop.write(num)
        for fol in self.files:
            typ = fol[fol.find('.') + 1:]
            fname = fol[0:fol.find('.')]
            new_file = str(fname + '.' + typ)
            sr = bytes(new_file, encoding='cp1251')
            fif = open(fol, "br+")
            s = fif.read()
            s.decode('cp1251', errors='ignore')
            pop.write(b'\nKEYSTART ' + sr + b'\n')
            pop.write(s)
            pop.write(b'\nKEYEND\n')
            fif.close()
        pop.close()

    def __str__(self):
        return "Folder: " + str(self.path + ", Files: " + str(self.files) + " File with your files: sop.nosh")


def compress(path):
    s = Nishia(path, [])
    m = s.no_files_in_directory()
    if m == 1:
        print("No files in such directory")
        sys.exit()

    print(s)

    print("Compressing...")
    s.compress_it()
    print("Complete!")

def uncompress(path_with_file):
    os.chdir(path_with_file)
    s = open("sop.nosh", "rb+")
    mm = s.readline().decode('cp1251', errors='ignore')[:-1]
    mm = int(mm)
    for i in range(mm):
        while True:
            f = s.readline()
            prov = f.decode('cp1251', errors='ignore')
            if prov.startswith('KEYSTART'):
                print(prov)
                break
        nameoffile = prov[prov.find(' ') + 1:]
        fil = open(nameoffile[:-1], "wb+")
        while True: 
            nexx = s.readline()
            provnexx = nexx.decode('cp1251', errors='ignore')
            if provnexx.startswith('KEYEND'):
                break
            fil.write(nexx)
        fil.close()
    
    s.close()   
    print('FINISH')