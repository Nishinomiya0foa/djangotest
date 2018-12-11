# 比较文档的不同


def Compare_difference_in_files(file1,file2):
    with open(file1, 'r', encoding='utf-8') as f1:
        lines1 = f1.readlines()
    with open(file2, 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
    # shorter = min(len(lines1),len(lines2))
    shorter_file = lines1 if len(lines1)<len(lines2)else lines2
    longer_file = lines1 if len(lines1)>len(lines2)else lines2
    for i in range(0, len(shorter_file)):
        if lines1[i] != lines2[i]:
            return lines1[i]

if __name__ == '__main__':
    file1 = 'C:\\Users\Administrator\Desktop\\111.txt'
    file2 = 'C:\\Users\Administrator\Desktop\\11.txt'
    compare_object = Compare_difference_in_files(file1, file2)
    print(compare_object)

