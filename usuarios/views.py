from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()

def usuarios(request):
    return render(request, 'usuarios.html')

@require_http_methods(["POST"])
def registrar_usuario(request):
    # Extract data from request
    data = request.POST
    nombre_usuario = data.get('nombre_usuario')
    email = data.get('email')
    contrasenia = data.get('contrasenia')
    cumpleaños = data.get('cumpleaños')  # Ensure the form sends this field in YYYY-MM-DD format

    try:
        # Create and save the new user instance
        user = User.objects.create(
            nombre_usuario=nombre_usuario,
            email=email,
            cumpleaños=cumpleaños,
            password=make_password(contrasenia),  # Properly hash the password
        )
        user.save()
        response_data = {'estatus_de_registro': 'Success'}
    except Exception as e:
        response_data = {'estatus_de_registro': 'Fail', 'error': str(e)}

    return JsonResponse(response_data)


@require_http_methods(["POST"])
def login_usuario(request):
    # Placeholder for user login logic
    response_data = {'estatus_login': 'Logged In or Error'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def logout_usuario(request):
    # Placeholder for user logout logic
    response_data = {'estatus_logout': 'Logged Out'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def borrar_usuario(request):
    # Placeholder for user deletion logic
    response_data = {'estatus_borrar_usuario': 'Deleted or Error'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def comentario_usuario(request):
    # Extract comment
    comentario = request.POST.get('comentario')
    
    # Process and save comment

    # Placeholder response
    response_data = {'estatus_comentario': 'Received or Error'}
    return JsonResponse(response_data)

@require_http_methods(["GET"])
def perfil_usuario(request):
    usuario_id = request.GET.get('usuario')
    # Fetch user profile based on usuario_id
    
    # Placeholder response
    response_data = {'usuario': usuario_id, 'nombre': 'User Name', 'email': 'user@example.com', 'reservas': 'List of Reservations'}
    return JsonResponse(response_data)

@require_http_methods(["POST"])
def crear_resenia_antro(request):
    # Extract review data
    usuario = request.POST.get('usuario')
    antro = request.POST.get('antro')
    estrellas = request.POST.get('estrellas')
    comentario = request.POST.get('comentario')

    # Process and save review

    # Placeholder response
    response_data = {'estatus_resenia': 'Created or Error'}
    return JsonResponse(response_data)