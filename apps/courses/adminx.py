import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "degree", "learn_times", "students"]  # 列表页显示的字段
    search_fields = ["name", "desc", "detail", "degree", "students"]
    list_filter = ["name", "desc", "detail", "degree", "learn_times", "students"]
    list_editable = ["degree", "desc"]  # 这样就不需要点进去进行编辑


class LessonAdmin(object):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course_name", "name", "add_time"]


class VideoAdmin(object):
    list_display = ["lesson", "name",  "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["les son", "name", 'add_time']


class CourseResourceAdmin(object):
    list_display = ["course", "name", 'download', "add_time"]
    search_fields = ["course", "name", 'download']
    list_filter = ["course_name", "name", 'download', "add_time"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
