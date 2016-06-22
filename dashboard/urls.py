from django.conf.urls import url

from dashboard import views


urlpatterns = [
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^create/class/$', views.CreateClass.as_view(), name='create_class'),
    url(r'^list/classes/$', views.StudentListClasses.as_view(), name='list_classes'),
    url(r'^teacher/classes/$', views.TeacherListClasses.as_view(), name='teacher_classes'),
    url(r'^add/class/(?P<pk>\d+)/$', views.AddClass.as_view(), name='add_class'),
    url(r'^remove_class/(?P<class_pk>\d+)/(?P<student_pk>\d+)/$', views.RemoveClass.as_view(), name='remove_class'),
    url(r'^student/classes/(?P<pk>\d+)$', views.ViewStudentClasses.as_view(), name='student_classes'),
    url(r'^course/(?P<pk>\d+)/$', views.TeacherClassDetail.as_view(), name='teacher_course_detail'),
    url(r'^class/(?P<pk>\d+)/$', views.StudentClassDetail.as_view(), name='student_course_detail'),
    url(r'^create/class/announcement/(?P<pk>\d+)/$', views.CreateAnnouncement.as_view(), name='create_announcement'),
    url(r'^upload/file/(?P<pk>\d+)/$', views.UploadFile.as_view(), name='upload_file'),
]
