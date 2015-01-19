from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from .models import Job

# change to generic class views (use get_queryset function)
def jobs(request):
    # this will eventually need to filter on expiration date too
    job_offers = Job.objects.filter(published=True)
    return render(
        request, 
        'jobs/jobs.html', 
        {
            'job_offers': job_offers
        }
    )

def job_details(request, id):
    job = get_object_or_404(Job, id=id)
    return TemplateResponse(
        request,
        'jobs/job_details.html',
        {
            'job': job,
        }
    )
