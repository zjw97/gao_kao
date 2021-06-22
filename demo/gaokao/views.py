from django.shortcuts import render, redirect
from django.http import HttpResponse
from gaokao.models import ProfessInformation, SportsInformation, ArtInformation
from gaokao.forms  import InputForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import matplotlib.image as mpig
from matplotlib.ticker import MaxNLocator
from PIL import Image
import numpy as np
from tkinter import messagebox
import tkinter
import functools



databases = {
    "putong": ProfessInformation,
    "tiyu": SportsInformation,
    "yishu": ArtInformation,
}

def filter_schools(request):
    save_para = {}
    conditional = {}
    # 获取用户提供的学校名称关键字
    db = databases[request.POST["type"]]
    db.objects.filter(psubject__exact="").update(psubject="不提科目要求")
    school = request.POST.get("school")
    if school:
        conditional['pschool__contains'] = school

    # 获取用户输入的专业关键
    profession = request.POST.get("profession")
    if profession:
        conditional['pprofess_name__contains'] = profession

    # 获取用户输入的分数线下限
    lscore = request.POST.get("lscore")
    if lscore:
        conditional['pscore_line__gte'] = lscore

    # 获取用户输入的分数线上限
    hscore = request.POST.get("hscore")
    if hscore:
        conditional['pscore_line__lte'] = hscore

    # 获取用户输入的位次下限值
    lrank = request.POST.get("lrank")
    if lrank:
        conditional['prank__gte'] = lrank

    # 获取用户输入的位次上限值
    hrank = request.POST.get("hrank", 0)
    if hrank:
        conditional['prank__lte'] = hrank

    # 获取用户输入的对地区的筛选要求
    region = request.POST.get("region")
    save_para["region"] = region
    if region:
        conditional['parea__contains'] = region

    # 根据获得的筛选条件
    schools = db.objects.filter(**conditional)  # 检索符合条件的结果, 这里用**可以将字典中的值都取
    # print(schools)
    # 根据考生的选考科目进行二次筛选
    sublist = []  # 选考科目
    for i in range(6):
        sub = request.POST.get("s" + str(i + 1))
        if sub:
            sublist.append(sub)
    if len(sublist) < 3:
        top = tkinter.Tk()
        top.geometry('0x0+999999+0')
        messagebox.showinfo('提示', '请至少选择3个考试科目')
        top.destroy()
        return schools, save_para

    schools = schools.filter(
        Q(psubject__contains=sublist[0]) | Q(psubject__contains=sublist[1]) | Q(psubject__contains=sublist[2]) | Q(
            psubject__contains="不提科目要求"))

    return schools, save_para

def ch_to_list(schools):

    school_list = []
    for i in range(schools.count()):  # 对各项信息分类后放入列表
        # 汇总筛选到的每一条数据，存放到字典中
        dic = {}
        dic["area"] = schools[i].parea
        dic["school"] = schools[i].pschool
        dic["profess_name"] = schools[i].pprofess_name
        dic["score_line"] = schools[i].pscore_line
        dic["subject"] = schools[i].psubject
        dic["plan_num"] = schools[i].pplan_num
        dic["rank"] = schools[i].prank
        dic["remark"] = schools[i].premark
        dic["year"] = schools[i].pyear
        school_list.append(dic)

    return school_list

# 查找数据
@login_required()
def search_school(request):
    data = {}  #存放全部数据
    if request.method == "GET":
        return render(request, "search_school.html")
    elif request.method == "POST":
        # request.COOKIES.
        # 获取所有的汇总信息并且得到筛选结果
        schools, last_search_para = filter_schools(request)

        draw = request.POST.get("draw")
        if draw:
            visualizeP(schools)

        year = request.POST.get("year")
        if year:
            schools = schools.filter(pyear__exact=year)
        # table_list = ch_to_list(schools)
        data["school"] = schools #将变量全部放入data
        # data.update(last_search_para)

        return render(request, "search_school.html", data)  #传递给search_book.html

# 可视化
def visualizeP(schools):
    res = {}
    year2index = {
        "18": 0,
        "19": 1,
        "20": 2,
    }
    for sch in schools:
        key = sch.pschool + ":" + sch.pprofess_name
        if key in res.keys():
            score_line = sch.pscore_line
            index = year2index[sch.pyear]
            res[key][index] = score_line
        else:
            res[key] = [np.nan, np.nan, np.nan]
            score_line = sch.pscore_line
            index = year2index[sch.pyear]
            res[key][index] = score_line

    # print(res)
    # 绘图，并保存
    x = [18, 19, 20]
    fig = plt.figure(figsize=(15, 10))
    # 清理res中所有为nan的数据
    for labels, y in res.items():
        index_list = []
        grade_list = []
        for i, grade in enumerate(y):
            if not np.isnan(grade):
                index_list.append(x[i])
                grade_list.append(grade)

        plt.plot(index_list, grade_list, ls="-", lw=1, marker="o", label=labels)
        for xx, yy in zip(index_list, grade_list):
            plt.text(xx, yy+0.3, str(yy), ha="center", va="bottom", fontsize=10.5)
    plt.legend(bbox_to_anchor=(1.01, 1.01), loc=0, borderaxespad=0)
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False  #去除中文乱码
    plt.xlabel("年份")
    plt.ylabel("分数")
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True)) #坐标轴整数显示
    plt.savefig("D:/研一/上课PPT/软件工程/结对项目/gao_kao/demo/static/fig.png", bbox_inches="tight", dpi=fig.dpi, pad_inches=0.2) #保存图像
    plt.close()

# 无法绘图时
def warning():
    img = Image.open("D:/研一/上课PPT/软件工程/结对项目/gao_kao/demo/static/warning.png")
    img.save("D:/研一/上课PPT/软件工程/结对项目/gao_kao/demo/static/fig.png")