from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from elements.file import FileInput

class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Image')

        self.image_upload_info_icon = Icon(page, f'{identifier}-image-upload-widget-info-icon', 'Icon image')
        self.image_upload_info_tittle = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Tittle image')
        self.image_upload_info_description = Text(page, f'{identifier}-image-upload-widget-info-description-text', 'Description image')

        self.upload_image_button = Button(page, f'{identifier}-image-upload-widget-upload-button', 'Upload image')
        self.upload_image_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload image')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Delete image')

    def click_remove_image(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_image_input.set_input_files(file)

    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')

        self.image_upload_info_tittle.check_visible()
        self.image_upload_info_tittle.check_have_text('Tap on "Upload image" button to select file')

        self.image_upload_info_icon.check_visible()

        if is_image_uploaded:
            self.preview_image.check_visible()
            self.remove_button.check_visible()

        else:
            self.preview_empty_view.check_visible(
                tittle='No image selected',
                description='Preview of selected image will be displayed here'
            )