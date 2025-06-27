from rest_framework.views import APIView
from rest_framework.response import Response

class PublicAPI(APIView):
    def get(self, request):
        return Response({"message": "This is a public endpoint."})
    
    def post(self, request):
        return Response({"message": "This is a public endpoint."})

from rest_framework.permissions import IsAuthenticated

class ProtectedAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello {request.user.username}, this is a protected endpoint."})

    def post(self, request):
        return Response({"message": f"Hello {request.user.username}, this is a protected endpoint."})
    

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import TelegramUser

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", {})
        chat = message.get("chat", {})
        username = chat.get("username")

        if message.get("text") == "/start" and username:
            TelegramUser.objects.get_or_create(username=username)
            return JsonResponse({"message": f"Welcome {username}, your data is saved!"})

    return JsonResponse({"message": "Invalid or ignored"})
