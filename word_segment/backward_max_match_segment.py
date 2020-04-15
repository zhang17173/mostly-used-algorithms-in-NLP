#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Author:Zhang Shiwei
# @Date  :2020/4/15

"""
基于词典的后向最大匹配分词算法
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
    后向最大匹配分词
    :param rawfile: 待分词文本
    :param dictfile: 词典文件
    :return:
    """
    dictionary, max_length = add_dict(dictfile)
    f_raw = open(rawfile, "r", encoding="utf-8")
    f_result = open("seg_results/backward.txt", "w", encoding="utf-8")
    for line in f_raw.readlines():
        words = list()  # 存储一句话分好的单词
        line = line.strip()
        while len(line) > 0:
            max_len = len(line) if len(line) < max_length else max_length  # 当前尝试的分词长度
            try_word = line[-max_len:]
            while try_word not in dictionary:  # 不断在词典中查找当前单词
                if len(try_word) == 1:
                    break
                else:
                    try_word = try_word[1:]
            words.append(try_word)
            line = line[:-len(try_word)]
        # 写入结果
        while words:
            word = words.pop()
            f_result.write(word + "|")
        f_result.write("\n")

    f_raw.close()
    f_result.close()


def main():
    segment("origin.txt", "dict.txt")


if __name__ == '__main__':
    main()
