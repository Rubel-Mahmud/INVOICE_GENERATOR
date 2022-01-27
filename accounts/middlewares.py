from django.shortcuts import HttpResponse


# This middleware will check the authenticated users
def authenticated_user_detector_middleware(get_response):
    print("Server is running")
    def authenticated_user_detector_function(request):
        # Code before the view
        print("Code before the view")
        print("Requested user : ",request.user)
        print("Login Status : ", request.user.is_authenticated)
        if not request.user.is_authenticated:
            return HttpResponse('<br><h2 style="padding-left:40px;">Please deactivate the middleware first and then "Login"</h2>')

        response = get_response(request)
        # Code after the view
        print('Code after view')
        print("Login Status : ", request.user.is_authenticated)

        return response

    return authenticated_user_detector_function
