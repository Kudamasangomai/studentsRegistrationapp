from .models import students,votes
from django import forms



class studentform(forms.ModelForm):

    student_lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(
        attrs={'class':'form-control' , 
               'autocomplete': 'off',
               'number':'false',
               'pattern':'[A-Za-z]',
               'title':'Enter Characters Only'}),
               min_length=3,    
              
               
               )

    student_firstname= forms.CharField(
	widget=forms.TextInput(attrs={'placeholder': 'Your Name Here'}),
	min_length=3,
	required=True
    )
 
    
    class Meta:
        model = students
        fields = '__all__'
        exclude = ['student_regnumber','date_created']


      

class votesform(forms.ModelForm):
    class  Meta:
        model = votes
        fields = '__all__'
    
