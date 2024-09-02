
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path , include
from student_managment_app import  views , adminView , studentView , stuffView 
from student_managment_app.EditResultVIewClass import EditResultViewClass
from . import settings


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('demo/' , views.DemoPage , name='demo page'),
    path('' , views.ShowloginPage, name='show_login_page'),
    path('doLogin' , views.doLogin, name='do_Login'),
    path('get_user_details' , views.GetUserDetails, name='get_user_details'),
    path('logout' , views.Logout_user, name='logout'),
    path('admin_home/', adminView.admin_home, name="admin_home"),
    path('add_staff/', adminView.add_staff, name="add_staff"),
    path('add_stuff_save', adminView.add_stuff_save, name="add_staff_save"),
    path('add_course/', adminView.add_course, name="add_course"),
    path('add_course_save', adminView.add_course_save, name="add_course_save"),
    path('add_student/', adminView.add_student, name="add_student"),
    path('add_student_save', adminView.add_student_save, name="add_student_save"),
    path('add_subject/', adminView.add_subject, name="add_subject"),
    path('add_subject_save', adminView.add_subject_save, name="add_subject_save"),
    path('manage_stuff/', adminView.manage_stuff, name="manage_stuff"),
    path('manage_student/', adminView.manage_student, name="manage_student"),
    path('manage_course/', adminView.manage_course, name="manage_course"),
    path('manage_subject/', adminView.manage_subject, name="manage_subject"),
    path('edit_stuff<int:stuff_id>', adminView.edit_stuff, name="edit_stuff"),
    path('edit_stuff_save', adminView.edit_stuff_save, name="edit_stuff_save"),
    path('edit_student<int:student_id>', adminView.edit_student, name="edit_student"),
    path('edit_student_save', adminView.edit_student_save, name="edit_student_save"),
    path('edit_course<int:course_id>', adminView.edit_course, name="edit_course"),
    path('edit_course_save', adminView.edit_course_save, name="edit_course_save"),
    path('edit_subject<int:subject_id>', adminView.edit_subject, name="edit_subject"),
    path('edit_subject_save', adminView.edit_subject_save, name="edit_subject_save"),
    path('manage_session', adminView.manage_session, name="manage_session"),
    path('add_session_save', adminView.add_session_save, name="add_session_save"),
    path('check_email_exist', adminView.check_email_exist,name="check_email_exist"),
    path('check_username_exist', adminView.check_username_exist,name="check_username_exist"),
    path('student_feedback_message', adminView.student_feedback_message,name="student_feedback_message"),
    path('student_feedback_message_replied', adminView.student_feedback_message_replied,name="student_feedback_message_replied"),
    path('student_leave', adminView.student_leave,name="student_leave"),
    path('student_leave_aprrove/<str:leave_id>', adminView.student_leave_aprrove,name="student_leave_aprrove"),
    path('student_disapprove_leave/<str:leave_id>', adminView.student_disapprove_leave,name="student_disapprove_leave"),
    path('stuff_feedback_message', adminView.stuff_feedback_message,name="stuff_feedback_message"),
    path('stuff_feedback_message_replied', adminView.stuff_feedback_message_replied,name="stuff_feedback_message_replied"),
    path('stuff_leave', adminView.stuff_leave,name="stuff_leave"),
    path('stuff_leave_aprrove/<str:leave_id>', adminView.stuff_leave_aprrove,name="stuff_leave_aprrove"),
    path('stuff_leave_disaprrove/<str:leave_id>', adminView.stuff_leave_disaprrove,name="stuff_leave_disaprrove"),
    path('admin_view_attendance', adminView.admin_view_attendance,name="admin_view_attendance"),
    path('admin_view_attendance_dates', adminView.admin_view_attendance_dates,name="admin_view_attendance_dates"),
    path('admin_get_attendance_student', adminView.admin_get_attendance_student,name="admin_get_attendance_student"),
    path('admin_profile/', adminView.admin_profile,name="admin_profile"),
    path('admin_profile_save', adminView.admin_profile_save,name="admin_profile_save"),
    path('admin_send_notification_student', adminView.admin_send_notification_student,name="admin_send_notification_student"),
    path('send_notification_student', adminView.send_notification_student,name="send_notification_student"),
    path('admin_send_notification_staff', adminView.admin_send_notification_staff,name="admin_send_notification_staff"),
    path('send_notification_staff', adminView.send_notification_staff,name="send_notification_staff"),
    
    
    
    
    
    
    # path('view_attendance/', view_attendance, name='view_attendance'),
    
    
    #Staff Urls
    path('stuff_home', stuffView.stuff_home, name="stuff_home"),
    path('stuff_take_attendance', stuffView.stuff_take_attendance, name="stuff_take_attendance"),
    path('get_attendance_dates', stuffView.get_attendance_dates, name="get_attendance_dates"),
    path('save_attendance_data', stuffView.save_attendance_data, name="save_attendance_data"),
    path('get_attendance_student', stuffView.get_attendance_student, name="get_attendance_student"),
    path('staff_update_attendance', stuffView.staff_update_attendance, name="staff_update_attendance"),
    path('save_updateattendance_data', stuffView.save_updateattendance_data, name="save_updateattendance_data"),
    path('stuff_apply_leave/', stuffView.stuff_apply_leave, name='stuff_apply_leave'),
    path('stuff_apply_leave_save', stuffView.stuff_apply_leave_save, name='stuff_apply_leave_save'),
    path('stuff_feedback/', stuffView.stuff_feedback, name='stuff_feedback'),
    path('stuff_feedback_save', stuffView.stuff_feedback_save, name='stuff_feedback_save'),
    path('get_students/', stuffView.get_students, name='get_students'),
    path('staff_profile/', stuffView.staff_profile,name="staff_profile"),
    path('staff_profile_save', stuffView.staff_profile_save,name="staff_profile_save"),
    path('staff_fcmtoken_save', stuffView.staff_fcmtoken_save, name="staff_fcmtoken_save"),
    path('staff_add_result', stuffView.staff_add_result, name="staff_add_result"),
    path('save_student_result', stuffView.save_student_result, name="save_student_result"),
    path('edit_student_result',EditResultViewClass.as_view(), name="edit_student_result"),
    path('fetch_result_student',stuffView.fetch_result_student, name="fetch_result_student"),
    path('fetch_result_student',stuffView.fetch_result_student, name="fetch_result_student"),
    
    
    
    
    
    
    
    #student Urls
    path('student_home', studentView.student_home, name="student_home"),
    path('student_view_attendance', studentView.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', studentView.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', studentView.student_apply_leave, name='student_apply_leave'),
    path('student_apply_leave_save', studentView.student_apply_leave_save, name='student_apply_leave_save'),
    path('student_feedback/', studentView.student_feedback, name='student_feedback'),
    path('student_feedback_save', studentView.student_feedback_save, name='student_feedback_save'),
    path('student_profile/', studentView.student_profile,name="student_profile"),
    path('student_profile_save', studentView.student_profile_save,name="student_profile_save"),
    path('student_fcmtoken_save', studentView.student_fcmtoken_save, name="student_fcmtoken_save"),
    
    
    
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
