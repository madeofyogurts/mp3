# icons used are from icons8.com
# for the code to work you will need three bitmaps which can be downloaded from github catalog

import wx


def button_creation(path, width, height, parent, position_x, position_y, toggle=False):
    bitmap = wx.Bitmap(path)
    image = bitmap.ConvertToImage()
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.Bitmap(image)
    if not toggle:
        button_created = wx.BitmapButton(parent, pos=(position_x, position_y), size=(height, width), bitmap=result)
    else:
        button_created = wx.BitmapToggleButton(parent, pos=(position_x, position_y), size=(height, width), label=result)
    return button_created


def label_creation(parent, user_text, fontsize):
    label_created = wx.StaticText(parent, style=wx.ALIGN_CENTER)
    label_text = str(user_text)
    font = wx.Font(int(fontsize), wx.SWISS, wx.NORMAL, wx.NORMAL)
    label_created.SetFont(font)
    label_created.SetLabel(label_text)
    return label_created

class MyFrame(wx.Frame):
    def __init__(self):

        super().__init__(parent=None, title="MP3 Player")
        panel = wx.Panel(self)

        lbl1 = label_creation(panel, "\n\tNow playing from", 18)
        lbl2 = label_creation(panel, "\n\n\n\tTwoja Stara", 14)

        test_button = button_creation("icon_backward.png", 50, 50, panel, 50, 100)
        play_button = button_creation("icon_play.png", 70, 70, panel, 120, 90, toggle=True)
        forward_button = button_creation("icon_forward.png", 50, 50, panel, 210, 100)

        self.Show()

app = wx.App()
frame = MyFrame()
app.MainLoop()
