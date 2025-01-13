import csv

def convert_txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for line in infile:
            # Sépare les colonnes par un espace ou une virgule (selon le format du .txt)
            row = line.strip().split()  
            writer.writerow(row)

    print(f"Conversion terminée : {output_file} généré avec succès.")

# Appel de la fonction
convert_txt_to_csv('exemple.txt', 'output.csv')
