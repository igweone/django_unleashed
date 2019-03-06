from django.http.response import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import get_object_or_404, render_to_response

from .models import Tag
from .models import Startup


def tag_list(request):
    return render_to_response('organizer/tag_list.html', {'tag_list':Tag.objects.all()})
    # tag_list = Tag.objects.all()
    # template = loader.get_template(
    #     'organizer/tag_list.html')
    # context = Context({'tag_list': tag_list})
    # output = template.render(context)
    # return HttpResponse(output)

    # return HttpResponse(loader.get_template('organizer/tag_list.html').render(Context({'tag_list':Tag.objects.all()})))



def tag_detail(request, slug):
    # tag = get_object_or_404(Tag, slug__iexact=slug)
    # template = loader.get_template('organizer/tag_detail.html')
    # context = Context({'tag':tag})
    # return HttpResponse(template.render(context))
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render_to_response('organizer/tag_detail.html', {'tag':tag})

def startup_list(request):
    return render_to_response('organizer/startup_list.html', {'startup_list': Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render_to_response('organizer/startup_detail.html', {'startup_list': startup})