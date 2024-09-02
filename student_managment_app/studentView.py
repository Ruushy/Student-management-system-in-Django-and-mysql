from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Students, CustomerUser, Courses  , Subjects, FeedBackStudent , Attendance , Stuffs , LeaveReportStudent , LeaveReportStuff , Attendance ,  FeedBackStuff , SessionYearModel , AttendanceReport , CustomerUser
from datetime import datetime
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def student_home(request):
    student_obj=Students.objects.get(admin=request.user.id)
    attendance_total=AttendanceReport.objects.filter(student_id=student_obj).count()
    attendance_present=AttendanceReport.objects.filter(student_id=student_obj,status=True).count()
    attendance_absent=AttendanceReport.objects.filter(student_id=student_obj,status=False).count()
    course=Courses.objects.get(id=student_obj.course_id.id)
    subjects=Subjects.objects.filter(course_id=course).count()
    subjects_data=Subjects.objects.filter(course_id=course)
    session_obj=SessionYearModel.objects.get(id=student_obj.session_year_id.id)
    # class_room=OnlineClassRoom.objects.filter(subject__in=subjects_data,is_active=True,session_years=session_obj)

    subject_name=[]
    data_present=[]
    data_absent=[]
    subject_data=Subjects.objects.filter(course_id=student_obj.course_id)
    for subject in subject_data:
        attendance=Attendance.objects.filter(subject_id=subject.id)
        attendance_present_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=True,student_id=student_obj.id).count()
        attendance_absent_count=AttendanceReport.objects.filter(attendance_id__in=attendance,status=False,student_id=student_obj.id).count()
        subject_name.append(subject.subject_name)
        data_present.append(attendance_present_count)
        data_absent.append(attendance_absent_count)

    return render(request,"student_template/home_content.html",{"total_attendance":attendance_total,"attendance_absent":attendance_absent,"attendance_present":attendance_present,"subjects":subjects,"data_name":subject_name,"data1":data_present,"data2":data_absent})



@csrf_exempt
def student_fcmtoken_save(request):
    token=request.POST.get("token")
    try:
        student=Students.objects.get(admin=request.user.id)
        student.fcm_token=token
        student.save()
        return HttpResponse("True")
    except:
        return HttpResponse("False")


def student_view_attendance(request):
    student=Students.objects.get(admin=request.user.id)
    course=student.course_id
    subjects=Subjects.objects.filter(course_id=course)
    return render(request,"student_template/student_view_attendance.html",{"subjects":subjects})

def student_view_attendance_post(request):
    subject_id = request.POST.get("subject")
    subject_obj = Subjects.objects.get(id=subject_id)
    user_object = CustomerUser.objects.get(id=request.user.id)
    stud_obj = Students.objects.get(admin=user_object)
    # current_session = SessionYearModel.objects.get(is_current_session=True)

    attendance = Attendance.objects.filter(subject_id=subject_obj)
    attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=stud_obj)
    
    return render(request,"student_template/student_attendance_data.html",{
        "attendance_reports":attendance_reports
    })
    
def student_apply_leave(request):
    student_objects = Students.objects.get(admin=request.user.id)
    leave_data = LeaveReportStudent.objects.filter(student_id=student_objects)
    return render(request, 'student_template/student_apply.html',{
        'leave_data':leave_data
    })
    

def student_apply_leave_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>method not Allowded</h2>")
    else:
        leave_data = request.POST.get("leave_data")
        leave_ms = request.POST.get("leave_msg")
        student_ob = Students.objects.get(admin=request.user.id)
        try:
            leave_report = LeaveReportStudent(student_id=student_ob,leave_date=leave_data,leave_message=leave_ms,leave_status=0)
            leave_report.save()
            messages.success(request, "applied successfulyy")
            return HttpResponseRedirect("/student_apply_leave")
        except:
            messages.error(request, "Failed to apply")
            return HttpResponseRedirect("/student_apply_leave")
        
def student_feedback(request):
    student_id = Students.objects.get(admin=request.user.id)
    feedback = FeedBackStudent.objects.filter(student_id=student_id)
    return render(request, 'student_template/student_feedback.html',{
        'feedback':feedback
    })
    
def student_feedback_save(request):
    if request.method != "POST":
        return HttpResponse("<h2>method not Allowded</h2>")
    else:
        feedback_data = request.POST.get("feadback_msg")
        student_ob = Students.objects.get(admin=request.user.id)
        try:
            feedback = FeedBackStudent(student_id=student_ob,feedback=feedback_data,feedback_reply="")
            feedback.save()
            messages.success(request, "feedback sent successfulyy")
            return HttpResponseRedirect("/student_feedback")
        except:
            messages.error(request, "Failed to sent feedback")
            return HttpResponseRedirect("/student_feedback")
        
def student_profile(request):
    user=CustomerUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            customuser=CustomerUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))