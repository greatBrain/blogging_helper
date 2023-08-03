from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from uploader import Uploader
import os

class EventHandler(FileSystemEventHandler):
      
      def __init__(self):
          pass         

      def on_created(self, event):                             
          file_name = Path(event.src_path).name          
          file_extention = os.path.splitext(file_name)
          Uploader.validate(file_name, file_extention)              


class Main:
     def __init__(self):
         self.observer = Observer()

     def run(self):
         #Monitors all events in current directory: 
         self.observer.schedule(EventHandler(), ".", recursive=True)
         self.observer.start()

         try:
             while self.observer.is_alive():
                   self.observer.join(1)

         except KeyboardInterrupt:
             self.observer.stop()
         self.observer.join()

if __name__=='__main__':
   Main().run()
