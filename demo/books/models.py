from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """图书的模型类"""
    btitle = models.CharField(verbose_name="名称", max_length=20)
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(verbose_name='阅读量', default=0)
    bcomment = models.IntegerField(verbose_name='评论量', default=0)
    is_delete = models.BooleanField(verbose_name='逻辑删除', default=False)

    class Meta:
        db_table = "tb_books"
        verbose_name = "图书"
        verbose_name_plural = "图书" # 都是比在admin显示采用

class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别'),
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = "英雄"

    def __str__(self):
        return self.hname