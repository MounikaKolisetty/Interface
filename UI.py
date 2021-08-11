import tkinter 
from tkinter import *
from tkinter import ttk
 
window_main = tkinter.Tk(className='Create PIN List', )
tabControl = ttk.Notebook(window_main)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Main_Interface')
tabControl.add(tab2, text ='BMC_Interface')
tabControl.add(tab3, text ='Transmission Interface')
tabControl.pack(expand = 1, fill ="both")

canvas = tkinter.Canvas(tab1, width=1200, height=700)
canvas.grid(rowspan=20, columnspan=20)

#Tab1/Main_Interface
check_1 = tkinter.IntVar()
check_2 = tkinter.IntVar()
check_3 = tkinter.IntVar()
check_4 = tkinter.IntVar()
check_5 = tkinter.IntVar()
check_6 = tkinter.IntVar()
check_7 = tkinter.IntVar()
check_8 = tkinter.IntVar()
check_9 = tkinter.IntVar()
check_10 = tkinter.IntVar()
check_11 = tkinter.IntVar()

def check1Clicked():
    if check_1.get() :
        print('Checkbox 1 selected')
    else :
        print('Checkbox 1 unselected')
 
def check2Clicked():
    if check_2.get() :
        print('Checkbox 2 selected')
    else :
        print('Checkbox 2 unselected')
 
def check3Clicked():
    if check_3.get() :
        print('Checkbox 3 selected')
    else :
        print('Checkbox 3 unselected')

def check4Clicked():
    if check_4.get() :
        print('Checkbox 4 selected')
    else :
        print('Checkbox 4 unselected')

def check5Clicked():
    if check_5.get() :
        print('Checkbox 5 selected')
    else :
        print('Checkbox 5 unselected')

def check6Clicked():
    if check_6.get() :
        print('Checkbox 6 selected')
    else :
        print('Checkbox 6 unselected')

def check7Clicked():
    if check_7.get() :
        print('Checkbox 7 selected')
    else :
        print('Checkbox 7 unselected')

def check8Clicked():
    if check_8.get() :
        print('Checkbox 8 selected')
    else :
        print('Checkbox 8 unselected')

def check9Clicked():
    if check_9.get() :
        print('Checkbox 9 selected')
    else :
        print('Checkbox 9 unselected')

def check10Clicked():
    if check_10.get() :
        print('Checkbox 10 selected')
    else :
        print('Checkbox 10 unselected')

def check11Clicked():
    if check_11.get() :
        print('Checkbox 11 selected')
    else :
        print('Checkbox 11 unselected')
 
tkinter.Label(tab1, text = "From").grid(row=0, column=2)
tkinter.Label(tab1, text = "To").grid(row=0, column=3)
check_but_1 = tkinter.Checkbutton(tab1, text = 'PIN Serial Number 1', variable = check_1,
                onvalue = 1, offvalue = 0, command=check1Clicked)
check_but_1.grid(row=1, column=1)
tkinter.Entry(tab1).grid(row=1, column=2)
tkinter.Entry(tab1).grid(row=1, column=3)

check_but_2 = tkinter.Checkbutton(tab1, text = 'PIN Serial Number 2', variable = check_2,
                onvalue = 1, offvalue = 0, command=check2Clicked)
check_but_2.grid(row=2, column=1)
tkinter.Entry(tab1).grid(row=2, column=2)
tkinter.Entry(tab1).grid(row=2, column=3)

check_but_3 = tkinter.Checkbutton(tab1, text = 'Machine Build dates', variable = check_3,
                onvalue = 1, offvalue = 0, command=check3Clicked)
check_but_3.grid(row=3, column=1)
tkinter.Entry(tab1).grid(row=3, column=2)
tkinter.Entry(tab1).grid(row=3, column=3)

check_but_4 = tkinter.Checkbutton(tab1, text = 'Engine Serial Number', variable = check_4,
                onvalue = 1, offvalue = 0, command=check4Clicked)
check_but_4.grid(row=4, column=1)
tkinter.Entry(tab1).grid(row=4, column=2)
tkinter.Entry(tab1).grid(row=4, column=3)

check_but_5 = tkinter.Checkbutton(tab1, text = 'Transmission Serial Number', variable = check_5,
                onvalue = 1, offvalue = 0, command=check5Clicked)
check_but_5.grid(row=5, column=1)
tkinter.Entry(tab1).grid(row=5, column=2)
tkinter.Entry(tab1).grid(row=5, column=3)

check_but_6 = tkinter.Checkbutton(tab1, text = 'Cab Serial Number', variable = check_6,
                onvalue = 1, offvalue = 0, command=check6Clicked)
check_but_6.grid(row=6, column=1)
tkinter.Entry(tab1).grid(row=6, column=2)
tkinter.Entry(tab1).grid(row=6, column=3)

check_but_7 = tkinter.Checkbutton(tab1, text = 'Front Axle Serial Number', variable = check_7,
                onvalue = 1, offvalue = 0, command=check7Clicked)
check_but_7.grid(row=7, column=1)
tkinter.Entry(tab1).grid(row=7, column=2)
tkinter.Entry(tab1).grid(row=7, column=3)

check_but_8 = tkinter.Checkbutton(tab1, text = 'Position reciever serial number', variable = check_8,
                onvalue = 1, offvalue = 0, command=check8Clicked)
check_but_8.grid(row=8, column=1)
tkinter.Entry(tab1).grid(row=8, column=2)
tkinter.Entry(tab1).grid(row=8, column=3)

check_but_9 = tkinter.Checkbutton(tab1, text = 'Green star serial number', variable = check_9,
                onvalue = 1, offvalue = 0, command=check8Clicked)
check_but_9.grid(row=9, column=1)
tkinter.Entry(tab1).grid(row=9, column=2)
tkinter.Entry(tab1).grid(row=9, column=3)

check_but_10 = tkinter.Checkbutton(tab1, text = 'StarFire reciever serial number', variable = check_10,
                onvalue = 1, offvalue = 0, command=check8Clicked)
check_but_10.grid(row=10, column=1)
tkinter.Entry(tab1).grid(row=10, column=2)
tkinter.Entry(tab1).grid(row=10, column=3)

#Tab2/BMC Interface

check_1_TT = tkinter.IntVar()
check_2_TT = tkinter.IntVar()
check_3_TT = tkinter.IntVar()
check_4_TT = tkinter.IntVar()
check_5_TT = tkinter.IntVar()
check_6_TT = tkinter.IntVar()

def check1BMCClicked():
    if check_1_TT.get() :
        print('Checkbox 1 selected')
    else :
        print('Checkbox 1 unselected')
 
def check2BMCClicked():
    if check_2_TT.get() :
        print('Checkbox 2 selected')
    else :
        print('Checkbox 2 unselected')
 
def check3BMCClicked():
    if check_3_TT.get() :
        print('Checkbox 3 selected')
    else :
        print('Checkbox 3 unselected')

def check4BMCClicked():
    if check_4_TT.get() :
        print('Checkbox 4 selected')
    else :
        print('Checkbox 4 unselected')

def check5BMCClicked():
    if check_5_TT.get() :
        print('Checkbox 5 selected')
    else :
        print('Checkbox 5 unselected')

def check6BMCClicked():
    if check_6_TT.get() :
        print('Checkbox 6 selected')
    else :
        print('Checkbox 6 unselected')

#TractorType
check_but_TractorType = tkinter.Checkbutton(tab2, text = 'Tractor Type', variable = check_1_TT,
                onvalue = 1, offvalue = 0, command=check1BMCClicked)
check_but_TractorType.grid(row=3, column=1)
check_but_6030= tkinter.Checkbutton(tab2, text = '6030', variable = check_2_TT,
                onvalue = 1, offvalue = 0, command=check2BMCClicked)
check_but_6030.grid(row=3, column=2)
check_but_6M= tkinter.Checkbutton(tab2, text = '6M', variable = check_3_TT,
                onvalue = 1, offvalue = 0, command=check3BMCClicked)
check_but_6M.grid(row=3, column=3)
check_but_6MC =  tkinter.Checkbutton(tab2, text = '6MC', variable = check_4_TT,
                onvalue = 1, offvalue = 0, command=check4BMCClicked)
check_but_6MC.grid(row=3, column=4)
check_but_6R= tkinter.Checkbutton(tab2, text = '6R', variable = check_5_TT,
                onvalue = 1, offvalue = 0, command=check5BMCClicked)
check_but_6R.grid(row=3, column=5)
check_but_6RC =  tkinter.Checkbutton(tab2, text = '6RC', variable = check_6_TT,
                onvalue = 1, offvalue = 0, command=check6BMCClicked)
check_but_6RC.grid(row=3, column=6)

#Tractor Series
check_1_TS = tkinter.IntVar()
check_2_TS = tkinter.IntVar()
check_3_TS = tkinter.IntVar()
check_4_TS = tkinter.IntVar()
check_5_TS = tkinter.IntVar()

def check1TSClicked():
    if check_1_TS.get() :
        print('Checkbox 1 selected')
    else :
        print('Checkbox 1 unselected')
 
def check2TSClicked():
    if check_2_TS.get() :
        print('Checkbox 2 selected')
    else :
        print('Checkbox 2 unselected')
 
def check3TSClicked():
    if check_3_TS.get() :
        print('Checkbox 3 selected')
    else :
        print('Checkbox 3 unselected')

def check4TSClicked():
    if check_4_TS.get() :
        print('Checkbox 4 selected')
    else :
        print('Checkbox 4 unselected')

def check5TSClicked():
    if check_5_TS.get() :
        print('Checkbox 5 selected')
    else :
        print('Checkbox 5 unselected')

Check_but_TractorSeries = tkinter.Checkbutton(tab2, text = 'Tractor Series', variable = check_1_TS,
                onvalue = 1, offvalue = 0, command=check1TSClicked)
Check_but_TractorSeries.grid(row=4, column=1)
check_but_30= tkinter.Checkbutton(tab2, text = '6x30', variable = check_2_TS,
                onvalue = 1, offvalue = 0, command=check2TSClicked)
check_but_30.grid(row=4, column=2)
check_but_40= tkinter.Checkbutton(tab2, text = '6x40', variable = check_3_TS,
                onvalue = 1, offvalue = 0, command=check3TSClicked)
check_but_40.grid(row=4, column=3)
check_but_50 =  tkinter.Checkbutton(tab2, text = '6x50', variable = check_4_TS,
                onvalue = 1, offvalue = 0, command=check4TSClicked)
check_but_50.grid(row=4, column=4)
check_but_60= tkinter.Checkbutton(tab2, text = '6x60', variable = check_5_TS,
                onvalue = 1, offvalue = 0, command=check5TSClicked)
check_but_60.grid(row=4, column=5)

#Tractor Model/Decal
#Tab3/TransmissionInterface
check_TT = tkinter.IntVar()
check_MPQT = tkinter.IntVar()
check_D = tkinter.IntVar()
check_E = tkinter.IntVar()
check_F = tkinter.IntVar()
check_EPQT = tkinter.IntVar()
check_G = tkinter.IntVar()
check_H = tkinter.IntVar()
check_J = tkinter.IntVar()
check_K = tkinter.IntVar()
check_L = tkinter.IntVar()
check_N = tkinter.IntVar()
check_Y = tkinter.IntVar()
check_CQT = tkinter.IntVar()
check_M = tkinter.IntVar()
check_W = tkinter.IntVar()
check_X = tkinter.IntVar()
check_TSS = tkinter.IntVar()
check_A = tkinter.IntVar()
check_PTR = tkinter.IntVar()
check_B = tkinter.IntVar()
check_C = tkinter.IntVar()
check_1 = tkinter.IntVar()
check_5 = tkinter.IntVar()
check_6 = tkinter.IntVar()
check_7 = tkinter.IntVar()
check_IVT = tkinter.IntVar()
check_P = tkinter.IntVar()
check_R = tkinter.IntVar()
check_S = tkinter.IntVar()
check_DPT = tkinter.IntVar()
check_T = tkinter.IntVar()
check_U = tkinter.IntVar()
check_V = tkinter.IntVar()
check_OTHERS = tkinter.IntVar()
check_Z = tkinter.IntVar()
check_2 = tkinter.IntVar()
check_3 = tkinter.IntVar()

def checkTTClicked():
    if (check_TT.get()):
        check_MPQT.set(1)
        check_EPQT.set(1)
        check_CQT.set(1)
        check_TSS.set(1)
        check_PTR.set(1)
        check_IVT.set(1)
        check_DPT.set(1)
        check_OTHERS.set(1)
        checkMPQTClicked()
        checkEPQTClicked()
        checkCQTClicked()
        checkTSSClicked()
        checkPTRClicked()
        checkIVTClicked()
        checkDPTClicked()
        checkOthersClicked()
    else:
        check_MPQT.set(0)
        check_EPQT.set(0)
        check_CQT.set(0)
        check_TSS.set(0)
        check_PTR.set(0)
        check_IVT.set(0)
        check_DPT.set(0)
        check_OTHERS.set(0)
        checkMPQTClicked()
        checkEPQTClicked()
        checkCQTClicked()
        checkTSSClicked()
        checkPTRClicked()
        checkIVTClicked()
        checkDPTClicked()
        checkOthersClicked()
      

def checkAllTypes():
    if (check_MPQT.get() & check_EPQT.get() & check_CQT.get() & check_TSS.get() & check_PTR.get() & check_IVT.get() & check_DPT.get() & check_OTHERS.get()):
        check_TT.set(1)
    else:
        check_TT.set(0)  

def checkMPQTClicked():
    if (check_MPQT.get()):
        check_D.set(1)
        check_E.set(1)
        check_F.set(1)
        checkAllTypes() 
    else:
        check_D.set(0)
        check_E.set(0)
        check_F.set(0)
        checkAllTypes() 

def checkallMPQT():
    if (check_D.get() & check_E.get() & check_F.get()):
        check_MPQT.set(1)
    else:
        check_MPQT.set(0)

def checkEPQTClicked():
    if (check_EPQT.get()):
        check_G.set(1)
        check_H.set(1)
        check_J.set(1)
        check_K.set(1)
        check_L.set(1)
        check_N.set(1)
        check_Y.set(1)
        checkAllTypes() 
    else:
        check_G.set(0)
        check_H.set(0)
        check_J.set(0)
        check_K.set(0)
        check_L.set(0)
        check_N.set(0)
        check_Y.set(0)
        checkAllTypes() 

def checkallEPQT():
    if (check_G.get() & check_H.get() & check_J.get() & check_K.get() & check_L.get() & check_N.get() & check_Y.get()):
        check_EPQT.set(1)
    else:
        check_EPQT.set(0)

def checkCQTClicked():
    if (check_CQT.get()):
        check_M.set(1)
        check_W.set(1)
        check_X.set(1)
        checkAllTypes() 
    else:
        check_M.set(0)
        check_W.set(0)
        check_X.set(0)
        checkAllTypes() 

def checkallCQT():
    if (check_M.get() & check_W.get() & check_X.get()):
        check_CQT.set(1)
    else:
        check_CQT.set(0)

def checkTSSClicked():
    if (check_TSS.get()):
        check_A.set(1)
        checkAllTypes() 
    else:
        check_A.set(0)
        checkAllTypes() 

def checkallTSS():
    if (check_A.get()):
        check_TSS.set(1)
    else:
        check_TSS.set(0)

def checkPTRClicked():
    if (check_PTR.get()):
        check_B.set(1)
        check_C.set(1)
        check_1.set(1)
        check_5.set(1)
        check_6.set(1)
        check_7.set(1)
        checkAllTypes() 
    else:
        check_B.set(0)
        check_C.set(0)
        check_1.set(0)
        check_5.set(0)
        check_6.set(0)
        check_7.set(0)
        checkAllTypes() 

def checkallPTR():
    if (check_B.get() & check_C.get() & check_1.get() & check_5.get() & check_6.get() & check_7.get()):
        check_PTR.set(1)
    else:
        check_PTR.set(0)

def checkIVTClicked():
    if (check_IVT.get()):
        check_P.set(1)
        check_R.set(1)
        check_S.set(1)
        checkAllTypes() 
    else:
        check_P.set(0)
        check_R.set(0)
        check_S.set(0)
        checkAllTypes() 

def checkallIVT():
    if (check_P.get() & check_R.get() & check_S.get()):
        check_IVT.set(1)
    else:
        check_IVT.set(0)

def checkDPTClicked():
    if (check_DPT.get()):
        check_T.set(1)
        check_U.set(1)
        check_V.set(1)
        checkAllTypes() 
    else:
        check_T.set(0)
        check_U.set(0)
        check_V.set(0)
        checkAllTypes() 

def checkallDPT():
    if (check_T.get() & check_U.get() & check_V.get()):
        check_DPT.set(1)
    else:
        check_DPT.set(0)

def checkOthersClicked():
    if (check_OTHERS.get()):
        check_Z.set(1)
        check_2.set(1)
        check_3.set(1)
        checkAllTypes() 
    else:
        check_Z.set(0)
        check_2.set(0)
        check_3.set(0)
        checkAllTypes() 

def checkallOthers():
    if (check_Z.get() & check_2.get() & check_3.get()):
        check_OTHERS.set(1)
    else:
        check_OTHERS.set(0)

Check_TransType = tkinter.Checkbutton(tab3, text = 'Transmission Type', variable = check_TT,
                onvalue = 1, offvalue = 0, command=checkTTClicked)
Check_TransType.grid(row=1, column=1)
#MPQT
Check_MPQT = tkinter.Checkbutton(tab3, text = "MPQT", variable = check_MPQT,
                onvalue = 1, offvalue = 0, command=checkMPQTClicked)
Check_MPQT.grid(sticky="W",row=1, column=2)

Check_D = tkinter.Checkbutton(tab3, text = "Code D", variable = check_D,
                onvalue = 1, offvalue = 0, command=checkallMPQT)
Check_D.grid(row=1, column=3)

Check_E = tkinter.Checkbutton(tab3, text = "Code E", variable = check_E,
                onvalue = 1, offvalue = 0, command=checkallMPQT)
Check_E.grid(row=1, column=4)

Check_F = tkinter.Checkbutton(tab3, text = "Code F", variable = check_F,
                onvalue = 1, offvalue = 0, command=checkallMPQT)
Check_F.grid(row=1, column=5)
#EPQT
Check_EPQT = tkinter.Checkbutton(tab3, text = "EPQT", variable = check_EPQT,
                onvalue = 1, offvalue = 0, command=checkEPQTClicked)
Check_EPQT.grid(sticky="W",row=2, column=2)

Check_G = tkinter.Checkbutton(tab3, text = "Code G", variable = check_G,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_G.grid(row=2, column=3)

Check_H = tkinter.Checkbutton(tab3, text = "Code H", variable = check_H,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_H.grid(row=2, column=4)

Check_J = tkinter.Checkbutton(tab3, text = "Code J", variable = check_J,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_J.grid(row=2, column=5)

Check_K = tkinter.Checkbutton(tab3, text = "Code K", variable = check_K,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_K.grid(row=2, column=6)

Check_L = tkinter.Checkbutton(tab3, text = "Code L", variable = check_L,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_L.grid(row=2, column=7)

Check_N = tkinter.Checkbutton(tab3, text = "Code N", variable = check_N,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_N.grid(row=2, column=8)

Check_Y = tkinter.Checkbutton(tab3, text = "Code Y", variable = check_Y,
                onvalue = 1, offvalue = 0, command=checkallEPQT)
Check_Y.grid(row=2, column=9)
#CQT
Check_CQT = tkinter.Checkbutton(tab3, text = "CQT", variable = check_CQT,
                onvalue = 1, offvalue = 0, command=checkCQTClicked)
Check_CQT.grid(sticky="W", row=3, column=2)

Check_M = tkinter.Checkbutton(tab3, text = "Code M", variable = check_M,
                onvalue = 1, offvalue = 0, command=checkallCQT)
Check_M.grid(row=3, column=3)

Check_W = tkinter.Checkbutton(tab3, text = "Code W", variable = check_W,
                onvalue = 1, offvalue = 0, command=checkallCQT)
Check_W.grid(row=3, column=4)

Check_X = tkinter.Checkbutton(tab3, text = "Code X", variable = check_X,
                onvalue = 1, offvalue = 0, command=checkallCQT)
Check_X.grid(row=3, column=5)
#TSS
Check_TSS = tkinter.Checkbutton(tab3, text = "TSS", variable = check_TSS,
                onvalue = 1, offvalue = 0, command=checkTSSClicked)
Check_TSS.grid(sticky="W", row=4, column=2)

Check_A = tkinter.Checkbutton(tab3, text = "Code A", variable = check_A,
                onvalue = 1, offvalue = 0, command=checkallTSS)
Check_A.grid(row=4, column=3)
#PTR
Check_PTR = tkinter.Checkbutton(tab3, text = "PTR", variable = check_PTR,
                onvalue = 1, offvalue = 0, command=checkPTRClicked)
Check_PTR.grid(sticky="W", row=5, column=2)

Check_B = tkinter.Checkbutton(tab3, text = "Code B", variable = check_B,
                onvalue = 1, offvalue = 0, command=checkallPTR)
Check_B.grid(row=5, column=3)

Check_C = tkinter.Checkbutton(tab3, text = "Code C", variable = check_C,
                onvalue = 1, offvalue = 0, command=checkallPTR)
Check_C.grid(row=5, column=4)

Check_1 = tkinter.Checkbutton(tab3, text = "Code 1", variable = check_1,
                onvalue = 1, offvalue = 0, command=checkallPTR)
Check_1.grid(row=5, column=5)

Check_5 = tkinter.Checkbutton(tab3, text = "Code 5", variable = check_5,
                onvalue = 1, offvalue = 0, command=checkallPTR)
Check_5.grid(row=5, column=6)

Check_6 = tkinter.Checkbutton(tab3, text = "Code 6", variable = check_6,
                onvalue = 1, offvalue = 0, command=checkallPTR)
Check_6.grid(row=5, column=7)

Check_7 = tkinter.Checkbutton(tab3, text = "Code 7", variable = check_7,
                onvalue = 1, offvalue = 0, command=checkallPTR)
Check_7.grid(row=5, column=8)
#IVT
Check_IVT = tkinter.Checkbutton(tab3, text = "IVT", variable = check_IVT,
                onvalue = 1, offvalue = 0, command=checkIVTClicked)
Check_IVT.grid(sticky="W", row=6, column=2)

Check_P = tkinter.Checkbutton(tab3, text = "Code P", variable = check_P,
                onvalue = 1, offvalue = 0, command=checkallIVT)
Check_P.grid(row=6, column=3)

Check_R = tkinter.Checkbutton(tab3, text = "Code R", variable = check_R,
                onvalue = 1, offvalue = 0, command=checkallIVT)
Check_R.grid(row=6, column=4)

Check_S = tkinter.Checkbutton(tab3, text = "Code S", variable = check_S,
                onvalue = 1, offvalue = 0, command=checkallIVT)
Check_S.grid(row=6, column=5)
#DPT
Check_DPT = tkinter.Checkbutton(tab3, text = "DPT", variable = check_DPT,
                onvalue = 1, offvalue = 0, command=checkDPTClicked)
Check_DPT.grid(sticky="W", row=7, column=2)

Check_T = tkinter.Checkbutton(tab3, text = "Code T", variable = check_T,
                onvalue = 1, offvalue = 0, command=checkallDPT)
Check_T.grid(row=7, column=3)

Check_U = tkinter.Checkbutton(tab3, text = "Code U", variable = check_U,
                onvalue = 1, offvalue = 0, command=checkallDPT)
Check_U.grid(row=7, column=4)

Check_V = tkinter.Checkbutton(tab3, text = "Code V", variable = check_V,
                onvalue = 1, offvalue = 0, command=checkallDPT)
Check_V.grid(row=7, column=5)
#OTHERS
Check_OTHERS = tkinter.Checkbutton(tab3, text = "OTHERS", variable = check_OTHERS,
                onvalue = 1, offvalue = 0, command=checkOthersClicked)
Check_OTHERS.grid(sticky="W", row=8, column=2)

Check_Z = tkinter.Checkbutton(tab3, text = "Code Z", variable = check_Z,
                onvalue = 1, offvalue = 0, command=checkallOthers)
Check_Z.grid(row=8, column=3)

Check_2 = tkinter.Checkbutton(tab3, text = "Code 2", variable = check_2,
                onvalue = 1, offvalue = 0, command=checkallOthers)
Check_2.grid(row=8, column=4)

Check_3 = tkinter.Checkbutton(tab3, text = "Code 3", variable = check_3,
                onvalue = 1, offvalue = 0, command=checkallOthers)
Check_3.grid(row=8, column=5)

#Codes
tkinter.Label(tab3, text = "CODES").grid(row=2, column=10)
tkinter.Label(tab3, text = "Code A: 12/12 fully synchronized").grid(sticky="W",row=3, column=10)
tkinter.Label(tab3, text = "Code B: 16/16 fully synchronized with power reverser, 30K").grid(sticky="W",row=4, column=10)
tkinter.Label(tab3, text = "Code C: 16/16 fully synchronized with power reverser, 40K").grid(sticky="W",row=5, column=10)
tkinter.Label(tab3, text = "Code D: 16/16 mechanical, partially power shifted, 30K").grid(sticky="W",row=6, column=10)
tkinter.Label(tab3, text = "Code E: 16/16 or 20/20 mechanical, partially power shifted, 40K").grid(sticky="W",row=7, column=10)
tkinter.Label(tab3, text = "Code F: 24/24 or 32/32 mechanical, partially power shifted, 40K").grid(sticky="W",row=8, column=10)
tkinter.Label(tab3, text = "Code G: 16/16 or 20/20 or 24/24 or 32/32 electronic, partially power shifted, 40K").grid(sticky="W",row=9, column=10)
tkinter.Label(tab3, text = "Code H: 16/16 electronic, partially power shifted, 30K").grid(sticky="W",row=10, column=10)
tkinter.Label(tab3, text = "Code J: 16/16 electronic, partially power shifted, 40K").grid(sticky="W",row=11, column=10)
tkinter.Label(tab3, text = "Code K: 20/20 or 24/24 or 32/32 electronic, partially power shifted w/ automatic gear shift, 40K").grid(sticky="W",row=12, column=10)
tkinter.Label(tab3, text = "Code L: 16/16 or 20/20 or 24/24 or 32/32 electronic, partially power shifted w/ automatic gear shift, 35K").grid(sticky="W",row=13, column=10)
tkinter.Label(tab3, text = "Code M: 16/16 electronic, partially power shifted w/ automatic gear shift, 40K").grid(sticky="W",row=14, column=10)
tkinter.Label(tab3, text = "Code N: 20/20 or 24/24 electronic, partially power shifted w/ automatic gear shift, 50K").grid(sticky="W",row=15, column=10)
tkinter.Label(tab3, text = "Code P: stepless, 40K").grid(sticky="W",row=16, column=10)
tkinter.Label(tab3, text = "Code R: stepless, 50K").grid(sticky="W",row=17, column=10)
tkinter.Label(tab3, text = "Code S: stepless, 35K").grid(sticky="W",row=18, column=10)
tkinter.Label(tab3, text = "Code T: 24/24 electric, double clutch w/ automatic gear and range shift, 40K").grid(sticky="W",row=19, column=10)
tkinter.Label(tab3, text = "Code U: 24/24 electric, double clutch w/ automatic gear and range shift, 50K").grid(sticky="W",row=20, column=10)
tkinter.Label(tab3, text = "Code V: 24/24 electric, double clutch w/ automatic gear and range shift, 60K").grid(sticky="W",row=21, column=10)
tkinter.Label(tab3, text = "Code W: 20/20 or 24/24 hydroelectric, partially power shifted, 35K").grid(sticky="W",row=22, column=10)
tkinter.Label(tab3, text = "Code X: 20/20 or 24/24 hydroelectric, partially power shifted, 40K").grid(sticky="W",row=23, column=10)
tkinter.Label(tab3, text = "Code Y: 16/16 or 32/32 electric, partially power shifted, 35K").grid(sticky="W",row=24, column=10)
tkinter.Label(tab3, text = "Code Z: 20/20 or 24/24 hydroelectric, partially power shifted, 50K").grid(sticky="W",row=25, column=10)
tkinter.Label(tab3, text = "Code 1: 16/16 partially synchronized with power reverser, 30K").grid(sticky="W",row=26, column=10)
tkinter.Label(tab3, text = "Code 2: 20/20 or 24/24 electronic, partially power shifted, w/ automatic gear and range shift, 35K").grid(sticky="W",row=27, column=10)
tkinter.Label(tab3, text = "Code 3: 20/20 or 24/24 electronic, partially power shifted, w/ automatic gear and range shift, 40K").grid(sticky="W",row=28, column=10)
tkinter.Label(tab3, text = "Code 5: 16/16 partially synchronized with synchronized reverser, 30K").grid(sticky="W",row=29, column=10)
tkinter.Label(tab3, text = "Code 6: 16/16 partially synchronized with power reverser, 40K").grid(sticky="W",row=30, column=10)
tkinter.Label(tab3, text = "Code 7: 32/16 partially synchronized with Hi / Lo, 40K").grid(sticky="W",row=31, column=10)

window_main.mainloop()