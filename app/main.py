from modules import observer

class Main:
      def __init__(self) -> None:
          self.observer_instance = observer.Main()   

      def run(self):
         try:            
            self.observer_instance.run()
         except RuntimeError as e:
            raise("Failed to run the program.", e)