from  modules.file_manager import File_Manager

class Validator:
      def __init__(self):
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]      
          self.manager = File_Manager() 

      def validate_files(self, file_full_path, file_name_splited=tuple):  

         try:

            if file_name_splited[1] == '.docx':  
               print(self.manager.read_document(file_full_path))

            elif file_name_splited[1] in self.IMAGE_FORMATS:             
               print(self.manager.optimize_img(file_full_path, file_name_splited[1]))

            return "Just .docx or image format accepted"
         
         except FileNotFoundError as e:           
            raise ("Wrong file, try again.", e)