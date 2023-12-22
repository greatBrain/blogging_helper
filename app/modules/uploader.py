import mechanicalsoup as mechsoup
from file_manager import File_Manager as FM

class Uploader:
      def __init__(self):
          self.browser_con = mechsoup.Browser()                
          self.URL = "https://gid.do/wp-admin/post-new.php"

      ''' Connecting with browser and getting web html'''
      def get_page_body(self):          
          web_page = self.browser_con.get(self.URL)
          page_html = web_page.soup

          return page_html
      
      def fill_text_fields(self, doc_text):
          form = self.get_web_page.select("")[0]          

      # We just upload the image, there's a Tiny plugin installed in the site that optimizes the images automatically.
      def upload_image(self):
          image = FM.get_image()

