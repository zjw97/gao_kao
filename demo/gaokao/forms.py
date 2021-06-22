# -*- coding: UTF-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from gaokao import models
from gaokao.config import *



# 主页中筛选信息输入组件
class InputForm(forms.Form):

    # 可输入的筛选信息
    school = forms.CharField(label="学校名称", required=False)  # 学校名称
    profession = forms.CharField(label="专业名称", required=False)  # 专业名称
    lscore = forms.IntegerField(label="分数", required=False)
    hscore = forms.IntegerField(label="分数", required=False)  # hscore对应筛选区间的最大值
    lrank = forms.IntegerField(label="排名", required=False)  # 筛选名词高于lrank的专业
    hrank = forms.IntegerField(label="排名", required=False)  # 筛选名次低于hrank的专业
    area = forms.ChoiceField(label="地区", choices=AREA, required=False, initial=0, widget=forms.Select)
    # area = forms.TypedChoiceField(label="地区", choices=AREA, required=False, initial="", widget=forms.Select())
    type = forms.ChoiceField(label="考生类型", choices=TYPE, required=False, initial="", widget=forms.Select)
    level = forms.ChoiceField(label="批次", choices=LEVEL, required=False, initial="", widget=forms.Select)
    subject_choice = forms.MultipleChoiceField(label="选考科目", choices=SUBJECT_CHOICE, required=True,
                                               widget=forms.CheckboxSelectMultiple)