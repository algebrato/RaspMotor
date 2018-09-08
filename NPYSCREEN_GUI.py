

import npyscreen as nps

class MainForm( nps.ActionFormWithMenus ):
    def create(self):
        
        self.add(nps.TitleFixedText, name = 'MainFormName', editable = False)
        self.add(nps.FixedText, value = 'MainFormText1', editable = False)
        self.add(nps.FixedText, value = 'MainFormText2', editable = False)

        #~ Main Menu and Edit User menu
        self.menu = self.new_menu(name = "Manu1", shortcut = "m")

class GUI ( nps.NPSAppManaged ):
    def onStart(self):
        self.addForm('MAIN', MainForm, name="Titolo")


