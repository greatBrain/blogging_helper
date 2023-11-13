import docx
import modules.helpers as helpers
#import tinify #Tiny PNG API

class File_Manager:          
      
      def __init__(self) -> None:
          self.data_file = None
          self.image = None

      def read_document(self, _file):
          try:           
            document_object = docx.Document(_file)             
            self.data_file = [paragraph.text for paragraph in document_object.paragraphs]
            return self.data_file          

          except Exception as e:  
            return ("Something is wrong:", e)    


      def set_image(self, image):
          self.image = image  


      def get_image(self):
          return self.image
      

      #Instead optimizing the images at local, i installed the Tiny optimizer in the site.

      '''def optimize_img(self, img_full_name, extension):          
          try:
              tinify.key = helpers.get_tinify_api() 
              optimized_image = tinify.from_file(img_full_name).to_file(os.path.join(self.files_directory, "image_optimized{}".format(extension)))                                         
              return True              
              
          except ConnectionError as  e:
                 raise "Connection error: %s" % e.message'''
        
      