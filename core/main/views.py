from django.shortcuts import render, redirect
from .models import Color, Notebooks

# Create your views here.

def index(request):
     # Get the list of all colors and distinct CPUs
    color_list = Color.objects.all()
    cpus = Notebooks.objects.values_list('cpu', flat=True).distinct()
    gpus = Notebooks.objects.values_list('gpu', flat=True).distinct()
    # Initialize the notebook query set
    notebook_list = Notebooks.objects.all()

    # Check if the form has been submitted via POST
    if request.method == 'POST':
        color_id = request.POST.get('color_id')
        cpu_name = request.POST.get('cpu_name')
        gpu_name = request.POST.get('gpu_name')

        # Filter by color_id if provided
        if color_id:
            notebook_list = notebook_list.filter(color=color_id)

        # Filter by cpu_name if provided
        if cpu_name:
            notebook_list = notebook_list.filter(cpu__iexact=cpu_name)

        if gpu_name:
            notebook_list = notebook_list.filter(gpu__iexact=gpu_name)


    return render(request, 'index.html', context={
        'notebook_list': notebook_list,
        'color_list': color_list,
        'cpus': cpus,
        'gpus':gpus
    })
