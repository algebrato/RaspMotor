
import time
import threading as thr
import urwid
import numpy as np
from Motor import *


#class MyTh(thr.Thread):
#    def __init__(self, name, durata):
#        thr.Thread.__init__(self)
#        self.name = nome
#        self.durata = durata
#    def run(self):
#        threadLock.acquire()
#        time.sleep(self.durata)
#        threadLock.release()



palette = [('I say', 'default,bold', 'default', 'bold'),]

xpos = urwid.Edit(('I say', "X Pos: "))
ypos = urwid.Edit(('I say', "Y Pos: "))
speed = urwid.Edit(('I say', "Speed X: ")) 


reply  = urwid.Text("")
status = urwid.Edit(('I say',"Status: "))



buttonGO   = urwid.Button(('I say',"GO"))
buttonExit = urwid.Button(('I say',"Exit"))

div = urwid.Divider()
pile = urwid.Pile([xpos, ypos, speed, div, status, reply, div, buttonGO, buttonExit])
top = urwid.Filler(pile, valign='top')


status.set_edit_text("Calibration")
motor = Motor(16,12,13,11)
status.set_edit_text("End calibration")

def on_GO_clicked(button):
    x = xpos.get_edit_text()
    y = ypos.get_edit_text()
    mul = speed.get_edit_text()

    x = int(x)
    y = int(y)
    mul = int(mul)
    reply.set_text("Moving to: (%i, %i)\n" % (x, y))

    
    if x > 0:
        status.set_edit_text("Moving...")
        motor.step_f(x,1./mul)
    else:
        status.set_edit_text("Moving...")
        motor.step_b(np.abs(x),1./mul)

    status.set_edit_text("Stop")


def Exit_clicked(button):
    motor.exit_tot()
    raise urwid.ExitMainLoop()


urwid.connect_signal(buttonGO, 'click', on_GO_clicked)
urwid.connect_signal(buttonExit, 'click', Exit_clicked)

urwid.MainLoop(top, palette).run()

