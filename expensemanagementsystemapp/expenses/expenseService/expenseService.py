from expensemanagementsystemapp.models import expenses

from django.core.files.storage import FileSystemStorage


class expense:
    @classmethod
    def addExpense(cls, expense_name,amount,file,created_date):
        try:
            saveqry = expenses(expense_name=expense_name, total_price=amount, upload_image=file.name,
                                    created_date=created_date)
            saveqry.save()

            fs = FileSystemStorage("static/dist/expensedoc/")

            fs.save(file.name, file)

            successobj = {'data': 'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj
    @classmethod
    def expensesList(cls):
        try:
            listqry = expenses.objects.all()
            datalist = []
            for values in listqry:
                datalist.append({
                    'expenseId' :values.expense_id,
                    'expenseName': values.expense_name,
                    'empensePrice': values.total_price,
                    'uploadImage': values.upload_image,
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def delExpenses(self, id):
        try:
            delqry = expenses.objects.get(expense_id=id)
            delqry.delete()
            successobj = {
                'response': "success"
            }
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj


    @classmethod
    def getEditExpensesData(cls, id):
        try:
            getuserqry = expenses.objects.get(expense_id=id)

            datalist = [{
                'expenseId' :getuserqry.expense_id,
                'expenseName': getuserqry.expense_name,
                'empensePrice': getuserqry.total_price,
                'uploadImage': getuserqry.upload_image,
            }]

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

    def updateExpensesData(cls, id,expenseName,uploadImage,empensePrice,modified_date):
        try:
            getqry = expenses.objects.get(expense_id=id)
            getqry.expense_name = expenseName
            getqry.total_price = empensePrice

            if uploadImage != getqry.upload_image:
                getqry.upload_image=uploadImage

                fs = FileSystemStorage("static/dist/expensedoc/")

                fs.save(uploadImage.name, uploadImage)

            getqry.modified_date = modified_date
            getqry.save()

            saveqryobj = {
                'response': "success"
            }
            return saveqryobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def expensesTotalCount(cls):
        try:
            countexpensesqry = expenses.objects.count()
            dataobj = {
                'expenseCount': countexpensesqry,
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return {'failureobj': saveqryfailureobj}