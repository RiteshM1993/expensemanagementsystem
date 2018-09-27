angular.module('emsApp',[
    'ui.router',
    'smart-table',
    'ngMaterial',
    'emsApp.registerUser',
    'emsApp.userlogin',
    'emsApp.dashboard',
    'emsApp.expense',


])

.config(['$stateProvider','$urlRouterProvider', function($stateProvider, $urlRouterProvider){


    $urlRouterProvider.otherwise('/login');


    $stateProvider
    .state('login',{
        url: '/login',
        templateUrl: '/static/components/emsui/components/login/views/login.html',
        controller: 'loginUserController',
        controllerAs: 'userLoginScope',
    })

     .state('forgotpassword',{
        url: '/forgotpassword',
        templateUrl: '/static/components/emsui/components/login/views/forgotpassword.html',
        controller: 'loginUserController',
        controllerAs: 'userLoginScope',
    })

    .state('registeruser',{
        url: '/registeruser',
        templateUrl: '/static/components/emsui/components/registeruser/views/registeruser.html',
        controller: 'userRegisterController',
        controllerAs: 'registerUserScope',
    })

            //listing registed users

//    .state('listusers',{
//        url:'/listusers',
//        templateUrl:'/static/components/emsui/components/registeruser/views/listusers.html',
//        controller: 'userRegisterController',
//        controllerAs: 'registerUserScope',
//    })

    .state('editusers',{
        url:'/editusers/:obj',
        templateUrl:'/static/components/emsui/components/registeruser/views/edituser.html',
        controller: 'userRegisterController',
        controllerAs: 'registerUserScope',
    })

//    Dashboard
    .state('dashboard',{
        url: '/dashboard',
        templateUrl: '/static/components/emsui/components/dashboard/views/dashboard.html',
        controller: 'dashboardController',
        controllerAs: 'dashboardScope',
    })


//    Dashboard
    .state('listexpenses',{
        url: '/listexpenses',
        templateUrl: '/static/components/emsui/components/expenses/views/listexpenses.html',
        controller: 'expensesController',
        controllerAs: 'expensesScope',
    })


    .state('addexpenses',{
        url: '/addexpenses',
        templateUrl: '/static/components/emsui/components/expenses/views/addexpenses.html',
        controller: 'expensesController',
        controllerAs: 'expensesScope',
    })

    .state('editexpenses',{
        url:'/editexpenses/:obj',
        templateUrl:'/static/components/emsui/components/expenses/views/editexpenses.html',
        controller: 'expensesController',
        controllerAs: 'expensesScope',
    })



}])

