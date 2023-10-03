import subprocess

print("")
print("")
print("Convertisseur Webm vers mov (format ProRes) Made by stanthblt")
print("")
print("https://github.com/stanthblt")
print("")
print("")

def convert_webm_to_mov(input_file, output_file):
    command = f'ffmpeg -i {input_file} -c:v prores -profile:v 3 -c:a pcm_s16le {output_file}'
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    print("Entrez le chemin complet du fichier vidéo ou faites glisser votre fichier")
    input_file = input("(ex: /Users/votre_nom_user/Downloads/test.webm): ")
    print("Entrez le chemin complet du fichier de sortie")
    output_file = input("(ex: /Users/votre_nom_user/Downloads/test.mov): ")

    convert_webm_to_mov(input_file, output_file)
