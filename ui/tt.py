import wx


def create(parent):
    return Frame1( parent )


# assign ID numbers
[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1LISTBOX1,
 ] = [wx.NewId() for _init_ctrls in range( 4 )]


class Frame1( wx.Frame ):
    def _init_ctrls(self, prnt):
        # BOA generated methods
        wx.Frame.__init__( self, id=wxID_FRAME1, name='', parent=prnt,
                           pos=wx.Point( 358, 184 ), size=wx.Size( 299, 387 ),
                           style=wx.DEFAULT_FRAME_STYLE, title=u'ListBox Test ...' )
        self.SetClientSize( wx.Size( 291, 347 ) )
        self.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
        self.button1 = wx.Button( id=wxID_FRAME1BUTTON1,
                                  label=u'Load ListBox',
                                  name='button1',
                                  parent=self,
                                  pos=wx.Point( 8, 8 ),
                                  size=wx.Size( 176,28 ),
                                  style=0 )
        self.button1.Bind( wx.EVT_BUTTON, self.OnButton1Button,
                           id=wxID_FRAME1BUTTON1 )
        self.listBox1 = wx.ListBox( choices=[],
                                    id=wxID_FRAME1LISTBOX1,
                                    name='listBox1',
                                    parent=self,
                                    pos=wx.Point( 8, 48 ),
                                    size=wx.Size( 184, 256 ),
                                    style=0 )
        self.listBox1.SetBackgroundColour( wx.Colour( 255, 255, 128 ) )
        self.listBox1.Bind( wx.EVT_LISTBOX,
                            self.OnListBox1Listbox,
                            id=wxID_FRAME1LISTBOX1 )
        self.button2 = wx.Button( id=wxID_FRAME1BUTTON2,
                                  label=u'Clear',
                                  name='button2',
                                  parent=self,
                                  pos=wx.Point( 104, 312 ),
                                  size=wx.Size( 87, 28 ),
                                  style=0 )
        self.button2.Bind( wx.EVT_BUTTON, self.OnButton2Button,
                           id=wxID_FRAME1BUTTON2 )

    def __init__(self, parent):
        self._init_ctrls( parent )

    def OnButton1Button(self, event):
        '''
        click button to load the listbox with names
        '''
        items=['a',
               'b',
               '3']

        self.listBox1.AppendItems(items)
        self.listBox1.Append( "Andreas" )
        self.listBox1.Append( "Erich" )
        self.listBox1.Append( "Udo" )
        self.listBox1.Append( "Jens" )
        self.listBox1.Append( "Bjorn" )
        self.listBox1.Append( "Heidrun" )
        self.listBox1.Append( "Ulla" )
        self.listBox1.Append( "Volger" )
        self.listBox1.Append( "Helmut" )
        self.listBox1.Append( "Freja" )
        self.SetTitle( "Select a name ..." )

    def OnListBox1Listbox(self, event):
        '''
        click list item and display the selected string in frame's title
        '''
        selName = self.listBox1.GetStringSelection()
        self.SetTitle( selName )

    def OnButton2Button(self, event):
        '''
        click button to clear the listbox items
        '''
        self.listBox1.Clear()


# --------------- end of class Frame1 --------------------
# program entry point ...
if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create( None )
    frame.Show()
    app.MainLoop()
