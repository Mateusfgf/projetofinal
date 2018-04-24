from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicar

def listar_postagem(request):
	    posts = Publicar.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
	    return render(request, 'bforum/listar_postagem.html', {'posts': posts})

def detalhando_postagem(request, pk):
	    post = get_object_or_404(Publicar, pk=pk)
	    return render(request, 'bforum/detalhando_postagem.html', {'post': post})