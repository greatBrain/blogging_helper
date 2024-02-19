from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from app.validator import Validator
import os

class EventHandler(FileSystemEventHandler):
      def on_created(self, event): 
          file_full_path = Path(event.src_path)                             
          file_name_splited = os.path.splitext(Path(event.src_path).name)          
          valid = Validator()
          valid.validate_files(file_full_path, file_name_splited)    
     

class DirObserver:
     def __init__(self):
         self.observer = Observer()   

     def _get_files_dir(self): 
         #Get current dir and after constructs the path where text/images files are.
         current_dir = os.getcwd()
         files_directory = os.path.abspath(os.path.join(current_dir, './files'))

         #Normalizes the path to make it platform independent(on Windows adds \ and Unix Like adds /)
         os.path.normpath(files_directory)
         return files_directory

     
     def run_observer(self, start_signal:True):
         self.observer.schedule(EventHandler(), self._get_files_dir(), recursive=True)

         if start_signal:
            self.observer.start()

     def stop_observer(self, stop_signal:True):
         if stop_signal:
            self.observer.stop()


'''try:
      while self.observer.is_alive():
            self.observer.join(1)
   except Exception as e:
         self.observer.stop()
   self.observer.join()'''