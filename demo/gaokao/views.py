from django.shortcuts import render
from gaokao import models

# 查找数据
def search_school(request):
    data = {}  #存放全部数据
    dic = {}   #字典
    lit = []   #列表，其中包含数个字典
    if request.POST:
        conditional = {}
        # 获取用户提供的学校名称关键字
        school = request.POST.get("school")
        conditional['pschool__contains'] = school  # 设置对学校名称关键字的筛选条件

        # 获取用户输入的专业关键
        profession = request.POST.get("profession")
        conditional['pprofess_name__contains'] = profession

        # 获取用户输入的分数线下限
        lscore = request.POST.get("lscore")
        conditional['pscore_line__gte'] = lscore

        # 获取用户输入的分数线上限
        hscore = request.POST.get("hscore")
        conditional['pscore_line__lte'] = hscore

        # 获取用户输入的位次下限值
        lrank = request.POST.get("lrank")
        conditional['prank__gte'] = lrank

        # 获取用户输入的位次上限值
        hrank = request.POST.get("hrank")
        conditional['prank__lte'] = hrank

        # 获取用户输入的对地区的筛选要求
        region = request.POST.get("region")
        conditional['parea__contains'] = region
        schools = models.ProfessInformation.objects.filter(**conditional)  #检索符合条件的结果, 这里用**可以将字典中的值都取出来
        for i in range(schools.count()):  #对各项信息分类后放入列表
            dic["school"] = schools[i].pschool
            dic["profess_name"]  = schools[i].pprofess_name
            dic["score_line"] = schools[i].pscore_line
            dic["rank"] = schools[i].prank
            dic["remark"] = schools[i].premark
            lit.append(dic)
            dic = {}
    data["school"] = lit #将变量全部放入data
    return render(request,"search_school.html",data)  #传递给search_book.html