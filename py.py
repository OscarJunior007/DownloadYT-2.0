import tkinter
from customtkinter  import *
import yt_dlp

from pytube import YouTube
from tkinter import messagebox

ventana = CTk()
ventana.title('Descargar MP3 YT')
ventana.geometry('800x400')
def descargar():

    url = link.get()
    if not url:
        messagebox.showinfo(title='Informacion',message='Debes pegar un link')
    if salsa.get() == 'on' and mp4.get() == 'on':
        ydl_opts = {
            'format': 'bestvideo + bestaudio/best',  # FFmpeg
            'outtmpl': 'C:\\Musica\\salsa\\ %(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
    elif salsa.get() == 'on' and mp3.get() == 'on':
        ydl_opts = {
            'format': 'bestaudio',  # Solo audio en máxima calidad
            'outtmpl': 'C:\\Musica\\salsa\\  %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extraer audio con FFmpeg
                'preferredcodec': 'mp3',  # Formato de audio preferido
                'preferredquality': '320',  # Calidad de audio (192 kbps)
            }],
        }
    elif vallenato.get() == 'on' and mp4.get() == 'on':
        ydl_opts = {
            'format': 'bestvideo + bestaudio/best',  # FFmpeg
            'outtmpl': 'C:\\Musica\\Vallenato\\ %(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
    elif vallenato.get() == 'on' and mp3.get() == 'on':
        ydl_opts = {
            'format': 'bestaudio',  # Solo audio en máxima calidad
            'outtmpl': 'C:\\Musica\\Vallenato\\  %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extraer audio con FFmpeg
                'preferredcodec': 'mp3',  # Formato de audio preferido
                'preferredquality': '320',  # Calidad de audio (192 kbps)
            }],
        }
    elif champeta.get() == 'on' and mp4.get() == 'on':
        ydl_opts = {
            'format': 'bestvideo + bestaudio/best',  # FFmpeg
            'outtmpl': 'C:\\Musica\\champeta\\ %(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
    elif champeta.get() == 'on' and mp3.get() == 'on':
        ydl_opts = {
            'format': 'bestaudio',  # Solo audio en máxima calidad
            'outtmpl': 'C:\\Musica\\champeta\\  %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extraer audio con FFmpeg
                'preferredcodec': 'mp3',  # Formato de audio preferido
                'preferredquality': '320',  # Calidad de audio (192 kbps)
            }],
        }
    elif reggeton.get() == 'on' and mp4.get() == 'on':
        ydl_opts = {
            'format': 'bestvideo + bestaudio/best',  # FFmpeg
            'outtmpl': 'C:\\Musica\\champeta\\ %(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
    elif reggeton.get() == 'on' and mp3.get() == 'on':
        ydl_opts = {
            'format': 'bestaudio',  # Solo audio en máxima calidad
            'outtmpl': 'C:\\Musica\\reggeton\\  %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extraer audio con FFmpeg
                'preferredcodec': 'mp3',  # Formato de audio preferido
                'preferredquality': '320',  # Calidad de audio (192 kbps)
            }],
        }
    else:
        ydl_opts = {
            'format': 'bestaudio',  # Solo audio en máxima calidad
            'outtmpl': 'C:\\Musica\\ %(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extraer audio con FFmpeg
                'preferredcodec': 'mp3',  # Formato de audio preferido
                'preferredquality': '320',  # Calidad de audio (192 kbps)
            }],
        }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            info = ydl.extract_info(url,download=False)
            titulo = info.get('title','titulo desconocido')
            if mp3.get() =='on':
                messagebox.showinfo(title='infomacion',message=f'{titulo}, se descargo exitosamente en formato MP3!')
            elif mp4.get() == 'on':
                messagebox.showinfo(title='infomacion', message=f'{titulo}, se descargo exitosamente en formato MP4!')
        print("Descarga completa")
    except Exception as e:
        print(f"Hubo un problema{e}")
        messagebox.showerror(title='ERROR', message=f'{titulo},No se pudo descargar, codigo error ({e})!')



is_light = True
def mode():
    global is_light
    #print(is_light)
    if is_light:
        boton_descargar.configure(text="Descargar",fg_color= "#000000",text_color='#FFFFFF')
        boton_mode.configure(text="Mode Dark",fg_color= "#000000",text_color='#FFFFFF')
        set_appearance_mode('light')
    else:
        boton_descargar.configure(text="Descargar",text_color='#000000',fg_color= "#FFFFFF")
        boton_mode.configure(text="Mode Light",text_color='#000000',fg_color= "#FFFFFF")
        set_appearance_mode('dark')
    is_light = not is_light

def selected_check():
   if vallenato.get() =='on':
        boton_descargar.configure(text="Descargar Vallenato")
        salsa_check.deselect()
        champeta_check.deselect()
        reggeton_check.deselect()
   if salsa.get() == 'on':
       boton_descargar.configure(text="Descargar Salsa")
       champeta_check.deselect()
       vallenato_check.deselect()
       reggeton_check.deselect()
   if champeta.get() == 'on':
       boton_descargar.configure(text="Descargar Champeta")
       vallenato_check.deselect()
       salsa_check.deselect()
       reggeton_check.deselect()
   if reggeton.get() == 'on':
       boton_descargar.configure(text="Descargar Reggeton")
       vallenato_check.deselect()
       salsa_check.deselect()
       champeta_check.deselect()
   if mp4.get() == 'on':
       mp3_check.deselect()

   if mp3.get() == 'on':
       mp4_check.deselect()

vallenato = tkinter.StringVar(value='off')
vallenato_check = CTkCheckBox(master=ventana,text='Crear carpeta Vallenato',variable=vallenato,onvalue='on',offvalue='off',command=selected_check)
vallenato_check.place(relx='0.11',rely='0.17',anchor='center')

salsa = tkinter.StringVar(value='off')
salsa_check = CTkCheckBox(master=ventana,text='Crear carpeta Salsa',variable=salsa,onvalue='on',offvalue='off',command=selected_check)
salsa_check.place(relx='0.10',rely='0.26',anchor='center')

champeta = tkinter.StringVar(value='off')
champeta_check = CTkCheckBox(master=ventana,text='Crear carpeta Champeta',variable=champeta,onvalue='on',offvalue='off',command=selected_check)
champeta_check.place(relx='0.12',rely='0.35',anchor='center')

reggeton = tkinter.StringVar(value='off')
reggeton_check = CTkCheckBox(master=ventana,text='Crear carpeta reggeton',variable=reggeton,onvalue='on',offvalue='off',command=selected_check)
reggeton_check.place(relx='0.12',rely='0.45',anchor='center')

mp4 = tkinter.StringVar(value='off')
mp4_check = CTkCheckBox(master=ventana,text='MP4',variable=mp4,onvalue='on',offvalue='off',command=selected_check)
mp4_check.place(relx='0.10',rely='0.9',anchor='center')

mp3 = tkinter.StringVar(value='off')
mp3_check = CTkCheckBox(master=ventana,text='MP3',variable=mp3,onvalue='on',offvalue='off',command=selected_check)
mp3_check.place(relx='0.10',rely='0.8',anchor='center')

boton_descargar = CTkButton(master=ventana,text='Descargar',text_color='#000000',font=('Lucida Console',20), fg_color= "#FFFFFF",command=descargar,corner_radius=10,hover=True,hover_color="#FF0000",border_color='#FFFFFF')
boton_descargar.place(relx='0.5',rely='0.6',anchor='center')

boton_mode:CTkButton = CTkButton(master=ventana,text='Chose Mode', fg_color= "#3b8cc6",command=mode,corner_radius=10,hover=True,hover_color="#FF0000",border_color='#FFFFFF')
boton_mode.place(relx='0.9',rely='0.9',anchor='center')

message = CTkLabel(master=ventana, text='La descarga puede durar entre 10-20 seugndos')
message.place(relx='0.5',rely='0.7',anchor='center')

message2 = CTkLabel(master=ventana,font=('arial',15), text='Las canciones se guardaran "Disco local C:" en un carpeta llamada (musica) \n y se creara una carpeta extra dependiendo el genero elegido.')
message2.place(relx='0.5',rely='0.8',anchor='center')

message3 = CTkLabel(master=ventana, text='Desarollado por Oscar Mejia.',text_color='#FF0000',font=('Magneto',15))
message3.place(relx='0.8',rely='0.10',anchor='center')

message4 = CTkLabel(master=ventana, text='Elegir genero:',text_color='#FF0000',font=('arial',18))
message4.place(relx='0.12',rely='0.10',anchor='center')

mode = set_appearance_mode('Dark')

link =  CTkEntry(master=ventana,placeholder_text='Pega el link aqui')
link.place(relx='0.5',rely='0.5',anchor='center')

ventana.mainloop()