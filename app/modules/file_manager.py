import docx
import modules.helpers as helpers
import tinify #Tiny PNG API

class File_Manager:          
      
      def __init__(self) -> None:
          self.data_file = None

      def read_document(self, _file):
          try:           
            document_object = docx.Document(_file)             
            self.data_file = [paragraph.text for paragraph in document_object.paragraphs]
            return self.data_file          

          except Exception as e:  
            return ("Something is wrong:", e)         
      
      def optimize_img(self, img_full_name, extension):          
          try:
              tinify.key = helpers.get_tinify_api() 
              optimized_image = tinify.from_file(img_full_name).to_file("image_optimized{}".format(extension))             
              
              #return optimized_image
              return True
              
              
          except ConnectionError as  e:
                 raise "Connection error: %s" % e.message