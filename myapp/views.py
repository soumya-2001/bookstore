from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Book
from django import forms


class BookForm(forms.Form):
    book_title=forms.CharField()
    ISBN_No=forms.IntegerField()
    author_name=forms.CharField()
    publisher=forms.CharField()
    year_of_publication=forms.IntegerField()
    genre=forms.CharField()
    price=forms.IntegerField()
# Create your views here.


class BookListView(View):
    def get(self,request,*args, **kwargs):
        qs=Book.objects.all()
        return render(request,"book_list.html",{"data":qs})

class BookDetailView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})
    
class BookDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id).delete()
        return redirect("book-list")
    
class BookCreateView(View):
    def get(self,request,*args, **kwargs):
        form=BookForm()
        return render(request,"book_add.html",{"form":form})
    
    # def post(self,request,*args, **kwargs):
    #     data={k:v for k,v in request.POST.items()}
    #     data.pop("csrfmiddlewaretoken")
    #     Book.objects.create(**data)
    #     return redirect("book-list")
    
    def post(self,request,*args, **kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Book.objects.create(**data)
            return redirect("book-list")
        else:
            return render(request,"book_add.html",{"form":form})
        
class BookCreateView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        book_object=Book.objects.get(id=id)
        data={
            "book_title":book_object.book_title,
            "ISBN_No":book_object.ISBN_No,
            "author_name":book_object.author_name,
            "publisher":book_object.publisher,
            "year_of_publication":book_object.year_of_publication,
            "genre":book_object.genre,
            "price":book_object.price,
        }
        form=BookForm(initial=data)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            id=kwargs.get("pk")
            Book.objects.filter(id=id).update(**data)
            return redirect("book-list")
        else:
            return render(request,"book_edit.html",{"form":form})

            