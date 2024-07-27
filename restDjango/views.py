from django.http import HttpResponse, HttpRequest
from .models import User
import json

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