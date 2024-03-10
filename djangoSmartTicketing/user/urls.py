from django.urls import path
from servicii.views import ServiciiListView, ServiciiDetaislView, ServiciiUpdateView,ServiciiCreateView,ServiciiDeleteView
from user.views import UserListView, UserDetaislView, UserUpdateView, UserCreateView, UserDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='user-all'),
    path('detail/<int:pk>', UserDetaislView.as_view(), name='user-detail'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='user-update'),
    path('create/<int:pk>',UserCreateView.as_view(), name='user-create'),
    path('delete/<int:pk>',UserDeleteView.as_view(), name='user-delete')
]

