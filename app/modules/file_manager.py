import docx

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
     
     
      def optimize_img(self, img):          
          pass    