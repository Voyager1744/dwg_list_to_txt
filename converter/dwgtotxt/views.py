from django.shortcuts import render
from .utils.dwg2txt import replace_data


def index(request):
    return render(request, 'input_page.html')


def convert_text(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input').split('\n')
        start_point = int(request.POST.get('start_point'))
        converted_text = replace_data(text_input, start_point)
        context = {
            'converted_text': converted_text,
        }
        return render(request, 'result_page.html', context)
    return render(request, 'input_page.html')
