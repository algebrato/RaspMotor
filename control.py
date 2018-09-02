#!/usr/bin/python


import RPi.GPIO as gpio
import time 
import numpy as np


class Motor:
    def __init__(self,o_1,o_2,o_3,o_4):
        print "Classe creata"
        
        self.o_1 = o_1
        self.o_2 = o_2
        self.o_3 = o_3
        self.o_4 = o_4

        self.i_posf = 1
        self.i_posb = 1

        gpio.setmode(gpio.BOARD)
        gpio.setup(self.o_1, gpio.OUT)
        gpio.setup(self.o_2, gpio.OUT)
        gpio.setup(self.o_3, gpio.OUT) 
        gpio.setup(self.o_4, gpio.OUT)
        
        print("Start Calibration...")
        
        try:       
            self.step_f(11,0.1)
            self.step_b(11,0.1)
        except IOError:
            #Da implementare
            print("Motor not connected")

        print("Init complete")


    def step_f(self, N_step, speed):
        print("Moving ...")
        for i in range(0, N_step):
            if self.i_posf == 1:
                status = np.array([1,0,0,0]) 
            elif self.i_posf == 2:
                status = np.array([1,1,0,0]) 
            elif self.i_posf == 3:
                status = np.array([0,1,0,0]) 
            elif self.i_posf == 4:
                status = np.array([0,1,1,0]) 
            elif self.i_posf == 5:
                status = np.array([0,0,1,0]) 
            elif self.i_posf == 6:
                status = np.array([0,0,1,1]) 
            elif self.i_posf == 7:
                status = np.array([0,0,0,1]) 
            elif self.i_posf == 8:
                status = np.array([1,0,0,1]) 
            
            #print(status[0],status[1],status[2],status[3])
            #print(self.i_posf,self.i_posb)
            gpio.output(self.o_1,status[0])
            gpio.output(self.o_2,status[1])
            gpio.output(self.o_3,status[2])
            gpio.output(self.o_4,status[3])

            time.sleep(speed)

            self.i_posb = 9 - self.i_posf     
            
            self.i_posf = self.i_posf + 1      
            self.i_posb = self.i_posb + 1             
            
            if(self.i_posf > 8):
                self.i_posf = 1

            if(self.i_posb > 8):
                self.i_posb = 1

        print("End Moving")


    def step_b(self,N_step,speed):
        print("Moving ...")
        for i in range(0, N_step):
            if self.i_posb == 1:
                status = np.array([1,0,0,1])  
            elif self.i_posb == 2:
                status = np.array([0,0,0,1]) 
            elif self.i_posb == 3:
                status = np.array([0,0,1,1]) 
            elif self.i_posb == 4:
                status = np.array([0,0,1,0])
            elif self.i_posb == 5:
                status = np.array([0,1,1,0]) 
            elif self.i_posb == 6:
                status = np.array([0,1,0,0]) 
            elif self.i_posb == 7:
                status = np.array([1,1,0,0]) 
            elif self.i_posb == 8:
                status = np.array([1,0,0,0])             
           
            #print(status[0],status[1],status[2],status[3])
            #print(self.i_posf,self.i_posb)
            gpio.output(self.o_1,status[0])
            gpio.output(self.o_2,status[1])
            gpio.output(self.o_3,status[2])
            gpio.output(self.o_4,status[3])
            
            time.sleep(speed)

            self.i_posf = 9 - self.i_posb

            self.i_posb = self.i_posb + 1
            self.i_posf = self.i_posf + 1
            

            if(self.i_posb > 8):
                self.i_posb = 1

            if(self.i_posf > 8):
                self.i_posf = 1

        print("End Moving")



    def exit_tot(self):
        gpio.cleanup()
        print("Pin cleanup")




if __name__ == "__main__":

    a = Motor(16,12,13,11)
    

    #for i in range(0,9):
    #    a.step_f(100,0.001)
    #    time.sleep(2)


    while(1):
        try:
            step = input()
            if step == 0:
                break
            else:
                if step > 0:
                    a.step_f(step,0.01)
                else:
                    a.step_b(np.abs(step),0.01)
        except SyntaxError:
            print "Invalid input. Retry..."
        except NameError:
            print "Invalid input. Retry..."
    
    time.sleep(1)

    a.exit_tot()








