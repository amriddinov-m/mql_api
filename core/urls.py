from django.urls import path

from core.views import BotApiView

urlpatterns = [
    path('bot/api/', BotApiView.as_view())
]