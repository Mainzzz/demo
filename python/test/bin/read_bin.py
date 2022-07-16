import os
from struct import Struct


def get_tmp_dir():
    parent_dir = os.getcwd()
    tmp_dir = os.path.abspath(os.path.join(parent_dir, "..", "tmp"))
    return tmp_dir


def write_records(records, format, f):
    """
    Write a sequence of tuples to a binary file of structures.
    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# Example
if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]
    data_path = os.path.join(get_tmp_dir(), 'data.bin')
    print(data_path)
    with open(data_path, 'wb') as f:
        write_records(records, '<idd', f)
