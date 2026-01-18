from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent

class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = self.page.get_by_test_id(f'{identifier}-image-upload-widget-preview-image')

        self.image_upload_info_icon = self.page.get_by_test_id(f'{identifier}image-upload-widget-info-icon')
        self.image_upload_info_tittle = self.page.get_by_test_id(f'{identifier}-image-upload-widget-info-title-text')
        self.image_upload_info_description = self.page.get_by_test_id(f'{identifier}-image-upload-widget-info-description-text')

        self.upload_image_button = self.page.get_by_test_id(f'{identifier}-image-upload-widget-upload-button')
        self.upload_image_input = self.page.get_by_test_id(f'{identifier}image-upload-widget-input')
        self.remove_button = self.page.get_by_test_id(f'{identifier}-image-upload-widget-remove-button')

    def click_remove_image(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_image_input.set_input_files(file)

    def check_visible(self, is_image_uploaded: bool = False):
        expect(self.image_upload_info_description).to_be_visible()
        expect(self.image_upload_info_description).to_have_text('Recommended file size 540X300')

        expect(self.image_upload_info_tittle).to_be_visible()
        expect(self.image_upload_info_tittle).to_have_text('Tap on "Upload image" button to select file')

        expect(self.image_upload_info_icon).to_be_visible()

        if is_image_uploaded:
            expect(self.preview_image).to_be_visible()
            expect(self.remove_button).to_be_visible()

        else:
            self.preview_empty_view.check_visible(
                tittle='No image selected',
                description='Preview of selected image will be displayed here'
            )