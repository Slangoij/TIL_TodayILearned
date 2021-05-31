from django.db import models

# Create your models here.
# 글의 카테고리
class Category(models.Model):
    # pk - 자동증가 정수 컬럼
    category_code = models.AutoField(primary_key=True)
    # CharField() 문자열 필드
    # 매개변수 verbose_name: 화면에 나올 때 라벨명
    category_name = models.CharField(max_length=200, verbose_name="글 카테고리")

    def __str__(self):
        return f"{self.pk}. {self.category_name}"


# 게시물(글)
# title(제목), content(글내용), create_at(등록 일시), update_at(수정 일시), writer(글쓴이-후에 추가)
class Post(models.Model):
    # 만약 이 값을 pk로 쓰려면 ,primary_key=True) 를 추가
    title = models.CharField(max_length=255, verbose_name="글제목") # Not NULL, 빈문자열 허용x
    content = models.TextField(verbose_name="글내용") # TextField: 대용량 text
    # null=False(기본): not null 여부 - False:Not null, True: null허용컬럼
    # blank=False(기본): 빈 문자열 허용여부
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name="글 분류",
                                 null=True, blank=True)
    # 작성일시 auto_now_add=True(기본값:False) => insert 시점의 일시를 저장하고 그 이후에는 update하지 않음
    create_at = models.DateTimeField(verbose_name='작성일시', auto_now_add=True)
    # 수정일시 auto_now=True(기본값:False) => insrt/update할 때마다 그 시점의 일시를 저장
    update_at = models.DateTimeField(verbose_name="최신 수정일시", auto_now=True)

    def __str__(self):
        return f"{self.pk}. {self.title}"