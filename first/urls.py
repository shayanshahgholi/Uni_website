from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('register', views.register_page, name='register_page'),
    path ('register_add', views.register, name='register'),
    path ('contact', views.contact_us_page, name='contact-us-page'),
    path ('contact_send', views.contact_us, name='contact'),
    path ('logout', views.logout_page, name='logout'),
    path ('login_user', views.login_user, name='login_user'),
    path ('login', views.login_page, name='login'),
    path ('profile', views.profile_page, name='profile'),
    path ('edit', views.edit_page, name='edit_page'),
    path ('edit_profile', views.edit_user, name='edit'),
    path ('panel', views.panel_page, name='panel_page'),
    path ('make_new_course', views.make_new_course_page, name='make_new_course_page'),
    path ('add_course', views.add_course, name='course'),
    path ('all_courses', views.all_courses, name='all_courses'),


]