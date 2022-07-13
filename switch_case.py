#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 7/13/22 16:11
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : switch_case.py


def case_fun_other(msg):
    print(msg)


def case_fun_2(msg):
    print(msg)


def case_fun_1(msg):
    print(msg)


class switchCase(object):

    def case_to_function(self, case):
        fun_name = "case_fun_" + str(case)
        method = getattr(self, fun_name, case_fun_other)
        return method


if __name__ == "__main__":
    cls = switchCase()
    cls.case_to_function(1)("case_fun_1")
    cls.case_to_function(2)("case_fun_2")
    cls.case_to_function(3)("case_fun_other")
