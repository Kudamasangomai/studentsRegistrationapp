from .models import students
from django import forms



class studentform(forms.ModelForm):
    
    class Meta:
        model = students
        fields = '__all__'
        exclude = ['student_regnumber','date_created']

    
        