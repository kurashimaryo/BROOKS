from django.conf.urls import url


from . import views

urlpatterns = [
        url(r'^$',views.index, name='index'),
        url('yourprof',views.yourprof, name='yourprof'),
        url('jfinal',views.jfinal, name='jfinal'),
        url('loginpage',views.loginpage, name='loginpage'),
        url('mypage',views.mypage, name='mypage'),
        url('makepj',views.makepj, name='makepj'),
        url('jlist',views.jlist, name='jlist'),
        url('wantlist',views.wantlist, name='wantlist'),
        url('makeprof',views.makeprof, name='makeprof'),
        url('jhlist',views.jhlist, name='jhlist'),
        url('jreal',views.jreal, name='jreal'),
        url('mdlreview',views.mdlreview, name='mdlreview'),
        url('finreview',views.finreview, name='finreview'),
        url('bothreview',views.bothreview, name='bothreview'),
        url('hreal',views.hreal, name='hreal'),
        
]