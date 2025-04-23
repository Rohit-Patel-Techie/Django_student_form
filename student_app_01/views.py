from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.conf import settings
from django.templatetags.static import static
import os
from django.contrib.auth.decorators import login_required

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            # return generate_pdf(student)
            return generate_pdf(request, student)
            # return HttpResponse("code is runnig")
    else:
        form = StudentForm()
    return render(request, 'form_01.html', {'form': form})

def generate_pdf(request,student):
    # html_string = render_to_string('pdf_01.html', {'student': student})
    logo_abspath = os.path.join(settings.BASE_DIR, 'student_app_01/static/images/andc_logo_01.png')
    logo_uri = 'file:///' + logo_abspath.replace('\\', '/')

    photo_url = request.build_absolute_uri(student.photo.url)
    signature_url = request.build_absolute_uri(student.signature.url)

    # Pass this to the template
    html_string = render_to_string('pdf_01.html', {
        'student': student,
        'logo_path': logo_uri,
        'photo_url': photo_url,
        'signature_url': signature_url
    })
    # print(html_string) 
    # //locally
    # html = HTML(string=html_string, base_url="http://127.0.0.1:8000/")
    # live render
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.student_name}_details.pdf"'
    return response

def test_view(request):
    student = Student.objects.first()
    # print(student)  # Get a student object for testing
    return render(request, 'pdf_01.html', {'student': student})
