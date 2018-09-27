from expensemanagementsystemapp.models import registeruser

class emsUser:
    @classmethod
    def saveUsers(self, username, email, password, createdDate):
        try:
            saveqry = registeruser(user_name=username,user_email =email,created_date=createdDate,user_password =password)

            saveqry.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    @classmethod
    def ezeDocsUserCount(cls):
        try:
            countuserqry = registeruser.objects.count()
            countpdfqry = uploadpdf.objects.count()
            dataobj = {
                'userCount': countuserqry,
                'pdfCount' : countpdfqry,
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return {'failureobj': saveqryfailureobj}

    @classmethod
    def ezeDocsUserList(cls):
        try:
            getqry = registeruser.objects.all()

            datalist = []

            for values in getqry:
                datalist.append({
                    'userId': values.user_id,
                    'userName': values.user_name,
                    'userEmail': values.user_email,
                })

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return {'failureobj': saveqryfailureobj}


    @classmethod
    def ezeDocsUserDelete(cls, id):
        try:
            delqry = registeruser.objects.get(user_id=id)

            delqry.delete()

            datatobj={
                'data': 'success',
            }

            return datatobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

    @classmethod
    def getEditUserData(cls, id):
        try:
            getuserqry = registeruser.objects.get(user_id=id)

            datalist = [{
                'userId': getuserqry.user_id,
                'userName': getuserqry.user_name,
                'userEmail': getuserqry.user_email,
            }]

            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

    @classmethod
    def updateUserData(cls, id, username, email, modifiedDate):
        try:
            getuserdata = registeruser.objects.get(user_id=id)

            getuserdata.user_name = username
            getuserdata.user_email = email
            getuserdata.modified_date = modifiedDate

            getuserdata.save()

            dataobj = {
                'data' : 'success',
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }

            return saveqryfailureobj

