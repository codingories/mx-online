from django.db import models

from apps.organizations.models import Teacher
from apps.users.models import BaseModel

# 1. 设计表结构有几个重要的点

"""
课程 章节 视频 课程资源
一个实体对应一张表
#1. 实体1<关系>实体2
课程 章节 视频 课程资源
#2. 实体的具体字段
#3. 每一个字段的类型，是否必填写
"""


class Course(BaseModel):  # 给每一个实体添加一个add_time,做日志分析用
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")  # 以最小单位存数据库，秒
    degree = models.CharField(verbose_name="难度", choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=10)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name="课程类别")
    tag = models.CharField(default='', max_length=20, verbose_name="课程标签")
    youneed_know = models.CharField(default='', max_length=256, verbose_name="课程须知")
    teacher_tell = models.CharField(default='', max_length=256, verbose_name="教师建议")

    detail = models.TextField(verbose_name="课程详情")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="封面图", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    # CASCADE 表示对应的外键删除了那么当前数据也会删除，及联删除。SET_NULL表示当前数据置空,此时null=True,blank=True必须设置
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, verbose_name=u"访问地址")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    name = models.CharField(verbose_name=u"名称", max_length=100)
    file = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="下载地址", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
