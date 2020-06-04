import wx
import pygame
import wx.media
import os
import tkinter
from tkinter.filedialog import askdirectory

path = ""
while path == "":
    path = askdirectory(title = "Select your music folder")
print("Your music folder location: ", path)

playlist = []
for (path, subdirs, files) in os.walk(path):
    for f in files:
        if ".mp3" in f:
            playlist.append(path + "/" + f)
playlist.sort()
m = 0
print("Your playlist:")
while m < len(playlist):
    print(playlist[m])
    m += 1

pygame.mixer.init()
def bitmap_button_creation(path, width, height, parent, position_x, position_y, toggle=False):
    bitmap = wx.Bitmap(path)
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.Bitmap(image)
    if not toggle:
        button_created = wx.BitmapButton(parent, pos=(position_x, position_y), size=(height, width), bitmap=result)

    else:
        button_created = wx.BitmapToggleButton(parent, pos=(position_x, position_y), size=(height, width), label=result)
    return button_created


def label_creation(parent, user_text, fontsize, position_x, position_y, color, weight=False):
    label_created = wx.StaticText(parent, style=wx.ALIGN_CENTER, pos=(position_x, position_y))
    label_text = str(user_text)
    if not weight:
        label_weight = wx.NORMAL
    elif weight == "bold":
        label_weight = wx.BOLD
    elif weight == "light":
        label_weight = wx.LIGHT
    font = wx.Font(int(fontsize), wx.SWISS, wx.NORMAL, label_weight)
    label_created.SetForegroundColour(color)
    label_created.SetFont(font)
    label_created.SetLabel(label_text)
    return label_created


class MyFrame(wx.Frame):
    def __init__(self):

        super().__init__(parent=None, title='MP3 Player', size=(800, 300))
        panel= MyPanel(self)
        self.SetBackgroundColour('#ffffff')
        pygame.mixer.init()
        self.Show()

n = 0

class MyPanel(wx.Panel):

    def __init__(self, parent):
        """Constructor"""
        #super(self,parent).__init__()

        wx.Panel.__init__(self, parent)


        playing_from_label = label_creation(self, 'NOW PLAYING FROM', 13, 99, 54, '#707070')
        user_whereabouts_label = label_creation(self, 'Twoja Stara in Desktop', 17, 99, 79, '#FF2D55')

        song_title_label = label_creation(self, 'Song Title', 22, 99, 123, '#000000', 'bold')
        artist_label = label_creation(self, 'Artist Name', 17, 99, 157, '#707070')

        time_from_beginning_label = label_creation(self, '06:15', 11, 99, 217, '#FF2D55')
        song_length_label = label_creation(self, '21:37', 11, 391, 217, '#FF2D55')
        # --------------------------------------

        # RIGHT SIDE WITH BUTTONS

        change_folder_button = wx.Button(self, label='CHANGE FOLDER', pos=(510, 54), size=(183, 36))

        test_button = bitmap_button_creation('icon_backward.png', 40, 40, self, 510, 130)
        play_button = bitmap_button_creation('icon_play.png', 80, 80, self, 560, 110, toggle=True)
        play_button.Bind(wx.EVT_TOGGLEBUTTON, self.onToggle)

        forward_button = bitmap_button_creation('icon_forward.png', 40, 40, self, 650, 130)
        dark_mode_button= bitmap_button_creation('icon_play.png',20,20,self,50,50, toggle=True)
        dark_mode_button.Bind(wx.EVT_TOGGLEBUTTON, self.change_background_color)
        slider = wx.Slider(self, 5, 6, 1, 100, (149, 217), (200, -1))
        slider.Bind(wx.EVT_ENTER_WINDOW, self.slider_work, id=5)

        self.Show()

    # ICONS=["play.png", "stop.png"]
    # X=[1,0]
    # self.toggle=0
    # def OnSetIcon(self, path):
    #     icon = wx.Icon(path)
    #     self.SetIcon(icon, path)
    #     self.toggle=X[self.toggle]



    def change_background_color(self, event):
        btn = event.GetEventObject()
        if btn.GetValue():
            self.SetBackgroundColour("medium grey")
            self.Refresh()
        else:
            self.SetBackgroundColour("#ffffff")
            self.Refresh()

    def forward_button_work(self,event):
        n += 1
        pygame.mixer.music.load(playlist[n])
        pygame.mixer.music.play()

    def slider_work(self, event):
        current_vol=pygame.mixer.music.get_volume()
        volume=int(current_vol)
        pygame.mixer.music.set_volume(volume)

    def onToggle(self, event):
        """"""
        # ICONS=["play.png", "stop.png"]
        # X=[1,0]
        # self.toggle=0
        # def OnSetIcon(self, path):
        #     icon = wx.Icon(path)
        #     self.SetIcon(icon, path)

        btn = event.GetEventObject()

        if pygame.mixer.music.get_busy():
            if btn.GetValue():
                #self.toggleBtn.SetBitmap(self.print_ico)
                #nowa_icona=changing_icon_play_pause(btn, stop_icon)
                #pygame.mixer.music.load("this_fear.wav")
                pygame.mixer.music.unpause()


                #use_icon = ICONS[self.toggle]

            else:
                pygame.mixer.music.pause()
        else:
            if btn.GetValue():
                #self.toggleBtn.SetBitmap(self.print_ico)

                pygame.mixer.music.load(playlist[n])
                pygame.mixer.music.play()

            else:
                pygame.mixer.music.pause()



        #def changing_icon_play_pause(odl_button, new_icon):
            # new_button = bitmap_button_creation(new_icon,80, 80, self, 560, 110, toggle=True)
            # old_button = new_button
            # return new_button


class MyApp(wx.App):
    def OnInit(self):
        self.frame= MyFrame(parent=None, title= "Panel Widow")
        self.frame.Show()

        return True

app = wx.App()
frame = MyFrame()
app.MainLoop()
