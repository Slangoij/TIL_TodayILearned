from django import forms
from .models import Post

# form 클래스 - forms.Form상속
# Model 클래스 - forms.ModelForm 상속
class PostForm(forms.ModelForm):
    # 내부(Nested/inner) 클래스로 Meta 클래스를 정의 => ModelForm 관련 설정
    
    class Meta:
        model = Post # Form을 만들 때 참조할 Model클래스 지정
        fields = "__all__" # create_al, update_at은 auto_now(자동 등록)했기 때문에 Form Field로 사용 안함
        # Model의 Field들 중 Form Field로 만들 Field들 지정. 모두 지정할 경우 문자열로 __all__지정
        # 몇 개만 지정할 경우 리스트에 Field이름을 지정 ex) fields = ['content', 'title']
        # 특정 Field를 제외한 나머지로 지정할 경우 exclude = ['title'] # title 빼고 나머지
