import xadmin

from apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    pass


class CourseOrgAdmin(object):
    pass


class CityAdmin(object):
    list_display = ["id", "name", "desc"]  # 列表页显示的字段
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]
    list_editable = ["name", "desc"]  # 这样就不需要点进去进行编辑


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
