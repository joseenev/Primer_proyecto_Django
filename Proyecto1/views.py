from django.http import HttpResponse

#Primera vista
def saludo(request):
    
    return HttpResponse("Hola Jose, estás aprendiendo Django")
#Una segunda vista que estará en otra url
def despedida(request):
    
    return HttpResponse("Hasta luego, seguiremos aprendiendo")
