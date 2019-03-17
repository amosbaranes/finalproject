from django.conf.urls import url
from .views import (course_detail, course_add, do_section, do_test,
                    show_results, course_list, index, show_results_all_sections)

app_name = "elearning"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^course_detail/(?P<pk>\d+)/$', course_detail, name='course_detail'),
    url(r'^course_list/$', course_list, name='course_list'),
    url(r'^course_add/$', course_add, name='course_add'),
    url(r'^section/(?P<section_id>\d+)/$', do_section, name='do_section'),
    url(r'^section/(?P<section_id>\d+)/test/$', do_test, name='do_test'),
    url(r'^section/(?P<section_id>\d+)/results/$', show_results, name='show_results'),
    url(r'^section/results_all/$', show_results_all_sections, name='show_results_all_sections'),
]
