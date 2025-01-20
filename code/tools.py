import numpy as np
import scipy
from scipy import signal
from scipy import stats
import pandas as pd
import os
stamp= False
import csv
import shutil



def clean(directory_path):
  # Percorso della directory da pulire
  #directory_path = 'code/inference/tug'

  # Itera sui file nella directory e rimuovili
  for filename in os.listdir(directory_path):
      file_path = os.path.join(directory_path, filename)
      if os.path.isfile(file_path):
          os.remove(file_path)

def process_file(folder_path_tug):
  from sqlalchemy.sql.expression import true
from scipy import stats







stamp= False
#folder_path_tug_walk= '/content/drive/MyDrive/LAVORO/Partita Iva/Bando dipartimento di scienze/Sviluppo/Data/TUG/Controlli/Linguaglossa Salvatore/Dati grezzi/tug1.txt'

def process_file(folder_path_tug, type,filename,map):
  with open(folder_path_tug, encoding='iso-8859-1') as f:
                  lines = f.readlines()
                  data = [line.strip().split() for line in lines[17:]]
                  df = pd.DataFrame(data, columns=['time', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'roll', 'pitch', 'yaw'])

                  dir="code/inference/tug/tmp"
                  print(dir)

                  if not os.path.exists(dir):
                    os.makedirs(dir)

                  e1=int(float(map[filename][0])*100)#100hz
                  e2=int(float(map[filename][1])*100)#100hz
                  e3=int(float(map[filename][2])*100)#100hz
                  e4=int(float(map[filename][3])*100)#100hz
                  e5=int(float(map[filename][4])*100)#100hz
                  e6=int(float(map[filename][5])*100)#100hz
                  print(map)
                  df_e1=df.head(e1)
                  df_e2=df[e1:(e1+e2)]
                  df_e3=df[(e1+e2):(e1+e2+e3)]
                  df_e4=df[(e1+e2+e3):(e1+e2+e3+e4)]
                  df_e5=df[(e1+e2+e3+e4):(e1+e2+e3+e4+e5)]
                  df_e6=df[(e1+e2+e3+e4+e5):]
                  n=filename.split(type)[1].split('.txt')[0]
                  df_e1.to_csv(dir+'/e1_'+n+'.csv', index=False) # up
                  df_e2.to_csv(dir+'/e2_'+n+'.csv', index=False) # go walk
                  df_e3.to_csv(dir+'/e3_'+n+'.csv', index=False) # spin 1
                  df_e4.to_csv(dir+'/e4_'+n+'.csv', index=False) # back
                  df_e5.to_csv(dir+'/e5_'+n+'.csv', index=False) # spin 2
                  df_e6.to_csv(dir+'/e6_'+n+'.csv', index=False) # down
                  return


def process_file_2(folder_path_tug,filename,map):
  with open(folder_path_tug, encoding='utf-16') as f:
                  lines = f.readlines()
                  data = [line.strip().split() for line in lines[8:]]

                  map[filename]=[data[0][2],data[1][3], data[2][3], data[3][3], data[4][3],data[5][2]]
                  print(map)
                  return map




def append_csv(source_file, target_file):
    with open(source_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)[1:]  # Salta la prima riga (intestazione)
    write_header = not os.path.exists(target_file)
    with open(target_file, 'a', newline='') as csv_file:

        writer = csv.writer(csv_file)
        if write_header:
            header = ['time', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z', 'roll', 'pitch', 'yaw']
            writer.writerow(header)
        writer.writerows(data)



def tug(folder_path_tug_base, typep):
  map = {}
  #try:
    #map=eeg_elaborated(file, typep)
  for filename in os.listdir(folder_path_tug_base+typep+"/Dati elaborati"):
    if typep in filename:
      file_path = os.path.join(folder_path_tug_base+typep+"/Dati elaborati", filename)

      process_file_2(file_path,filename, map)

  for filename in os.listdir(folder_path_tug_base+typep+"/Dati grezzi"):
    if typep in filename:
      file_path = os.path.join(folder_path_tug_base+typep+"/Dati grezzi", filename)
      #print(file_path)
      df_buff=process_file(file_path, typep,filename,map)
  '''except Exception as e:
      print(e)
      pass'''
  return



def compactTug(file, typep,typep2):
  TUG_df = pd.DataFrame()
  # ciclo attraverso tutti i file nella cartella
  folder_path=file+'/'

 

  for f in os.listdir(folder_path):
    file_path = os.path.join(folder_path, f)
    for i in range(1,7):
      e= "e"+str(i)
      if e in file_path:
        output="code/inference/tug/"+"global_"+e+".csv"

        append_csv(file_path, output)
        print(output)

  return ""


def create_inference_tug_df():

    folder_path_tug_base  = 'data/'
    t= "tug"
    typep2="Tug"
    tug( folder_path_tug_base, t)
    compactTug("code/inference/tug/tmp/",t,typep2)
    shutil.rmtree("code/inference/tug/tmp/")





#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


folder_path_eeg = 'data/eeg/'

def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def eeg():
  EEG_df = pd.DataFrame()
  # ciclo attraverso tutti i file nella cartella
  folder_path=folder_path_eeg
  print("------->", folder_path)
  for ff in os.listdir(folder_path):
      
      if  ff != ".ipynb_checkpoints":  # o qualsiasi altro formato di file
          file_path = os.path.join(folder_path, ff)
          try:
            with open(file_path, encoding='iso-8859-1') as f:
                lines = f.readlines()
            # loggo i dati dalla riga 8 in poi
            data = [line.strip().split() for line in lines[10:]]
            # creo il DataFrame
            df = pd.DataFrame(data, columns=['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10', 'g11', 'g12', 'g13', 'g14', 'g15', 'g16', 'g17', 'g18', 'g19', 'g20', 'g21'])
            df = df.drop('g21', axis=1)
            #print(filename)
            #print(df) 
            EEG_df = pd.concat([EEG_df, df], axis=0)
          except Exception as e:
            print("Error!", e)

  EEG_df['is_float'] = EEG_df['g1'].apply(is_float)
  # selezioniamo le righe del dataframe che non contengono un float nella colonna2
  rows_to_drop = EEG_df.loc[~EEG_df['is_float'], :].index
  # eliminiamo le righe selezionate dal dataframe
  EEG_df = EEG_df.drop(rows_to_drop)
  # eliminiamo la colonna temporanea creata con i risultati della funzione
  EEG_df = EEG_df.drop('is_float', axis=1)
  return EEG_df


def create_inference_eeg():
  eeg_df=eeg()
  eeg_df.to_csv('code/inference/eeg/eeg.csv', index=False)


def weighted_average(results, weights, threshold=0.5):
    weighted_sum = sum(result * weight for result, weight in zip(results, weights))
    sum_weights = sum(weights)
    weighted_average = weighted_sum / sum_weights

    if weighted_average > threshold:
        return 1,weighted_average
    else:
        return 0,weighted_average