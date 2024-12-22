from django.db import models
import uuid


class StudentMaster(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, blank=False, null=False)
    name= models.CharField(max_length=200)
    email = models.EmailField()
    code= models.UUIDField(null=True, blank=True)


class ProfileMaster(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, blank=False, null=False)
    student_rel = models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)