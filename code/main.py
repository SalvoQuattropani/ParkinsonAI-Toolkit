import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from tkinter import ttk
import pandas as pd
import random
import datetime
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import collections
import sys
sys.path.append('./code')
import tools
import inference
import os
from PIL import Image, ImageTk
import sv_ttk


results=[]
weights=[]

results_res=[]
weights_res=[]
mean_res=0

tools.clean('code/inference/tug')
tools.clean('code/inference/eeg')
tools.create_inference_tug_df()

def erese():
    textbox1_val.set("")
    textbox2_val.set("")
    textbox3_val.set("")
    textbox4_val.set("")
    textbox5_val.set("")
    textbox6_val.set("")
    textbox7_val.set("")
    textbox8_val.set("")
    textbox9_val.set("")
    textbox12_val.set("")
    textbox13_val.set("")
    textbox14_val.set("")
    textbox15_val.set("")
    textbox16_val.set("")
    textbox17_val.set("")
    textbox18_val.set("")
    textbox19_val.set("")
    textbox20_val.set("")
    textbox21_val.set("")
    textbox22_val.set("")
    textbox23_val.set("")
    textbox24_val.set("")
    textbox26_val.set("")
    results=[]
    weights=[]
    results_res=[]
    weights_res=[]
    mean_res=1


# funzione che reimposta tutte le checkbox e le textbox
def reset_function(start=False):
    # reimposta il valore di tutte le checkbox a 0
    if start!=True:
        #response_tug_var.set(0)
        #response_eeg_var.set(0)
        tug_var.set(0)
        eeg_var.set(0)
        

    progress_var.set(0)
    # imposta il valore di tutte le textbox a una stringa vuota
    erese()
    



# funzione che viene chiamata quando si preme il pulsante "Start"
def start_function():
    reset_function(True)
    erese()
    

    progress_bar.start()  # Avvia la progress bar
    progress_var.set(0)
    root.update()
    results=[]
    weights=[]
    
    

    



    # recupero il percorso del file selezionato
    try:
        

    #------------------------------
        if tug_var.get() ==1 :
            if os.listdir("data/tug"):
                tools.create_inference_tug_df()
                
                v,rate,tug_res1=inference.inference_tug_PD_UP()
                textbox1_val.set(tug_res1)
                progress_var.set(5)
                root.update()
                results.append(v)
                weights.append(rate)

                v,rate,tug_res2=inference.inference_tug_PD_GO1()
                textbox2_val.set(tug_res2)
                progress_var.set(10)
                root.update()
                results.append(v)
                weights.append(rate)


                v,rate,tug_res3=inference.inference_tug_PD_SPIN1()
                textbox3_val.set(tug_res3)
                progress_var.set(15)
                root.update()
                results.append(v)
                weights.append(rate)

                v,rate,tug_res4=inference.inference_tug_PD_BACK()
                textbox4_val.set(tug_res4)
                progress_var.set(18)
                root.update()
                results.append(v)
                weights.append(rate)


                v,rate,tug_res5=inference.inference_tug_PD_SPIN2()
                textbox5_val.set(tug_res5)
                progress_var.set(20)
                root.update()
                results.append(v)
                weights.append(rate)


                v,rate,tug_res6=inference.inference_tug_PD_DOWN()
                textbox6_val.set(tug_res6)
                progress_var.set(25)
                root.update()
                results.append(v)
                weights.append(rate)

                


                #-----------

                v,rate,tug_res7=inference.inference_tug_MCI_UP()
                textbox7_val.set(tug_res7)
                progress_var.set(30)
                root.update()
                results.append(v)
                weights.append(rate)

                v,rate,tug_res8=inference.inference_tug_MCI_GO1()
                textbox8_val.set(tug_res8)
                progress_var.set(35)
                root.update()
                results.append(v)
                weights.append(rate)


                v,rate,tug_res9=inference.inference_tug_MCI_SPIN1()
                textbox9_val.set(tug_res9)
                progress_var.set(40)
                root.update()
                results.append(v)
                weights.append(rate)

                v,rate,tug_res20=inference.inference_tug_MCI_BACK()
                textbox20_val.set(tug_res20)
                progress_var.set(45)
                root.update()
                results.append(v)
                weights.append(rate)


                v,rate,tug_res11=inference.inference_tug_MCI_SPIN2()
                textbox21_val.set(tug_res11)
                progress_var.set(50)
                root.update()
                results.append(v)
                weights.append(rate)


                v,rate,tug_res22=inference.inference_tug_MCI_DOWN()
                textbox22_val.set(tug_res22)
                progress_var.set(55)
                root.update()
                results.append(v)
                weights.append(rate)

            #--------
        
                mean_res, mean_aver=tools.weighted_average(results,weights,0.5)


                #if response_tug_var.get()==1:
                if int(mean_res) == 1:
                    if os.listdir("data/tug"):
                        tools.create_inference_tug_df()
                        v,rate,tug_res12=inference.inference_tug_Response_UP()
                        textbox12_val.set(tug_res12)
                        progress_var.set(60)
                        root.update()
                        results_res.append(v)
                        weights_res.append(rate)

                        v,rate,tug_res13=inference.inference_tug_Response_GO1()
                        textbox13_val.set(tug_res13)
                        progress_var.set(65)
                        root.update()
                        results_res.append(v)
                        weights_res.append(rate)


                        v,rate,tug_res14=inference.inference_tug_Response_SPIN1()
                        textbox14_val.set(tug_res14)
                        progress_var.set(70)
                        root.update()
                        results_res.append(v)
                        weights_res.append(rate)

                        v,rate,tug_res15=inference.inference_tug_Response_BACK()
                        v,rate,textbox15_val.set(tug_res15)
                        progress_var.set(75)
                        root.update()
                        results_res.append(v)
                        weights_res.append(rate)


                        v,rate,tug_res16=inference.inference_tug_Response_SPIN2()
                        textbox16_val.set(tug_res16)
                        progress_var.set(80)
                        root.update()
                        results_res.append(v)
                        weights_res.append(rate)


                        v,rate,tug_res17=inference.inference_tug_Response_DOWN()
                        textbox17_val.set(tug_res17)
                        progress_var.set(85)
                        root.update()
                        results_res.append(v)
                        weights_res.append(rate)
                else:
                    val= "NEGATIVO con il 100% di ricorrenza"
                    textbox12_val.set(val)
                    textbox13_val.set(val)
                    textbox14_val.set(val)
                    textbox15_val.set(val)
                    textbox16_val.set(val)
                    textbox17_val.set(val)
                    textbox26_val.set(val)


            
    #------------------------------
        if eeg_var.get()==1:
            if os.listdir("data/eeg"):
                tools.create_inference_eeg()
                v,rate,eeg_PD_res=inference.inference_eeg_pd_controlli()

                textbox18_val.set(eeg_PD_res)
                progress_var.set(90)
                root.update()
                results.append(v)
                weights.append(rate)

                #if tau_var.get() == 1:# and r==1:

                v,rate,eeg_mci_res=inference.inference_eeg_mci_Nc()
                textbox19_val.set(eeg_mci_res)
                progress_var.set(95)
                root.update()
                results.append(v)
                weights.append(rate)

                mean_res, mean_aver=tools.weighted_average(results,weights,0.5)

                #if response_eeg_var.get() == 1:
                if int(mean_res)==1:
                    tools.create_inference_eeg()
                    v,rate,eeg_resp_res=inference.inference_eeg_resp()
                    textbox24_val.set(eeg_resp_res)
                    progress_var.set(99)
                    root.update()
                    #results_res.append(v)
                    #weights_res.append(rate)
                else:
                    val= "NEGATIVO con il 100% di ricorrenza"
                    textbox24_val.set(val)


        



        progress_var.set(100)
        root.update()
        progress_bar.stop()

        try:
            

            #if response_tug_var.get() == 1:
            overall_res_tug, aver=tools.weighted_average(results_res,weights_res,0.5)
            if int(overall_res_tug) == 1:
                textbox26_val.set("POSITIVO al "+ str((aver*100))+ "%")
            else:
                textbox26_val.set("NEGATIVO al "+ str(100-(aver*100))+ "%")
        except Exception as e:
            print(e)
            pass
        try:
            '''if response_eeg_var.get() == 1:
                overall_res_eeg, aver=tools.weighted_average(results_res,weights_res,0.5)
                if int(overall_res_eeg) == 1:
                    textbox25_val.set("POSITIVO al "+ str((aver*100))+ "%")
                else:
                    textbox25_val.set("NEGATIVO al "+ str(100-(aver*100))+ "%")
            '''
            if tug_var.get()==1 or eeg_var.get() == 1:
                overall_res, aver=tools.weighted_average(results,weights,0.5)
                if int(overall_res) == 1:
                    textbox23_val.set("POSITIVO al "+ str((aver*100))+ "%")
                else:
                    textbox23_val.set("NEGATIVO al "+ str(100-(aver*100))+ "%")
        except Exception as e:
            print(e)
            pass
        
        root.update()
#------------------------------

    except Exception as e:
        progress_var.set(0)
        progress_bar.stop()
        messagebox.showerror("Errore", e)
        exit(0)



def show_info():
    messagebox.showinfo("Info", " -(TUG,WALK,EEG) \'POSITIVO\' significa che è positivo al Parkinson \n\n -(TAU) \'POSITIVO\' significa che è positivo al Parkinson di tipo TAU")


import sv_ttk

# creo la finestra principale
root = tk.Tk()
root.geometry("1024x800")
root.resizable(False, False)
root.title("Parkinson Classifier")


#sv_ttk.use_dark_theme()

#sv_ttk.use_light_theme()

#button = ttk.Button(root, text="Toggle theme", command=sv_ttk.toggle_theme)
#button.pack()

# Set the initial theme


# Pack a big frame so, it behaves like the window background



sv_ttk.set_theme("light")
image = Image.open("code/setup/icon/question_mark.png")  # Sostituisci "question_mark.png" con il percorso dell'immagine sul tuo sistema
image = image.resize((50, 32))  # Regola le dimensioni dell'icona se necessario
icon = ImageTk.PhotoImage(image)
  

progress_var = tk.DoubleVar()
style = ttk.Style()
style.configure("Custom.Horizontal.TProgressbar",
                troughcolor='#e0e0e0',
                bordercolor='#e0e0e0',
                background='#69c0ff',
                troughrelief='flat',
                relief='flat')
style.layout("Custom.Horizontal.TProgressbar",
             [('Custom.Horizontal.TProgressbar.trough',
               {'children': [('Custom.Horizontal.TProgressbar.pbar',
                              {'sticky': 'ns',
                               'children': [('Custom.Horizontal.TProgressbar.label',
                                              {'sticky': 'nswe'})],
                               'side': 'left',
                               'expand': 1})],
                'sticky': 'nswe'})])

progress_bar = ttk.Progressbar(root, mode='determinate', style="Custom.Horizontal.TProgressbar",
                               variable=progress_var, length=250)
progress_bar.pack(pady=20)
progress_bar['maximum'] = 100
progress_bar.place(x=500, y=700)





fixed_label = tk.Label(root, text="RESULT (Parkinson)") #ci dice se è parkinson o controlli
fixed_label.place(x=500, y=600)
textbox23_val = tk.StringVar()
textbox23_val.set("")
textbox23 = tk.Entry(root, width=45,state="readonly",textvariable=textbox23_val,disabledbackground="white")
textbox23.place(x=610, y=600)

fixed_label = tk.Label(root, text="RESULT (Response)") #ci dice se è parkinson o controlli
fixed_label.place(x=50, y=650)
textbox26_val = tk.StringVar()
textbox26_val.set("")
textbox26 = tk.Entry(root, width=45,state="readonly",textvariable=textbox26_val,disabledbackground="white")
textbox26.place(x=160, y=650)




info = tk.Button(root, command=show_info)
info.config(image=icon, width=50, height=32, relief="flat", bd=0)

info.pack()
info.place(x=700, y=10)




# creo le text box sulla destra
fixed_label = tk.Label(root, text="PD (UP)")
fixed_label.place(x=50, y=100)
textbox1_val = tk.StringVar()
textbox1_val.set("")
textbox1 = tk.Entry(root, width=45,state="readonly",textvariable=textbox1_val,disabledbackground="white")
textbox1.place(x=160, y=100)

# creo le text box sulla destra
fixed_label = tk.Label(root, text="PD (GO 1)")
fixed_label.place(x=50, y=150)
textbox2_val = tk.StringVar()
textbox2_val.set("")
textbox2 = tk.Entry(root, width=45,state="readonly",textvariable=textbox2_val,disabledbackground="white")
textbox2.place(x=160, y=150)

# creo le text box sulla destra
fixed_label = tk.Label(root, text="PD (SPIN 1)")
fixed_label.place(x=50, y=200)
textbox3_val = tk.StringVar()
textbox3_val.set("")
textbox3 = tk.Entry(root, width=45,state="readonly",textvariable=textbox3_val,disabledbackground="white")
textbox3.place(x=160, y=200)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="PD (BACK)")
fixed_label.place(x=50, y=250)
textbox4_val = tk.StringVar()
textbox4_val.set("")
textbox4 = tk.Entry(root, width=45,state="readonly",textvariable=textbox4_val,disabledbackground="white")
textbox4.place(x=160, y=250)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="PD (SPIN 2)")
fixed_label.place(x=50, y=300)
textbox5_val = tk.StringVar()
textbox5_val.set("")
textbox5 = tk.Entry(root, width=45,state="readonly",textvariable=textbox5_val,disabledbackground="white")
textbox5.place(x=160, y=300)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="PD (DOWN)")
fixed_label.place(x=50, y=350)
textbox6_val = tk.StringVar()
textbox6_val.set("")
textbox6 = tk.Entry(root, width=45,state="readonly",textvariable=textbox6_val,disabledbackground="white")
textbox6.place(x=160, y=350)

#--------------------------------------------------------------------------------------------



# creo le text box sulla destra
fixed_label = tk.Label(root, text="MCI (UP)")
fixed_label.place(x=500, y=100)
textbox7_val = tk.StringVar()
textbox7_val.set("")
textbox7 = tk.Entry(root, width=45,state="readonly",textvariable=textbox7_val,disabledbackground="white")
textbox7.place(x=610, y=100)

# creo le text box sulla destra
fixed_label = tk.Label(root, text="MCI (GO 1)")
fixed_label.place(x=500, y=150)
textbox8_val = tk.StringVar()
textbox8_val.set("")
textbox8 = tk.Entry(root, width=45,state="readonly",textvariable=textbox8_val,disabledbackground="white")
textbox8.place(x=610, y=150)

# creo le text box sulla destra
fixed_label = tk.Label(root, text="MCI (SPIN 1)")
fixed_label.place(x=500, y=200)
textbox9_val = tk.StringVar()
textbox9_val.set("")
textbox9 = tk.Entry(root, width=45,state="readonly",textvariable=textbox9_val,disabledbackground="white")
textbox9.place(x=610, y=200)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="MCI (BACK)")
fixed_label.place(x=500, y=250)
textbox20_val = tk.StringVar()
textbox20_val.set("")
textbox20 = tk.Entry(root, width=45,state="readonly",textvariable=textbox20_val,disabledbackground="white")
textbox20.place(x=610, y=250)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="MCI (SPIN 2)")
fixed_label.place(x=500, y=300)
textbox21_val = tk.StringVar()
textbox21_val.set("")
textbox21 = tk.Entry(root, width=45,state="readonly",textvariable=textbox21_val,disabledbackground="white")
textbox21.place(x=610, y=300)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="MCI (DOWN)")
fixed_label.place(x=500, y=350)
textbox22_val = tk.StringVar()
textbox22_val.set("")
textbox22 = tk.Entry(root, width=45,state="readonly",textvariable=textbox22_val,disabledbackground="white")
textbox22.place(x=610, y=350)

#------------------------------------------------------------------------------------------------


# creo le text box sulla destra
fixed_label = tk.Label(root, text="Response (UP)")
fixed_label.place(x=50, y=400)
textbox12_val = tk.StringVar()
textbox12_val.set("")
textbox12 = tk.Entry(root, width=45,state="readonly",textvariable=textbox12_val,disabledbackground="white")
textbox12.place(x=160, y=400)

# creo le text box sulla destra
fixed_label = tk.Label(root, text="Response (GO 1)")
fixed_label.place(x=50, y=450)
textbox13_val = tk.StringVar()
textbox13_val.set("")
textbox13 = tk.Entry(root, width=45,state="readonly",textvariable=textbox13_val,disabledbackground="white")
textbox13.place(x=160, y=450)

# creo le text box sulla destra
fixed_label = tk.Label(root, text="Response (SPIN 1)")
fixed_label.place(x=50, y=500)
textbox14_val = tk.StringVar()
textbox14_val.set("")
textbox14 = tk.Entry(root, width=45,state="readonly",textvariable=textbox14_val,disabledbackground="white")
textbox14.place(x=160, y=500)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="Response (BACK)")
fixed_label.place(x=500, y=400)
textbox15_val = tk.StringVar()
textbox15_val.set("")
textbox15 = tk.Entry(root, width=45,state="readonly",textvariable=textbox15_val,disabledbackground="white")
textbox15.place(x=610, y=400)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="Response (SPIN 2)")
fixed_label.place(x=500, y=450)
textbox16_val = tk.StringVar()
textbox16_val.set("")
textbox16 = tk.Entry(root, width=45,state="readonly",textvariable=textbox16_val,disabledbackground="white")
textbox16.place(x=610, y=450)


# creo le text box sulla destra
fixed_label = tk.Label(root, text="Response (DOWN)")
fixed_label.place(x=500, y=500)
textbox17_val = tk.StringVar()
textbox17_val.set("")
textbox17 = tk.Entry(root, width=45,state="readonly",textvariable=textbox17_val,disabledbackground="white")
textbox17.place(x=610, y=500)

#--------------------------------------------------------------------------------------------



fixed_label = tk.Label(root, text="PD (EEG)") #ci dice se è parkinson o controlli
fixed_label.place(x=50, y=550)
textbox18_val = tk.StringVar()
textbox18_val.set("")
textbox18 = tk.Entry(root, width=45,state="readonly",textvariable=textbox18_val,disabledbackground="white")
textbox18.place(x=160, y=550)


fixed_label = tk.Label(root, text="MCI (EEG)") #ci dice se è parkinson o controlli
fixed_label.place(x=500, y=550)
textbox19_val = tk.StringVar()
textbox19_val.set("")
textbox19 = tk.Entry(root, width=45,state="readonly",textvariable=textbox19_val,disabledbackground="white")
textbox19.place(x=610, y=550)


fixed_label = tk.Label(root, text="Response (EEG)") #ci dice se è parkinson o controlli
fixed_label.place(x=50, y=600)
textbox24_val = tk.StringVar()
textbox24_val.set("")
textbox24 = tk.Entry(root, width=45,state="readonly",textvariable=textbox24_val,disabledbackground="white")
textbox24.place(x=160, y=600)





tug_var = tk.BooleanVar()
tug_checkbutton = tk.Checkbutton(root, text="TUG", variable=tug_var)
# Posizionamento della checkbox
tug_checkbutton.place(x=50, y=50)



eeg_var = tk.BooleanVar()
tug_checkbutton = tk.Checkbutton(root, text="EEG", variable=eeg_var)
# Posizionamento della checkbox
tug_checkbutton.place(x=150, y=50)

'''
response_tug_var = tk.BooleanVar()
response_tug_var_checkbutton = tk.Checkbutton(root, text="Response TUG", variable=response_tug_var)
# Posizionamento della checkbox
response_tug_var_checkbutton.place(x=250, y=50)


response_eeg_var = tk.BooleanVar()
response_eeg_var_checkbutton = tk.Checkbutton(root, text="Response EEG", variable=response_eeg_var)
# Posizionamento della checkbox
response_eeg_var_checkbutton.place(x=400, y=50)
'''




# creo il pulsante "Start"
start_button = tk.Button(root,width=20, text="Start", command=start_function)
start_button.place(x=100, y=700)



# crea un pulsante "Reset"
reset_button = tk.Button(root,width=20, text="Reset", command=reset_function)
reset_button.place(x=300, y=700)



# avvio la finestra principale
root.mainloop()
