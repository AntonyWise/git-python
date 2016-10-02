# coding utf-8

import os
import psutil  # pip install
import sys
import shutil  # file copy...
import random


def dupl_file(filename):
    if os.path.isfile(filename):
        newfile = filename + ".dupl"
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("File", newfile, "is create")
            return True
        else:
            print("Error!")
            return False


def duple_files(dirname):
    file_list = os.listdir()
    i = 0
    while i < len(file_list):
        dupl_file(file_list[i])  # exec
        i = i + 1

def sys_info():
    print("Hello:", os.getlogin())
    print("System code:", sys.getfilesystemencoding())


def del_dupl(dirname):
    file_list = os.listdir(dirname)
    del_count = 0
    for f in file_list:
        fullname = os.path.join(dirname, f)

        if fullname.endswith(".py"):
            print("No duplicates! " + fullname)
        else:
            os.remove(fullname)
            if not os.path.exists(fullname):
                print("Delete " + fullname)
                del_count = del_count + 1
    return del_count


def main():
    answer = " "

    while answer != "Q":
        answer = input("[Y/N/Q]: ")
        if answer == "Y":
            print("[1] - files")
            print("[2] - process")
            print("[3] - system")
            print("[4] - duplication")
            print("[5] - delete .dupl")
            print("[6] - delete random")
            do = int(input("Number: "))
            if do == 1:
                print(os.listdir())
            elif do == 2:
                print(psutil.pids())
            elif do == 3:
                sys_info()
            elif do == 4:
                duple_files('.')
            elif do == 5:
                print("Delete duplicates?")
                dirname = input("Select dir: ")
                count = del_dupl(dirname)
                print("Deleted:", count)
            elif do == 6:
                dirname = input("Dir name?")
                random_delete(dirname)

            else:
                print("Error!")
        else:
            print("Go away!")

if __name__ == "__main__":
    main()


def random_delete(dirname):
    file_list = os.listdir(dirname)
    if file_list:  # есть ли элементы в директории
        i = random.randrange(0, len(file_list))
        fullname = os.path.join(dirname, file_list[i])

        if os.path.isfile(fullname):
            os.remove(fullname)
            print("File ", fullname, " delete")
