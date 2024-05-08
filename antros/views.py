from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from .models import User

def usuarios(request):
    render(request, 'antros.html')

@require_http_methods(["POST"])
def registrar_antro(request):
    # Extract data from request
    data = request.POST
    nombre = data.get('Nombre')
    email = data.get('Email')
    celular_de_contacto = data.get('Celular_de_contacto')
    contrasenia = data.get('Contrasenia')
    localidad = data.get('Localidad')
    documento_verificacion = data.get('Documento_verificacion')
    tipo_de_antro = data.get('Tipo_de_antro')
    rango_de_precios = data.get('Rango_de_precios')
    
    # Process data and save to database
    
    # Placeholder response
    response_data = {'message': 'Gracias por tu registro, si eres seleccionado, estaremos en contacto contigo.'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def logout_antro(request):
    # Placeholder for club logout logic
    response_data = {'status': 'Logged Out'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def borrar_antro(request):
    # Placeholder for deleting club from database
    response_data = {'status': 'Deleted'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def comentario_antro(request):
    comentario = request.POST.get('comentario')
    email_destinatario = 'service@example.com'  # Email of the person in charge of service to clubs
    
    # Send an email to the person in charge
    send_mail(
        'New Comment on Club',
        comentario,
        'from@example.com',
        [email_destinatario],
        fail_silently=False,
    )
    
    # Placeholder response
    response_data = {'status': 'Comment Sent'}
    return JsonResponse(response_data)

@require_http_methods(["GET"])
def detalles_reservaciones(request):
    antro_id = request.GET.get('antro_id')
    # Fetch reservation details based on antro_id from the database
    
    # Placeholder response
    response_data = {'details': 'Details of Reservations for the specified club'}
    return JsonResponse(response_data)

