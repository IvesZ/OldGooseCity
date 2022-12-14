from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import TodoSerializer,UserSerializer
from .models import Todo, User
from django.http import HttpResponse
import json
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class userView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

 
def hello(request):
    return HttpResponse("Hello world ! ")


def login(request):
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    try:
        user = User.objects.get(email=email)
        if(user is None or (user.password!=pwd)):
            res_data = {"errorMsg": "unautharized"}
            return HttpResponse(json.dumps(res_data), content_type="application/json",status=200)
        else:
            res_data = {"errorMsg": "success", "token":email}
            return HttpResponse(json.dumps(res_data), content_type="application/json",status=200)
    except:
        res_data = {"errorMsg": "unautharized"}
        return HttpResponse(json.dumps(res_data), content_type="application/json",status=200)

    
def register(request):
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    queryset = User.objects.all()
    user = User.objects.filter(email=email)
    if len(user) == 0:
        User(len(queryset)+1, email, pwd).save()
        res_data = {"errorMsg": "success"}
        return HttpResponse(json.dumps(res_data),content_type="application/json",status=200)
    else:
        res_data = {"errorMsg": "User Already Exists"}
        return HttpResponse(json.dumps(res_data),content_type="application/json",status=401)


def add_cart(request):
    email = request.POST.get("token")
    id = request.POST.get("id")
    user = User.objects.get(email=email)
    user.shoppingCard.append(id)
    user.save()
    res_data = {"resMsg": "success"}
    return HttpResponse(json.dumps(res_data), content_type="application/json", status=200)


def remove_cart(request):
    email = request.POST.get("token")
    id = request.POST.get("id")
    user = User.objects.get(email=email)
    if id in user.shoppingCard:
        user.shoppingCard.remove(id)
        user.save()
        res_data = {"resMsg": "success removed"}
        return HttpResponse(json.dumps(res_data), content_type="application/json", status=200)
    else:
        res_data = {"resMsg": "it is not in cart"}
        return HttpResponse(json.dumps(res_data), content_type="application/json", status=201)


def get_chopping_card(request):
    email = request.POST.get("token")
    print(email)
    user = User.objects.get(email=email)
    product_list = user.shoppingCard
    res_data = []
    for index in range(len(product_list)):
        product = Todo.objects.filter(id=product_list[index])
        info = {
            "id": product[0].id,
            "product_name": product[0].product_name,
            "description": product[0].description,
            "link": product[0].link,
            "image": product[0].image,
            "condition": product[0].condition,
            "prices": product[0].prices,
            "free_returns": product[0].free_returns,
        }
        res_data.append(info)
    return HttpResponse(json.dumps(res_data), content_type="application/json", status=200)


