''' Identifies what kind of file has been found, image or .docx.'''

from modules.file_manager import File_Manager
from modules.text_tager import Tager

class Validator:
      def __init__(self):
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]      
          self.manager = File_Manager()

      def validate_files(self, file_full_path, file_name_splited=tuple):  

         try:

            if file_name_splited[1] == '.docx':                 
               self.manager.set_data_document(file_full_path)

               #Just for trial purposes
               '''for i in self.manager.get_data_document():
                   print(i)'''
               
               self.manager.get_data_document()

            elif file_name_splited[1] in self.IMAGE_FORMATS:                            
               self.manager.set_image_file(file_full_path)     

            return "Just .docx or an image format is allowed."
         
         except FileNotFoundError as e:           
            raise ("Wrong file, try again.", e)