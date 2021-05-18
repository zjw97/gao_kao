from django.db import models

class ProfessInformation(models.Model):
    """专业的模型类的模型类"""
    LEVEL_CHOICE = (
        (1, '第一批'),
        (2, '第二批'),
        (3, '第三批')
    )
    parea = models.CharField(verbose_name="地区", max_length=20, null=False)
    pschool = models.CharField(verbose_name="学校", max_length=100, null=False)
    psch_code = models.CharField(verbose_name="学校代码", max_length=4, null=False)
    pprofess_name = models.CharField(verbose_name="专业名称", max_length=100, null=False)
    pprofess_code = models.CharField(verbose_name="专业代码", max_length=3, null=False)
    psubject = models.CharField(verbose_name="学科要求", max_length=100, null=True)
    premark = models.CharField(verbose_name="备注", max_length=1000, null=True)
    pplan_num = models.SmallIntegerField(verbose_name="计划数", null=True)
    pscore_line = models.SmallIntegerField(verbose_name="分数线", null=True)
    prank = models.IntegerField(verbose_name="位次", null=True)
    plever = models.CharField(verbose_name="层次", max_length=3, choices=LEVEL_CHOICE,null=False)
    pyear = models.CharField(verbose_name="年份", max_length=4, null=False)

    class Meta:
        db_table = "tb_profess" #指名数据库表名

    def __str__(self):
        return self.pprofess_name #指定数据对象的显示信息