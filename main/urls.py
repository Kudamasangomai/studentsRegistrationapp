from django.urls import path
from . import views
from .views import (ListStudents,home)


urlpatterns = [
  
  	path('',views.home,name="home"),
	#path('',home.as_view(),name="home"),

	#htmx urls
	path('add_student',views.add_student,name="add-student"),
	path('<int:pk>', views.detailstudent, name='student-detail'),
	path('delete_student/<int:pk>',views.delete_student,name="delete-student"),
	path('update_student/<int:pk>',views.update_student,name="update-student"),
	path('update_student_store/<int:pk>',views.update_student_store,name="update-student-store"),
	path('students/',ListStudents.as_view(),name="student-list"),
	path('students/form',views.form,name="form"),
	path('students/searchedstudent',views.searched_student,name="search-student"),
	path('students/vote/<int:pk>',views.vote,name="vote"),
	path('students/downvote/<int:pk>',views.downvote,name="downvote"),
	
  	
  
  	
]

