from django import forms
from dispute_site.models import *

class CommentaryForm(forms.Form):
    text = forms.CharField(label='', max_length=COMMENT_SIZE)


class QuestionForm(forms.Form):
    header = forms.CharField(label='Заголовок', max_length=QUESTION_SIZE)
    text = forms.CharField(label='Сущность вопроса', max_length=COMMENT_SIZE)
    theme = forms.CharField(label='Ваш взгляд на этот вопрос', max_length=CATEGORY_SIZE)
