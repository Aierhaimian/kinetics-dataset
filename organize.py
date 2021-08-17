# -*- coding:utf-8 -*-

import os
import shutil
import csv
import argparse


parser = argparse.ArgumentParser(description='Organize Kinetics dataset for labels.')
parser.add_argument('--dataset', type=str, default='kinetics_400')
parser.add_argument('--types', type=str, default='train')


def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        return False
    return True


def read_csv(args):
    file_name = './{}/annotations/{}.csv'.format(args.dataset, args.types)
    content = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        content = list(reader)
    return content


def find_and_move_file(video_name, label_path, folder_path):
    for root, lists, files in os.walk(folder_path):
        for file in files:
            if video_name in file:
                src_path = os.path.join(folder_path, file)
                dst_path = os.path.join(label_path, file)
                shutil.move(src_path, dst_path)
                return True

    return True


def main():
    # parsing args
    args = parser.parse_args()

    root = os.getcwd()
    folder_path = os.path.join(root, args.dataset, args.types)

    reader = read_csv(args)
    for i in range(1, len(reader)):
        print(reader[i])
        label_path = os.path.join(folder_path, reader[i][0])
        makedir(label_path)
        find_and_move_file(reader[i][1], label_path, folder_path)

    return True


if __name__ == '__main__':
    main()

