from datetime import datetime
from django.db import models
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
    name = models.CharField(verbose_name="课程名", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")  # 以最小单位存数据库，秒

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name
