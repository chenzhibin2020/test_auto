# -*- coding: utf-8 -*-
"""
@File    : deepdiff_01.py
@Author  : chenzhibin
@Time    : 2023/5/28 13:45
"""
# 程序说明: 
# 程序结果: 是否报错：xx，是否拿到结果：xx


from deepdiff import DeepDiff


# # case01 --对比字符串--------
# a = 'abc'
# b = 'abd'
#
# print(DeepDiff(a, b))


# #  case02 对比文本内容
#
# f1 = open(r"files\test01.txt",'r')
# f2 = open(r"files\test02.txt",'r')
#
# print(DeepDiff(f1, f2))

# # case03 对比json 样式的字典
#
# json1={
#     'code': 0,
#     "message": "成功",
#     "data": {
#         "total": 28,
#         "id":123
#              }
#        }
#
# json2={
#     'code': 0,
#     "message": "成功",
#     "data": {
#         "total": 29
#
#              }
#        }
#
# print(DeepDiff(json1, json2))


# 参数使用
""" 
ignore order(忽略排序)
ignore string case(忽略大小写)
exclude_paths排除指定的字段
"""

# # ignore order(忽略排序)
# ls1=['a','b','c']
# ls2=['a','c','b']
# print("不忽略顺序")
# print(DeepDiff(ls1, ls2))
# print("忽略顺序")
# print(DeepDiff(ls1, ls2,ignore_order=True))


# # ignore string case(忽略大小写)
# json1={
#     "message": "SUCESS",
#     'code': 0,
#     "data": {
#         "total": 29
#              }
#        }
#
# json2={
#     'code': 0,
#     "message": "Sucess",
#     "data": {
#         "total": 29
#
#              }
#        }
#
# print("不ignore_string_case")
# print(DeepDiff(json1, json2))
# print(" ignore_string_case")
# print(DeepDiff(json1, json2,ignore_string_case=True))

# # exclude_paths排除指定的字段
# json1={
#     "message": "SUCESS",
#     'code': 0,
#     "data": {
#         "total": 29
#              }
#        }
#
# json2={
#     'code': 0,
#     "message": "Sucess",
#     "data": {
#         "total": 29
#
#              }
#        }
#
# print("不exclude_paths")
# print(DeepDiff(json1, json2))
# print(" exclude_paths")
# print(DeepDiff(json1, json2,exclude_paths='message'))


########################3 参数介绍####################



# # 1. cutoff_distance_for_pairs: (1 >= float > 0，默认值=0.3)
#
# # 此参数通常结合ignore_order=true使用，用于结果中展示差异的深度。值越大，则结果中展示的差异深度越大。
#
# # t1 = [[[1.0]]]
# # t2 = [[[20.0]]]
# t1 = [[[[1.0]]]]
# t2 = [[[[20.0]]]]
# print("cutoff_distance_for_pairs=0.3")
# print(DeepDiff(t1, t2, ignore_order=True, cutoff_distance_for_pairs=0.3))
# print("cutoff_distance_for_pairs=0.2")
# print(DeepDiff(t1, t2, ignore_order=True, cutoff_distance_for_pairs=0.2))
# print("cutoff_distance_for_pairs=0.1")
# print(DeepDiff(t1, t2, ignore_order=True, cutoff_distance_for_pairs=0.1))

# 2. ignore_types
"""
ignore_string_type_changes
默认= False
忽略字符串类型的更改。例如，如果ignore_string_type_changes设置为True，则b " Hello "与"
Hello "被认为是相同的。
"""
# print(DeepDiff(b'hello', 'hello', ignore_string_type_changes=True))

# ignore_numeric_type_changes

"""
默认= False
是否忽略数值类型更改。例如，如果ignore_numeric_type_changes设置为True，则认为10和
10.0是相同的。
PS:此参数仅作用于numbers对象比较，如果拿numbers和string比较则不生效。
"""

# t1 = 10.0
# t2 = 10
# print(DeepDiff(t1, t2))
# print(DeepDiff(t1, t2,ignore_numeric_type_changes=True))


# #######   3. view  #################
"""
DeepDiff支持对比结果选择text视图和tree视图展示。主要区别在于，tree视图具有遍历对象的功能，
可以看到哪些对象与哪些其他对象进行了比较。
虽然视图选项决定了输出的格式，但无论你选择哪种视图，你都可以通过使用pretty()方法得到一个更适
合阅读的输出。
"""

t1= {"name": "yanan", "pro": {"sh": "shandong", "city": ["zibo", "weifang"]}}
t2 = {"name": "changsha", "pro": {"sh": "shandong", "town": ["taian",
"weifang"]}}

# print("view='tree' : ")
# ddiff = DeepDiff(t1, t2, view='tree')
# print(ddiff)
#
#
# # 默认为text
# print("view='text' : ")
# ddiff = DeepDiff(t1, t2, view='text')
# print(ddiff)

############## 4. pretty()方法 #####################

# # 通过 pretty 进行美化输出
# print(" tree pretty()' : ")
# print("view='tree' : ")
# ddiff = DeepDiff(t1, t2, view='tree')
# print(ddiff.pretty())
#
# # 默认为text
# print("text pretty()' : ")
# ddiff = DeepDiff(t1, t2, view='text')
# print(ddiff.pretty())

# --------------举例2 --------------

# t1 = {
# 'Author': '展昭',
# 'wechat': 'ZZ666'
# }
# t2 = {
# 'Author': '展昭',
# 'wechat': 'ZZ666',
# 'Blog' : 'https://www.hctestedu.com/'
# }
# t3 = {
# 'Author': '展昭',
# 'wechat': 'ZZ777'
# }
# t4 = {
# 'Author': '展昭',
# 'wechat': 777
# }
# t5 = [{
# 'Author': '展昭',
# 'wechat': 'ZZ666'
# }]
# # Key值不同
# print(DeepDiff(t1, t3).pretty())
# # Key新增
# print(DeepDiff(t1, t2).pretty())
# # Key减少
# print(DeepDiff(t2, t1).pretty())
# # Key值类型改变
# print(DeepDiff(t1, t4).pretty())
# # 结构不同
# print(DeepDiff(t1, t5).pretty())
# # Key值相同
# result = DeepDiff(t1, t1).pretty()
# print(DeepDiff(t1, t1).pretty())
# assert "" == result


# -----------------------------------------------part2 --DeepSearch-------------------

from deepdiff import DeepSearch
"""
use_regexp
使用正则表达式，默认False。
strict_checking
强校验，默认Ture。为True时，它将检查要匹配的对象的类型，因此在搜索 '1234' 时，它将不匹
配 int 1234。
case_sensitive
当=True，大小写敏感。
"""


# obj = ["long somewhere", "string", 0, "somewhere great!"]
# # 使用正则表达式
# item = "some*"
# ds = DeepSearch(obj, item, use_regexp=True)
# print("使用正则表达式")
# print(ds)
# # 大小写敏感
# item = 'someWhere'
# ds = DeepSearch(obj, item, case_sensitive=True)
# print("大小写敏感")
# print(ds)
# item = 'some'
# ds = DeepSearch(obj, item, case_sensitive=True)
# print("大小写敏感")
# print(ds)
# # 强校验
# item = 0
# ds = DeepSearch(obj, item, strict_checking=True)
# print("强校验")
# print(ds)
# item = "0"
#
# ds = DeepSearch(obj, item, strict_checking=True)
# print("强校验")
# print(ds)


############ 5 grep
# grep是DeepSearch提供的一个更好用的方法。它所接受的参数与DeepSearch完全相同，只是需要你用
# 管道将对象送入它，而不是将它作为参数传递。它的工作原理和 linux shell中的grep 一样


# from deepdiff import grep
# obj = ["long somewhere", "string", 0, "somewhere great!"]
# item = "somewhere"
# ds = obj | grep(item)
# print("使用grep ：")
# print(ds)

# ------------ Extract
from deepdiff import extract
obj = {"a": [{'2': 'b'}, 3], "b": [4, 5]}
# root+键名+list下标+键名
path = "root['a'][0]['2']"
print("使用 Extract ")
print(extract(obj,path))
