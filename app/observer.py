from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from app.validator import Validator
import os
from threading import Event
import app.helpers as help


class EventHandler(FileSystemEventHandler):
      def on_created(self, event): 
          file_full_path = Path(event.src_path)                             
          file_name_splited = os.path.splitext(Path(event.src_path).name)          
          valid = Validator()
          valid.validate_files(file_full_path, file_name_splited)

class DirObserver:
     def __init__(self):
         self.observer = Observer()

         # Signal the thread to stop:    
         self.thread_event = Event() 

     def _get_files_dir(self):          
         current_dir = os.getcwd()
         files_directory = os.path.abspath(os.path.join(current_dir, './files'))

         if help.check_dir_exists(files_directory):
            #Normalizes the path to make it platform 
            #independent(on Windows adds \ and Unix Like adds /)
            os.path.normpath(files_directory)
            return files_directory
        
     
     def run_observer(self):
         # Check if the thread is not already running:
         if not self.thread_event.is_set():
            self.observer.schedule(EventHandler(), self._get_files_dir(), recursive=True)
            print("Running")
            self.observer.start()

     def stop_observer(self):
         self.observer.stop() #Stop the observer
         self.observer.join() # Waits for the observer to finish
         self.thread_event.set() # Stop the threading   
         self.thread_event.clear()
         print("Stopped") 
          