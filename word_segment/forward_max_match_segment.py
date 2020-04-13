#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Author:Zhang Shiwei
# @Date  :2020/4/13

"""
基于词典的前向最大匹配分词算法
"""


def add_dict(dictfile):
    """
    加载词典
    :param dictfile: 词典文件
    :return:
    """
    f_dict = open(dictfile, "r", encoding="utf-8")
    max_length = 1
    dictionary = list()
    for line in f_dict.readlines():
        dictionary.append(line.strip())
        if len(line.strip()) > max_length:
            max_length = len(line.strip())
    f_dict.close()
    return dictionary, max_length


def segment(rawfile, dictfile):
    """
    前向最大匹配分词
    :param rawfile: 待分词文本
    :param dictfile: 词典文件
    :return:
    """
    dictionary, max_length = add_dict(dictfile)
    f_raw = open(rawfile, "r", encoding="utf-8")
    f_result = open("forward_seg.txt", "w", encoding="utf-8")
    for line in f_raw.readlines():
        line = line.strip()
        while len(line) > 0:
            max_len = max_length
            if len(line) < max_length:
                max_len = len(line)

            try_word = line[:max_len]
            while try_word not in dictionary:
                if len(try_word) == 1:
                    break
                else:
                    try_word = try_word[:len(try_word) - 1]
            f_result.write(try_word + "|")
            print(try_word)
            line = line[len(try_word):]
        f_result.write("\n")

    f_raw.close()
    f_result.close()


def main():
    segment("origin.txt", "dict.txt")


if __name__ == '__main__':
    main()
