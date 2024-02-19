import tkinter
import customtkinter
import os
from PIL import ImageTk, Image
from app import observer


class MainWindow:
      def __init__(self) -> None:  
           self.mainDir = os.path.dirname(__file__)
           self.imagesDir = os.path.join(self.mainDir, "images")
           self.app = customtkinter.CTk()    
           self.mode = customtkinter.set_appearance_mode("dark")
           self.theme = customtkinter.set_default_color_theme("green")
           self.button = object

           #Images in button
           self.turn_off_image = customtkinter.CTkImage(Image.open(os.path.join(self.imagesDir, "turned_off.png")), size=(150, 150))
           self.turn_on_image = customtkinter.CTkImage(Image.open(os.path.join(self.imagesDir, "turned_on.png")), size=(150, 150))

           self.observer = observer.DirObserver()

      def create_window(self) -> None:  
          self.app.title("")  
          icon = ImageTk.PhotoImage(Image.open(os.path.join(self.imagesDir, "robotic-arm-logo.png"))) #Linux doesn't accept .ico as icon:
          self.app.wm_iconphoto(True, icon)             
          self.app.geometry("480x650")          
          title_label = customtkinter.CTkLabel(master=self.app, text="Blogger", font=("sans", 24))
          title_label.pack(pady = 40)
          self.app.resizable(False, False)          
          self.create_button()


      def create_button(self) -> None:
          self.button = customtkinter.CTkButton(master=self.app, 
                                                text="",                                                 
                                                image= self.turn_off_image,                                                    
                                                hover=False,                                                
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                command=self.on_click                                                 
                                            )
          self.button.pack(pady=20, padx=20)
          self.button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


      def on_click(self):
          signal = True #To start/stop observer

          if self.button._image==self.turn_off_image:
             self.button.configure(image=self.turn_on_image)               
             self.observer.run_observer(signal)
             
          else:
             self.button.configure(image=self.turn_off_image)
             self.observer.stop_observer(signal)