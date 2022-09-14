
from django.urls import path
from . import views
from .views import (ListStudents)


urlpatterns = [
  
  	path('',views.home,name="home"),
	path('add_student',views.add_student,name="add-student"),
	path('<int:pk>', views.detailstudent, name='student-detail'),
	path('delete_student/<int:pk>',views.delete_student,name="delete-student"),
	path('update_student/<int:pk>',views.update_student,name="update-student"),
	path('update_student_store/<int:pk>',views.update_student_store,name="update-student-store"),
	path('students/',ListStudents.as_view(),name="student-list"),
	path('students/form',views.form,name="form")
  	
  
  	
]

