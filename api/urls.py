from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^students/$', views.StudentsListCreateAPIView.as_view(), name='list_create_students'),
    url(r'^student/class=(?P<subject>\w+)/$', views.StudentNameClassAPIView.as_view({'get': 'list'}), name='student_class_name'),
    url(r'^users/$', views.UsersListAPIView.as_view(), name='list_users'),
    url(r'^user/(?P<pk>\d+)/$', views.UserRetrieveUpdateAPIView.as_view(), name='retrieve_update_user'),
    url(r'^announcements/$', views.AnnouncementsListCreateAPIView.as_view(), name='list_create_announcements'),
]
