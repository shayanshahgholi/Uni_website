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
            raise forms.ValidationError("password and confirm_password does not match")

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
    start_time = forms.CharField(label='Start_time:(HH:MM)', max_length=5)
    end_time = forms.CharField(label='End_name: (HH:MM)', max_length=5)
    first_day = forms.CharField(label='First_day')
    second_day = forms.CharField(label='Last_day')
    #def clean(self):
    #    cleaned_data = super(CourserForm, self).clean()
    #    start_time = cleaned_data.get("start_time")
    #    end_time = cleaned_data.get("end_time")
    #    print(start_time, end_time)
    #    if (not re.match(start_time, re.compile('(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)'))):
    #        self.add_error('start_time', 'Invalid start-time format')
    #    if (not re.match(end_time, re.compile('(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)'))):
    #        self.add_error('end_time', 'Invalid end-time format')
    #    return cleaned_data
