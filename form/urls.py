from django.urls import path
from . import views


app_name = 'form'

urlpatterns = [
    path('', views.QuestionView.as_view(), name='question_view_url'),
    path('<int:question_id>/', views.QuestionDetalView.as_view(), name='question_detail_view_url'),
    path('<int:question_id>/value/', views.VoteQuestionView.as_view(), name='vote_question_view'),
]
