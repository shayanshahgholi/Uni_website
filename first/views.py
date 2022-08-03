from .forms import CourseForm, RegisterForm, ContactForm
from django.template import loader
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from first.models import Course, MoreDetail
from django.contrib.auth.decorators import user_passes_test


def index(request):
    template = loader.get_template('home.html')
    if (request.user.is_authenticated):
        return HttpResponse(template.render({'main': "login_base.html"}, request))
    else:
        return HttpResponse(template.render({'main': 'base.html'}, request))


def register_page(request):
    template = loader.get_template('register.template')
    return HttpResponse(template.render({'form': RegisterForm}, request))


def contact_us_page(request):
    template = loader.get_template('contact_us.template')
    return HttpResponse(template.render({'form': ContactForm}, request))


def contact_us(request):
    form = ContactForm(data=request.POST)
    if not form.is_valid():
        template = loader.get_template('error.html')
        return HttpResponse(template.render({'error': str(form.errors)}, request))
    else:
        title = form.cleaned_data['title']
        text = form.cleaned_data['Text']
        email = form.cleaned_data['Email']
        try:
            send_mail(
                title,
                text + ' From: ' + email,
                'shshayan94@gmail.com',
                ['shshayan94@gmail.com', 'danial.erfanian@divar.ir'],
                fail_silently=False,
            )
            template = loader.get_template('done.html')
            return HttpResponse(template.render({'message': 'Message send successfully'}, request))
        except:
            template = loader.get_template('error.html')
            return HttpResponse(template.render({'error': 'username exist, please choose another one'}, request))


def register(request):
    form = RegisterForm(data=request.POST)
    if not form.is_valid():
        template = loader.get_template('error.html')
        return HttpResponse(template.render({'error': str(form.errors)}, request))
    else:
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['Email']
        gender = request.POST.get('gender')
        bio = request.POST.get('bio')
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name)
            more_detail = MoreDetail(user=user)
            more_detail.bio = bio
            more_detail.gender = gender
            more_detail.save()
        except:
            template = loader.get_template('error.html')
            return HttpResponse(template.render({'error': 'username exist, please choose another one'}, request))

        return HttpResponseRedirect('/first')


@login_required(login_url='/first/login')
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/first')


def login_page(request):
    template = loader.get_template('login.template')
    return HttpResponse(template.render({}, request))


def login_user(request):
    username = request.POST.get('uname', None)
    password = request.POST.get('psw', None)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/first')
    else:
        template = loader.get_template('error.html')
        return HttpResponse(template.render({'error': 'Wrong Password'}, request))


@login_required(login_url='/first/login')
def profile_page(request):
    template = loader.get_template('Profile.template')
    return HttpResponse(template.render({'user': request.user}, request))


@login_required(login_url='/first/login')
def edit_page(request):
    template = loader.get_template('edit_profile.template')
    return HttpResponse(template.render({'user': request.user}, request))


@login_required(login_url='/first/login')
def edit_user(request):
    fname = request.POST.get('first_name', None)
    lname = request.POST.get('last_name', None)
    gender = request.POST.get('gender')
    bio = request.POST.get('bio', None)
    image_src = request.POST.get('avatar')
    if (fname != None and fname != ''):
        request.user.first_name = fname
    if (lname != None and lname != ''):
        request.user.last_name = lname
    detail = MoreDetail.objects.filter(user=request.user).get()
    if (bio != None and bio != ''):
        detail.bio = bio
    print(image_src)
    detail.avatar = image_src
    detail.gender = gender
    request.user.save()
    detail.save()
    return HttpResponseRedirect('/first/profile')


@login_required(login_url='/first/login')
def panel_page(request):
    template = loader.get_template('panel.template')
    print(request.user.is_superuser)
    return HttpResponse(template.render({'user': request.user}, request))


@user_passes_test(lambda u: u.is_superuser)
def make_new_course_page(request):
    template = loader.get_template('make_new_course.template')
    return HttpResponse(template.render({}, request))


@user_passes_test(lambda u: u.is_superuser)
def add_course(request):
    form = CourseForm(data=request.POST)
    if not form.is_valid():
        template = loader.get_template('error.html')
        return HttpResponse(template.render({'error': str(form.errors)}, request))
    else:
        course = Course()
        course.department = form.cleaned_data['department']
        course.name = form.cleaned_data['name']
        course.course_number = form.cleaned_data['course_number']
        course.group_number = form.cleaned_data['group_number']
        course.teacher = form.cleaned_data['teacher']
        course.start_time = form.cleaned_data['start_time']
        course.end_time = form.cleaned_data['end_time']
        course.first_day = form.cleaned_data['first_day']
        course.second_day = form.cleaned_data['second_day']
        course.save()
        return HttpResponseRedirect('/first/all_courses')


@login_required(login_url='/first/login')
def all_courses(request):
    template = loader.get_template('all_courses.template')
    return HttpResponse(template.render({'courses': Course.objects.all()}, request))
