# urls.py url -  View 연결
# polls/urls.py -> polls app용 url pattern 설정스크립트

from django.urls import path
from . import views
from .models import Question
from django.views.generic import ListView, DetailView

# 이 url pattern의 namespace(prefix)로 사용할 값 설정
# app 설정의 이름 호출 시 다른 app과 구분하기 위해 사용
app_name = "polls"

urlpatterns = [
    # CBV를 등록: ViewClass이름.as_view()
    # path("list", views.QuestionListView.as_view(), name='list'),
    path('list', ListView.as_view(model=Question, template_name="polls/list.html"), name='list'),
    path("form/<int:question_id>", views.VoteView.as_view(), name='vote'),
    # path('vote', views.vote, name='vote'),
    # path('result/<int:pk>', views.QuestionDetailView.as_view(), name='vote_result'),
    path('result/<int:pk>', DetailView.as_view(model=Question, template_name="polls/vote_result.html"), name='vote_result'),
]