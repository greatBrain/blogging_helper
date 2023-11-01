import docx

class File_Manager:          
      
      def __init__(self, data_file) -> None:
          self.data_file = data_file

      def read_document(self):
          try:           
            document_object = docx.Document(self.data_file)             
            docx_file_text = [paragraph.text for paragraph in document_object.paragraphs]
            return docx_file_text            

          except Exception as e:  
            return ("Something is wrong:", e)          
      
      def _cache_data(self):
          pass
          

      def optimize_img(self, img):          
          pass    