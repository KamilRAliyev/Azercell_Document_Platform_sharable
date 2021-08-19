from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from . import models
from . import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from taggit.models import Tag
from django.contrib.auth import authenticate, login, logout


@login_required
def home(request, **kwargs):
    documents = models.Document.objects.all().order_by('-created_at')
    form = forms.DocumentForm(request.POST, request.FILES or None)
    context = {
        'form': form,
        'documents': documents[:10],
        'nbar': 'home',
        'navTags': Tag.objects.all(),
    }

    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            document = models.Document()
            tags = form.cleaned_data['tags']
            document.name = form.cleaned_data.get('document_name')
            document.type = form.cleaned_data.get('document_type')
            document.section = form.cleaned_data.get('section')
            document.file = form.cleaned_data.get('file')
            document.date = form.cleaned_data.get('date')
            document.description = form.cleaned_data.get('description')
            document.user = request.user
            document.save()
            for tag in tags:
                document.tags.add(tag)
            messages.add_message(request,
                                 messages.SUCCESS,f"Document: {document.name} is saved.")
            return redirect('/home/')
    
    return render(request, 'library_app/content/home.html', context=context)

@login_required
def document(request, pk):
    document = models.Document.objects.get(id=pk)
    context = {
        'document': document,
        'user': document.user,
        'navTags': Tag.objects.all(),
    }

    return render(request, 'library_app/content/document.html', context=context)

@login_required
def types(request, type):
    documents = models.Document.objects.filter(type__contains=type)
    context = {
        'documents': documents,
        'nbar': type,
        'navTags': Tag.objects.all(),
    }
    return render(request, 'library_app/content/table.html', context=context)

@login_required
def sections(request, section):
    documents = models.Document.objects.filter(section__contains=section)
    context = {
        'documents': documents,
        'nbar': section,
        'navTags': Tag.objects.all(),
    }
    return render(request, 'library_app/content/table.html', context=context)

@login_required
def dashboard(request, tag_slug=None):
    documents = models.Document.objects.all().order_by('-created_at')
    tag = None
    context = {
        'documents': documents,
        'nbar': 'dashboard',
        'navTags': Tag.objects.all(),
    }
    

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        context['nbar']=tag.slug
        documents = documents.filter(tags__in=[tag])
        context['documents'] = documents
    
    
    return render(request, 'library_app/content/table.html', context=context)


@login_required
def document_delete(request, pk):
    document = get_object_or_404(models.Document, pk=pk)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        document.delete()                     # delete the cat.
        return redirect('/')             # Finally, redirect to the homepage.

    return redirect('/')
    # If method is not POST, render the default template.
    # *Note*: Replace 'template_name.html' with your corresponding template name.

def user_is_not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(user_is_not_logged_in)
def login_view(request):
    form = forms.Loginform(request.POST or None)
    context = {
        'form': form
    }

    if request.method=="POST":
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
            else:
                messages.add_message(request,
                                    messages.ERROR,"Wrong Username or Password. Please, try again.")
                return redirect('/login/')
    else:
        return render(request,'library_app/auth/login.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login/')