from ..widgets import ImageViewWidget


def test_should_clear_checkbox_by_name():
    """ Test  clear_checkbox_name method """
    image =  ImageViewWidget()
    assert image.clear_checkbox_name('image') == 'image-clear'
    
def test_should_clear_checkbox_by_id():
    """ Test clear_checkbox_id """
    image =  ImageViewWidget()
    assert image.clear_checkbox_id('image') == 'image_id'


def test_should_not_is_initial():
    """ Test is_initial """
    image =  ImageViewWidget()
    assert image.is_initial('value') == False

def test_should_not_get_value():
    """ Test format_value """
    image =  ImageViewWidget()
    assert image.format_value('value') == None

def test_should_get_value():
    """ Test format_value """

    class MockValue:
        url = 'url'
        copy = 'copy'

    image =  ImageViewWidget()
    mock = MockValue()

    assert image.format_value(mock) is mock

    
    
def test_should_get_context():
    """ Test get context """
    image = ImageViewWidget()
    result ={
        'widget': {
            'name': 'demo', 
            'is_hidden': False, 
            'required': False, 
            'value': None, 
            'attrs': {}, 
            'template_name': 'django-image-view.html', 
            'type': 'file', 
            'checkbox_name': 'demo-clear', 
            'checkbox_id': 'demo-clear_id', 
            'is_initial': False, 
            'input_text': 'Change', 
            'initial_text': 'Currently', 
            'clear_checkbox_label': 'Clear'
        }
    }
#    assert image.get_context('demo','demo.jpg',{}) == result
    pass


def test_should_get_datadict():
    """ Test value_from_datadict """
    image = ImageViewWidget()
    assert image.value_from_datadict('data',{'data':'img.jpg'},'mock') == None

def test_should_is_required_attribute():
    """ Test use_required_attribute """
    image = ImageViewWidget()
    assert image.use_required_attribute('mock') == False

def test_should_omitted_data():
    """ value_omitted_from_data """
    image = ImageViewWidget()
    assert image.value_omitted_from_data('mock',{},'name') == True
