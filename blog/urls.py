from django.urls import path
from .views import Index, ArticleDetailView

urlpatterns = [
    path('', Index.as_view(), name='bloglist'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
]