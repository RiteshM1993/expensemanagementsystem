import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from expensemanagementsystemapp.login.loginService.loginService import emsLogin
import time


@api_view(['GET'])
def checkEmail(request):
    email=request.GET['email']

    emslogin_obj = emsLogin()

    result = emslogin_obj.checkRegisteredEmail(email)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['PUT'])
def updatePassword(request):
    id = request.data['id']
    newpass = request.data['newpass']
    emslogin_obj = emsLogin()

    result = emslogin_obj.updateuserPassword(id,newpass)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['POST'])
def loginUser(request):
    email = request.data['email']
    passcode = request.data['password']

    emslogin_obj = emsLogin()

    result = emslogin_obj.login(email,passcode)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

