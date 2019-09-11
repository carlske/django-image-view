from ..widgets import ImageViewWidget
import pytest

class ImageViewWidgetTest:
    """ Class Image View Widget Test """
    
    image =  ImageViewWidget()

    def test_should_clear_checkbox_by_name(self):
        """ Test  clear_checkbox_name method """
        assert image.clear_checkbox_name('image') == 'image-clear'
    

    def test_should_clear_checkbox_by_id(self):
        """ Test clear_checkbox_id """
        assert image.clear_checkbox_id('image') == 'image_id'


    def test_should_not_is_initial(self):
        """ Test is_initial """
        assert image.is_initial('value') == False


    def test_should_not_get_value(self):
        """ Test format_value """
        assert image.format_value('value') == None


    def test_should_get_value(self):
        """ Test format_value """

        class MockValue:
            url = 'url'
            copy = 'copy'

        mock = MockValue()

        assert image.format_value(mock) is mock

        
    def test_should_get_context(self):
        """ Test get context """
        con = image.get_context('point', None, attrs={'geom_type': 'POINT2'})
#        assert 'POINT2'== 'POINT2'
        pass


    def test_should_get_datadict(self):
        """ Test value_from_datadict """
        assert image.value_from_datadict('data',{'data':'img.jpg'},'mock') == None


    def test_should_is_required_attribute(self):
        """ Test use_required_attribute """
        assert image.use_required_attribute('mock') == False


    def test_should_omitted_data(self):
        """ value_omitted_from_data """
        assert image.value_omitted_from_data('mock',{},'name') == True
