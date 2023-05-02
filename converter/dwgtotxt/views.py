from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data', '')
        output_data = input_data.upper()
        context = {'output_data': output_data}
        return render(request, 'dwgtotxt.html', context)
