from gui import main_window

def run_app():
    window = main_window.MainWindow()
    window.create_window()
    window.app.mainloop()

if __name__ == "__main__":
   run_app()