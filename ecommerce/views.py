#respuestas con strings
from this import d
from django.http import HttpResponse

#renderizados de templates
from django.template import Template , Context, loader



def say_hello(request):
    

    return HttpResponse("Hola mundo") 


def say_hello_whit_name(request,name):
    

    return HttpResponse(f"Hola {name}") 

def print_add(request,num1,num2):
    return HttpResponse(f"{num1} + {num2} = {num1+num2}")


def index(request,name):
    #paso 1: cargar contenido html
    archivo = open(r"C:\Users\takes\Documents\python coder\django1\ecommerce\ecommerce\templates\index.html", "r")

    contenido_html = archivo.read()
    archivo.close()

    #paso 2: crear la plantilla
    plantilla = Template(contenido_html)

    #paso 3: crear contexto
    contexto = Context({"nombre": name})
    
    #paso 4: preparar documento para renderizar
    documento_a_renderizar = plantilla.render(contexto)


    #paso 5: devolver la respuesta al usuario
    return HttpResponse(documento_a_renderizar)


#paso 0: crear el contexto
def notas(request):
    
    datos ={"notas":[ 9,4,3,7,10],"estudiante": "Cristian" }
    
    #paso 1: cargar contenido HTML
    archivo = open(r"C:\Users\takes\Documents\python coder\django1\ecommerce\ecommerce\templates\notas.html", "r")
    contenido = archivo.read()
    archivo.close()

    #paso 2: crear plantilla
    plantilla = Template(contenido)

    #paso 3: crear contexto
    contexto = Context(datos)

    #paso 4: renderizar HTML con la informacion del contexto
    documento = plantilla.render(contexto)

    #paso 5: retornar el documento como respuesta
    return HttpResponse(documento)


def alumnos(request):
    
    datos = {"curso": "Python", "alumnos": ["Leonel", "Pedro", "Santi", "Maria", "Enrique"]}
    
    plantilla = loader.get_template("alumnos.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)
