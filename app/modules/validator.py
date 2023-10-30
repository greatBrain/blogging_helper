from  modules.file_manager import File_Manager

class Validator:
      def __init__(self):
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]
          self.manager = File_Manager()
          #self.file_full_path = file_full_path 
          #self.file_name_splited = file_name         
      

      def validate(self, file_full_path, file_name_splited=tuple):          
          
          if file_name_splited[1] == '.docx':                           
             #self.manager.open_document(file_full_path)
             print("Halo")

          elif file_name_splited[1] in self.IMAGE_FORMATS:             
             #self.manager.optimize_img(file_full_path)
             print("Halo-2")

          return "Extension de archivo incorrecta."
      