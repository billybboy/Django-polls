from django.urls import path

from . import views
# Let Django knows which app view to create for a url when using the {% url %} template tag
app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('polls/<int:pk>/result/', views.ResultView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]