import re

def scv_handle(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2,'a+', encoding='utf-8') as f2:
        for line in f1.readlines():
            celphone = re.match(r'[\t]$', line)
            if celphone:
                if 'T' in line and celphone.group() in f2:
                    f2.write(celphone.group())


if __name__ == '__main__':
    file1 = 'C:\/Users\Administrator\Desktop\\11.txt'
    file2 = 'C:\\Users\Administrator\Desktop\\111.txt'
    _files_need_handle = scv_handle(file1, file2)
