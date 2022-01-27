from django.shortcuts import redirect, HttpResponse

# def example_middleware(get_response):
#     # This code will execute after run server
#     print("The server is start right now.")
#     print("The middleware initial vaules will goes here..")
#
#     def inner_function(request):
#         # This code will execute before the view is execute
#         print("Code before the view is executed..")
#         response = get_response(request)
#         # This code will execute after the view is execute
#         print("Code after the view is executed..")
#         return response
#
#     return inner_function



# # This middleware will check the url path and ridirect the user to the right view
# def url_validator_middleware(get_response):
#
#     def url_validator_function(request):
#         # Code before the view
#         user_input_path = request.path
#         if user_input_path in ['/home/', '/home']:
#             return redirect('home')
#         response = get_response(request)
#         # Code after the view
#         print("Code after the view executed..")
#
#         return response
#
#     return url_validator_function


# # When middleware return None value then the next middleware and views will executed
# # If the middleware return Httpresponse then next middleware will not be executed
# def return_None_middleware(get_response):
#
#     def return_value_function(request):
#         # Code before the view
#         print("Code before the view")
#         return HttpResponse('<h1>The Middleware Page</h1>')
#         response = get_response(request)
#         # Code after the view
#         print("Code after the view")
#
#         return response
#
#     return return_value_function

