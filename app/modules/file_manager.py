import docx

class File_Manager:          
      
      async def open_document(self, document):
          try:           
            document = docx.Document(self.file)             
            doc_text = [doc_text.append(paragraph.text) for paragraph in document.paragraphs]
            self.fill_fields(doc_text)

          except Exception as e:  
            return ("Something is wrong:", e)  
          

      async def optimize_img(self, img):          
          pass    