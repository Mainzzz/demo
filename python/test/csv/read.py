import os


def csv_dir():
    print('***获取当前目录***')
    print(os.getcwd())
    print(os.path.abspath(os.path.dirname(__file__)))


if __name__ == '__main__':
    print('csv read')
    csv_dir()
