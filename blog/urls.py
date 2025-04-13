from django.urls import path, include
from .views import Index, ArticleDetailView, LikeArticle, DeleteArticleView, CreateArticleView, UpdateArticleView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('', Index.as_view(), name='bloglist'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='post_detail'),
    path('like/<int:pk>/', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_post'),
    path('create/', CreateArticleView.as_view(), name='create_post'),
    path('<int:pk>/update/', UpdateArticleView.as_view(), name='update_post'),
]