import docx
from  modules.file_manager import File_Manager

class Validator:
      def __init__(self):
          self.image_formats = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]
          self.manager = File_Manager()

      
      def validate(self, file):
          
          if file[1] == '.docx':                           
             self.manager.open_document()

          elif file[1] in self.image_formats:             
             self.manager.optimize_img()

          return "Extension de archivo incorrecta."