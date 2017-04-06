from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]                        # Choice 모델 클래스 같이 보기
    list_display = ('qustion_text', 'pub_date')     # 레코드 리스트 항목 지정
    list_filter = ['pub_date']                      # 필터 사이드 바 추가
    search_fields = ['question_text']               # 검색 박스 추가

admin.site.register(Question)
admin.site.register(Choice)
