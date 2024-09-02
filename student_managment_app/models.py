from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class CustomerUser(AbstractUser):
   user_type_data=((1,"HOD"),(2,"Staff"),(3,"Student"))
   user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

   
class SessionYearModel(models.Model):
   id=models.AutoField(primary_key=True)
   session_start_year = models.DateField()
   session_end_year = models.DateField()

class AdminHOD(models.Model):
   id = models.AutoField(primary_key=True)
   admin = models.OneToOneField(CustomerUser, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   

class Stuffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomerUser, on_delete=models.CASCADE) 
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fcm_token = models.TextField(default="")
    objects=models.Manager()   


class Courses(models.Model):
   id = models.AutoField(primary_key=True)
   course_name = models.CharField(max_length=50)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()

class Subjects(models.Model):
   id = models.AutoField(primary_key=True)
   subject_name = models.CharField(max_length=50)
   course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
   staff_id = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   

   
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomerUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    prodile_pic=models.FileField()
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    address = models.TextField()
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    fcm_token = models.TextField(default="")
    objects=models.Manager()
    
    
class Attendance(models.Model):
   id = models.AutoField(primary_key=True)
   subject_id = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
   session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
   attendance_date=models.DateField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
    

class AttendanceReport(models.Model):
   id = models.AutoField(primary_key=True)
   student_id = models.ForeignKey( Students, on_delete=models.DO_NOTHING)
   attendance_id = models.ForeignKey( Attendance, on_delete=models.CASCADE)
   status = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   

   
class LeaveReportStudent(models.Model):
   id = models.AutoField(primary_key=True)
   student_id = models.ForeignKey( Students, on_delete=models.CASCADE)
   leave_date = models.CharField(max_length=50)
   leave_message = models.TextField()
   leave_status = models.IntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   
class LeaveReportStuff(models.Model):
   id = models.AutoField(primary_key=True)
   stuff_id = models.ForeignKey( Stuffs, on_delete=models.CASCADE)
   leave_date = models.CharField(max_length=50)
   leave_message = models.TextField()
   leave_status = models.IntegerField(default=0)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   
class FeedBackStudent(models.Model):
   id = models.AutoField(primary_key=True)
   student_id = models.ForeignKey( Students, on_delete=models.CASCADE)
   feedback= models.TextField()
   feedback_reply = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   
class FeedBackStuff(models.Model):
   id = models.AutoField(primary_key=True)
   stuff_id = models.ForeignKey( Stuffs, on_delete=models.CASCADE)
   feedback= models.TextField()
   feedback_reply = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   
   
class NotificationStudent(models.Model):
   id = models.AutoField(primary_key=True)
   student_id = models.ForeignKey( Students, on_delete=models.CASCADE)
   message= models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()


class NotificationStuff(models.Model):
   id = models.AutoField(primary_key=True)
   stuff_id = models.ForeignKey( Stuffs, on_delete=models.CASCADE)
   message= models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now_add=True)
   objects=models.Manager()
   
class StudentResult(models.Model): 
   id=models.AutoField(primary_key=True)
   student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
   subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
   subject_exam_marks=models.FloatField(default=0)
   subject_assignment_marks=models.FloatField(default=0)
   created_at=models.DateField(auto_now_add=True)
   updated_at=models.DateField(auto_now_add=True)
   objects=models.Manager()
   
@receiver(post_save, sender=CustomerUser)
def create_user_profile(sender,instance,created,**kwargs):
   if created:
      if instance.user_type==1:
         AdminHOD.objects.create(admin=instance)
      if instance.user_type==2:
         Stuffs.objects.create(admin=instance,address="")
      if instance.user_type==3:
         Students.objects.create(admin=instance,course_id=Courses.objects.get(id=1),session_year_id=SessionYearModel.objects.get(id=1) ,address="",prodile_pic="",gender="")
       
@receiver(post_save, sender=CustomerUser)
def save_user_profile(sender,instance,**kwargs):
   if instance.user_type==1:
      instance.adminhod.save()
   if instance.user_type==2:
      instance.stuffs.save()
   if instance.user_type==3:
      instance.students.save()
      
    
