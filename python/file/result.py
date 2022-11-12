import glob
import os


# path = "D:\\code\\demo\\python\\tmp"
# for file_name in os.listdir(path):
#     print(file_name)
def mkdir(new_path): 
    folder = os.path.exists(new_path) 
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(new_path)            #makedirs 创建文件时如果路径不存在会创建这个路径
        print("Create new result folder.")
    else:
        print("There is this folder!")

path = os.getcwd()
result_path = os.getcwd() + '\\' + 'Results'
mkdir(result_path)
# print(result_path)
for txt_file in glob.glob(os.path.join(path, '*.txt')):
    print(txt_file)
    #  os.remove(txt_file)

