import json
import docx

class Formatter:

      def __init__(self, blog_entry_file_text, blog_entry_image):
          
          self._text_file = blog_entry_file_text
          self._image_file = blog_entry_image

          self.json_response = {'category':'', 
                             'title':'',
                             'summary':'',                              
                             'body':'', 
                             'tags':'',
                             'image_url':''
                            }
          
          self.TEXT_STYLES = {         
                  'Heading 3':'Category',         
                  'Heading 2':'Title',                                     
                  'Caption':'Summary',
                  'Body Text':'Body',
                  'Heading 5':'Tags',
                  'Heading 6':'Tags',
               } 

      def run(self):
          pass                    
      
      def get_text(self):
          docx_document_object = docx.Document(self._text_file)    
          return docx_document_object.paragraphs
      
      
      #Filter text by sections and returns it as a generator.
      def classify_text(self):                          
          for item in self.get_text():              
              text_style = item.style.name
              block_text = self.TEXT_STYLES.get(text_style, 'Default Paragraph Style')
              _text_dict = {block_text:item.text}              
              yield _text_dict
              
      
      def get_response(self):                    
           for i in self.classify_text():
               print(i) 
        