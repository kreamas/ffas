# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm, Nombre, eligeNombre, eligeNombreZ
from django.http import HttpResponse, JsonResponse

import pandas as pd

import json

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte  = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk =  pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:        
        form = PostForm()
        
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, intance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/post_edit.html', {'form': form})


def search(request):
    titulo = request.GET.get('title')  #diccionario, lo que viene dentro del parentesis es el nombre del input text de html, al ser un diccionario podemos usar su metodo get
    region = request.GET.get('region')  #diccionario, lo que viene dentro del parentesis es el nombre del input text de html, al ser un diccionario podemos usar su metodo get
    distrito = request.GET.getlist('distrito')  #diccionario, lo que viene dentro del parentesis es el nombre del input text de html, al ser un diccionario podemos usar su metodo get
    repre = request.GET.getlist('repre')  #diccionario, lo que viene dentro del parentesis es el nombre del input text de html, al ser un diccionario podemos usar su metodo get
    boton = request.GET.get('btn')  #diccionario, lo que viene dentro del parentesis es el nombre del input text de html, al ser un diccionario podemos usar su metodo get
    
    ititulo = titulo
    iregion = region


    idistrito = ""
    for i in range(len(distrito)):
        idistrito = idistrito + ", " + distrito[i]

    idistrito = idistrito[2:]

    
    if boton == 'sRef':
        if iregion == "REGION 1":
            repre = ['REPRE 1', 'REPRE 2', 'REPRE 3']
        elif iregion == "REGION 2":
            repre = ['REPRE 4', 'REPRE 5']
        elif iregion == "REGION 3":
            repre = ['REPRE 6', 'REPRE 7', 'REPRE 8']
        else:
            repre = ['REPRE 9', 'REPRE 10']

    irepre = ""
    for i in range(len(repre)):
        irepre = irepre + "," + repre[i]

    irepre = irepre[1:]

    #d = {'one' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
    #     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

    d = {'one' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
    #     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

    df = pd.DataFrame(d)
    
    jsonDFv1 = df.to_json()
    print(jsonDFv1)
    
    jsonDF = [['mush', 2], ['onion',4], ['potato', 3], ['corn', 7]]

    
    
    print(df)

    #return HttpResponse(json.dumps(imprime), content_type = 'application/json')
    return JsonResponse({'nombre': ititulo, 'region': iregion, 'distrito': idistrito, 'repre': irepre, 'df': jsonDF})

  
    
    
def post_msj1(request):
    
    #Esto pasara si se da click
    if request.method == "POST":
        form = Nombre(request.POST)
        elige = eligeNombre(request.POST)
        eligeZ = eligeNombreZ(request.POST)
        
        if form.is_valid() and elige.is_valid() and eligeZ.is_valid():
            nombre = form.cleaned_data['miNombre']
            nelige = elige.cleaned_data['filter_by']
            melige = eligeZ.cleaned_data['filtro']

            print(nombre)
            print(nelige)
            print(melige)
            
            return redirect('post_msj2')        #Aqui pongo el name del view asociado a donde quiero que se vaya la informacion

    #...y esto pasa cuando recien se carga la pagina del render            
    else:
        form = Nombre()
        elige = eligeNombre()
        eligeZ = eligeNombreZ()
    return render(request, 'blog/post_msj1.html', {'form': form, 'elige': elige, 'eligeZ': eligeZ})       
    


    
def post_msj2(request):         #Este es el view que mando llamar en el POST de post_msj1
    form = "Saludos"
    
    return render(request, 'blog/post_msj2.html', {'form': form})
    
    