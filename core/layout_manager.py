# layout_manager.py

class LayoutManager:
    def __init__(self):
        pass

    def _create_title_slide(self, presentation, title, subtitle):
        """
        Create a title slide with the given title and subtitle.
        """
        print(f"Creating title slide with title: {title} and subtitle: {subtitle}")
        slide_layout = presentation.slide_layouts[0]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = subtitle

    def _create_title_and_content_slide(self, presentation, title, content):
        """
        Create a title and content slide with the given title and content.
        """
        print(f"Creating title and content slide with title: {title}")
        slide_layout = presentation.slide_layouts[1]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = content

    def _create_section_header_slide(self, presentation, title, body):
        """
        Create a section header slide with the given title and body text.
        """
        print(f"Creating section header slide with title: {title}")
        slide_layout = presentation.slide_layouts[2]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = body

    def _create_two_content_slide(self, presentation, title, content_left, content_right):
        """
        Create a two-content slide with the given title and content.
        """
        print(f"Creating two content slide with title: {title}")
        slide_layout = presentation.slide_layouts[3]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = content_left
        slide.placeholders[2].text = content_right

    def _create_comparison_slide(self, presentation, title, text_left, content_left, text_right, content_right):
        """
        Create a comparison slide with the given title and content.
        """
        print(f"Creating comparison slide with title: {title}")
        slide_layout = presentation.slide_layouts[4]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = text_left
        slide.placeholders[2].text = content_left
        slide.placeholders[3].text = text_right
        slide.placeholders[4].text = content_right

    def _create_title_only_slide(self, presentation, title):
        """
        Create a title-only slide with the given title.
        """
        print(f"Creating title-only slide with title: {title}")
        slide_layout = presentation.slide_layouts[5]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title

    def _create_blank_slide(self, presentation):
        """
        Create a blank slide.
        """
        print(f"Creating blank slide")
        slide_layout = presentation.slide_layouts[6]
        slide = presentation.slides.add_slide(slide_layout)

    def _create_content_with_caption_slide(self, presentation, title, content, caption):
        """
        Create a content with caption slide with the given title, content, and caption.
        """
        print(f"Creating content with caption slide with title: {title}")
        slide_layout = presentation.slide_layouts[7]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = content
        slide.placeholders[2].text = caption

    def _create_picture_with_caption_slide(self, presentation, title, picture, caption):
        """
        Create a picture with caption slide with the given title, picture, and caption.
        """
        print(f"Creating picture with caption slide with title: {title}")
        slide_layout = presentation.slide_layouts[8]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].insert_picture(picture)
        slide.placeholders[2].text = caption

    def _create_title_and_vertical_text_slide(self, presentation, title, vertical_text):
        """
        Create a title and vertical text slide with the given title and vertical text.
        """
        print(f"Creating title and vertical text slide with title: {title}")
        slide_layout = presentation.slide_layouts[9]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = title
        slide.placeholders[1].text = vertical_text

    def _create_vertical_title_and_text_slide(self, presentation, vertical_title, vertical_text):
        """
        Create a vertical title and text slide with the given vertical title and text.
        """
        print(f"Creating vertical title and text slide with title: {vertical_title}")
        slide_layout = presentation.slide_layouts[10]
        slide = presentation.slides.add_slide(slide_layout)
        slide.shapes.title.text = vertical_title
        slide.placeholders[1].text = vertical_text
