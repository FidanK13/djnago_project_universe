from django.urls import path

from .views import home_view, works_view, about_view, work_view, contact_view, \
    work_create_view, register_view, login_view,logout_view, components_view

urlpatterns = [
    path("",home_view),
    path("home/",home_view, name='home_page'),
    path("works/",works_view, name='works_page'),
    path("about/",about_view),
    path("work/<int:work_id>/", work_view, name='work_page'),
    path("contact/", contact_view),
    path("work-create/",work_create_view),
    path("register/",register_view, name='register_page'),
    path("login/",login_view,name='login_page'),
    path("logout/", logout_view, name='logout_page'),
    path("components/", components_view),
]
