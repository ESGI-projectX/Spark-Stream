from read_data_stream import read_most_recent_csv
from main_visualisation import monitoring_today_validation

if __name__ == "__main__":
    directory_total_path = "../data/ouput3"
    directory_titre_path = "../data/output2"
    directory_arret_path = "../data/output"

    df_total = read_most_recent_csv(directory_total_path)
    df_titre = read_most_recent_csv(directory_titre_path)
    df_arret = read_most_recent_csv(directory_arret_path)

    monitoring_today_validation(df_total, df_titre, df_arret)
