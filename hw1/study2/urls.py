from django.conf.urls.defaults import *

urlpatterns = patterns('study2.views',
    # main links.
    (r'^$', 'index'),
    (r'^consent/?$', 'consent'),
    (r'^doTrials/?$', 'beginSession'),
    (r'^choseBetweenUis/?$', 'choseBetweenUis'), 
    (r'^questionnaire/?$', 'questionnaire'), 
)

