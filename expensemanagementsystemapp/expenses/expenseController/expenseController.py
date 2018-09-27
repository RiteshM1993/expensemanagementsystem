import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime
from django.utils import timezone

from expensemanagementsystemapp.expenses.expenseService.expenseService import expense


@api_view(['POST'])
def saveEmpense(request):
    expense_name = request.data['expenseName']
    amount = request.data['expenseAmount']
    file = request.data['file']

    created_date = datetime.now(tz=timezone.utc)
    expense_obj = expense()
    result = expense_obj.addExpense(expense_name,amount,file,created_date)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def getExpenses(request):
    expense_obj = expense()

    result = expense_obj.expensesList()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['DELETE'])
def deleteExpenses(request):
    id = request.GET['id']
    expense_obj = expense()
    result = expense_obj.delExpenses(id)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getEditExpData(request):
    id = request.GET['id']

    expense_obj = expense()

    result = expense_obj.getEditExpensesData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['PUT'])
def updateExpense(request):
    id = request.data['id']
    expenseName = request.data['expenseName']
    uploadImage = request.data['uploadImage']
    empensePrice = request.data['empensePrice']
    modified_date = datetime.now(tz=timezone.utc)

    expense_obj = expense()
    result = expense_obj.updateExpensesData(id,expenseName,uploadImage,empensePrice,modified_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def expenseCount(request):
    expense_obj = expense()

    result = expense_obj.expensesTotalCount()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)