from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect, JsonResponse
from .models import Marker
import json

# Create your views here.

def handle_uploaded_json(request,json_txt,api_type):
    # json_dump = json.dumps(json_txt)
    json_ob = json.loads(json_txt)

    vertices = json_ob['vertex']
    for v in vertices:
        m = Marker()
        m.x = v['x']
        m.y = v['y']
        m.marker_type=api_type
        m.save()

    markers = Marker.objects.filter(marker_type=api_type).all()

    return markers

def test(request):
    return render(request, 'test.html', {'debug':'debug'})

def getMarkerData(request):
    markers = Marker.objects.order_by('id').values()
    return JsonResponse({'results': list(markers)}, safe=False)

def marker_list(request):
    return render(request, 'map.html', {})

def upload_file(request):
    if request.method == 'POST':
        vertex_json = request.POST.get('vertex_json')
        api_type = request.POST.get('api_type')
    
        handle_uploaded_json(request,vertex_json,api_type)

    return render(request, 'map.html')
   
