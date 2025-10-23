
import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Study
from .forms import StudyForm

# Create your views here.

logger = logging.getLogger(__name__)

def study_list(request):
    try:
        studies = Study.objects.all()
        return render(request, 'studies/study_list.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error fetching studies: {e}")
        messages.error(request, "Failed to load studies.")
        return render(request, 'studies/study_list.html', {'studies': []})

def study_create(request):
    form = StudyForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, "Study added successfully!")
            return redirect('study_list')
        except Exception as e:
            logger.error(f"Error creating study: {e}")
            messages.error(request, "Error creating study.")
    return render(request, 'studies/study_form.html', {'form': form, 'title': 'Add Study'})

def study_view(request, pk):
    study = get_object_or_404(Study, pk=pk)
    return render(request, 'studies/study_view.html', {'study': study})

def study_update(request, pk):
    study = get_object_or_404(Study, pk=pk)
    form = StudyForm(request.POST or None, instance=study)
    if request.method == 'POST' and form.is_valid():
        try:
            form.save()
            messages.success(request, "Study updated successfully!")
            return redirect('study_list')
        except Exception as e:
            logger.error(f"Error updating study: {e}")
            messages.error(request, "Error updating study.")
    return render(request, 'studies/study_form.html', {'form': form, 'title': 'Edit Study'})

def study_delete(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)
        study.delete()
        messages.success(request, "Study deleted successfully!")
    except Exception as e:
        logger.error(f"Error deleting study: {e}")
        messages.error(request, "Error deleting study.")
    return redirect('study_list')
