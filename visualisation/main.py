from read_data_stream import read_most_recent_csv
from main_visualisation import monitoring_today_validation

if __name__ == "__main__":
    directory_total_path = "../data/output3/"
    directory_titre_path = "../data/output2/"
    directory_arret_path = "../data/output/"

    df_total = read_most_recent_csv(directory_total_path)
    df_titre = read_most_recent_csv(directory_titre_path)
    df_arret = read_most_recent_csv(directory_arret_path)

    df_total = df_total.sort_index()
    df_titre = df_titre.sort_values(by = ['JOUR', 'CATEGORIE_TITRE'])
    df_arret = df_arret.sort_values(by = ['JOUR', 'LIBELLE_ARRET'])


    print(df_total)
    print(df_titre)
    print(df_arret)

    monitoring_today_validation(df_total, df_titre, df_arret)
