from pytube import YouTube
from tkinter import filedialog
from tkinter import Tk
from sys import argv
from moviepy.editor import AudioFileClip
import os

def escolher_pasta():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', 1)
    download_dir = filedialog.askdirectory()
    root.destroy()
    try:
        download_path = ys.download(download_dir)
        print("Download completo!!")
        return download_dir
    except Exception as e:
        print(f"Ocorreu um erro ao tentar baixar o vídeo: {e}")




link = argv[1] if len(argv) > 1 else input("Digite o link do vídeo: ")

try:
    yt = YouTube(link)
except Exception as e:
    print(f"Ocorreu um erro ao tentar acessar o vídeo")
    exit()

print("Deseja ver as informações do vídeo? (s/n) ")
ask = input()

if ask == 's' or ask == 'S':
    print("Título: ", yt.title)
    print("Número de views: ", yt.views)
    print("Tamanho do vídeo: ", yt.length, "segundos")
    print("Avaliação do vídeo: ", yt.rating)
else:
    print("Ok")

ask = input("Deseja baixar o vídeo? (s/n) \n")
if ask == 's' or ask == 'S':
    qualidade = input("Deseja baixar a melhor qualidade? (s/n)\n")
    if qualidade == 's' or qualidade == 'S':
        ys = yt.streams.get_highest_resolution()
        print("Baixando...")
        escolher_pasta()

    else:
        qualidade = input("Qual qualidade deseja baixar? (360p, 720p, 1080p)\n ")

        if qualidade == '360p' or qualidade == '720p' or qualidade == '1080p':
            ys = yt.streams.get_by_resolution(qualidade)
            print("Baixando...")
            escolher_pasta()
        else:
            print("Opção inválida!!")     

else:
    print("Deseja baixar o áudio? (s/n) ")
    ask = input()
    if ask == 's' or ask == 'S':
        ys = yt.streams.get_audio_only()
        print("Baixando...")
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', 1)
        download_dir = filedialog.askdirectory()
        root.destroy() 

        try:
            download_path = ys.download(download_dir)
        except Exception as e:
            print(f"Ocorreu um erro ao tentar baixar o vídeo: {e}")

        mp4_path = download_path
        mp3_path = mp4_path.replace(".mp4", ".mp3")

        audioclip = AudioFileClip(mp4_path)
        audioclip.write_audiofile(mp3_path)
        audioclip.close()
        print(mp4_path)
        os.remove(mp4_path)

        print("Download concluido!")

    else:
        print("Finalizando programa...")