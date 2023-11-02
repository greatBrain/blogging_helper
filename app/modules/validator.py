from  modules.file_manager import File_Manager

class Validator:
      def __init__(self):
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]      
          self.manager = File_Manager() 

      def validate(self, file_full_path, file_name_splited=tuple):  

         try:

            if file_name_splited[1] == '.docx':  
               print(self.manager.read_document(file_full_path))

            elif file_name_splited[1] in self.IMAGE_FORMATS:             
               self.manager.optimize_img()

            return "Just docx and image format accepted"
         
         except Exception as e:           
            raise ("Wrong file, try again.". e)
      