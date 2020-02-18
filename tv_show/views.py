from django.shortcuts import render, redirect
from tv_show.models import *
# Create your views here.

def index(request):
    return redirect('/shows')
def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'shows.html',context)
def show_id(request, show_id):
    context={
        'show': Show.objects.get(id=show_id)
    }
    return render(request,'display_show.html', context)

def edit_show(request, show_id):
    if request.POST:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect('/shows')
    else:
        context={
            'show':Show.objects.get(id=show_id)
        }
        return render(request, 'edit_show.html', context)

def new_show_form(request):
    return render(request, 'add_show.html')

def add_show(request):
    new_show = Show.objects.create(title=request.POST['title'],network=request.POST['network'], release_date= request.POST['release_date'],description=request.POST['description'])
    return redirect('/shows/'+ str(new_show.id))

def delete_show(request,show_id):
    dlt_show = Show.objects.get(id=show_id)
    dlt_show.delete()
    return redirect('/shows')