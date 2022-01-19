from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name="create_comment"),
    # path('<slug:slug>/<slug:new_post_slug>/', views.PostUpdateView.as_view(), name='new_post'),
    # path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', cache_page(60 * 15)(views.HomeView.as_view()), name="home"),
    # path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
    # path('', views.HomeView.as_view(), name='home'),
]