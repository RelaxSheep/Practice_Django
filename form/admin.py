from django.contrib import admin
from .models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['content', 'public_date', 'was_published_recently']
    list_filter = ['public_date'] #Them sidebar filter theo public date
    search_fields = ['content'] #Them box tim kiem theo content
    # fields = ['content', 'public_date']
    fieldsets = [
        ('Content', {'fields' : ['content']}),
        ('Public date', {'fields': ['public_date']})
    ]
    inlines  = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['option', 'question', 'has_many_votes']
    list_filter = ['question']
    search_fields = ['option']
    fieldsets = [
        ('Option', {'fields': ['option', 'vote'], 'classes': ['collapse']}),
        ('Question', {'fields': ['question']}),
    ]

admin.site.register(Choice, ChoiceAdmin)