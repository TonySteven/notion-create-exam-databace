#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 4/22/22 10:56
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : utils.py


def t2s(t):
    """

    Args:
        t: mm:ss

    Returns: 秒数

    """
    if ':' in t:
        m, s = t.strip().split(":")
        return int(m) * 60 + int(s)
    else:
        return ''


def stu_question2options(stu_question_options):
    """

    :param stu_question_options:
    :return:
    """
    result = []
    for item in stu_question_options:
        sort_order = item["sortOrder"]
        # content内容截取前80个字符
        content = item["content"][0:80]
        result.append({"name": sort_order + ' ' + content})

    return result
