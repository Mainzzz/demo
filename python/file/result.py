import glob
import os
import shutil
import zipfile


# path = "D:\\code\\demo\\python\\tmp"
# for file_name in os.listdir(path):
#     print(file_name)
def mkdir(new_path):
    folder = os.path.exists(new_path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(new_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("Create new result folder.")
    else:
        print("There is this folder!")


def get_zip(files, zip_name):
    testlist = os.listdir(files)
    zp = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    print(testlist)
    for i in range(0, len(testlist)):
        # zp.write(testlist[i])
        # if os.path.join(files, testlist[i]) != zip_name:
        zp.write(os.path.join(files, testlist[i]), testlist[i])
    zp.close()
    print('压缩完成')
    for i in range(0, len(testlist)):
        os.remove(os.path.join(files, testlist[i]))


path = os.getcwd()
test_name = os.path.basename(path)
result_path = os.getcwd() + '\\' + 'Results'
zip_path = result_path + '\\' + test_name + '.zip'
mkdir(result_path)
print(result_path)
print(zip_path)
for csv_file in glob.glob(os.path.join(path, '*.csv')):
    print(csv_file)
    #  os.remove(csv_file)

# move selected subfix file to direct folder
for f in os.listdir(path):
    filename = os.path.join(path, f)
    if (f.split(".")[-1] == "txt") or (f.split(".")[-1] == "csv"):
        print(f)
        shutil.move(filename, result_path)
print("done")

for file_name in os.listdir(result_path):
    print(file_name)

get_zip(result_path, zip_path)
