from modules.formatter import Formatter #Provisional
#from modules.response import Json_Response

class Validator:
      def __init__(self):
          self.blog_entry_file_text = None
          self.blog_entry_image = None

          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".JPG", ".JPEG", 
                                ".png", ".PNG", ".webp", ".tiff", ".gif"
                                ]
      
      def validate_files(self, file_full_path, file_name_splited=tuple):
          try:               
             for ext in file_name_splited:
                 if ext == '.docx': 
                    self.blog_entry_file_text = file_full_path

                 elif ext in self.IMAGE_FORMATS:
                      self.blog_entry_image = file_full_path
             
             self.formatter = Formatter(self.blog_entry_file_text, self.blog_entry_image)             
             
             """Running the 'Formatter' class as a function,
             using the __call__ built-in method"""
             self.formatter()             
         
          except FileNotFoundError as e:           
            raise ("Wrong file, try again.", e)