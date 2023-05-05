from django.shortcuts import redirect,render
from .models import ToDo
from .forms import FormToDo
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def todo(request):
    todo = None
    if request.user.is_authenticated:
        todo = ToDo.objects.filter(user=request.user)
    context={
        'ToDo': todo
    }
    return render(request, 'room/todo.html',context)




@login_required(login_url='/login')
def create_ToDo(request):
    if request.POST.get('title') not in '':
        title_get = request.POST.get('title')

        if request.method == "POST":
            ToDo.objects.create(
                user=request.user,
                title = title_get
            )
            return redirect ('todo')
    else:
        return redirect ('todo')

    
    return render(request, 'room/todo.html')


# # @login_required(login_url='/login')
# # def create_ToDo(request):

# #     todo = FormToDo()

# #     if request.method == "POST":
# #         todo = FormToDo(request.POST)
# #         if todo.is_valid():
# #             todo.save()
# #             return redirect ('todo')
# #     return render(request, 'room/todo.html')




def update_ToDo(request,pk):
    todo = ToDo.objects.get(id=pk)
    form = FormToDo(instance=todo)
    if request.method=='POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('todo')
    context = {
        'form':form
    }
    return render(request,'room/update.html',context)


def delete_ToDo(request,pk):
    todo = ToDo.objects.get(id=pk)
    todo.delete()
    return redirect('todo')
   
        

def logoutUser(request):
    logout(request)
    return redirect('todo')


def to_log(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('todo')
        else:
            messages.error(request,'ERROR')

    return render(request,'room/to_log.html')



def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'usern does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('todo')
        else:
            messages.error(request,'username OR password does not exist')

    return render(request,'room/login.html')






