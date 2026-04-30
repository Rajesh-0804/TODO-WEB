from django import forms
from toDo.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title','description','due_date','priority','status']
    