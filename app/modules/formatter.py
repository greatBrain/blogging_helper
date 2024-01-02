import json
import docx
import time

class Formatter:

      def __init__(self, blog_entry_file_text, blog_entry_image):
          self._text_file = blog_entry_file_text
          self._image_file = blog_entry_image
          
          self.TEXT_STYLES = {         
                  'Heading 3':'Category',         
                  'Heading 2':'Title',                                     
                  'Caption':'Summary',
                  'Body Text':'Body',
                  'Heading 5':'Tags',
                  'Heading 6':'Tags',
                }
      
      def _get_text_from_file(self):          
          return docx.Document(self._text_file).paragraphs
      
      #Filtering text by blocks.
      def _classify_text(self):   
          yield list(map(lambda item : {self.TEXT_STYLES.get(item.style.name, 'Default Paragraph Style'): item.text}, self._get_text_from_file()))
      
      
      def _get_formatted_text(self):
          
          body_text = {}

          for index, item in enumerate(self._classify_text()):              
              return item
              
      
      def get_response(self):                    
          print(self._get_formatted_text())
      
      def run(self):
          self.get_response()
         
      
      __call__ = run
      #To be executed from the Validator class.         