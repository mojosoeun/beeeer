from .models import Place

def place_list(request):
    return Place.objects.all()
