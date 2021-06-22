# -*- coding: UTF-8 -*-
import os
import platform

platform.uname()

# forms表单的选择参数
# 地区选项
AREA = {
    ("", ""), ("北京", "北京"), ("天津", "天津"), ("河北", "河北"), ("山西", "山西"), ("内蒙古", "内蒙古"), ("辽宁", "辽宁"), ("吉林", "吉林"), ("黑龙江", "黑龙江"), ("上海", "上海"), ("江苏", "江苏"), ("浙江", "浙江"), ("安徽", "安徽"), ("福建", "福建"), ("江西", "江西"), ("山东", "山东"), ("河南", "河南"), ("湖北", "湖北"), ("湖南", "湖南"), ("广东", "广东"),
    ("广西", "广西"), ("海南", "海南"), ("重庆", "重庆"), ("四川", "四川"), ("贵州", "贵州"), ("云南", "云南"), ("陕西", "陕西"), ("甘肃", "甘肃"), ("青海", "青海"), ("宁夏", "宁夏"),
    ("新疆", "新疆"), ("香港", "香港")
}
# 考生类型
TYPE = {
    ("", ""), ("普通类", "普通类"), ("艺术类", "艺术类"), ("体育类", "体育类")
}

LEVEL = {
    ("", ""), ("第一批", "第一批"), ("第二批", "第二批"), ("第三批", "第三批")
}

SUBJECT_CHOICE = {
    ("物理", "物理"), ("化学", "化学"), ("生物", "生物"), ("政治", "政治"), ("历史", "历史"), ("地理", "地理")
}