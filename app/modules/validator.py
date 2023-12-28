''' Identifies what kind of file has been found, image or .docx.'''
from modules.formatter import Formatter

class Validator:
      def __init__(self):
          self.blog_entry_file_text = None
          self.blog_entry_image = None
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"] 


      #To know if files encountered are we are expecting for:
      def validate_files(self, file_full_path, file_name_splited=tuple):
          try:               
             for ext in file_name_splited:
                 if ext == '.docx': 
                    self.blog_entry_file_text = file_full_path

                 elif ext in self.IMAGE_FORMATS:
                      self.blog_entry_image = file_full_path                       
            
             self.formatter = Formatter(self.blog_entry_file_text, self.blog_entry_image)
             #self.formatter.classify_text()
             self.formatter.get_response()
         
          except FileNotFoundError as e:           
            raise ("Wrong file, try again.", e)