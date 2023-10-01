import csv
data = r"C:\Users\User\Downloads\7-_WYKAZ_IMION_MĘSKICH_WG_POLA_IMIĘ_PIERWSZE_WYSTĘPUJĄCYCH_W_REJESTRZE_PESEL_Z_UWZGLĘDNIENIEM_IMION_OSÓB_ZMARŁYCH.csv"
data_save = r"C:\Users\User\Downloads\Wykaz_imion_meskich.txt"
imiona = []

with open(data, 'r', encoding="utf-8") as f:
    csv_file = csv.reader(f)
    next(csv_file)
    for row in csv_file:
        imiona.append(row[0])

with open(data_save, 'w', encoding='utf-8') as save:
    for i in imiona:
        save.write(i+'\n')