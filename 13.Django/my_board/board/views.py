from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy

from .forms import PostForm
from .models import Post

# Create your views here.
# 글 등록

# CreateView 등록(저장-insert 처리)
#   get 방식 요청: 입력양식 화면으로 이동(render())
#   post방식 요청: 입력(등록) 처리
#                  성공페이지로 이동(redirect)
#                  처리실패: 입력양식 화면으로 이동(render())
class PostCreateView(CreateView):
    template_name = 'board/post_create.html' # 입력양식 화면 template 경로
    form_class = PostForm # 요청파라미터를 처리할 Form을 지정
    # success_url = reverse_lazy("board:detail") # 등록 처리 후 이동할 경로->redirect방식 이동->view의 url을 등록
    
    # success_url 설정을 대신
    #   success_url에서 insert한 Model객체를 접근하려면 이 메소드를 overriding해야 한다.
    #   insert한 모델 객체 조회: self.objct
    def get_success_url(self):
        # 반환값: 등록 성공 후 redirect 방식으로 이동할 View의 url을 문자열로 반환
        return reverse_lazy('board:detail', args=[self.object.pk]) # args: path parameter로 전달할 값들을 리스트에 순서대로 넣는다.


# 하나의 글 정보 조회(pk)
# DetailView - pk로 조회한 결과를 template으로 보내주는 Generic View
#   url 패턴: pk를 path 파라미터로 받는다. <type:pk> 변수명을 pk로 지정해야 한다.
#             이 path parameter값을 이용해 select
class PostDetailView(DetailView):
    template_name = "board/post_detail.html" # 응답할 template의 경로
    model = Post
    # pk로 조회할 Model 클래스. 조회결과를 "post"(모델클래스명 소문자로 변경), "object"라는 이름으로 template에게 전달


# 글 수정처리
# UpdateView
#  - GET 요청처리: pk로 수정할 정보를 조회해서 template(수정 form)으로 전달
#  - POST요청처리: update 처리. redirect방식으로 View를 요청
#  - template_name: 수정 form template파일의 경로
#  - form_class: Form/ModelForm 클래스 등록
#  - model: Model 클래스 등록 (수정폼 template에 전달할 값을 조회하기 위해)
#  - success_url: 수정 처리 후 redirect방식으로 이동할 View의 url (path parameter로 update한 Model정보를
#                 사용할 경우 get_success_url()를 오버라이딩) 
class PostUpdateView(UpdateView):
    template_name = "board/post_update.html"
    form_class = PostForm
    model = Post

    def get_success_url(self):
        return reverse_lazy('board:detail', args=[self.object.pk])