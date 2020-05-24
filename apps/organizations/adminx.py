import xadmin

from apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin(object):
    pass


class CourseOrgAdmin(object):
    pass


class CityAdmin(object):
    pass


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
