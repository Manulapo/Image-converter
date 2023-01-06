import os
from PIL import Image
# Specifica la cartella da controllare
value = input('Seleziona cartella:')
folder = 'F:/Scrivania/' + value
quality = 80

def check_folder(path):
  # Ottieni tutti i file e le sottocartelle della cartella
  items = os.listdir(path)
  # Per ogni elemento della cartella
  for item in items:
    # Costruisci il percorso completo del file o della cartella
    item_path = os.path.join(path, item)
    # Verifica se è una cartella
    if os.path.isdir(item_path):
      # Se è una cartella, esegui lo script all'interno della cartella
      check_folder(item_path)
    else:
      # Se è un file, verifica se è un'immagine
        item_path = os.path.join(path, item)
        if item.endswith('.jpg'):
        # Se è un'immagine, apri il file con Pillow
            image = Image.open(item_path)
            # Converti l'immagine in formato JPEG
            image.save(item_path, quality=quality)
            print(item, 'converted')
        elif item.endswith('.png'):
            # Se è un'immagine, apri il file con Pillow
            image = Image.open(item_path)
            # Converti l'immagine in formato JPEG
            image_converted = image.convert('RGB')
            image_converted.save(item_path, quality=quality)
            print(item, 'converted')

check_folder(folder)
print('Conversione Riuscita')
