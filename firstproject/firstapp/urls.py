from django.urls import path

from .views import (
    RegisterView,UserListView,UserDetailView, ProductListView, ProductDetailView,
    ArticleListView, ArticleDetailView,UserProfileView,
    SampleEmailNotification,UserCSVExportView,UserExcelExportView,
     ProductCSVExportView ,ProductExcelExportView, ArticleExcelExportView,ArticleCSVExportView,
    UserSearchView,ProductSearchView,ArticleSearchView,  
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('sample/email/notification/', SampleEmailNotification.as_view(), name='sample-email'),
    path('export/users/csv/', UserCSVExportView.as_view(), name='export-users-csv'),
    path('export/users/excel/', UserExcelExportView.as_view(), name='export-users-excel'),
    path('export/products/csv/', ProductCSVExportView.as_view(), name='export-products-csv'),
    path('export/products/excel/', ProductExcelExportView.as_view(), name='export-products-excel'),
    path('export/articles/csv/', ArticleCSVExportView.as_view(), name='export-articles-csv'),
    path('export/articles/excel/', ArticleExcelExportView.as_view(), name='export-articles-excel'),
    path('users/search/', UserSearchView.as_view(), name='user-search'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('articles/search/', ArticleSearchView.as_view(), name='article-search'),
]