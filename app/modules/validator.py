from  modules.file_manager import File_Manager

class Validator:
      def __init__(self):
          self.IMAGE_FORMATS = [".jpg", ".jpeg", ".png", ".webp", ".tiff", ".gif"]      
          self.manager = File_Manager() 


      def validate_files(self, file_full_path, file_name_splited=tuple):  

         try:

            if file_name_splited[1] == '.docx':                 
               self.manager.read_document(file_full_path)

            elif file_name_splited[1] in self.IMAGE_FORMATS:             
               #Instead optimizing the images at local, i installed the Tiny optimizer in the site.
               #self.manager.optimize_img(file_full_path, file_name_splited[1])
               self.manager.set_image(file_full_path)               

            return "Just .docx or an image format is accepted."
         
         except FileNotFoundError as e:           
            raise ("Wrong file, try again.", e)