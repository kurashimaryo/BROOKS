from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import post

def index (request):
 #   return HttpResponse("HelloWorld")
     posts = post.objects.order_by('-published')
     return render(request, 'posts/index.html', {'posts': posts})

def detailpj(request,post_id):
    post1 = get_object_or_404(post, pk=post_id)
    return render(request, 'posts/detailpj.html', {'post2': post1})

def yourprof(request):
    param = {
            'msg' :'相手のプロフィール画面',
            }
    return render(request, 'posts/yourprof.html',param)

def jfinal(request):
    param = {
            'msg' :'応募最終確認画面',
            }
    return render(request, 'posts/jfinal.html',param)

def loginpage(request):
    param = {
            'msg' :'ログイン画面',
            }
    return render(request, 'posts/loginpage.html',param)

def mypage(request):
    param = {
            'msg' :'マイページ画面',
            }
    return render(request, 'posts/mypage.html',param)

def makepj(request):
    param = {
            'msg' :'案件作成画面',
            }
    return render(request, 'posts/makepj.html',param)

def jlist(request):
    param = {
            'msg' :'受注者候補一覧画面',
            }
    return render(request, 'posts/jlist.html',param)

def wantlist(request):
    param = {
            'msg' :'やりたい案件一覧画面',
            }
    return render(request, 'posts/wantlist.html',param)

def makeprof(request):
    param = {
            'msg' :'プロフィール作成画面',
            }
    return render(request, 'posts/makeprof.html',param)

def jhlist(request):
    param = {
            'msg' :'受注/発注一覧画面',
            }
    return render(request, 'posts/jhlist.html',param)

def jreal(request):
    param = {
            'msg' :'取引状況画面(受注)',
            }
    return render(request, 'posts/jreal.html',param)

def mdlreview(request):
    param = {
            'msg' :'中間成果物レビュー画面',
            }
    return render(request, 'posts/mdlreview.html',param)

def finreview(request):
    param = {
            'msg' :'最終成果物レビュー画面',
            }
    return render(request, 'posts/finreview.html',param)

def bothreview(request):
    param = {
            'msg' :'双方レビュー画面',
            }
    return render(request, 'posts/bothreview.html',param)

def hreal(request):
    param = {
            'msg' :'取引状況画面(発注)',
            }
    return render(request, 'posts/hreal.html',param)