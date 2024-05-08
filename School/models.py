from django.db import models


#model for school data

class School(models.Model):
    school_id = models.BigIntegerField(primary_key=True)
    school_name = models.CharField(max_length=100)
    school_phone = models.CharField(max_length=15)
    school_address = models.CharField(max_length=255)
    school_contact = models.CharField(max_length=100)
    school_contact_person = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.school_name



#model for management data
class SchoolManagement(models.Model):
    schoolMgtID = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)


    def __str__(self):
        return self.name

#defining relationship between School and SchoolManagement
class SchoolManagementSchools(models.Model):
    schoolmgtschoolID = models.BigIntegerField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    schoolmanagement = models.ForeignKey(SchoolManagement, on_delete=models.CASCADE)