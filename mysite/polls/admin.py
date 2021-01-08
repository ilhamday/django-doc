from django.contrib import admin

from .models import Question, Choice

# Interface for choice in tabular style
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # reordering fields on the edit form in django admin
    # fields = ['pub_date', 'question_text']

    # split the form 
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
