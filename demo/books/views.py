from django.shortcuts import render,HttpResponse
from books import models 

"""
# 添加数据
def add_book(request):
    books = models.BookInfo.objects.create(btitle="如来神掌",bpub_data="1995-04-13") 
    print(books, type(books)) # Book object (18) 
    return HttpResponse("<p>数据添加成功！</p>")

# 全部数据
def all_book(request):
    books = models.BookInfo.objects.all() 
    print(books,type(books)) # QuerySet类型，类似于list，访问url时数据显示在命令行窗口中。
    return HttpResponse(books)

# 查找数据(一个)
def get_book(request):
    books = models.BookInfo.objects.get(id=5)
    print(books, type(books))  # 模型类的对象
    return HttpResponse(books)

# 筛选数据(多个)
def filter_book(request):
    books = models.BookInfo.objects.filter(id=3)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse(books)

# 查找不符合条件的数据
def exclude_book(request):
    books = models.BookInfo.objects.exclude(id=2)
    print(books, type(books))  # QuerySet类型，类似于list。
    return HttpResponse(books)

# 数据排序
def order_book(request):
    books = models.BookInfo.objects.order_by("id") # 查询所有，按照价格升序排列 
    books = models.BookInfo.objects.order_by("-id") # 查询所有，按照价格降序排列
    return HttpResponse(books)

# 查询数据量
def count_book(request):
    books = models.BookInfo.objects.count() # 查询所有数据的数量 
    return HttpResponse(books)

# 查询第一个数据
def first_book(request):
    books = models.BookInfo.objects.first() # 返回所有数据的第一条数据
    return HttpResponse(books)

# 查询最后一个数据
def last_book(request):
    books = models.BookInfo.objects.last() # 返回所有数据的最后一条数据
    return HttpResponse(books)

# 判断是否有数据
def exist_book(request):
    books = models.BookInfo.objects.exists()  
    return HttpResponse(books)

# 查询特定字段数据
def value_book(request):
    # 查询所有的id字段的数据 
    books = models.BookInfo.objects.values("id") 
    print(books[0]["id"], type(books)) # 得到的是第一条记录的price字段的数据
    return HttpResponse(books)
"""

# 查找数据
def search_book(request):
    data = {}  #存放全部数据
    dic = {}   #字典 
    lit = []   #列表，其中包含数个字典
    if request.POST:
        inp = request.POST.get("q")  #获得输入
        books = models.BookInfo.objects.filter(btitle__contains=inp)  #检索符合条件的结果
        typ = request.POST.get("type")
        if typ:
            books = books.filter(btype=typ)
        for i in range(books.count()):  #对各项信息分类后放入列表
            dic["title"] = books[i].btitle
            dic["date"]  = str(books[i].bpub_data)
            lit.append(dic)
            dic = {}
    data["book"] = lit #将变量全部放入data
    return render(request,"search_book.html",data)  #传递给search_book.html