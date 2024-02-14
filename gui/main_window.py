import tkinter
import customtkinter
import os
from PIL import ImageTk, Image
import app.main as main

#### IMPORTING APP MODULE NOT WORKING ####

class MainWindow:
      def __init__(self) -> None:  
           self.mainDir = os.path.dirname(__file__)
           self.imagesDir = os.path.join(self.mainDir, "images")
           self.app = customtkinter.CTk()    
           self.mode = customtkinter.set_appearance_mode("system")
           self.theme = customtkinter.set_default_color_theme("green")
           self.button = object

           #Images in button
           self.turn_off_image = customtkinter.CTkImage(Image.open(os.path.join(self.imagesDir, "turn_off_icon.ico")), size=(155, 155))
           self.turn_on_image = customtkinter.CTkImage(Image.open(os.path.join(self.imagesDir, "turn_on_icon.ico")), size=(155, 155))

      def create_window(self):  
          self.app.title("")  
          #Linux doesn't accept .ico as icon:
          icon = ImageTk.PhotoImage(Image.open(os.path.join(self.imagesDir, "robotic-arm-logo.png")))  
          self.app.wm_iconphoto(True, icon)             
          self.app.geometry("550x400")          
          title_label = customtkinter.CTkLabel(master=self.app, text="Blogging Ayudante", font=("sans", 24))
          title_label.pack(pady = 30)
          self.app.resizable(False, False)          
          self.create_button()


      def create_button(self):
          self.button = customtkinter.CTkButton(master=self.app, 
                                                text="",                                                 
                                                image= self.turn_off_image,    
                                                font=("Arial", 20),
                                                border_spacing=(2),
                                                hover=False,                                                
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                command=self.on_click                                                 
                                            )
          self.button.pack(pady=20, padx=20)
          self.button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    
      def set_app_status(self, text):
          app_status = text
          return app_status

      def on_click(self):
          if self.button._image==self.turn_off_image:
             self.button.configure(image=self.turn_on_image)  
             main.run()           
             
          else:
             self.button.configure(image=self.turn_off_image)

      def run(self):    
          return self.app.mainloop()  


if __name__ == "__main__":
    root = MainWindow()
    root.create_window()
    root.run()