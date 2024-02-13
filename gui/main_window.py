import tkinter
import customtkinter
import os
from PIL import ImageTk, Image

class MainWindow:
      def __init__(self) -> None:  
           self.mainDir = os.path.dirname(__file__)
           self.imagesDir = os.path.join(self.mainDir, "images")
           self.app = customtkinter.CTk()    
           self.mode = customtkinter.set_appearance_mode("system")
           self.theme = customtkinter.set_default_color_theme("green")
           self.button = object

      def create_window(self):  
          self.app.title("")  
          #Linux doesn't accept .ico as icon:
          icon = ImageTk.PhotoImage(Image.open(os.path.join(self.imagesDir, "robotic-arm-logo.png")))  
          self.app.wm_iconphoto(True, icon)             
          self.app.geometry("550x400")
          title_label = customtkinter.CTkLabel(master=self.app, text="Auto Blogger", font=("Arial", 23))
          title_label.pack(pady = 50)
          self.app.resizable(False, False)          
          self.create_button()


      def create_button(self):
          self.button = customtkinter.CTkButton(master=self.app, 
                                                text="",                                                 
                                                image= customtkinter.CTkImage(
                                                    Image.open(os.path.join(self.imagesDir, "turn_off_icon.ico")),
                                                    size=(125, 125)
                                                ),     
                                                font=("Arial", 20),
                                                border_spacing=(2),
                                                hover=False,                                                
                                                fg_color="transparent",
                                                bg_color="transparent",
                                                command=self.on_click
                                            )
          self.button.pack(pady=20, padx=20)
          self.button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

      def on_click(self):
          if self.button._image=="turn_off_icon.ico":
             print("SAluuudo")

      def run(self):    
          return self.app.mainloop()  


if __name__ == "__main__":
    root = MainWindow()
    root.create_window()
    root.run()



''' 
#frame_button = customtkinter.CTkFrame(master=self.app, corner_radius=10)
#frame_button.pack(pady=30, padx=30, fill="both", expand=True)
'''

#Logo image:
'''logo = customtkinter.CTkImage(
           Image.open(os.path.join(self.imagesDir, "robotic-arm-logo.png")),
           size=(150, 150)
          )'''
#Label that contains the logo image
'''logo_label = customtkinter.CTkLabel(master=self.app, image=logo, text="")
logo_label.pack(pady = 50)'''