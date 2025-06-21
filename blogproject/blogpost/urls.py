from django.urls import path
from .views import BlogList,BlogDetail,BlogCreate,BlogDelete,BlogUpdate

urlpatterns = [
    path('', BlogList.as_view(), name='list'),  # ルートURLをリストビューに
    path('list/', BlogList.as_view(), name='list_alt'),  # 既存のlist URLも維持
    path('detail/<int:pk>', BlogDetail.as_view(), name='detail'),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
    path('update/<int:pk>', BlogUpdate.as_view(), name='update'),
]

