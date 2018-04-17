#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# **********************************************************
# * Author        : huangtao
# * Email         : huangtao@yimian.me
# * Create time   : 2018/4/17 下午2:34
# * Last modified : 2018/4/17 下午2:34
# * Filename      : util.py.py
# * Description   : 公共方法
# **********************************************************

import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def clearHtml(str):
    if '☞' in str:
        str = str.replace('☞', '<')
    res = re.sub(r'<(?!img).*?>', '',str)
    res = re.sub(r'<img.*?alt="','',res)
    res = re.sub(r'<[^>]+>','',res)
    res = res.replace('">',"")
    return res