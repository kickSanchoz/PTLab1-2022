# -*- coding: utf-8 -*-
import argparse
import sys

from XmlReader import XmlReader
from CalcExcellentStudent import CalcExcellentStudent


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


# -p "../data/data.txt"
def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = XmlReader()
    data = reader.read(path)
    print(data)

    excellentStudent = CalcExcellentStudent(data).find()
    if len(excellentStudent) != 0:
        print("Стобалльники: ", excellentStudent)
    else:
        print("Нет студента, имеющего 100 баллов по всем дисциплинам")


if __name__ == "__main__":
    main()
