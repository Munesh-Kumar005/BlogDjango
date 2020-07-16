from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact  #myself
from django.contrib import messages #myself
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from blog.models import Post  
# Create your views here.


def home(request):
    allPosts = Post.objects.all().order_by('-views')[:3]
    context = {'allPosts': allPosts}

    #return HttpResponse('hello home')
    return render(request,'home/home.html',context)


def about(request):
    return render(request, 'home/about.html')


def contact(request):
     if request.method == "POST":
          name = request.POST['name']
          email = request.POST['email']
          phone = request.POST['phone']
          content = request.POST['content']
          if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content)< 10:
              messages.error(request,'plz fill form correctly')
          else:
                  contact = Contact(name=name, email=email,phone=phone,content=content)
                  contact.save() 
                  messages.success(request, 'Your message is sent.')
    
     return render(request, 'home/contact.html')
 
 
def search(request):
    #allPosts = Post.objects.all()
    query = request.GET['query']
    if len(query)>72:
        allPosts=objects.none()
    else:    
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        if allPosts.count()==0:
            messages.warning(request, 'No search result found plz refine your query')
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
     #return HttpResponse('hello searche')


def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #validation
        
        if len(username) >10:
            messages.error(request, 'your name mustbe under 10 char')
            return redirect('home')
    
        if not username.isalnum():
            messages.error(request, 'your name mustbe alpha numeric')
            return redirect('home')
    
        if pass1 != pass2:
            messages.error(request, 'your pssword do not match')
            return redirect('home')
    
            
    #creatye a user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, 'your account successfully created')
        return redirect('/')
    
   
    else:
        return HttpResponse('404 Not found')
 #return render(request, 'home/search.html', params)


def handleLogin(request):
    loginusername = request.POST['loginusername']
    loginpass = request.POST['loginpass']
    
    user = authenticate(username=loginusername, password=loginpass)
    if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            messages.success(request, ' successfully loged in')
            return redirect('home')

    else:
            # No backend authenticated the credentials
        messages.error(request, ' Invalid  carrendentials please try again')
        return redirect('home')
        return HttpResponse('404 Not found')




def handleLogout(request):
    logout(request)
    messages.success(request, '  successfullylogout')
    return redirect('home')
  #  return HttpResponse('logout')
