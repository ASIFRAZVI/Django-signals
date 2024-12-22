from django.db.models.signals import pre_save, pre_delete, post_delete, post_save
from django.dispatch import Signal
from django.dispatch import receiver
from .models import StudentMaster , ProfileMaster
import uuid

# Custom signals
# student_updated = Signal()
# student_deleted = Signal()

# Signal to create a profile after a student is created
@receiver(post_save, sender= StudentMaster)
def save_profile(sender, instance, created, **kwargs):
    if created:
        ProfileMaster.objects.create(student_rel=instance)
        
# # pre seving the profile obj
@receiver(pre_save, sender=StudentMaster)
def update_student(sender, instance, **kwargs):
    if not instance.code:
        instance.code= uuid.uuid4()
    # no need of calling the instance.save
    
@receiver(post_delete, sender=ProfileMaster)
def delete_student(sender, instance, **kwargs):
    # Get the related StudentMaster instance
    student_instance = instance.student_rel
    # Delete the StudentMaster instance
    student_instance.delete()
    
@receiver(pre_delete, sender=StudentMaster)  
def pre_del_student(sender, instance, **kwargs):
    print("pre delete student ****************************")
    
# @receiver(student_updated)
# def update_student(sender, **kwargs):
#     student = kwargs.get('student')
#     print(f"Student updated: {student.name} *-*-*-/*-/-")
    

# @receiver(student_deleted)
# def notify_student_deleted(sender, **kwargs):
#     student = kwargs.get('student')
#     print(f"Student deleted: {student.name} //***********")   


