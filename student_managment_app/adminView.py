from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from django.contrib import messages
from . models import CustomerUser , Stuffs, NotificationStuff ,  NotificationStudent, Attendance, LeaveReportStudent , LeaveReportStuff , FeedBackStudent , FeedBackStuff , Courses ,Subjects , Stuffs , Students , SessionYearModel , AttendanceReport
import datetime
import json
from django.urls import reverse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage

def admin_home(request):
    student_count1=Students.objects.all().count()
    staff_count=Stuffs.objects.all().count()
    subject_count=Subjects.objects.all().count()
    course_count=Courses.objects.all().count()

    course_all=Courses.objects.all()
    course_name_list=[]
    subject_count_list=[]
    student_count_list_in_course=[]
    for course in course_all:
        subjects=Subjects.objects.filter(course_id=course.id).count()
        students=Students.objects.filter(course_id=course.id).count()
        course_name_list.append(course.course_name)
        subject_count_list.append(subjects)
        student_count_list_in_course.append(students)

    subjects_all=Subjects.objects.all()
    subject_list=[]
    student_count_list_in_subject=[]
    for subject in subjects_all:
        course=Courses.objects.get(id=subject.course_id.id)
        student_count=Students.objects.filter(course_id=course.id).count()
        subject_list.append(subject.subject_name)
        student_count_list_in_subject.append(student_count)

    staffs=Stuffs.objects.all()
    attendance_present_list_staff=[]
    attendance_absent_list_staff=[]
    staff_name_list=[]
    for staff in staffs:
        subject_ids=Subjects.objects.filter(staff_id=staff.admin.id)
        attendance=Attendance.objects.filter(subject_id__in=subject_ids).count()
        leaves=LeaveReportStuff.objects.filter(stuff_id=staff.id,leave_status=1).count()
        attendance_present_list_staff.append(attendance)
        attendance_absent_list_staff.append(leaves)
        staff_name_list.append(staff.admin.username)

    students_all=Students.objects.all()
    attendance_present_list_student=[]
    attendance_absent_list_student=[]
    student_name_list=[]
    for student in students_all:
        attendance=AttendanceReport.objects.filter(student_id=student.id,status=True).count()
        absent=AttendanceReport.objects.filter(student_id=student.id,status=False).count()
        leaves=LeaveReportStudent.objects.filter(student_id=student.id,leave_status=1).count()
        attendance_present_list_student.append(attendance)
        attendance_absent_list_student.append(leaves+absent)
        student_name_list.append(student.admin.username)


    return render(request,"hod_template/home_content.html",{"student_count":student_count1,"staff_count":staff_count,"subject_count":subject_count,"course_count":course_count,"course_name_list":course_name_list,"subject_count_list":subject_count_list,"student_count_list_in_course":student_count_list_in_course,"student_count_list_in_subject":student_count_list_in_subject,"subject_list":subject_list,"staff_name_list":staff_name_list,"attendance_present_list_staff":attendance_present_list_staff,"attendance_absent_list_staff":attendance_absent_list_staff,"student_name_list":student_name_list,"attendance_present_list_student":attendance_present_list_student,"attendance_absent_list_student":attendance_absent_list_student})


def add_staff(request):
    return render(request, "hod_template/add_staff.html")

def add_stuff_save(request):
   
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("Address")
        try:
            user =CustomerUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.Stuffs.address=address
            user.save()
            messages.success(request, "Added successfulyy")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/add_staff")



def add_course(request):
    return render(request, "hod_template/add_course.html")


def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Added successfulyy")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/add_course")
             
def add_student(request):
    courses = Courses.objects.all()
    session = SessionYearModel.objects.all()
    
    return render(request, "hod_template/add_student.html",{
        "course":courses , 
        'session':session
    })          

def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("Address")
        session_id = request.POST.get("session")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        profile_pic = request.FILES['prodile_pic']
        fs=FileSystemStorage()
        filename=fs.save(profile_pic.name,profile_pic)
        profile_pic_url = fs.url(filename)
        
        try:
            user =CustomerUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type = 3)
            user.students.address=address
            course_ob=Courses.objects.get(id=course_id)
            user.students.course_id_id=course_ob
            user.students.session_year_idr=session_id
            user.students.gender = gender
            user.students.prodile_pic=profile_pic_url
                
            user.save()
            messages.success(request, "Added successfulyy")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/add_student")

def add_subject(request):
    courses = Courses.objects.all()
    stuffs = CustomerUser.objects.filter(user_type=2)
    return render(request, "hod_template/add_subject.html",{
        "course":courses,
        "stuff":stuffs
    })     
    
def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        subject_name = request.POST.get("subject")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        stuff_id = request.POST.get("stuff")
        stuff= CustomerUser.objects.get(id=stuff_id)
        
        try:
            subject=Subjects(subject_name=subject_name,course_id=course, staff_id=stuff)
            subject.save()
            messages.success(request, "Added successfulyy")
            return HttpResponseRedirect("/add_subject")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/add_subject")
        
def manage_stuff(request):
    stuff = Stuffs.objects.all()
    return render(request, "hod_template/manage_stuff.html",{
        'stuff':stuff
    })
    
def manage_student(request):
    student = Students.objects.all()
    session = SessionYearModel.objects.all()
    
    return render(request, "hod_template/manage_student.html",{
        'student':student,
        'session':session
    })
    
def manage_course(request):
    course = Courses.objects.all()
    session = SessionYearModel.objects.all()
    return render(request, "hod_template/manage_course.html",{
        'course':course,
        'session':session
    })
    
def manage_subject(request):
    subject = Subjects.objects.all()
    return render(request, "hod_template/manage_subject.html",{
        'subject':subject
    })
    
def edit_stuff(request,stuff_id):
    stuff = Stuffs.objects.get(admin=stuff_id)
    return render(request, "hod_template/edit_staff.html",{
        'stuff':stuff
    })
    
def edit_stuff_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        stuff_id = request.POST.get("stuff_id")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        
        user = CustomerUser.objects.get(id=stuff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        try:
            user.save()
            messages.success(request, "edited successfulyy")
            return HttpResponseRedirect("/manage_stuff")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("manage_stufff")
        
def edit_student(request,student_id):
    courses = Courses.objects.all()
    student = Students.objects.get(admin=student_id)
    session = SessionYearModel.objects.all()
    
    return render(request, "hod_template/edit_student.html",{
        'student':student,
        'course':courses,
        'session':session
    })
    
def edit_student_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("Address")
        session_id = request.POST.get("session")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        if request.FILES.get('prodile_pic',False):
            profile_pic = request.FILES['prodile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None
        
        try:
            user =CustomerUser.objects.get(id=student_id)
            user.first_name =first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            
            student = Students.objects.get(admin=student_id)
            student.address =address
            student.gender = gender
            if profile_pic_url != None:
                student.prodile_pic=profile_pic_url
            session = SessionYearModel.objects.get(id=session_id)
            student.session_year_id=session
        
            
            course = Courses.objects.get(id=course_id)
            student.course_id=course
            student.save()

            messages.success(request, "edited successfulyy")
            return HttpResponseRedirect("/manage_student")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/manage_student")
        
def edit_course(request,course_id):
    course = Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course.html",{
        'course':course})
    
def edit_course_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get("course_name")
        
        try:
            course = Courses.objects.get(id=course_id)
            course.course_name=course_name
            course.save()
            messages.success(request, "edited successfulyy")
            return HttpResponseRedirect("/manage_course")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/manage_course")
        
def edit_subject(request,subject_id):
    courses = Courses.objects.all()
    stuffs = CustomerUser.objects.filter(user_type=2)
    subject= Subjects.objects.get(id=subject_id)
    return render(request,"hod_template/edit_subject.html",{
        'subject':subject,
        "course":courses,
        "stuff":stuffs
        })
    
def edit_subject_save(request):
    if request.method != "POST":
        return HttpResponse("method not allowed")
    else:
        subject_id = request.POST.get("subject_id")
        subject_name = request.POST.get("subject")
        staff_id = request.POST.get("stuff")
        course_id = request.POST.get("course")
        
        try:
            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name=subject_name
            stuff = CustomerUser.objects.get(id=staff_id)
            subject.staff_id = stuff
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            subject.save()
            messages.success(request, "edited successfulyy")
            return HttpResponseRedirect("/manage_subject")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/manage_subject")


def manage_session(request):
    return render(request, "hod_template/manage_session.html")


def add_session_save(request):
    if request.method != "POST":
            return HttpResponseRedirect("/manage_session")
    else:
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        
        try:
            session = SessionYearModel(session_start_year=session_start, session_end_year = session_end)
            session.save()
            messages.success(request, "added successfulyy")
            return HttpResponseRedirect("/manage_session")
        except:
            messages.error(request, "Failed to add")
            return HttpResponseRedirect("/manage_session")

@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=CustomerUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)



  
@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=CustomerUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def student_feedback_message(request):
    feedbacks = FeedBackStudent.objects.all()
    return render(request, "hod_template/student_feedback.html",{
        'feedback':feedbacks
    })
@csrf_exempt
def student_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStudent.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
    
def student_leave(request):
    leave = LeaveReportStudent.objects.all()
    return render(request, "hod_template/student_leave.html",{
        'leave':leave
    })
def student_leave_aprrove(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("student_leave"))

def student_disapprove_leave(request,leave_id):
    leave=LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("student_leave"))

def stuff_feedback_message(request):
    feedbacks = FeedBackStuff.objects.all()
    return render(request, "hod_template/staff_feedback.html",{
        'feedback':feedbacks
    })

@csrf_exempt
def stuff_feedback_message_replied(request):
    feedback_id=request.POST.get("id")
    feedback_message=request.POST.get("message")

    try:
        feedback=FeedBackStuff.objects.get(id=feedback_id)
        feedback.feedback_reply=feedback_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
    
def stuff_leave(request):
    leave = LeaveReportStuff.objects.all()
    return render(request, "hod_template/staff_leave.html",{
        'leave':leave
    })
def stuff_leave_aprrove(request , leave_id):
    leave=LeaveReportStuff.objects.get(id=leave_id)
    leave.leave_status=1
    leave.save()
    return HttpResponseRedirect(reverse("stuff_leave"))

def stuff_leave_disaprrove(request , leave_id):
    leave=LeaveReportStuff.objects.get(id=leave_id)
    leave.leave_status=2
    leave.save()
    return HttpResponseRedirect(reverse("stuff_leave"))

def admin_view_attendance(request):
    subjects=Subjects.objects.all()
    session_year_id=SessionYearModel.objects.all()
    return render(request,"hod_template/admin_view_attendance.html",{
        "subjects":subjects,
        "session_year_id":session_year_id
        })
    
@csrf_exempt
def admin_view_attendance_dates(request):
    subject=request.POST.get("subject")
    session_year_id=request.POST.get("session_year_id")
    subject_obj=Subjects.objects.get(id=subject)
    session_year_obj=SessionYearModel.objects.get(id=session_year_id)
    attendance=Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date),"session_year_id":attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj), safe=False)

    
@csrf_exempt   
def admin_get_attendance_student(request):
    attendance_date=request.POST.get("attendance_date")
    attendance=Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    list_data=[]

    for student in attendance_data:
        data_small={"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

def admin_profile(request):
    user=CustomerUser.objects.get(id=request.user.id)
    return render(request,"hod_template/admin_profile.html",{
        "user":user
        })

def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customer_user = CustomerUser.objects.get(id=request.user.id)
            customer_user.first_name = first_name
            customer_user.last_name = last_name
            # if password!=None and password!="":
            #     customer_user.set_password(password)
            customer_user.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("/"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("admin_profile"))
        
def admin_send_notification_student(request):
    students=Students.objects.all()
    return render(request,"hod_template/student_notification.html",{"students":students})

def send_notification_student(request):
    student_id=request.POST.get("id")
    student_message=request.POST.get("message")

    try:
        notifaction_message=NotificationStudent.objects.get(student_id=student_id)
        notifaction_message.message=student_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")
    
def admin_send_notification_staff(request):
    staff=Stuffs.objects.all()
    return render(request,"hod_template/admin_notification.html",{"staff":staff})

def send_notification_staff(request):
    staff_id=request.POST.get("id")
    staff_message=request.POST.get("message")

    try:
        notifaction_message=NotificationStuff.objects.get(stuff_id=staff_id)
        notifaction_message.message=staff_message
        feedback.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")