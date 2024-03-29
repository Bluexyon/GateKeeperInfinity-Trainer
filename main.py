import PySimpleGUI as sg
import OffsetCalc
import threading
import time
import sys
#Max Health Thread Loop Run Condition
maxHealthChange = False
#Damage Thread Loop Run Condition
damageChange = False
#Move Speed Thread Loop Run Condition
moveSpeedChange = False
#Attack Speed Thread Loop Run Condition
attackSpeedChange = False
#Master Loop Run Condition that kills all running loops in threads
masterThreadState = 1

#Max Health Thread function definition
def maxHealthWorker():
    while maxHealthChange == True & masterThreadState == 1:
            time.sleep(0.5)
            OffsetCalc.gameProces.write_float(OffsetCalc.getPointerAddress(OffsetCalc.gameAssBase + 0x03F5E2B0, [0xB8, 0x8, 0x20, 0x118, 0x10, 0x28, 0x120]),healthVal)
            print("Max Health is being modified")

#Damage Thread function definition
def damageWorker():
    while damageChange == True & masterThreadState == 1:
            time.sleep(0.5)
            OffsetCalc.gameProces.write_float(OffsetCalc.getPointerAddress(OffsetCalc.gameAssBase + 0x03F5AF98, [0x20, 0xB8, 0x28, 0x28, 0x90, 0x38, 0x120]),damageVal)
            print("Damage is being modified")

#Move Speed Thread function definition
def moveSpeedWorker():
    while moveSpeedChange == True & masterThreadState == 1:
            time.sleep(0.005)
            OffsetCalc.gameProces.write_float(OffsetCalc.getPointerAddress(OffsetCalc.gameAssBase + 0x03FD5730, [0xB8, 0x18, 0x130, 0x240, 0x118, 0x2F0, 0x11C]),moveSpeedVal)
            print("Movement Speed Modifier is being changed")

#Move Speed Thread function definition
def attackSpeedWorker():
    while attackSpeedChange == True & masterThreadState == 1:
            time.sleep(0.5)
            OffsetCalc.gameProces.write_float(OffsetCalc.getPointerAddress(OffsetCalc.gameAssBase + 0x03FC6AB0, [0xB8, 0x8, 0x110, 0x128, 0x120, 0x30, 0x108]),attackSpeedVal)
            print("Attack Speed Modifier is being changed")

#Define the window's contents
layout = [[sg.Text("Max Health",background_color="#1F2041",text_color="#DCCDE8"),sg.Input(size="9",key='maxHealthInput'),sg.Button("Set",key='maxHealthBTN',button_color="#141429 on #DCCDE8",)],
          [sg.Text("Damage",background_color="#1F2041",text_color="#DCCDE8"),sg.Input(size="9",key='damageInput'),sg.Button("Set",key='damageBTN', button_color="#141429 on #DCCDE8")],
          [sg.Text("Movement Speed",background_color="#1F2041",text_color="#DCCDE8"),sg.Input(size="9",key='moveSpeedInput'),sg.Button("Set",key='moveSpeedBTN', button_color="#141429 on #DCCDE8")],
          [sg.Text("Attack Speed",background_color="#1F2041",text_color="#DCCDE8"),sg.Input(size="9",key='attackSpeedInput'),sg.Button("Set",key='attackSpeedBTN', button_color="#141429 on #DCCDE8")],
          [sg.Text("Blue Currency",background_color="#1F2041",text_color="#DCCDE8"),sg.Input(size="9",key='bCurrencyInput'),sg.Button("Set",key='bCurrencyBTN', button_color="#141429 on #DCCDE8")],
          [sg.Text("Gold Currency",background_color="#1F2041",text_color="#DCCDE8"),sg.Input(size="9",key='gCurrencyInput'),sg.Button("Set",key='gCurrencyBTN', button_color="#141429 on #DCCDE8")]]

# Create the window
window = sg.Window('Gate Keeper Infinity Game Trainer', layout, background_color="#1F2041")

#Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    
    #Check if Button Set of MaxHealth with key maxHealthBtn is clicked
    if event == 'maxHealthBTN':
        #Reset Healthchange thread if its running
        maxHealthChange = False
        #Get value from HealthInput
        healthVal = float(values['maxHealthInput'])
        #Start Loop Run Condition for Thread
        maxHealthChange = True
        #Start Thread
        threading.Thread(target=maxHealthWorker).start()

    #Check if Button Set of Damage with key damageBtn is clicked
    if event == 'damageBTN':
        #Reset damagechange thread if its running
        damageChange = False
        #Get value from damageInput
        damageVal = float(values['damageInput'])
        #Start Loop Run Condition for Thread
        damageChange = True
        #Start Thread
        threading.Thread(target=damageWorker).start()

    #Check if Button Set of Movement Speed with key movSpeedBtn is clicked
    if event == 'moveSpeedBTN':
        #Reset moveSpeedchange thread if its running
        moveSpeedChange = False
        #Get value from moveSpeedInput
        moveSpeedVal = float(values['moveSpeedInput'])
        #Start Loop Run Condition for Thread
        moveSpeedChange = True
        #Start Thread
        threading.Thread(target=moveSpeedWorker).start()

    #Check if Button Set of Movement Speed with key movSpeedBtn is clicked
    if event == 'attackSpeedBTN':
        #Reset moveSpeedchange thread if its running
        attackSpeedChange = False
        #Get value from moveSpeedInput
        attackSpeedVal = float(values['attackSpeedInput'])
        #Start Loop Run Condition for Thread
        attackSpeedChange = True
        #Start Thread
        threading.Thread(target=attackSpeedWorker).start()

    #Check if Button Set of Blue Currency with key bCurrencyBtn is clicked
    if event == 'bCurrencyBTN':
        #Get value from bCurrencyInput
        bCurrencyVal = int(values['bCurrencyInput'])
        OffsetCalc.gameProces.write_int(OffsetCalc.getPointerAddress(OffsetCalc.gameAssBase + 0x03FC6AB0, [0xB8, 0x8, 0x148, 0x10, 0xA8, 0x28, 0x18]),bCurrencyVal)
    if event == 'gCurrencyBTN':
        #Get value from gCurrencyInput
        gCurrencyVal = int(values['gCurrencyInput'])
        OffsetCalc.gameProces.write_int(OffsetCalc.getPointerAddress(OffsetCalc.gameAssBase + 0x03F62038, [0x78, 0xB8, 0x8, 0x18]),gCurrencyVal)

    
    
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "safetySwitch" or event == ('Exit' or 'exit'):
        #Kill all Running Threads before exiting Programm
        masterThreadState = 0
        break
    
# Finish up by removing from the screen
window.close()
sys.exit()