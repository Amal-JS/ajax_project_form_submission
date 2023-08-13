from django.forms import ModelForm
from . models import Sample


class Custom_Form(ModelForm):
    class Meta:
        model = Sample
        fields = '__all__'