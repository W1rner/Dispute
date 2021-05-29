"""Dispute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from dispute_site import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about_page),
    path('error/', views.error_page),
    # path('', views.popular_page),
    # path('about/', views.about_page),
    path('popular/', views.popular_page, name='popular'),
    path('recomended/', views.recomended_page, name='recomended'),
    path('cathegory/', views.cathegory_page),
    path('account/', include('accounts.urls')),
    path('users/user/', views.userpage_page),

    # path('createcomment/', views.commentary_page, name='commentary_page'),
    path('createquestion/', views.create_question_page),
    path('questions/', views.questions_page),
    path('questions/quest/', views.quest_page),
    # path('/questions/quest?id={{quest.id}}/comment', views.add_comment, name='add_comment'),
]

handler404 = views.custom_404_page
