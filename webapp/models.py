from django.db import models

class Course(models.Model):
    Course_id=models.IntegerField(primary_key=True)
    Course_name=models.CharField(max_length=30)
    Faculty=models.CharField(max_length=30)
    Duration=models.CharField(max_length=10)
    course_content=models.FileField(upload_to='contents')
    # def __str__(self):
        # return self.Course_name
    def __str__(self):
        return self.Course_name + ": " + str(self.course_content)
class FeedbackData(models.Model):
    name=models.CharField(max_length=30)
    rating=models.IntegerField()
    feedback=models.CharField(max_length=100)
    date=models.DateTimeField(max_length=30)

class ContactData(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    mobile=models.BigIntegerField()
    comments=models.TextField(max_length=100)
    date = models.DateTimeField(max_length=30)