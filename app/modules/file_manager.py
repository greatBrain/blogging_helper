import docx
import json

class File_Manager:          
      
      def __init__(self):
          self.data_file = None
          self.image = None

      def read_document(self, _file):
          
          try:           
            document_object = docx.Document(_file)                                      
            
            for item in document_object.paragraphs:

                items = {
                          "text":item.text, 
                          "text_style_name":item.style.name,
                        }
                                          
                json_response = json.dumps(items, indent=2)
                print(json_response)

          except Exception as e:  
            return ("Something is wrong:", e) 

      def set_image(self, image):
          self.image = image

      def get_image(self):
          return self.image