from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from .models import Gallery

class ImageViewWidget(forms.Widget):
    """ Image View Widget """

    template_name = 'django-image-view.html'
    clear_checkbox_label = _('Clear')
    initial_text = _('Currently')
    input_text = _('Change')
    type_input = 'file'

    class Media:
        """ There all styles Image View Wibget """
        js = (
            'django-image-view/js/admin_button_script.js',
        )
        css = {
            'all': (
                'django-image-view/css/admin_button_widget.css',
            )
        }

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        checkbox_name = self.clear_checkbox_name(name)
        checkbox_id = self.clear_checkbox_id(checkbox_name)
        context['widget'].update({
            "type": self.type_input,
            'url': self.get_url_image(value),
            'checkbox_name': checkbox_name,
            'checkbox_id': checkbox_id,
            'is_initial': self.is_initial(value),
            'input_text': self.input_text,
            'initial_text': self.initial_text,
            'clear_checkbox_label': self.clear_checkbox_label,
        })
        return context

    def get_url_image(self,value):
        """
        Given the url of the file input, return the url image to show image.
        """
        if hasattr(value,'url'):
            return value.url
        return ''
    
    def clear_checkbox_name(self, name):
        """
        Given the name of the file input, return the name of the clear checkbox
        input.
        """
        return name + '-clear'

    def clear_checkbox_id(self, name):
        """
        Given the name of the clear checkbox input, return the HTML id for it.
        """
        return name + '_id'

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return bool(value and getattr(value, 'url', False))
    

    def is_changed_value(self,value):
        """
        Validatre
        """


class GalleryForm(forms.ModelForm):
    """ Gallery Form  """
    image = forms.CharField(widget=ImageViewWidget)

    class Meta:
        model = Gallery 
        fields = '__all__'

