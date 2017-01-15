from .models import Place

def post_list(request):
    return Place.objects.all()
