import pandas as pd
from keras.models import load_model
import collections
import joblib



def inference_tug_PD_UP():
    df_infer = pd.read_csv("code/inference/tug/global_e1.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_pd_controlli_e1.joblib")
    # Utilizzare il modello caricato per effettuare l'inferenza sul nuovo dataset
    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)

    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]




def inference_tug_PD_GO1():
    df_infer = pd.read_csv("code/inference/tug/global_e2.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_pd_controlli_e2.joblib")
    # Utilizzare il modello caricato per effettuare l'inferenza sul nuovo dataset
    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)

    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]

def inference_tug_PD_SPIN1():
    df_infer = pd.read_csv("code/inference/tug/global_e3.csv")

    loaded_model = load_model("code/models/tug/keras_model_pd_controlli_e3.h5")

    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] =predicted_labels
    print(predicted_labels)
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)

    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]


def inference_tug_PD_BACK():
    df_infer = pd.read_csv("code/inference/tug/global_e4.csv")

    loaded_model = load_model("code/models/tug/keras_model_2_pd_controlli_e4.h5")

    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] =predicted_labels
    print(predicted_labels)
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)

    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]




def inference_tug_PD_SPIN2():
    df_infer = pd.read_csv("code/inference/tug/global_e5.csv")

    loaded_model = joblib.load("code/models/tug/knn_model_pd_controlli_e5.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]

def inference_tug_PD_DOWN():
    df_infer = pd.read_csv("code/inference/tug/global_e6.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_pd_controlli_e6.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]




def inference_eeg_pd_controlli():


    df_infer = pd.read_csv("code/inference/eeg/eeg.csv")
    # Caricare il modello esportato da un file

    loaded_model = load_model("code/models/eeg/keras_model_PD_Controlli_eeg.h5")

    # Utilizzare il modello addestrato per effettuare l'inferenza sul nuovo dataset
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] =predicted_labels
    #print(predicted_labels)
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)

    #print(counter)
    #print(most_common[0][0])
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza  ")
    rate=round((most_common[0][1])/len(predicted_labels)*100,2)
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return[int(most_common[0][0]),rate,"NEGATIVO con il "+  str(rate)+ "% di ricorrenza"]


def inference_eeg_mci_Nc():
    df_infer = pd.read_csv("code/inference/eeg/eeg.csv")
    loaded_model = joblib.load("code/models/eeg/clf_model_PD_Controlli_eeg.joblib")
    # Utilizzare il modello caricato per effettuare l'inferenza sul nuovo dataset
    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)
    df_infer['mode'] = predicted_labels
    #print(df_infer)
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    #print(counter)
    #print(most_common[0][0])
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=round((most_common[0][1])/len(predicted_labels)*100,2)
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return[int(most_common[0][0]),rate,"NEGATIVO con il "+  str(rate)+ "% di ricorrenza"]


def inference_eeg_resp():
    df_infer = pd.read_csv("code/inference/eeg/eeg.csv")
    loaded_model = joblib.load("code/models/eeg/clf_model_eeg_response.joblib")
    # Utilizzare il modello caricato per effettuare l'inferenza sul nuovo dataset
    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)
    df_infer['mode'] = predicted_labels
    #print(df_infer)
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    #print(counter)
    #print(most_common[0][0])
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=round((most_common[0][1])/len(predicted_labels)*100,2)
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return[int(most_common[0][0]),rate,"NEGATIVO con il "+  str(rate)+ "% di ricorrenza"]


def inference_tug_Response_UP():
    df_infer = pd.read_csv("code/inference/tug/global_e1.csv")

    loaded_model = joblib.load("code/models/tug/knn_model_oltre20_nonoltre20_e1.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]



def inference_tug_Response_GO1():
    df_infer = pd.read_csv("code/inference/tug/global_e2.csv")

    loaded_model = joblib.load("code/models/tug/knn_model_oltre20_nonoltre20_e2.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]


def inference_tug_Response_SPIN1():
    df_infer = pd.read_csv("code/inference/tug/global_e3.csv")

    loaded_model = load_model("code/models/tug/keras_model_2_oltre20_nonoltre20_e3.h5")
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]




def inference_tug_Response_BACK():
    df_infer = pd.read_csv("code/inference/tug/global_e4.csv")

    loaded_model = load_model("code/models/tug/keras_model_oltre20_nonoltre20_e4.h5")
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] = predicted_labels
    #print(type(predicted_labels))
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]



def inference_tug_Response_SPIN2():
    df_infer = pd.read_csv("code/inference/tug/global_e5.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_oltre20_nonoltre20_e5.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]




def inference_tug_Response_DOWN():
    df_infer = pd.read_csv("code/inference/tug/global_e6.csv")

    loaded_model = load_model("code/models/tug/keras_model_2_oltre20_nonoltre20_e6.h5")
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] = predicted_labels
    #print(type(predicted_labels))
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]





def inference_tug_MCI_UP():
    df_infer = pd.read_csv("code/inference/tug/global_e1.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_mci_nc_e1.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]



def inference_tug_MCI_GO1():
    df_infer = pd.read_csv("code/inference/tug/global_e2.csv")

    loaded_model = load_model("code/models/tug/keras_model_2_mci_nc_e2.h5")
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] = predicted_labels
    #print(type(predicted_labels))
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]


def inference_tug_MCI_SPIN1():
    df_infer = pd.read_csv("code/inference/tug/global_e3.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_mci_nc_e3.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]







def inference_tug_MCI_BACK():
    df_infer = pd.read_csv("code/inference/tug/global_e4.csv")

    loaded_model = load_model("code/models/tug/keras_model_2_mci_nc_e4.h5")
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] = predicted_labels
    #print(type(predicted_labels))
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]



def inference_tug_MCI_SPIN2():
    df_infer = pd.read_csv("code/inference/tug/global_e5.csv")

    loaded_model = joblib.load("code/models/tug/clf_model_mci_nc_e5.joblib")

    predicted_labels = loaded_model.predict(df_infer)
    print("Etichette previste per il nuovo dataset:", predicted_labels)

    df_infer['label'] = predicted_labels
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]

def inference_tug_MCI_DOWN():
    df_infer = pd.read_csv("code/inference/tug/global_e6.csv")

    loaded_model = load_model("code/models/tug/keras_model_2_mci_nc_e6.h5")
    predicted_labels = loaded_model.predict(df_infer)
    predicted_labels = [list(row).index(max(row)) for row in predicted_labels]
    df_infer['label'] = predicted_labels
    #print(type(predicted_labels))
    counter = collections.Counter(predicted_labels)
    most_common = counter.most_common(1)
    print("La classe predetta è " + str(most_common[0][0])+ " con il "+ str((most_common[0][1])/len(predicted_labels)*100), "% di ricorrenza ")
    rate=(most_common[0][1])/len(predicted_labels)*100
    if int(most_common[0][0]) == 1:
        return [int(most_common[0][0]),rate,"POSITIVO con il "+ str(rate)+ "% di ricorrenza"]
    else:
        return [int(most_common[0][0]),rate,"NEGATIVO con il "+ str(rate)+ "% di ricorrenza"]