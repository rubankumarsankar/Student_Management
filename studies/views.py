import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Study
from .forms import StudyForm

# Create a logger instance
logger = logging.getLogger(__name__)

# ==========================
# View: List all studies
# ==========================
def study_list(request):
    try:
        studies = Study.objects.all().order_by('id')
        logger.info("Fetched all studies successfully.")
        return render(request, 'studies/study_list.html', {'studies': studies})
    except Exception as e:
        logger.error(f"Error loading study list: {e}")
        messages.error(request, "An error occurred while loading studies.")
        return render(request, 'studies/study_list.html', {'studies': []})

# ==========================
# View: Create a new study
# ==========================
def study_create(request):
    try:
        if request.method == 'POST':
            form = StudyForm(request.POST)
            if form.is_valid():
                study = form.save()
                logger.info(f"New study created: {study.study_name}")
                messages.success(request, "Study added successfully!")
                return redirect('study_list')
            else:
                logger.warning("Invalid form data submitted for study creation.")
        else:
            form = StudyForm()
        return render(request, 'studies/study_form.html', {'form': form, 'title': 'Add Study'})
    except Exception as e:
        logger.exception(f"Error creating study: {e}")
        messages.error(request, "An unexpected error occurred while adding the study.")
        return redirect('study_list')

# ==========================
# View: View study details
# ==========================
def study_view(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)
        logger.info(f"Viewing study: {study.study_name}")
        return render(request, 'studies/study_view.html', {'study': study})
    except Exception as e:
        logger.exception(f"Error viewing study {pk}: {e}")
        messages.error(request, "Unable to view the study details.")
        return redirect('study_list')

# ==========================
# View: Update a study
# ==========================
def study_update(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)
        if request.method == 'POST':
            form = StudyForm(request.POST, instance=study)
            if form.is_valid():
                form.save()
                logger.info(f"Study updated: {study.study_name}")
                messages.success(request, "Study updated successfully!")
                return redirect('study_list')
            else:
                logger.warning(f"Invalid data while updating study {study.id}.")
        else:
            form = StudyForm(instance=study)
        return render(request, 'studies/study_form.html', {'form': form, 'title': 'Edit Study'})
    except Exception as e:
        logger.exception(f"Error updating study {pk}: {e}")
        messages.error(request, "An error occurred while updating the study.")
        return redirect('study_list')

# ==========================
# View: Delete a study
# ==========================
def study_delete(request, pk):
    try:
        study = get_object_or_404(Study, pk=pk)
        study.delete()
        logger.warning(f"Study deleted: {study.study_name}")
        messages.success(request, "Study deleted successfully!")
    except Exception as e:
        logger.exception(f"Error deleting study {pk}: {e}")
        messages.error(request, "An error occurred while deleting the study.")
    return redirect('study_list')
