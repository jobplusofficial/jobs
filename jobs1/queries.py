from jobs1.models import Job,Catagories,Courses_and_certification,Categary_label
from django.db.models import F, Q, When
import random
no_of_pages = 11
class NumberOfRecordsBy:

    def search_records(company_name1,profile1,location1,experience1,category_name,page_number):
        # exp_list = ['0-2','2-4','5+']
        # num_list = []
        # start = 0
        # end = 20
        # print(experience1)
        # if(experience1 == exp_list[0]):
        #     num_list = [0,2]
        #     start = 0
        #     end = 2
        # elif(experience1 == exp_list[1]):
        #     num_list = [2,3,4]
        #     start =2
        #     end = 4
        # elif(experience1 == exp_list[2]) :
        #     num_list = [5,20]
        #     start = 5
        #     end = 20
        # else :
        #     num_list = [0,20]

        if experience1!="Experience":
            data1=Job.objects.filter(exp_from__lte=experience1,exp_to__gte=experience1,catagories__in = Catagories.objects.values('id')
        .filter(catagory=category_name),location__icontains=location1,looking_for__contains = profile1 , company_name__icontains=company_name1)
        else:
            data1=Job.objects.filter(catagories__in = Catagories.objects.values('id')
        .filter(catagory=category_name),location__icontains=location1,profile_name__icontains = profile1 , company_name__icontains=company_name1)
        data = data1[(page_number-1)*no_of_pages:page_number*no_of_pages]
        data2 = Courses_and_certification.objects.all()
        data3=Job.objects.filter(catagories__in = Catagories.objects.values('id')
        .filter(catagory='competative_coding'))
        page_list=[]
        no_of_records=0
        no_of_records=data1.count()
        counts = int(no_of_records/no_of_pages)
        print('number of records',no_of_records)

        if (no_of_records%no_of_pages)!=0:
            counts=counts+1
        print(counts) 
        for i in range(1,counts+1):
            page_list.append(i)
        categories = Categary_label.objects.all()
        print(page_list)
        page_list_len = len(page_list)
        return {'company_name':company_name1,'jobs':data,'certs':data2,'comp_coding':data3,'page_list':page_list,
        'category_name':category_name,'location':location1,'profile':profile1,'no_of_records':no_of_records,'categories':categories,'page_number':page_number,'page_list_len':page_list_len}
    


    def jobs_by_category(category_name,page_number):
        data = Job.objects.filter(catagories__in = Catagories.objects.values('id')
        .filter(catagory=category_name)).order_by('-post_date')[(page_number-1)*no_of_pages:page_number*no_of_pages]
        data2 = Courses_and_certification.objects.all()
        data3=Job.objects.filter(catagories__in = Catagories.objects.values('id')
        .filter(catagory='competative_coding'))
        page_list=[]
        no_of_records=Job.objects.filter(catagories__in = Catagories.objects.values('id')
        .filter(catagory=category_name)).count()
        counts = int(no_of_records/no_of_pages)
        print(counts)
        if (no_of_records%no_of_pages)!=0:
            counts = counts+1
        print(counts) 
        for i in range(1,counts+1):
            page_list.append(i)
        categories = Categary_label.objects.all()
        page_list_len = len(page_list)
        params = {'jobs':data,'certs':data2,'comp_coding':data3,'page_list':page_list,'category_name':category_name,'no_of_records':no_of_records,'categories':categories,'page_number':page_number,'page_list_len':page_list_len}

        return params