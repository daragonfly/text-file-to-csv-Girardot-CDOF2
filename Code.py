import csv

def convert_tete_to_csv(input_file, output_file):
    # Lire les données du fichier d'entrée
    with open(input_file, 'r') as infile:
        data = infile.readlines()
    
    # Écriture dans le fichier de sortie
    with open(output_file, 'w') as outfile:
        writer = csv.writer(outfile)
        
        writer.writerow(["Col1", "Col2", "Col3", "Col4"])  # Supposition des colonnes
        
        for line in data:
            row = line.strip().split(",")  
        
            writer.writerow(row)
    
    print("Fichier converti avec succès !")

# Appel de la fonction
convert_tete_to_csv("fichier.tete", "output.csv")
