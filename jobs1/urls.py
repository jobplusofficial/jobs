from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Jsihome"),
    path('index/<str:category_name>/<int:page_number>', views.index1, name="Jsihome1"),
    path('about_us/', views.about_us, name="AboutUs"),
    path('contact_us/', views.contact_us, name="ContactUs"),
    path('details_page/', views.details_page, name="Details_Page"),
    path('detailed/<str:post_type>/<str:job_id>', views.detailed1, name="DetailedPage1"),
    path('detailed/<str:post_type>/<int:job_id>', views.detailed1, name="DetailedPage1"),
    path('contact1/<str:category_name>/<int:page_number>', views.get_name),
    path('base2/', views.base2),

]
