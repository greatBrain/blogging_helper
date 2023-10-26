import docx
import mechanicalsoup as mechsoup

class Uploader:
      def __init__(self):
          self.browser_con = mechsoup.Browser()                
          self.BLOG_URL = ""          


      ''' Connecting with browser and getting web html'''
      async def get_web_page(self):          
          web_page = self.browser_con.get(self.BLOG_URL)
          page_html = web_page.soup
          return page_html     

      
      async def fill_fields(self, doc_text):
          form = self.get_web_page.select("container")[0]
          form.select("input")[0]["title"] = "zeus"
          