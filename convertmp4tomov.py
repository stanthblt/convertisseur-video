import subprocess

print("")
print("")
print("Convertisseur mp4 vers mov Made by stanthblt")
print("")
print("https://github.com/stanthblt")
print("")
print("")

def convert_mp4_to_mov(input_file, output_file):
    command = f'ffmpeg -i "{input_file}" -c:v copy -c:a aac "{output_file}"'
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    print("Entrez le chemin complet du fichier vidéo ou faites glisser votre fichier")
    input_file = input("(ex: /Users/votre_nom_user/Downloads/test.mp4): ")
    print("Entrez le chemin complet du fichier de sortie")
    output_file = input("(ex: /Users/votre_nom_user/Downloads/test.mov): ")
    convert_mp4_to_mov(input_file, output_file)
