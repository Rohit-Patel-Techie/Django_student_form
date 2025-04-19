# from django import forms
# from .models import Student
# # from django.forms import ModelForm

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = '__all__'
#         widgets = {
#             'birth_date': forms.DateInput(attrs={'type': 'date'}),
#             'gender': forms.RadioSelect(),
#             'status': forms.RadioSelect(),
#         }

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'status': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student Name'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Father Name'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mother Name'}),
            'present_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Present Address', 'rows': 3}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nationality'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Occupation'}),
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Name'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'signature': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }