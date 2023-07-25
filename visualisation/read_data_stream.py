import os
import pandas as pd
import glob




def read_most_recent_csv(directory_path, number_files=46):
    file_pattern =  os.path.join(directory_path, "*csv")

    # files = [fichier for fichier in os.listdir(directory_path) if fichier.endswith(".csv")]
# Convert directory_path to an absolute path
    # absolute_path = os.path.abspath(directory_path)

    # List all files in directory_path
    # files = [os.path.join(absolute_path, f) for f in os.listdir(absolute_path) if f.endswith(".csv")]
    
    
    # "/home/duincan/Desktop/Spark-Stream/data/output3/*.csv"
    
    
    # os.path.join(directory_path, "*csv")

    print('ici')
    print(os.getcwd())
    print('la')

    files = glob.glob(file_pattern)

    


    # Trier les fichiers par date de modification (du plus récent au plus ancien)
    sorted_files = sorted(files, key=lambda x: os.path.getmtime(x))
    latest_files = sorted_files[-number_files:]
    


    # Lire et agréger les données des fichiers
    dataframes = []
    for file_path in latest_files:
        print(file_path)
        df = pd.read_csv(file_path, sep=",", parse_dates=['JOUR'], index_col='JOUR')

        

        

        if len(df) > 0:

            dataframes.append(df)
    merged_df = pd.concat(dataframes)

    return merged_df