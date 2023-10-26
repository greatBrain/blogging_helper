from modules import observer


if __name__=='__main__':
   observer_instance = observer.Main()

   try:
      observer_instance.run()
                     
   except ExceptionGroup:
         pass