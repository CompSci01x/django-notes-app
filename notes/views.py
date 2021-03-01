from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
from .models import Note
from django.views.generic import ListView, DetailView

# Create your views here.

# Home View for notes - displayed in a list
class IndexView(ListView):
    template_name = 'notes/index.html'
    context_object_name = 'note_list'
    
    def get_queryset(self):
        return Note.objects.order_by('-id')



# Detail View - view note detail
class NoteDetailView(DetailView):
    model = Note



# Create Note View - create new note
def createNoteView(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('notes:index')
    
    else:
        form = NoteForm()

    return render(request, 'notes/note.html', {'form': form})



# Edit Note View
def editNote(request, pk, template_name='notes/edit.html'):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect('notes:index')

    return render(request, template_name, {'form': form})



# Delete Note
def deleteNote(request, pk, template_name='notes/confirm_delete.html'):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:index')

    return render(request, template_name, {'object': note})


