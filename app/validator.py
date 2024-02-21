from app.formatter import Formatter

class Validator:
      def __init__(self):        
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".JPG", ".JPEG",".png", ".PNG", ".webp", ".tiff", ".gif"]

      def validate_files(self, file_absolute_path, file_name_splited=tuple):
          try:
             blog_entry_file_text:str=''
             blog_entry_image:str=''
             
             for ext in file_name_splited:
                 if ext == '.docx': 
                    blog_entry_file_text = file_absolute_path

                 elif ext in self.IMAGE_FORMATS:
                    blog_entry_image = file_absolute_path             
             
             if (blog_entry_file_text is not None) and (blog_entry_image is not None):
                formatter = Formatter(blog_entry_file_text, blog_entry_image)
                formatter() #Instance called as a method        


             '''if blog_entry_file_text is not None:
                formatter = Formatter(blog_entry_file_text)
                formatter() '''
         
          except FileNotFoundError as e:           
             raise ("Wrong file, try again.", e)