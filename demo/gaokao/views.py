from django.shortcuts import render
from gaokao import models

# 查找数据
def search_school(request):
    data = {}  #存放全部数据
    dic = {}   #字典
    lit = []   #列表，其中包含数个字典
    if request.POST:
        inp = request.POST.get("q")  # 获得输入
        # reg = request.POST.get("region")  # 获得输入
        schools = models.ProfessInformation.objects.filter(pschool__contains=inp)  #检索符合条件的结果
        # typ = request.POST.get("type")
        # if typ:
        #     books = books.filter(btype=typ)
        for i in range(schools.count()):  #对各项信息分类后放入列表
            dic["school"] = schools[i].pschool
            dic["profess_name"]  = schools[i].pprofess_name
            dic["score_line"] = schools[i].pscore_line
            dic["rank"] = schools[i].prank
            lit.append(dic)
            dic = {}
    data["school"] = lit #将变量全部放入data
    return render(request,"search_school.html",data)  #传递给search_book.html