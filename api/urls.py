from django.conf.urls import url

from api import views


urlpatterns = [
    url(r'^students/$', views.StudentsListCreateAPIView.as_view(), name='list_create_students'),
    url(r'^(?P<subject>\w+)/$', views.StudentRetrieveUpdateAPIView.as_view({'get': 'list'}), name='retrieve_update_student'),
    url(r'^users/$', views.UsersListAPIView.as_view(), name='list_users'),
]
