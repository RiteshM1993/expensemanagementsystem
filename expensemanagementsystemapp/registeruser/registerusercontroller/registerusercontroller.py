import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from expensemanagementsystemapp.registeruser.registeruserservice.registeruserservice import emsUser
from django.utils import timezone
from datetime import datetime


@api_view(['POST'])
def saveUser(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    createdDate = datetime.now(tz=timezone.utc)

    emsuser_obj = emsUser()

    result = emsuser_obj.saveUsers(username,email,password,createdDate)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def userCount(request):
    emsuser_obj = emsUser()

    result = emsuser_obj.ezeDocsUserCount()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listUsers(request):
    emsuser_obj = emsUser()

    result = emsuser_obj.ezeDocsUserList()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['DELETE'])
def deleteUser(request):
    id = request.GET['id']

    emsuser_obj = emsUser()

    result = emsuser_obj.ezeDocsUserDelete(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getEditData(request):
    id = request.GET['id']

    emsuser_obj = emsUser()

    result = emsuser_obj.getEditUserData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['PUT'])
def updateUser(request):
    id = request.data['id']
    email = request.data['email']
    username = request.data['username']
    modifiedDate = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    emsuser_obj = emsUser()

    result = emsuser_obj.updateUserData(id, username, email, modifiedDate)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)