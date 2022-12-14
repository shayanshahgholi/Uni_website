from django import forms
from django.core.validators import MinLengthValidator
import re

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    Email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', max_length=100,
                                widget=forms.PasswordInput(),
                                validators=[MinLengthValidator(limit_value=8, message='short password')])
    confirm_password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput(),
                                        validators=[MinLengthValidator(limit_value=8)])
    first_name = forms.CharField(label='First_name' , max_length=200)
    last_name = forms.CharField(label='Last_name')
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("confirm_password does not match to password")

class ContactForm(forms.Form):
    title = forms.CharField(label='Title', max_length=250 , 
                        validators=[MinLengthValidator(limit_value=10, message='Short title')])
    Email = forms.EmailField(label='Email')
    Text = forms.CharField(label='Text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['Email'].required = True
        self.fields['Text'].required = True


class CourseForm(forms.Form):
    department = forms.CharField(label='Department', max_length=200)
    name = forms.CharField(label='Course name',max_length=200, 
                            validators=[MinLengthValidator(limit_value=8, message='Short name')])
    course_number = forms.IntegerField(label='Course_number')
    group_number = forms.IntegerField(label='Group_number')
    teacher = forms.CharField(label='teacher' , max_length=200)
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    first_day = forms.CharField(label='First_day')
    second_day = forms.CharField(label='Last_day')


