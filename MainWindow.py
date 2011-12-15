#Boa:Frame:Frame1

import wx
import wx.lib.masked.textctrl
import wx.stc
import wx.richtext
import os
import Mail

wildcard = "PDF Document(*.pdf)|*.pdf|" \
            "All files (*.*)|*.*"
currentDirectory = os.getcwd()
            
def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON5, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, 
 wxID_FRAME1STATICBOX3, wxID_FRAME1STATICBOX4, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT12, 
 wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5, 
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8, 
 wxID_FRAME1STATICTEXT9, wxID_FRAME1STYLEDTEXTCTRL1, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL10, wxID_FRAME1TEXTCTRL11, wxID_FRAME1TEXTCTRL12, 
 wxID_FRAME1TEXTCTRL13, wxID_FRAME1TEXTCTRL14, wxID_FRAME1TEXTCTRL2, 
 wxID_FRAME1TEXTCTRL3, wxID_FRAME1TEXTCTRL4, wxID_FRAME1TEXTCTRL5, 
 wxID_FRAME1TEXTCTRL6, wxID_FRAME1TEXTCTRL7, wxID_FRAME1TEXTCTRL8, 
 wxID_FRAME1TEXTCTRL9, 
] = [wx.NewId() for _init_ctrls in range(38)]

class Frame1(wx.Frame):
    login_id=""
    pswd= ""
        
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(406, 25), size=wx.Size(741, 623),
              style=wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL,
              title='Mobile Bill Calculator & Mailer')
        self.SetClientSize(wx.Size(725, 585))
        self.Show(True)
        self.Bind(wx.EVT_BUTTON, self.calculate, id=wxID_FRAME1BUTTON1)
        self.Bind(wx.EVT_BUTTON, self.clear, id=wxID_FRAME1BUTTON2)
        self.Bind(wx.EVT_BUTTON, self.send_mail, id=wxID_FRAME1BUTTON3)
        self.Bind(wx.EVT_BUTTON, self.open_file, id=wxID_FRAME1BUTTON5)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Total amount', name='staticText1', parent=self,
              pos=wx.Point(80, 48), size=wx.Size(64, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='My data/SMS usage charges', name='staticText2',
              parent=self, pos=wx.Point(16, 80), size=wx.Size(137, 13),
              style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label="His SMS usage charges", name='staticText3', parent=self,
              pos=wx.Point(24, 112), size=wx.Size(128, 13), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label="His data usage charges", name='staticText4', parent=self,
              pos=wx.Point(24, 144), size=wx.Size(130, 13), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label='Previous Balance', name='staticText5', parent=self,
              pos=wx.Point(72, 176), size=wx.Size(82, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(168, 40), size=wx.Size(72, 21), style=0,
              value='')

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(168, 72), size=wx.Size(72, 21), style=0,
              value='')

        self.textCtrl3 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL3, name='textCtrl3',
              parent=self, pos=wx.Point(168, 104), size=wx.Size(72, 21),
              style=0, value='')

        self.textCtrl4 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL4, name='textCtrl4',
              parent=self, pos=wx.Point(168, 140), size=wx.Size(72, 21),
              style=0, value='15')

        self.textCtrl5 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL5, name='textCtrl5',
              parent=self, pos=wx.Point(168, 173), size=wx.Size(72, 21),
              style=0, value='')

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='Enter data', name='staticBox1', parent=self,
              pos=wx.Point(8, 16), size=wx.Size(240, 192), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2, label='Amount',
              name='staticBox2', parent=self, pos=wx.Point(280, 16),
              size=wx.Size(232, 192), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label="Each Person's call charges", name='staticText6',
              parent=self, pos=wx.Point(288, 48), size=wx.Size(126, 13),
              style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label="My total amount", name='staticText7', parent=self,
              pos=wx.Point(336, 80), size=wx.Size(80, 13), style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label="His total amount", name='staticText8', parent=self,
              pos=wx.Point(336, 112), size=wx.Size(80, 13), style=0)

        self.textCtrl6 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL6, name='textCtrl6',
              parent=self, pos=wx.Point(424, 47), size=wx.Size(72, 21), style=0,
              value='')

        self.textCtrl7 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL7, name='textCtrl7',
              parent=self, pos=wx.Point(424, 80), size=wx.Size(72, 21), style=0,
              value='')

        self.textCtrl8 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL8, name='textCtrl8',
              parent=self, pos=wx.Point(424, 112), size=wx.Size(72, 21),
              style=0, value='')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='Calculate',
              name='button1', parent=self, pos=wx.Point(184, 224),
              size=wx.Size(75, 23), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='Clear',
              name='button2', parent=self, pos=wx.Point(288, 224),
              size=wx.Size(75, 23), style=0)

        self.styledTextCtrl1 = wx.stc.StyledTextCtrl(id=wxID_FRAME1STYLEDTEXTCTRL1,
              name='styledTextCtrl1', parent=self, pos=wx.Point(16, 272),
              size=wx.Size(504, 232), style=0)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='Send Mail',
              name='button3', parent=self, pos=wx.Point(576, 392),
              size=wx.Size(75, 23), style=0)

        self.textCtrl9 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL9, name='textCtrl9',
              parent=self, pos=wx.Point(576, 296), size=wx.Size(116, 21),
              style=0, value='')

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9, label='To',
              name='staticText9', parent=self, pos=wx.Point(552, 304),
              size=wx.Size(16, 16), style=0)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label='Subject', name='staticText10', parent=self,
              pos=wx.Point(536, 344), size=wx.Size(37, 13), style=0)

        self.textCtrl10 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL10,
              name='textCtrl10', parent=self, pos=wx.Point(576, 336),
              size=wx.Size(116, 21), style=0, value='')

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label='User Name', name='staticText11', parent=self,
              pos=wx.Point(600, 96), size=wx.Size(53, 13), style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3, label='Login',
              name='staticBox3', parent=self, pos=wx.Point(536, 16),
              size=wx.Size(176, 184), style=0)

        self.textCtrl11 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL11,
              name='textCtrl11', parent=self, pos=wx.Point(544, 112),
              size=wx.Size(160, 21), style=0, value='')

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label='Password', name='staticText12', parent=self,
              pos=wx.Point(600, 152), size=wx.Size(47, 13), style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label='Send Mail', name='staticBox4', parent=self, pos=wx.Point(8,
              248), size=wx.Size(696, 320), style=0)

        self.textCtrl12 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL12,
              name='textCtrl12', parent=self, pos=wx.Point(544, 168),
              size=wx.Size(160, 21), style=wx.TE_PASSWORD, value='')

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label='Attachment', name='staticText13', parent=self,
              pos=wx.Point(24, 512), size=wx.Size(57, 13), style=0)

        self.textCtrl13 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL13,
              name='textCtrl13', parent=self, pos=wx.Point(24, 528),
              size=wx.Size(240, 21), style=0, value='')

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label='Browse',
              name='button5', parent=self, pos=wx.Point(272, 528),
              size=wx.Size(75, 23), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label='From', name='staticText14', parent=self, pos=wx.Point(608,
              40), size=wx.Size(25, 13), style=0)

        self.textCtrl14 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL14,
              name='textCtrl14', parent=self, pos=wx.Point(544, 56),
              size=wx.Size(160, 21), style=0, value='')

    def calculate(self,e):
        total= float(self.textCtrl1.GetValue())
        my_sms= float(self.textCtrl2.GetValue())
        his_sms= float(self.textCtrl3.GetValue())
        his_data= float(self.textCtrl4.GetValue())
        prev_bal= float(self.textCtrl5.GetValue())
        
        call_charges_per_person = round(((total - my_sms - his_sms - his_data - prev_bal)/2),2)
        
        my_amt = call_charges_per_person + my_sms
        his_amt = call_charges_per_person + his_sms + his_data + prev_bal
        cur_bal = his_amt-prev_bal
        
        self.textCtrl6.SetValue(str(call_charges_per_person))
        self.textCtrl7.SetValue(str(my_amt))
        self.textCtrl8.SetValue(str(his_amt))
        
        self.styledTextCtrl1.SetTextRaw('''
    Hi,\n        
    Total amount $ %.2f
    Your sms usage = $ %.2f, my sms/data usage = $ %.2f 
    Your data plan = $ %.2f 
        
    Each person's share = (%.2f-%.2f-%.2f-%.2f)/2  = $ %.2f
    Your share = $ %.2f+%.2f+%.2f = $ %.2f  
    
    Previous balance = $ %.2f 
                                 \t\t\t --------------
    Amount due = $ %.2f +%.2f  =    $ %.2f  
                                 \t\t\t --------------
        ''' % (total,his_sms,my_sms, his_data, total, my_sms, his_sms, his_data, call_charges_per_person,
        call_charges_per_person, his_sms, his_data, cur_bal, prev_bal, cur_bal, prev_bal, his_amt))
        
    def clear(self, event):
        self.textCtrl1.SetValue("")
        self.textCtrl2.SetValue("")
        self.textCtrl3.SetValue("")
        #self.textCtrl4.SetValue("")
        self.textCtrl5.SetValue("")
        self.textCtrl6.SetValue("")
        self.textCtrl7.SetValue("")
        self.textCtrl8.SetValue("")
        self.styledTextCtrl1.SetText("")
    
    def open_file(self, event):
        """
        Create and show the Open FileDialog
        """
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=currentDirectory,
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                self.textCtrl13.SetValue(path)
        dlg.Destroy()
    
    '''def set_login(self, event): 
        if (self.textCtrl11.GetValue() =="" or self.textCtrl12.GetValue()==""):
            wx.MessageBox('Login Id or Password can not be blank', 'Info', wx.OK | wx.ICON_EXCLAMATION)
        else:
            self.login_id = self.textCtrl11.GetValue()
            self.pswd = self.textCtrl12.GetValue()
            wx.MessageBox('Login Id & Password set', 'Info', wx.OK | wx.ICON_INFORMATION)'''
    
    def send_mail(self, event):
        if (self.textCtrl9.GetValue() =="" or self.textCtrl10.GetValue()==""):
            wx.MessageBox('To and Subject can not be blank', 'Info', wx.OK | wx.ICON_EXCLAMATION)
        else:
            to = self.textCtrl9.GetValue()
            subject = self.textCtrl10.GetValue()
            body = self.styledTextCtrl1.GetText()
            attach = self.textCtrl13.GetValue()
            self.login_id = self.textCtrl11.GetValue()
            self.pswd = self.textCtrl12.GetValue()
            sender = self.textCtrl14.GetValue()
            if (self.textCtrl11.GetValue() =="" or self.textCtrl12.GetValue()==""):
                wx.MessageBox('Login Id or Password can not be blank', 'Info', wx.OK | wx.ICON_EXCLAMATION)
            else:
                msg = Mail.SendMail(self.login_id,sender,self.pswd, to, subject, body, attach)
                if (msg =="Error Sending mail" or msg =="Error in Authentication"):
                    wx.MessageBox(msg, 'Error', wx.OK | wx.ICON_ERROR)
                    
                else:
                    wx.MessageBox('Mail Sent!', 'Info', wx.OK | wx.ICON_INFORMATION)
               
    def __init__(self, parent):
        self._init_ctrls(parent)

