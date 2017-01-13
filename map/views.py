from .models import Bar

def post_list(request):
    return Bar.objects.all()
