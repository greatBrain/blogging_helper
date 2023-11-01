from  modules.file_manager import File_Manager

class Validator:
      def __init__(self):
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]      

      def validate(self, file_full_path, file_name_splited=tuple):  

         try:

            if file_name_splited[1] == '.docx':  
               self.manager = File_Manager(file_full_path)                                           

            elif file_name_splited[1] in self.IMAGE_FORMATS:             
               self.manager = File_Manager(file_full_path)
            return "Just docx and image format accepted"
         
         except Exception as e:           
            raise ("Wrong file, try again.". e)
      