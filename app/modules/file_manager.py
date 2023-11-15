import docx
#import json

class File_Manager:          
      
      def __init__(self):
          self.data_file = None
          self.image_file = None


      def set_data_docuement(self, data_file):
          self.data_file = data_file


      def set_image_file(self, image_file):
          self.image_file = image_file


      def get_data_document(self):                
          document_object = docx.Document(self.data_file)

          for item in document_object.paragraphs:
              items = {"text":item.text, "text_style_name":item.style.name}              
              yield items

      def get_image(self):
          return self.image