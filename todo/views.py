from django.contrib.auth import authenticate, logout as custlogout ,login as custlogin
from todo.forms import CreateUserForm, TodoForm
from todo.models import Todo
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            print(request.FILES)
            form = CreateUserForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('LoginUser')
        context = {'form': form}
        return render(request, 'register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        context = {}
        if request.method == 'POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                custlogin(request, user)
                return redirect('HomePage')
            else:
                messages.info(request, 'Email or Password or both are incorrect')
        return render(request, 'login.html', context)

def logout(request):
    custlogout(request)
    return redirect('LoginUser')

@login_required(login_url='LoginUser')
def homepage(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return HttpResponse(render(request,"homepage.html",context))

@login_required(login_url='LoginUser')
def createtodo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = TodoForm()
    context = {'form': form}
    return HttpResponse(render(request,"create.html",context))

@login_required(login_url='LoginUser')
def deletetodo(request, id):
    todo={}
    try:
        todo=Todo.objects.get(id=id)
        todo.delete()
    except:
        raise Http404
    context = {'todo': todo}
    return render(request, "delete.html",context)

@login_required(login_url='LoginUser')
def updatetodo(request, id=None):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    print(form.is_valid())
    if form.is_valid():
        obj = form.save(commit=False)
        obj.instance.user = request.user
        obj.save()
    context = {'todo': todo, 'form': form}
    return render(request,"update.html",context)


# def updatetodo(request, id=id):
#     form = TodoForm(request.GET)
#     if request.method == 'GET':
#         todo=Todo.objects.get(id=id)

#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()

#     if request.method == 'POST':
#         print(form.is_valid())
#         if form.is_valid():
#             print(request.POST)
#             obj = {}
#             obj['task'] = form.cleaned_data['task']
#             obj['description'] = form.cleaned_data['description']
#             obj['bydate'] = form.cleaned_data['bydate']
#             obj['bytime'] = form.cleaned_data['bytime']
#             obj['user'] = request.user
#             Todo.objects.filter(id=id).update(**obj)

#     todo=Todo.objects.get(id=id)
#     form = TodoForm({'task': todo.task, 'description': todo.description, 'bydate': todo.bydate, 'bytime': todo.bytime})

#     if request.method == 'POST':
#         if form.is_valid():
#             obj = {}
#             obj['task'] = form.cleaned_data['task']
#             obj['description'] = form.cleaned_data['description']
#             obj['bydate'] = form.cleaned_data['bydate']
#             obj['bytime'] = form.cleaned_data['bytime']
#             obj['user'] = request.user
#             Todo.objects.update_or_create(id=id, defaults=obj)
#             form = TodoForm(request.POST or None, obj)
        
#     context = {'todo': todo, 'form': form}
#     return render(request, "update.html",context)

