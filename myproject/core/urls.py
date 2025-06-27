from django.urls import path
from .views import PublicAPI, ProtectedAPI, telegram_webhook

urlpatterns = [
    path('telegram/webhook/', telegram_webhook),
    path('public/', PublicAPI.as_view()),
    path('protected/', ProtectedAPI.as_view()),
]
