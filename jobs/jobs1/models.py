from django.db import models

class Job(models.Model):
    id = models.CharField(max_length=100,primary_key=True) 
    choices1 = [("Maharashtra","Maharashtra"),("Telangana","Telangana"),("Tamilnadu","Tamilnadu"),("karnataka","karnataka")]
    company_name = models.CharField(max_length=100)
    looking_for = models.CharField(max_length=1500)
    profile_name = models.CharField(max_length=200)
    description = models.CharField(max_length=50000)
    location = models.CharField(max_length=200)
    exp_from = models.IntegerField()
    exp_to = models.IntegerField()
    post_date = models.DateField()
    last_date = models.DateField()
    apply_link = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name +" job_id: "+ str(self.id)

class Categary_label(models.Model):
    id = models.IntegerField(primary_key=True)
    choice_id = models.CharField(max_length=100)
    choice_name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.id)+"-"+self.choice_id+"-"+self.choice_name
    
class Catagories(models.Model):
    # choice = [ ("all_jobs" ,"All Jobs"),
    #     ("private_tech_jobs" ,"Private Tech Jobs"),
    #     ("private_non_tech_jobs" ,"Private Non Tech Jobs"),
    #     ("part_time_jobs" ,"Part Time Jobs"),
    #     ("govt_tech_jobs" ,"Govt. Tech Jobs"),
    #     ("govt_non_tech_jobs" ,"Govt. Non Tech Jobs"),
    #     ("internships" ,"Internships"),
    #     ("competative_coding" ,"Competative Coding"),
    #     ("free_courses" ,"Free Courses"),
    #     ("certifications" ,"Certifications")
        
    # ]
    choice = [(val.choice_id,val.choice_name) for val in Categary_label.objects.all()]
    id = models.CharField(max_length=100,primary_key=True)
    job_id = models.ForeignKey(Job,on_delete= models.CASCADE)
    catagory = models.CharField(max_length=100,choices=choice,default=1)
    
    def __str__(self):
        return " catagory: "+ self.catagory + "cat_id: "+str(self.id)

    class Meta:
       unique_together = ("job_id", "catagory")

class Courses_and_certification(models.Model):
    certification_name = models.CharField(max_length=200)
    organised_by = models.CharField(max_length=200)
    description = models.CharField(max_length=50000)
    post_date = models.DateField()
    last_date = models.DateField()
    apply_link = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.certification_name

class Visitors(models.Model):
    date = models.DateField()
    mac_address = models.CharField(max_length=200,default='1')
    index_page = models.IntegerField(default=0)
    detail_page = models.IntegerField(default=0)
    contact_us = models.IntegerField(default=0)
    about_us = models.IntegerField(default=0)
    def __str__(self):
        return str(self.date)+" "+" index: " + str(self.index_page) +" details: "+str(self.detail_page)