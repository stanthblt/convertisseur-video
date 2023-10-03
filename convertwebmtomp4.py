import os

print("")
print("")
print("Convertisseur Webm vers mp4 Made by stanthblt")
print("")
print("https://github.com/stanthblt")
print("")
print("")

def convert_webm_to_mp4(input_file, output_file):
    command = f'ffmpeg -i {input_file} {output_file}'
    os.system(command)
print("Entrez le chemin complet du fichier vidéo ou faites glisser votre fichier")
input_file = input("(ex: /Users/votre_nom_user/Downloads/test.webm): ")
print("Entrez le chemin complet du fichier de sortie")
output_file = input("(ex: /Users/votre_nom_user/Downloads/test.mp4): ")
convert_webm_to_mp4(input_file, output_file)
