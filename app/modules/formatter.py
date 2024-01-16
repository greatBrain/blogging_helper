import json
import docx
import time

class Formatter:

      def __init__(self, blog_entry_file_text, blog_entry_image):
          self._text_file = blog_entry_file_text

          self.image = blog_entry_image
          
          self.TEXT_STYLES = {         
                  'Heading 3':'Category',         
                  'Heading 2':'Title',                                     
                  'Caption':'Summary',
                  'Body Text':'Body',
                  'Heading 5':'Tags',
                  'Heading 6':'Tags',
                }
      
      def _get_text_from_file(self):          
          return docx.Document(self._text_file).paragraphs
      
      #Filtering text by blocks.
      def _classify_text(self):   
          #In a refactor, this function will be 
          #converted into a generator, for more speed and scalabillity:
          #yield list(map(lambda item : {self.TEXT_STYLES.get(item.style.name, 'Default Paragraph Style'): item.text}, self._get_text_from_file()))
          return list(map(lambda item : {self.TEXT_STYLES.get(item.style.name, 'Default Paragraph Style'): item.text}, self._get_text_from_file()))
      
      
      def _format_text(self):          
          data = self._classify_text()
          formatted_body_text = []

          #When while loop starts, this will be set to 0.
          index_counter = -1          

          while index_counter <= len(data): 
                index_counter +=1                              

                for item in data:
                   if item.get('Body'):
                      if item['Body']=="": 
                         data.remove(item)                                                                                             
                      formatted_body_text.append(item['Body'])                      
                      data.remove(item)


          #if self.image!=None:
          data.append({'Body':formatted_body_text})
          data.append(self.image)
          json_obj = json.dumps(data, indent=4)
          with open('data.json', 'w') as json_file:
              json_file.write(json_obj)


      def get_response(self):  
                            
          self._format_text()
      
      def run(self):
          self.get_response()         
      
      __call__ = run
      #To be executed from the Validator class.         