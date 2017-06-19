from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice,User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from .forms import NameForm,UserForm,UserFormLogin
from django.contrib.sessions.models import Session
from django.contrib import auth 
from .auth import UsernamePasswordAuth
import datetime
import time
import pdb
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')#[:5]
# 	template = loader.get_template('polls/index.html')
# 	context = {'latest_question_list':latest_question_list}
# 	return HttpResponse(template.render(context,request))


# def detail(request,question_id):
# 	question = get_object_or_404(Question,pk=question_id)
# 	return render(request,'polls/detail.html',{'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	print(question_id)
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail',{'question':question,'error_message':"You didn't select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# return HttpResponse(reverse('polls:results',args=(question.id,)))
		# return render(request,'polls/results.html',{'question':question})
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,))) 


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    queryset =  Question.objects.order_by('-pub_date')
    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]
		
class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'




def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
            return HttpResponse('hiiiiiiiiiiiiiiii')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/getName.html', {'form': form})


		
def register(request):
    curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());

    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            #pdb.set_trace()
            #try:
            filterResult = User.objects.filter(username = username)
            if len(filterResult)>0:
                return render(request,'polls/register.html',{"errors":"用户名已存在"})
            else:
                password1 = uf.cleaned_data['password1']
                password2 = uf.cleaned_data['password2']
                print(password1)
                errors = []
                if (password2 != password1):
                    errors.append("两次输入的密码不一致!")
                    return render(request,'polls/register.html',{'errors':errors})
                    #return HttpResponse('两次输入的密码不一致!,请重新输入密码')
                password = password2
                email = uf.cleaned_data['email']
            #将表单写入数据库
                user = User.objects.create(username=username,password=password1,email = email)
                #user = User(username=username,password=password,email=email)
                user.save()
                pdb.set_trace()
            #返回注册成功页面
                return render(request,'polls/success.html',{'username':username,'operation':"注册"})
    else:
        uf = UserForm()
    return render(request,'polls/register.html',{'uf':uf})







def login2(request):
    
    if request.user.is_authenticated():
        print("11")
        response = render(request,'polls/success.html',{'operation':"成功"})
        response.set_cookie('lucky_num','1')
        return response
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        print("22")
        if user is not None and user.is_active:
            print("33")
            auth.login(request, user)
            response = render(request,'polls/success.html',{'operation':"成功"})
            response.set_cookie('lucky_num','1')
        else:
            print("44")
            uf = UserFormLogin()
            request.session['numbera'] = 110
            response = render(request,"polls/userlogin.html",{'uf':uf})
            return response
    else:
        uf = UserFormLogin()
        request.session['numbera'] = 110
        response = render(request,"polls/userlogin.html",{'uf':uf})
    return response




def login3(request):
    
    if request.user.is_authenticated():
        print("11")
        response = render(request,'polls/success.html',{'operation':"成功"})
        response.set_cookie('lucky_num','1')
        return response
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        print("22")
        if user is not None and user.is_active:
            print("33")
            auth.login(request, user)
            response = render(request,'polls/success.html',{'operation':"成功"})
            response.set_cookie('lucky_num','1')
        else:
            print("44")
            uf = UserFormLogin()
            request.session['numbera'] = 110
            response = render(request,"polls/userlogin.html",{'uf':uf})
            return response
    else:
        uf = UserFormLogin()
        request.session['numbera'] = 110
        response = render(request,"polls/userlogin.html",{'uf':uf})
    return response



def login(request): 
    ss =  "sessionid:"+str(request.session.session_key)
    print(ss)
    if request.method == "POST":
        uf = UserFormLogin(request.POST)

        if 'numbera' in request.session:
            lucky_number = request.session['numbera']
            print(lucky_number)
        else:
            print("no numbera")
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']            
            userResult = User.objects.filter(username=username)
            #pdb.set_trace()
            if len(userResult) == 0:
                return  HttpResponse("该用户不存在")
            else:
                for user in userResult:
                    if user.password == password:

                        sid = request.COOKIES['sessionid']
                        s = Session.objects.get(pk=sid)
                        s_info='Session ID' + sid + 'date:'+str(s.expire_date) + 'data:'+str(s.get_decoded())
                        response = render(request,'polls/success.html',{'operation':s_info})
                        response.set_cookie('lucky_num','1')
                        return response
                return  HttpResponse("密码错误")
                        
    else:
        uf = UserFormLogin()
        request.session['numbera'] = 110
        response = render(request,"polls/userlogin.html",{'uf':uf})
        
    return response