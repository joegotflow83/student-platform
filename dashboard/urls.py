from django.conf.urls import url

from dashboard import views


urlpatterns = [
    url(r'^$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^create_class/$', views.CreateClass.as_view(), name='create_class'),
    url(r'^list_classes/$', views.ListClasses.as_view(), name='list_classes'),
    url(r'^add_class/(?P<pk>\d+)/$', views.AddClass.as_view(), name='add_class'),
    url(r'^student/classes/(?P<pk>\d+)/$', views.ViewStudentClasses.as_view(), name='student_classes'),
]
