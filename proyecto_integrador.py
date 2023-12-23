from datasets import load_dataset
import numpy as np

# Descarga y carga el dataset
dataset = load_dataset("mstz/heart_failure")

# Accede a la partición 'train' del dataset
data = dataset["train"]

# Muestra la estructura del dataset
print(data)

# Accede a la lista de edades y calcula el promedio
ages_list = data['age']  
ages_np_array = np.array(ages_list)  
average_age = np.mean(ages_np_array)

print("El promedio de edad de las personas participantes es:", average_age)
