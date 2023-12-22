from modules.file_manager import File_Manager
import json

class Tager:

      def __init__(self):   

          self.file_manager = File_Manager()  

          self.TEXT_STYLES = {
                  'Heading 1':'Title', 
                  'Heading 2':'Title', 
                  'Heading 3':'Title',
                  'Caption':'Summary',
                  'Body Text':'Body',
                  'Endnote':'Footer',
               }
                         
          
          self.json_object = {'category':'', 
                             'title':'',
                             'summary':'',                              
                             'body':'', 
                             'tags':'',
                             'image_url':''
                            }
      
      #Calls function get_data_document from file_manager module, as a generator. 
      def classify_text(self):
          for item in self.file_manager.get_data_document.paragraphs:
              text_style = item.style.name
              block_text = self.TEXT_STYLES.get(text_style, 'Default Paragraph Style')
              print(f'{block_text}: {item.text}')
              print("\n")