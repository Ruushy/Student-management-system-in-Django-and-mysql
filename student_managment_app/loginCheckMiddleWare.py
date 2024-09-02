from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import  HttpResponseRedirect
from django.urls import reverse , path



class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self,request,view_func,view_args,view_kwargs):
            modulename=view_func.__module__
            print(modulename)
            user=request.user
            if user.is_authenticated:
                if user.user_type == 1:
                    if modulename == "student_management_app.adminView":
                        pass
                    elif modulename == "student_management_app.views" or modulename == "django.views.static":
                        pass
                    elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                        pass
                    else:
                        return HttpResponseRedirect(reverse("admin_home"))
                elif user.user_type == 2:
                    if modulename == "student_management_app.StuffViews" or modulename == "student_management_app.EditResultVIewClass":
                        pass
                    elif modulename == "student_management_app.views" or modulename == "django.views.static":
                        pass
                    else:
                        return HttpResponseRedirect(reverse("stuff_home"))
                elif user.user_type == 3:
                    if modulename == "student_management_app.studentViews" or modulename == "django.views.static":
                        pass
                    elif modulename == "student_management_app.views":
                        pass
                    else:
                        return HttpResponseRedirect(reverse("student_home"))
                else:
                    return HttpResponseRedirect(reverse("show_login_page"))

            else:
                if request.path == reverse("show_login_page") or request.path == reverse("do_Login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("show_login_page"))
                    
                    
                    
                    
                    
                    
                    
                    
#   def process_view(self,request,view_func,view_args,view_kwargs):
#         modulename=view_func.__module__
#         user=request.user
#         if user.is_authenticated:
#             if user.user_type == "1":
#                 if modulename == "student_managment_app.adminView":
#                     pass
#                 elif modulename == "student_managment_app.view":
#                     pass
#                 else :
#                     return HttpResponseRedirect(reverse("admin_home"))
#             elif user.user_type == "2":
#                 if modulename == "student_managment_app.stuffView":
#                     pass
#                 elif modulename == "student_managment_app.view":
#                     pass
#                 else :
#                     return HttpResponseRedirect(reverse("stuff_home"))
            
#             elif user.user_type == "3":
#                 if modulename == "student_managment_app.studentView":
#                     pass
#                 elif modulename == "student_managment_app.view":
#                     pass
#                 else :
#                     return HttpResponseRedirect(reverse("student_home"))
#             else:
#                 return HttpResponseRedirect(reverse("show_login_page"))
                
                
            
            
#         else:
#             if request.path == reverse("show_login_page") or request.path == reverse("do_Login"):
#                 pass
#             else:
#                 return HttpResponseRedirect(reverse("show_login_page"))