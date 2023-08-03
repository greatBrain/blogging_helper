import docx
import mechanicalsoup as mechsoup


class Uploader:
      def __init__(self):
          self.browser_con = mechsoup.Browser()
          self.file = ''

      def validate(self, file=str, file_extention=tuple):          
          image_formats = [".jpg", ".jpeg", ".png", ".webp"] 
          self.file = file

          if file_extention[1] == '.docx':                           
             self.open_document()

          elif file_extention[1] in image_formats:             
             self.set_img()

      
      def open_document(self):                  
          try:           
            document = docx.Document(self.file)             
            doc_text = [doc_text.append(paragraph.text) for paragraph in document.paragraphs]
            self.fill_fields(doc_text)

          except Exception as e:  
            return ("Something is wrong:", e)  


      
      
      ''' Connecting with browser and getting web html'''
      def get_web_page(self):
          #Test url
          url = "http://olympus.realpython.org/login"
          web_page = self.browser_con.get(url)
          page_html = web_page.soup
          return page_html


      def fill_fields(self, doc_text):
          form = self.get_web_page.select("container")[0]
          form.select("input")[0]["title"] = "zeus"

      def set_img(self):
          pass    