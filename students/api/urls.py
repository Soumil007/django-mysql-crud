from django.urls import path
from students.api.views import api_all,api_all_student_record,api_create_student_record,api_update_student_record,api_delete_student_record

app_name = "students"

urlpatterns = [
    path('all/',api_all,name='all'),
    path('<int:student_id>/',api_all_student_record,name='singular'),
    path('create/',api_create_student_record,name='create'),
    path('update/<int:student_id>/',api_update_student_record,name='update'),
    path('delete/<int:student_id>/',api_delete_student_record,name='delete')
]