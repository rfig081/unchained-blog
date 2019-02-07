from django.urls import path, re_path
from blog import views



urlpatterns = [
    #Class Views
    path('', views.PostListView.as_view(),name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('post/new/', views.CreatePostView.as_view(),name='post_new'),
    path('drafts/', views.DraftListView.as_view(),name='post_draft_list'),
    re_path('^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(),name='post_detail'),  
    re_path('^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(),name='post_edit'), 
    re_path('^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(),name='post_delete'), 

    #Function Views    
    re_path('^post/(?P<pk>\d+)/publish/$', views.post_publish,name='post_publish'), 
    re_path('^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post,name='add_comment_to_post'), 
    re_path('^comment/(?P<pk>\d+)/approve/$', views.comment_approve,name='comment_approve'),      
    re_path('^comment/(?P<pk>\d+)/delete/$', views.comment_delete,name='comment_delete'),
]