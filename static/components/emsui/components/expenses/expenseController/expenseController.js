angular.module('expensesController',[])
.controller('expensesController',['expensesService','$stateParams','$state',function(expensesService,$stateParams,$state){

    var expensesScope = this;

    expensesScope.saveExpenses = function(){


       var formdata = new FormData();

       formdata.append('expenseName', expensesScope.expenseName);
       formdata.append('expenseAmount', expensesScope.expenseAmount);
       formdata.append('file', expensesScope.expenseFile);

        var success = function(response){
            console.log(response)
            expensesScope.successmsg = true
            expensesScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            expensesScope.successmsg = false
            expensesScope.errormsg = true
        }

        expensesService.addexpenses(formdata,success,failure)
    }

    expensesScope.getDetails = function(){
        var success = function(response){
            console.log(response.data.data)
            expensesScope.details = response.data.data
           }

        var failure = function(response){
            console.log(response)

        }

        expensesService.listExpenses(success,failure)
    }

// Delete user
    expensesScope.deleteExpense = function(id, $index){

        if (confirm('Are you sure?')){
            var success = function(response){
                expensesScope.users.splice($index,1)
            }

            var failure = function(response){
                console.log(response)
                console.log('fail')
            }

            expensesService.deleteExpenses(id,success,failure)
        }

    }
//
//
//    Change State with id
    expensesScope.changeState = function(expenseId){
        $state.go('editexpenses',{
            'obj': expenseId
        })
    }

//    get user values to update
    expensesScope.getDatatoUpdate= function(){
        id = $stateParams.obj

        var success = function(response){
            console.log('success')
            expensesScope.data = response.data.data[0]
            console.log(expensesScope.data)
            expensesScope.data.upload = '/static/dist/expensedoc/'+ expensesScope.data.uploadImage

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        expensesService.geteditdata(id, success, failure)

    }

//    Update User

    expensesScope.saveUpdatedUser = function(){

        dataobj = {
            "id" : expensesScope.data.expenseId,
            "expenseName" : expensesScope.data.expenseName,
            "uploadImage" : expensesScope.data.uploadImage,
            "empensePrice" : expensesScope.data.empensePrice,
        }

        var success = function(response){
            console.log(expensesScope.data)
            expensesScope.successmsg = true
            expensesScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            expensesScope.successmsg = false
            expensesScope.errormsg = true
        }

        expensesService.updatedExpense(dataobj, success, failure)
    }



    return expensesScope;

}])


.directive('fileModel',['$parse', function($parse){
return{
    restrict: 'A',
    link: function(scope,element,attrs){
          var model=$parse(attrs.fileModel);
          var modelSetter = model.assign;

          element.bind('change', function(){
            scope.$apply(function(){
            modelSetter(scope, element[0].files[0]);
               });
          });
       }
    };
 }]);