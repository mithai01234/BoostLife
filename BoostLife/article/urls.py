from .views import *
from django.urls import path

urlpatterns = [
    path('api/article/', ImageInfoList.as_view(), name='image-info-list'),
    path('api/article/five/', ImageInfoListFive.as_view(), name='image-info-list'),

    path('backend/articles/',article_list, name='article_list'),
    path('backend/articles/add/', article_add, name='article_add'),
    path('backend/articles/delete/<int:article_id>/', article_delete, name='article_delete'),
    path('backend/articles/edit/<int:article_id>/', article_edit, name='article_edit'),
    path('backend/articles/update/<int:article_id>/', article_update, name='article_update'),

    path('backend/article/activate_article/<int:product_id>/', activate_article, name='article/activate_article'),
    path('backend/article/deactivate_article/<int:product_id>/', deactivate_article,
         name='article/deactivate_article')

]