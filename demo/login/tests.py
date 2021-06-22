from django.test import TestCase
from django.db.models.query import QuerySet
from django.shortcuts import reverse, redirect
from django.http import HttpRequest

from login.forms import RegisterForm
from login.models import User
from login.views import *
import random
import string


# Create your tests here.
class RegisterPageCase(TestCase):


    def setUp(self):
        print("start test Register Page")

    def tearDown(self):
        print("Register page test over")

    def test_get_register_page(self):
        response = self.client.get("/register/")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_correct(self):
        user = {
            "username": "testuser",
            "password": "123456",
            "repassword": "123456",
            "email": "testexample@test.com",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        self.assertRedirects(response, "/login/")

    def test_post_register_page_no_repassword(self):
        user = {
            "username": "testuser",
            "password": "123456",
            "email": "testexample@test.com",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, 'register_form', "repassword", "请确认密码")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_no_username(self):
        user = {
            "password": "123456",
            "repassword": "123456",
            "email": "testexample@test.com",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, 'register_form', "username", "请输入用户名")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_no_password(self):
        user = {
            "username": "testuser",
            "repassword": "123456",
            "email": "testexample@test.com",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, 'register_form', "password", "请输入密码")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_no_email(self):
        user = {
            "username": "testuser",
            "password": "123456",
            "repassword": "123456",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, "register_form", "email", "请输入电子邮箱")

    def test_post_register_page_no_telephone(self):
        user = {
            "username": "testuser",
            "password": "123456",
            "repassword": "123456",
            "email": "testexample@test.com",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, "register_form", "telephone", "请输入手机号")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_no_telephone(self):
        user1 = {
            "username": "testuser",
            "password": "123456",
            "repassword": "123456",
            "email": "1018510885@qq.com",
            "telephone": "18258268826",
        }
        user2 = {
            "username": "testuser",
            "password": "123456",
            "repassword": "123456",
            "email": "1018510885@qq.com",
            "telephone": "18258268826",
        }
        self.client.post("/register/", data=user1)
        response2 = self.client.post("/register/", data=user2)
        self.assertFormError(response2, "register_form", "username", "用户名已存在")
        self.assertTemplateUsed(response2, "register.html")

    def test_post_register_page_random_user(self):
        # 随机生成500个用户进行测试
        for i in range(50):
            # 生成随机用户名
            username = random.choice(string.ascii_letters)
            length = random.randint(7, 19)
            for i in range(length):
                username = username + random.choice(string.ascii_letters + string.digits)
            # 生成随机密码
            password = ""
            length = random.randint(6, 16)
            for i in range(length):
                password = password + random.choice(string.ascii_letters + string.digits)

            repassword = password

            email = "1018510885@qq.com"
            telephone = "1" + str(random.choice([3, 4, 5, 7, 8]))

            for i in range(9):
                telephone += random.choice(string.digits)

            user = {
                "username": username,
                "password": password,
                "repassword": repassword,
                "email": email,
                "telephone": telephone,
            }
            response = self.client.post("/register/", data=user)

            uer = User.objects.get(username=username)
            self.assertEqual(type(uer), User)
            self.assertRedirects(response, "/login/")

    def test_post_register_page_ch_username(self):
        user = {
            "username": "朱佳炜12345",
            "password": "123456",
            "repassword": "123456",
            "telephone": "18258268826",
            "email": "1018510885@qq.com",
        }
        response = self.client.post("/register/", data=user)
        self.assertRedirects(response, "/login/")

    def test_post_register_page_username_startwith_digits(self):
        user = {
            "username": "12345朱佳炜",
            "password": "123456",
            "repassword": "123456",
            "telephone": "18258268826",
            "email": "1018510885@qq.com",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, "register_form", "username", "用户名不能包含特殊字符，且不能以数字开头")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_ch_telephone(self):
        user = {
            "username": "朱佳炜12345",
            "password": "123456",
            "repassword": "123456",
            "telephone": "朱佳炜11111111",
            "email": "1018510885@qq.com",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, "register_form", "telephone", "手机号格式错误")
        self.assertTemplateUsed(response, "register.html")

    def test_post_login_page_ch(self):
        user = {
            "username": "123testuser",
            "password": "123456",
        }
        response = self.client.post("/login/", data=user)
        self.assertFormError(response, "login_form", "username", "用户名不存在")



