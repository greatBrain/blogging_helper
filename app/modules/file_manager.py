import docx

class File_Manager:          
      
      def read_document(self, docx_file):
          try:           
            document_object = docx.Document(docx_file)             
            file_data= [paragraph.text for paragraph in document_object.paragraphs]
            return file_data
            # self.fill_fields(doc_text)

          except Exception as e:  
            return ("Something is wrong:", e)  
          

      def optimize_img(self, img):          
          pass    