from django.shortcuts import render, redirect   
from django.contrib.messages import error
from .models import data, book
import bcrypt

def index(request):
    if request.session:
        del request.session

    return render(request, 'first_app/login.html')

def register(request):
    if request.method == "POST":
        errors = data.objects.validate_registration(request.POST)
        if errors:
            for err in errors:
                error(request, err)
            print(errors)
            return redirect('/')
        else:
            new_id = data.objects.register_user(request.POST)

          
            return redirect('/success')
    
def login(request):
     if request.method == "POST":
        users = data.objects.filter(email=request.POST["email"])

        user = users[0]

        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['id']= user.id
            request.session['first_name']= user.first_name
            print(success)
            return redirect("/success")

        else:
        
            error(request, 'blah blah')
            return redirect("/")


def success(request):
    context={
        'user': data.objects.get(id=request.session["id"]),
        'all_books' : book.objects.all(),
    }
    return render (request, "first_app/base.html", context)



def add(request):
    if request.method == 'POST':
        title=request.POST["title"]
        description=request.POST["description"]
        uploaded_by=data.objects.get(id=request.session['id'])

        book.objects.create(title=title,description=description, uploaded_by=uploaded_by)
    return redirect("/success")




def edit (request, show_id):
    my_id = show_id
    my_session=str(request.session["id"])

    context = {
        'user': data.objects.get(id=request.session["id"]),
        'show' : book.objects.get(id=show_id),
        'who_likes': book.objects.get(id=show_id).users_who_like.all()

    } 


    if (my_id==my_session):
        return render (request, "first_app/edit.html", context)

    else: 
        return render (request, "first_app/show.html", context)



def like(request,show_id):
    book.objects.get(id=show_id).users_who_like.add(data.objects.get(id=request.session['id']))

    return redirect("/show/"+show_id)







def delete(request, show_id):
    x = book.objects.get(id=show_id)
    x.delete()

    return redirect('/')

# def update (request, show_id):
#     errors = tv.objects.basic_validator(request.POST)
#     id=show_id

#     if (len(errors))>0:
#         for key, value in errors.items():
#             messages.error(request,value)
#         return redirect('/show/'+id+'/edit')
#     else:
#         x=tv.objects.get(id=show_id)
        
#         x.title=request.POST["title"]
#         x.network=request.POST["network"]
#         x.release_date=request.POST["release_date"]
#         x.description=request.POST["description"]
#         x.save()
#         messages.success(request, 'TV show updated succesfully!!!')

#     return redirect ("/show/"+id)