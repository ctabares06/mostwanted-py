from django.http import HttpResponse
from .models import Wanted

def index(req):
    last_5_wanted = Wanted.objects.order_by("-id")[:5]
    output = ", ".join([q.name for q in last_5_wanted])
    return HttpResponse(output)

def detail(req, id):
    text = "detailed view for %s wanted"
    return HttpResponse(text % id)

# Create your views here.
