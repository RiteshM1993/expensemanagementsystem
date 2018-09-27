angular.module('expensesService',[])
.service('expensesService',['$http',function($http){
     var expenses = {};

     expenses.addexpenses = function(formdata,success,failure){
        $http({
            method:'POST',
            url:'api/saveexpenses/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)
     }

     expenses.listExpenses = function(success,failure){
        $http.get('api/getexpenses/').then(success,failure)
     }

     expenses.deleteExpenses = function(id,success,failure){
        $http.delete('api/deleteexpenses/?id='+id).then(success,failure)
     }

     expenses.geteditdata = function(id, success, failure){
        $http.get('api/geteditexpensedata/?id='+id).then(success,failure)
     }

     expenses.updatedExpense = function(dataobj, success, failure){
        $http.put('api/updateexpense/',{
            'id' : dataobj.id,
            "expenseName" : dataobj.expenseName,
            "uploadImage" : dataobj.uploadImage,
            "empensePrice" : dataobj.empensePrice,
        }).then(success,failure)
     }

     return expenses;

}])