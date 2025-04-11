from django.urls import path, include
from .views import Index, ArticleDetailView, LikeArticle

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='bloglist'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('like/<int:pk>/', LikeArticle.as_view(), name='like_article'),

]