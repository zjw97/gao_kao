from django.db import models

#定义BookInfo
class BookInfo(models.Model):
    """图书的模型类"""
    btitle = models.CharField(verbose_name="名称", max_length=20) 
    bpub_data = models.DateField(verbose_name="发布日期")
    bread = models.IntegerField(verbose_name="阅读量", default=0)
    bcomment = models.IntegerField(verbose_name="评论量", default=0)
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)
    image = models.ImageField(verbose_name="图书封面", null=True, blank=True,upload_to="books")
    btype = models.CharField(verbose_name="类型", max_length=20, default="")

    class Meta:
        db_table = "tb_books" #指名数据库表名

    def __str__(self):
        return self.btitle #指定数据对象的显示信息