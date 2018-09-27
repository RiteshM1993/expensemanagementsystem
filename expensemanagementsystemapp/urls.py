from django.conf.urls import url
from expensemanagementsystemapp import views
from expensemanagementsystemapp.registeruser.registerusercontroller import registerusercontroller
from expensemanagementsystemapp.login.loginController import loginController

from expensemanagementsystemapp.expenses.expenseController import expenseController

urlpatterns = [
    # First time rendering from django side
    url(r'^$', views.loginView.as_view()),

    # register user urls starts
    url(r'^api/saveuser/$', registerusercontroller.saveUser),
    url(r'^api/listusers/$', registerusercontroller.listUsers),
    url(r'^api/deleteusers/$', registerusercontroller.deleteUser),
    url(r'^api/geteditdata/$', registerusercontroller.getEditData),
    url(r'^api/updateuser/$', registerusercontroller.updateUser),
    # register user urls ends

    # Login user Starts
    url(r'^api/checkemail/$', loginController.checkEmail),
    url(r'^api/updatepassword/$', loginController.updatePassword),
    url(r'^api/login/$', loginController.loginUser),
    # Login user Ends
# session api
#     url(r'^api/checksession/$', loginController.checksession),

    # expense urls Starts
    url(r'^api/saveexpenses/$', expenseController.saveEmpense),
    url(r'^api/getexpenses/$', expenseController.getExpenses),
    url(r'^api/deleteexpenses/$', expenseController.deleteExpenses),
    url(r'^api/geteditexpensedata/$', expenseController.getEditExpData),
    url(r'^api/updateexpense/$', expenseController.updateExpense),

    #Dashboard starts
    url(r'^api/fetchexpensecount/$', expenseController.expenseCount),
    #Daashboard ends






]