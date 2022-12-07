from django.urls import path

from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('<int:news_id>/', views.mypage, name="mypage"),
     path('<int:news_id>/授業ページ', views.lecture1, name="lecture1"),
     path('<int:news_id>/授業ページ２', views.mypage2, name="lecture2"),
     path('<int:news_id>/関数', views.mypage, name="function"),
     path('<int:news_id>/四則演算', views.calcu, name="calucu")
     path('<int:news_id>/代入と式の値', views.assi, name="assi")
     path('<int:news_id>/関数問題', views.function, name="function"),
     path('<int:news_id>/四則演算問題', views.mypage, name="calcutest"),
     path('<int:news_id>/演習問題', views.alltest, name="alltest")
]
