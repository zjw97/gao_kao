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

    def test_post_register_page_wrong1(self):
        user = {
            "username": "testuser",
            "password": "123456",
            "email": "testexample@test.com",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        # self.assertFormError(response, RegisterForm, "repassword", "请确认密码")
        self.assertTemplateUsed(response, "register.html")

    def test_post_register_page_wrong2(self):
        user = {
            "password": "123456",
            "repassword": "123456",
            "email": "testexample@test.com",
            "telephone": "13955556666",
        }
        response = self.client.post("/register/", data=user)
        self.assertFormError(response, RegisterForm, "username", "请输入用户名")
        self.assertTemplateUsed(response, "register.html")

    # def test_post_register_page_wrong(self):
    #     # 随机生成500个用户进行测试
    #     for i in range(500):
    #         # 生成随机用户名
    #         username = random.choice(string.ascii_letters)
    #         length = random.randint(7, 19)
    #         for i in range(length):
    #             username = username + random.choice(string.ascii_letters + string.digits)
    #         # 生成随机密码
    #         password = ""
    #         length = random.randint(6, 16)
    #         for i in range(length):
    #             password = password + random.choice(string.ascii_letters + string.digits)
    #
    #         repassword = password
    #
    #         email = "1018510885@qq.com"
    #         telephone = "1" + str(random.choice([3, 4, 5, 7, 8]))
    #
    #         for i in range(9):
    #             telephone += random.choice(string.digits)
    #
    #         user = {
    #             "username": username,
    #             "password": password,
    #             "repassword": repassword,
    #             "email": email,
    #             "telephone": telephone,
    #         }
    #         response = self.client.post("/register/", data=user)
    #
    #         uer = User.objects.get(username=username)
    #         self.assertEqual(type(uer), User)
    #         self.assertRedirects(response, "/login/")