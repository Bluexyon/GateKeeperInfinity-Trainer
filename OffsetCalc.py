import PySimpleGUI as sg
from pymem import *
from pymem.process import *
from pymem.ptypes import *
import sys

#Hook into Process with exception Handeling for when Program is not found
try:
    gameProces = Pymem("Gatekeeper Infinity.exe")
except pymem.exception.ProcessNotFound:
    #when process is not found create a window saying that the process was not found
    #layout for error window
    layout = [[sg.Text("Error: Game Process not found",text_color="red",background_color="#1F2041")]]
    #window creation
    window = sg.Window('Gate Keeper Infinity Game Trainer', layout, background_color="#1F2041")
    #while loop that sustains window on screen
    while True:
        event, values = window.read()
        #check for event of window closing and exit loop
        if event == sg.WIN_CLOSED or event == ('Exit' or 'exit'):
            break
    #Destroy the window
    window.close()
    #Exit Program
    sys.exit()

#Retrieve DLL load address that contains the variables addresses
gameAssBase = module_from_name(gameProces.process_handle, "GameAssembly.dll").lpBaseOfDll

#Callculate Pointer to address containing variable data
def getPointerAddress(base, offsets):
    address = gameProces.read_longlong(base)
    print(address)
    for i in offsets:
        if i != offsets[-1]:
            address = gameProces.read_longlong(address+i)
    return address + offsets[-1]


#------------------------------------------------------------UNUSED CODE----------------------------------------------------------------------
#def getPointerAddress(base, offsets):
#    remote_pointer = RemotePointer(gameProces.process_handle, base)
#    for i in offsets:
#        if i != offsets[-1]:
#            remote_pointer = RemotePointer(gameProces.process_handle, remote_pointer.value + i)
#    return remote_pointer + offsets[-1]

#print(gameProces.read_float(getPointerAddress(gameAssBase + 0x03F5E2B0, [0xB8, 0x8, 0x20, 0x118, 0x10, 0x28, 0x120])))
#print(0x2CADBC0C540+0x00000120)

#while True:
    #gameProces.write_float(getFloatPointerAddress(gameAssBase + 0x03F5E2B0, [0xB8, 0x8, 0x20, 0x118, 0x10, 0x28, 0x120]), 500.0)
#base_pointer_address = gameAssBase+0x3FC6AB0

#player_maxhealth = gameProces.read_float(gameAssBase + 0x3FC6AB0)
#print(base_pointer_address)