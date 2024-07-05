from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
import os, openai

from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone

openai.api_base = "https://api.pawan.krd/pai-001/v1"


openai.api_key = "Your API Key"


def ask_openai(request, question):
    chats = Chat.objects.filter(user=request.user)[0:10]
    messages = []
    temp = {
        "role": "system",
        "content": "You are a helpful assistant. Your name is ShomserVai.",
    }
    messages.append(temp)
    for chat in chats:
        temp = {"role": "user", "content": chat.question}
        # print(temp)
        messages.append(temp)
        temp = {"role": "assistant", "content": chat.response}
        # print(temp)
        messages.append(temp)
    messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    response = openai.ChatCompletion.create(
        model="pai-001",
        messages=messages,
    )

    # print(response.choices[0]["message"]["content"])
    return response.choices[0]["message"]["content"].strip()


# Create your views here.
def chatbot(request):
    if not request.user.is_authenticated:
        return redirect("login")

    chat = Chat.objects.filter(user=request.user)
    if request.method == "POST":
        question = request.POST.get("message")
        response = ask_openai(request=request, question=question)
        chat = Chat(
            user=request.user,
            question=question,
            response=response,
            created_at=timezone.now(),
        )
        chat.save()
        return JsonResponse({"response": response})
    return render(request, "chatbot.html", {"chats": chat})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("chatbot")
        else:
            error_message = "Invalid username or password"
            return render(request, "login.html", {"error_message": error_message})
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect("chatbot")
            except:
                error_message = "Error creating account"
                return render(
                    request, "register.html", {"error_message": error_message}
                )
        else:
            error_message = "Password dont match"
            return render(request, "register.html", {"error_message": error_message})
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
