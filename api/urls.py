from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^students/$', views.StudentsListCreateAPIView.as_view(), name='list_create_students'),
    url(r'^student/class=(?P<subject>\w+)/$', views.StudentNameClassAPIView.as_view({'get': 'list'}), name='student_class_name'),
    url(r'^users/$', views.UsersListCreateAPIView.as_view(), name='list_create_users'),
    url(r'^user/(?P<pk>\d+)/$', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_user'),
    url(r'^announcements/$', views.AnnouncementsListCreateAPIView.as_view(), name='viewset_announcements'),
    url(r'^announcement/(?P<pk>\d+)/$', views.AnnouncementRetrieveUpdateDestroyAPIView.as_view(), name='announcement_retrieve_update_destroy'),
    url(r'^classes/$', views.ClassesViewSet.as_view({'get': 'list'}), name='viewset_classes'),
]
