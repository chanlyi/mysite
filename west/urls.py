from django.conf.urls import patterns, include, url

#urlpatterns = patterns('',
#    url(r'^$', 'west.views.first_page'),
#)

#urlpatterns = patterns('',
#    url(r'^staff/','west.views.staff'),
#)

#urlpatterns = patterns('',
#    url(r'^templay/','west.views.templay'),
#)

#urlpatterns = patterns('.',
#    url(r'^investigate/','west.views.investigate'),
#)

urlpatterns = patterns('',
    #url(r'^form/','west.views.form'),
    (r'^$', 'west.views.first_page'),
    (r'^staff/','west.views.staff'),
    (r'^templay/','west.views.templay'),
    (r'^form/','west.views.form'),
    (r'^investigate/','west.views.investigate'),
)

