from django.http import HttpResponse, HttpRequest
from .models import User
import json
from django.shortcuts import get_object_or_404

def users(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        users = User.objects.all()
        serialized_users = [user.name for user in users]
        return HttpResponse(json.dumps(serialized_users))

    if request.method == 'POST':
        body = json.loads(request.body)
        user = User(name=body['name'], email=body['email'], age=body['age'])
        # comment
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

def update_or_delete_user(request: HttpRequest, id: int) -> HttpResponse:

    if request.method == 'GET':
        user = get_object_or_404(User, id= id)
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

    if request.method == 'PUT':
        body = json.loads(request.body)
        user = User.objects.get(id=id)
        user.name = body['name']
        user.email = body['email']
        user.age = body['age']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email, 'age': user.age}))

    if request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponse(json.dumps({'id': id, 'deleted': True}))