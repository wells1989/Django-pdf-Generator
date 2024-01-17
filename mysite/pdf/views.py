from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import io

import pdfkit

# Create your views here.
def accept(request):

    if request.method == "POST":
        details = {
            "name": request.POST.get('name'),
            "email": request.POST.get('email'),
            "phone": request.POST.get('phone'),
            "summary": request.POST.get('summary'),
            "degree": request.POST.get('degree'),
            "school": request.POST.get('school'),
            "university": request.POST.get('university'),
            "previous_work": request.POST.get('previous_work'),
            "skills": request.POST.get('skills'),
        }

        order = Profile(**details)
        order.save()

    return render(request, 'pdf/accept.html')

def resume(request, id): # id will be id of user to download their cv
    user_profile = Profile.objects.get(pk=id) # getting user profile from database via id

    template = loader.get_template('pdf/resume.html') # loads template without context i.e. without user data
    html = template.render({'user_profile': user_profile}) # passes in context

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
    }

    pdf = pdfkit.from_string(html, False, options, configuration=config) # takes a html string and converts to pdf document, format = from_string(input, output_path, options=None, toc=None, cover=None, css=None, configuration=None, cover_first=False, input_encoding=None, **kwargs) 

    response = HttpResponse(pdf,content_type="application/pdf") # pdf file, content_type states it's a pdf file
    response['Content-Disposition'] = f"attachment; filename=resume.pdf" # treating the file as an attachment rather than displaying in the browser
    filename = "resume.pdf"

    return response


def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})
