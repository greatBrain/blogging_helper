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
          validator.validate(file_full_path, file_name_splited)

class Main:
     def __init__(self):
         self.observer = Observer()         

     def run(self):
         
         #Monitors each event at current directory: 
         self.observer.schedule(EventHandler(), "../files", recursive=True)
         self.observer.start()

         try:
             while self.observer.is_alive():
                   self.observer.join(1)

         except KeyboardInterrupt:
             self.observer.stop()
         self.observer.join()