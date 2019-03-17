from django.conf.urls import url
from .views import index, signup, TeamMemberView

app_name = "main"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup/', signup, name='signup'),
    url(r'^dteammember/(?P<pk>\d+)/', TeamMemberView.as_view(), name='dteammember'),
]
