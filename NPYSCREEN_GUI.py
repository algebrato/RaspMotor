

import npyscreen as nps

class MainForm( nps.ActionFormWithMenus ):
    def create(self):
        
        OK_BUTTON_TEXT = "Send a request"

        self.add(nps.TitleText, name="X shift:")
        self.add(nps.TitleText, name="Y shift:")
        self.add(nps.FixedText, value = 'Actual Position: ', editable = False)
        self.add(nps.TitleSelectOne, max_height=4, value = [1,], name = "Speed: ", values=["10x","100x","1000x"]) 

        # Main Menu and Edit User menu
        self.menu = self.new_menu(name = "Menu 1", shortcut = "m")


    def on_cancel(self):
        exiting = nps.notify_yes_no("Vuoi veramente uscire?","Close Application", editw = 2)
        if(exiting):
            self.exit_application()
        else:
            pass
        


    def exit_application(self):
        self.editing = False
        self.parentApp.setNextForm(None)
        self.parentApp.switchFormNow()



class GUI ( nps.NPSAppManaged ):
    def onStart(self):
        self.addForm('MAIN', MainForm, name = "XY Stage - Control Interface")


