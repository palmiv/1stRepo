from django.shortcuts import get_object_or_404, render

from .models import Name


def index(request):
    latest_name_list = Name.objects.order_by('-pub_date')[:5]
    context = {'latest_name_list': latest_name_list}
    return render(request, 'polls/index.html', context)

def detail(request, name_id):
    name = get_object_or_404(Name, pk=name_id)
    return render(request, 'polls/detail.html', {'name': name})

def results(request, name_id):
    response = "You're looking at the results of name %s."
    return HttpResponse(response % name_id)

def vote(request, name_id):
    return HttpResponse("You're voting on name %s." % name_id)
