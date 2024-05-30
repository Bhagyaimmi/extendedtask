from django.urls import path
from firstapp import views



urlpatterns = [
    path('register/',views.RegisterView.as_view(), name='register'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('articles/', views.ArticleListView.as_view(), name='article-list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
    path('sample/email/notification/', views.SampleEmailNotification.as_view(), name='sample-email'),
    path('export/users/csv/', views.UserCSVExportView.as_view(), name='export-users-csv'),
    path('export/users/excel/', views.UserExcelExportView.as_view(), name='export-users-excel'),
    path('export/products/csv/', views.ProductCSVExportView.as_view(), name='export-products-csv'),
    path('export/products/excel/', views.ProductExcelExportView.as_view(), name='export-products-excel'),
    path('export/articles/csv/', views.ArticleCSVExportView.as_view(), name='export-articles-csv'),
    path('export/articles/excel/', views.ArticleExcelExportView.as_view(), name='export-articles-excel'),
    path('token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('password/reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    
]