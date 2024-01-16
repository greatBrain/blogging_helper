from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from  modules.validator import Validator
import os

class EventHandler(FileSystemEventHandler):          

      def on_created(self, event):
          file_full_path = Path(event.src_path)                             
          file_name_splited = os.path.splitext(Path(event.src_path).name)          
          validator = Validator()
          validator.validate_files(file_full_path, file_name_splited)    
     

class Main:
     def __init__(self):
         self.observer = Observer()                           
         self.files_directory = "../files"

     def run(self): 
         
         #Normalizes the path to make it platform independent(on Windows adds \ and Unix Like adds /)
         os.path.normpath(self.files_directory) 

         #Monitors each event at current directory: 
         self.observer.schedule(EventHandler(), self.files_directory, recursive=True)
         self.observer.start()

         try:
             while self.observer.is_alive():
                   self.observer.join(1)

         except KeyboardInterrupt:
             self.observer.stop()
         self.observer.join()