from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin): #검색기능 추가
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)