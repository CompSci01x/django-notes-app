from django.forms import ModelForm, Textarea, TextInput
from .models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        
        widgets = {

            'title': TextInput(attrs={'style': 'border-style: solid; border-color:grey; border-radius: 5px;',
                                    'placeholder': 'Note title ...'}),

            'text': Textarea(attrs={'style': 'border-style: solid; border-color:grey; border-radius: 5px;', 
                                    'cols': 20, 
                                    'rows': 3,
                                    'placeholder': 'Jot down a note ...'})
        }
        
        labels = {
            'text': 'Note text'
        }
