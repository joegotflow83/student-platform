from django.conf.urls import url
from django.contrib.auth import views as auth_views

from accounts import views


urlpatterns = [
    url(r'^user_signup/$', views.StudentSignup.as_view(), name='user_signup'),
    url(r'^teacher_signup/$', views.TeacherSignup.as_view(), name='teacher_signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
]
