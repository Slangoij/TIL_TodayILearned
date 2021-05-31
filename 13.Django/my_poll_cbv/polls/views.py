from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse # reverse함수 : path 설정 이름으로 url 문자열을 만들어주는 함수

from django.views.generic import ListView, View, DetailView
from .models import Question, Choice

# ListView - 모델의 전체 데이터를 조회해서 template에게 전달. (Paging 기능제공)
class QuestionListView(ListView):
    model = Question # 조회할 모델클래스 지정
    template_name = "polls/list.html" # 응답할 template 경로
    # 조회결과를 template에게 전달 - 이름: '모델클래스명(소문자)_list', 'object_list'
    # 다른이름으로 전달할 경우 : context_object_name = '전송할이름'

# 투표 작업을 처리
# GET 요청: 투표 양식 (vote_form)
# POST 요청: 투표 처리 (vote)
class VoteView(View):
    # get방식 요청 처리
    def get(self, request, *args, **kwargs):
        # kwargs: path parameter를 조회
        print("==========================VoteView.get()")
        question_id = kwargs['question_id']
        try:
            question = Question.objects.get(pk=question_id)
            return render(request, "polls/vote_form.html", {"question":question})
            # 바로 해당 app의 templates 디렉토리에서 조회하므로 경로명은 이를 참고
        except:
            return render(request, 'polls/error.html',
                        {"error_message":"없는 질문을 작성하셨습니다."})
    
    # post방식 요청 처리
    def post(self, request, *args, **kwargs):
        print("==========================VoteView.post()")
        choice_id = request.POST.get('choice')

        # question_id = request.POST.get('question_id')
        question_id = kwargs['question_id']
        if not choice_id:
            question = Question.objects.get(pk=question_id)
            return render(request, 'polls/vote_form.html',
                        {
                            "question":question,
                            "error_message":"보기를 선택하세요."
                        })
        choice = Choice.objects.get(pk=choice_id)
        choice.vote += 1
        choice.save() # pk가 있다면 update, 없으면 insert

        url_str = reverse("polls:vote_result", args=[question_id])
        return redirect(url_str)

# DetailView: 특정 모델의 Primary key를 받아서 조회한 결과를 template에 전달
# primary key는 path parameter로 받아야 한다. urls.py에서 path parameter의 변수명은 <타입:pk>
# question의 id(pk)를 받아서 질문 하나를 조회한 후 template(vote_result.html)로 이동
class QuestionDetailView(DetailView):
    model = Question # 데이터를 조회할 Model 클래스 지정
    template_name = "polls/vote_result.html" # 이동할 template 경로