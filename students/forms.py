from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','course','marks','age','photo']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control w-75 mx-auto'}),
            'course':forms.TextInput(attrs={'class':'form-control w-75 mx-auto'}),
            'marks':forms.NumberInput(attrs={'class':'form-control w-75 mx-auto'}),
            'age':forms.NumberInput(attrs={'class':'form-control w-75 mx-auto'}),  
          }
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(name)<3:
            raise forms.ValidationError("Name must contain atleast 3 chars")
        return name