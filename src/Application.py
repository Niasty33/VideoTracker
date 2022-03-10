import tkinter as tk
from models.video import Video 
from views.views import View 
from controllers.controllers import Controller 

class Application(tk.Tk):

    def __init__(self):

        super().__init__()
        self.title('Video Tracker')
        # create a video model
        video = Video()
        # create a view and place it on the root window
        view = View(self)

        # create a controller
        controller = Controller(video, view)

        # set the controller to view
        view.setController(controller)
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()