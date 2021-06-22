# -*- coding: UTF-8 -*-
from login import models
from django import forms
import re
from django.core.exceptions import ValidationError
from login.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=8,
        error_messages={
        'min_length': "用户名长度至少8位",
        'max_length': "用户名最长20位",
        "required": "请输入用户名"},
        label="用户名", widget=forms.TextInput({"placeholder": "用户名", }))
    password = forms.CharField(max_length=16, min_length=6, label="密码", required=True,
        widget=forms.PasswordInput({
        "placeholder": "密码", }),
        error_messages={
            "required":"请输入密码"})
    repassword = forms.CharField(max_length=16, min_length=6, label="确认密码", required=True,
        widget=forms.PasswordInput({
        "placeholder": "确认密码"}),
        error_messages={"required": "请确认密码"})
    telephone = forms.CharField(max_length=11, min_length=11, label="手机号码",
        required=True,
        widget=forms.TextInput({
        "placeholder": "手机号"}),
        error_messages={"required": "请输入手机号"})
    email = forms.EmailField(required=True, label="电子邮箱", widget=forms.TextInput({"placeholder": "电子邮箱"}),
                            error_messages={"required": "请输入电子邮箱"})


    def clean_username(self):
        username = self.cleaned_data.get("username").strip()
        user = User.objects.filter(username=username)
        matchObj = re.match(r'^[a-zA-Z\u4e00-\u9fa5][a-zA-Z\u4e00-\u9fa50-9]{7,19}$', username)
        if not matchObj:
            raise ValidationError("用户名不能包含特殊字符，且不能以数字开头")
        if len(user):
            raise ValidationError("用户名已存在")
        else:
            return username

    def clean_telephone(self):
        telephone = self.cleaned_data.get("telephone")
        result = re.match(r"^1[3|4|5|7|8][0-9]{9}$", telephone)
        if result:
            return telephone
        else:
            raise ValidationError("手机号格式错误")

    def clean_repassword(self):
        pwd1 = self.cleaned_data.get("repassword")
        pwd2 = self.cleaned_data.get("password")
        if pwd1 == pwd2:
            return pwd1
        else:
            raise ValidationError("输入密码不一致")




class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=8,
                               error_messages={'min_length': "用户名长度至少8位", 'max_length': "用户名最长20位"}, label="用户名",
                               widget=forms.TextInput({"placeholder": "用户名", }))
    password = forms.CharField(max_length=16, min_length=6, label="密码",
                               widget=forms.PasswordInput({"placeholder": "密码"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username)
        if len(user) == 1 :
            return username
        elif len(user) == 0:
            raise ValidationError("用户名不存在")

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            if user.check_password(password):
                return password
            else :
                raise ValidationError("密码错误")


