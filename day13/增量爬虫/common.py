# 公共的工具类
import hashlib


# 从列表中取第一个元素
def first_object(list_obj):
    if len(list_obj) == 0:
        return ''
    else:
        return list_obj[0]


# 进入hash加密
def hash_item(str_obj):
    md5 = hashlib.md5()
    md5.update(bytes(str_obj, encoding='utf-8'))
    sign = md5.hexdigest()
    return sign
