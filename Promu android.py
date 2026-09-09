import tkinter as tk
from PIL import Image, ImageTk
from socket import *
from tkinter import messagebox, font
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter as sf
from scipy.integrate import cumtrapz
from funciones_fisica import *

def cerrar_ventana():
    root.destroy()

# Funciones para abrir las otras ventanas
def abrir_ventana_salto():
    salto_ventana.deiconify()
    root.withdraw()

def abrir_ventana_modo():
    ventana_modo.deiconify()
    root.withdraw()
    
def abrir_ventana_creditos():
    ventana_creditos.deiconify()
    root.withdraw()
    
def abrir_ventana_login():
    root.withdraw()
    global s
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(5)
    try:
        inicio_sesion.deiconify()
        s.connect(dir_socket_servidor)
        HELLO = 'HELLO ' + s.getsockname()[0]+ '\r\n'
        s.send(HELLO.encode())
        respuesta = s.recv(1024).decode()
        print(respuesta)
    except:
        messagebox.showerror(message="No se ha podido conectar al servidor. Comprueba si estás conectado a UPVNET", title="Error de conexión")
        volver_i()
        
def cambiar_tema(imagen):
    background_label.config(image=imagen)
    background_label1.config(image=imagen)
    background_label3.config(image=imagen)
    background_opciones.config(image=imagen)
    background_medidas.config(image=imagen)
    backgroundsalto.config(image=imagen)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Subway Jumpers")
root.geometry("800x700")

# Cargar las imágenes
img_iniciar_sesion = Image.open("sesion.png")
img_salto = Image.open("salto3.png")
img_modo = Image.open("modo4.png")
img_leaderboard = Image.open("leaderboard3.png")
img_creditos = Image.open("creditos2.png")
img_fondo = Image.open("fondo5.png")
img_insertar_usuario = Image.open("insertar_usuario.png")  # Nueva imagen para insertar usuario
img_volver = Image.open("volver.png")  # Nueva imagen para volver
img_contraseña = Image.open("insertar_contraseña.png") 
img_fondo_creditos = Image.open("fondocred1.png")
img_enviar_salto = Image.open("enviar_salto.png")
img_leaderboard2 = Image.open("leaderboard.png")
img_cerrar_sesion = Image.open("cerrar_sesion.png")
img_enviar = Image.open("enviar.png")
img_fondo2= Image.open("fondo2.png")
img_fondo6= Image.open("fondo6.png")
img_botonjake= Image.open("botonjake.png")
img_botontricky=Image.open("botontricky.png")
img_botonfresh=Image.open("botonfresh.png")
img_fondojake2=Image.open("modo_azul.png") 
img_fondotricky2=Image.open("modo_rosa.png") 
img_fondofresh2=Image.open("modo_verde.png")
img_fondo_personajes=Image.open("fondo_personajes2.png") 
img_fondo7= Image.open("fondo7.png")
img_analizarsalto= Image.open("analizarsalto.png")
img_top10= Image.open("top10.png")
img_fuerza= Image.open("fuerza.png")
img_potencia= Image.open("potencia.png")
img_velocidad= Image.open("velocidad.png")
img_fondosalto = Image.open("fondosalto.png")
img_fondoranking = Image.open("fondoranking.png")
img_fondoresultados = Image.open("fondoresultado.png")


# Redimensionar las imágenes
size = (200, 60)
img_iniciar_sesion = img_iniciar_sesion.resize(size)
img_salto = img_salto.resize(size)
img_modo = img_modo.resize(size)
img_leaderboard = img_leaderboard.resize(size)
img_creditos = img_creditos.resize(size)
img_insertar_usuario = img_insertar_usuario.resize(size)
img_volver = img_volver.resize(size)  
img_contraseña = img_contraseña.resize(size) 
img_enviar_salto = img_enviar_salto.resize(size)
img_leaderboard2 = img_leaderboard2.resize(size)
img_cerrar_sesion = img_cerrar_sesion.resize(size)
img_enviar = img_enviar.resize(size)
img_botonjake= img_botonjake.resize((230,140))
img_botontricky=img_botontricky.resize((230,140))
img_botonfresh=img_botonfresh.resize((230,140))
img_analizarsalto= img_analizarsalto.resize(size)
img_top10= img_top10.resize(size)
img_fuerza= img_fuerza.resize(size)
img_potencia=img_potencia.resize(size)
img_velocidad=img_velocidad.resize(size)
img_fondosalto= img_fondosalto.resize((1500,900))
img_fondoranking= img_fondoranking.resize((1500,900))
img_fondoresultados= img_fondoresultados.resize((1550,900))
img_fondojake2 = img_fondojake2.resize((1600,900))
img_fondotricky2= img_fondotricky2.resize((1600,900))
img_fondofresh2 = img_fondofresh2.resize((1600,900))
img_fondo2=img_fondo2.resize((1600,900))
img_fondo_personajes = img_fondo_personajes.resize((1600,900))
#Asignar
img_iniciar_sesion = ImageTk.PhotoImage(img_iniciar_sesion)
img_salto = ImageTk.PhotoImage(img_salto)
img_modo = ImageTk.PhotoImage(img_modo)
img_leaderboard = ImageTk.PhotoImage(img_leaderboard)
img_creditos = ImageTk.PhotoImage(img_creditos)
img_fondo = ImageTk.PhotoImage(img_fondo)
img_insertar_usuario = ImageTk.PhotoImage(img_insertar_usuario)  
img_volver = ImageTk.PhotoImage(img_volver) 
img_contraseña = ImageTk.PhotoImage(img_contraseña) 
img_fondo_creditos = ImageTk.PhotoImage(img_fondo_creditos)
img_enviar_salto = ImageTk.PhotoImage(img_enviar_salto)
img_leaderboard2 = ImageTk.PhotoImage(img_leaderboard2)
img_cerrar_sesion = ImageTk.PhotoImage(img_cerrar_sesion)
img_enviar = ImageTk.PhotoImage(img_enviar)
img_fondo6= ImageTk.PhotoImage(img_fondo6)
img_botonjake= ImageTk.PhotoImage(img_botonjake)
img_botontricky=ImageTk.PhotoImage(img_botontricky)
img_botonfresh= ImageTk.PhotoImage(img_botonfresh)
img_fondo2=ImageTk.PhotoImage(img_fondo2)
img_fondojake2 = ImageTk.PhotoImage(img_fondojake2)
img_fondotricky2= ImageTk.PhotoImage(img_fondotricky2)
img_fondofresh2 = ImageTk.PhotoImage(img_fondofresh2)
img_fondo_personajes = ImageTk.PhotoImage(img_fondo_personajes)
img_fondo7= ImageTk.PhotoImage(img_fondo7)
img_analizarsalto= ImageTk.PhotoImage(img_analizarsalto)
img_top10= ImageTk.PhotoImage(img_top10)
img_fuerza= ImageTk.PhotoImage(img_fuerza)
img_potencia= ImageTk.PhotoImage(img_potencia)
img_velocidad= ImageTk.PhotoImage(img_velocidad)
img_fondosalto = ImageTk.PhotoImage(img_fondosalto)
img_fondoranking= ImageTk.PhotoImage(img_fondoranking)
img_fondoresultados= ImageTk.PhotoImage(img_fondoresultados)


# Widget Label para mostrar la imagen de fondo
background_label = tk.Label(root, image=img_fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Botones
boton_iniciar_sesion = tk.Button(root, image=img_iniciar_sesion, command=abrir_ventana_login, width=180, height=40)
boton_iniciar_sesion.place(relx=0.51, rely=0.5, anchor="center")

boton_salto = tk.Button(root, image=img_salto, command=abrir_ventana_salto, width=180, height=40)
boton_salto.place(relx=0.51, rely=0.6, anchor="center")

boton_modo = tk.Button(root, image=img_modo, command=abrir_ventana_modo, width=180, height=40)
boton_modo.place(relx=0.51, rely=0.7, anchor="center")

boton_creditos = tk.Button(root, image=img_creditos, command=abrir_ventana_creditos, width=180, height=40)
boton_creditos.place(relx=0.51, rely=0.8, anchor="center")

# Ventana inicio de sesión

# info arqred

dir_IP_servidor = '158.42.188.200'
puerto_servidor = 64010
dir_socket_servidor = (dir_IP_servidor, puerto_servidor)
s = socket(AF_INET, SOCK_STREAM)

# funciones botones is

def introducir_usuario():
    usuario = usuario_texto.get()
    USER = 'USER ' + usuario + '\r\n'
    print(USER)
    
    s.send(USER.encode())
    respuesta = s.recv(1024).decode()
    print(respuesta)
    if respuesta[:3] == '200':
        boton_contraseña.pack_forget()
        contraseña_texto.pack(pady=30)
        boton_contraseña.pack(pady=30)
    else:
        messagebox.showerror(message="Usuario no registrado", title="Error de usuario")

def introducir_contraseña():
    contraseña = contraseña_texto.get()
    PASS = 'PASS ' + contraseña + '\r\n'
    print(PASS)
    s.send(PASS.encode())
    respuesta = s.recv(1024).decode()
    if respuesta[:3] == '200':
        messagebox.showinfo(message="Bienvenido", title="Conectado")
        volver(opciones,inicio_sesion)
    else:
        messagebox.showerror(message="Contraseña incorrecta", title="Error de contraseña")

def volver(abrir, cerrar):
    abrir.deiconify()
    cerrar.withdraw()
    
def volver_i():
    s.close()
    volver(root,inicio_sesion)

# Ventana y Botones inicio sesion

inicio_sesion = tk.Toplevel() 
inicio_sesion.geometry("800x700")
inicio_sesion.title('Inicio de sesión')

background_label1 = tk.Label(inicio_sesion, image=img_fondo2)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

boton_volver_i = tk.Button(inicio_sesion, image=img_volver, command=volver_i, width=190, height=40)  # Botón con imagen
boton_volver_i.pack(pady=60)

usuario_texto = tk.Entry(inicio_sesion)
usuario_texto.pack(pady=60)

boton_usuario = tk.Button(inicio_sesion, image=img_insertar_usuario, command=introducir_usuario, width=190, height=40)  # Botón con imagen
boton_usuario.pack(pady=60)

contraseña_texto = tk.Entry(inicio_sesion)
boton_contraseña = tk.Button(inicio_sesion, image=img_contraseña, text='Insertar contraseña', command=introducir_contraseña, width=190, height=40)
inicio_sesion.withdraw()

# Ventana opciones arqred

opciones = tk.Toplevel()
opciones.withdraw()

#Funciones

def cerrar_sesión():
    s.send(('QUIT \r\n').encode())
    s.close()
    opciones.withdraw()
    root.deiconify()

def salto():
    opciones.withdraw()
    medida.deiconify()

def salto_desde_leaderboard():
    leaderboard.destroy()
    medida.deiconify()
    
def leaderboard_command():
    global leaderboard
    global contador_boton_top
    if contador_boton_top == 1:
        medida.withdraw()
        contador_boton_top =0 
        boton_ver_Topm.pack_forget()
    leaderboard=tk.Toplevel()
    leaderboard.geometry("800x700")
    mostrar_Top_10()
    boton_enviar_medida_leaderboard= tk.Button(leaderboard, image=img_enviar,command=salto_desde_leaderboard, width=180, height=40)
    boton_enviar_medida_leaderboard.pack(pady=10)
    boton_volverl= tk.Button(leaderboard, image=img_volver,command=volver_opciones_l, width=180, height=40)
    boton_volverl.pack(pady=10)
    opciones.withdraw()
    leaderboard.deiconify()

def volver_opciones_l():
    leaderboard.destroy()
    opciones.deiconify()
    
def enviar_medida():
    global contador_boton_top
    global boton_ver_Topm
    nombre= nombre_texto.get()
    grupo_ProMu= grupo_texto.get()
    altura= int(altura_texto.get())
    fecha= fecha_texto.get()
    send_DATA= {"nombre":nombre,"grupo_ProMu":grupo_ProMu,"altura":altura,"fecha":fecha}
    send_DATA_json= json.dumps(send_DATA)
    send_data= 'SEND_DATA '+send_DATA_json+'\r\n'
    print(send_data)
    s.send((send_data).encode())
    respuesta= s.recv(1024).decode()
    print(respuesta)
    if respuesta[:3] == '200':
        messagebox.showinfo(message="Datos enviados", title="Estado de datos")
        messagebox.showinfo(message="¡Has entrado en el Top 10!", title="Estado de datos")
    elif respuesta[:3] == '201':
        messagebox.showinfo(message="Datos enviados", title="Estado de datos")
    else:
        messagebox.showerror(message="Algo salió mal", title="Error de medida")
    if contador_boton_top == 0:
        contador_boton_top = 1

bold_font = font.Font(family='Heveltica', size=16, weight='bold')
bold_font1= font.Font(family="Heveltica", size=13, weight="bold")
def mostrar_Top_10():
    comando_get= 'GET_LEADERBOARD\r\n'
    
    s.send((comando_get).encode())
    respuesta= s.recv(1024).decode()
    ran=0.35
    background_ranking = tk.Label(leaderboard, image=img_fondoranking)
    background_ranking.place(x=0, y=0, relwidth=1, relheight=1)

    if respuesta[:3] == '202':
        no_datos= tk.Label(leaderboard, text="Aún no hay datos registrados")
        no_datos.pack()
        
        
    elif respuesta[:3] == '200':
        
        while True:
            respuesta= s.recv(1024).decode()
        
            ranking_texto = tk.Label(leaderboard, text='Ranking', fg='white', bg="#D1A403", font=bold_font)
            nombre_texto = tk.Label(leaderboard, text='Nombre', fg='white',bg="#D1A403",  font=bold_font)
            grupo_texto = tk.Label(leaderboard, text='Grupo' , fg='white',bg="#D1A403", font=bold_font)
            altura_texto = tk.Label(leaderboard, text='Altura', fg='white', bg="#D1A403",font=bold_font)
            fecha_texto = tk.Label(leaderboard, text='Fecha', fg='white',bg="#D1A403", font=bold_font)
            
            ranking_texto.place(relx=0.1, rely=0.30, anchor='center')
            nombre_texto.place(relx=0.3, rely=0.30, anchor='center')
            grupo_texto.place(relx=0.5, rely=0.30, anchor='center')
            altura_texto.place(relx=0.7, rely=0.30, anchor='center')
            fecha_texto.place(relx=0.9, rely=0.30, anchor='center')
            if respuesta[:3] == '202':
                print('No hay más datos registrados')
                break
            else:
                datos = json.loads(respuesta)
                ranking = datos['ranking']
                nombre = datos['nombre']
                grupo = datos['grupo_ProMu']
                altura = datos['altura']
                fecha = datos['fecha']
                
                ranking_texto = tk.Label(leaderboard, text=ranking, fg='white',bg="#9D2C0E",font=bold_font1)
                nombre_texto = tk.Label(leaderboard, text=nombre, fg='white',bg="#9D2C0E",font=bold_font1)
                grupo_texto = tk.Label(leaderboard, text=grupo , fg='white',bg="#9D2C0E",font=bold_font1)
                altura_texto = tk.Label(leaderboard, text=altura, fg='white',bg="#9D2C0E",font=bold_font1)
                fecha_texto = tk.Label(leaderboard, text=fecha, fg='white',bg="#9D2C0E",font=bold_font1)

                ranking_texto.place(relx=0.1, rely=ran+0.05, anchor='center')
                nombre_texto.place(relx=0.3, rely=ran+0.05, anchor='center')
                grupo_texto.place(relx=0.5, rely=ran+0.05, anchor='center')
                altura_texto.place(relx=0.7, rely=ran+0.05, anchor='center')
                fecha_texto.place(relx=0.9, rely=ran+0.05, anchor='center')

                ran += 0.05
                

#------------------------------
#Opciones ventana
opciones = tk.Toplevel()
opciones.geometry("800x700")
opciones.title("Opciones")

background_opciones = tk.Label(opciones, image=img_fondo6)
background_opciones.place(x=0, y=0, relwidth=1, relheight=1)

boton_medida= tk.Button(opciones, image=img_enviar_salto,command=salto, width=180, height=40)
boton_medida.pack(pady=30, ipadx=20, ipady=5 )
boton_medida.place(relx=0.5, rely=0.20, anchor='center')

boton_leaderboard= tk.Button(opciones,image= img_leaderboard2, text='LeaderBoard',command=leaderboard_command, width=180, height=40)
boton_leaderboard.pack(pady=30, ipadx=20, ipady=5 )
boton_leaderboard.place(relx=0.5, rely=0.40, anchor='center')

boton_cs= tk.Button(opciones, image=img_cerrar_sesion, command=cerrar_sesión, width=180, height=40)
boton_cs.pack(pady=30, ipadx=20, ipady=5 )
boton_cs.place(relx=0.5, rely=0.60, anchor='center')
opciones.withdraw()

contador_boton_top=0

#---------------------------------
#Medida ventana
medida=tk.Toplevel()
medida.geometry("800x700")
medida.title("Medida")

background_medidas = tk.Label(medida, image=img_fondo7)
background_medidas.place(x=0, y=0, relwidth=1, relheight=1)

boton_volverm= tk.Button(medida,image=img_volver,command=lambda: volver(opciones,medida), width=180, height=40)
boton_volverm.pack(pady=30)

nombre_texto= tk.Entry(medida)
nombre_texto.insert(0,'Nombre del saltador')
nombre_texto.pack(pady=40, ipadx=20, ipady=5)
nombre_texto.place(relx=0.5, rely=0.20, anchor='center')

grupo_texto= tk.Entry(medida)
grupo_texto.insert(0,'Grupo promu')
grupo_texto.pack(pady=40, ipadx=20, ipady=5)
grupo_texto.place(relx=0.5, rely=0.30, anchor='center')

altura_texto= tk.Entry(medida)
altura_texto.insert(0,'Altura del salto(mm)')
altura_texto.pack(pady=40, ipadx=20, ipady=5)
altura_texto.place(relx=0.5, rely=0.40, anchor='center')

fecha_texto= tk.Entry(medida)
fecha_texto.insert(0,'Fecha de hoy')
fecha_texto.pack(pady=40, ipadx=20, ipady=5)
fecha_texto.place(relx=0.5, rely=0.50, anchor='center')

boton_enviar_medida= tk.Button(medida, image=img_salto,command=enviar_medida, width=180, height=40)
boton_enviar_medida.pack(pady=40, ipadx=20, ipady=5)
boton_enviar_medida.place(relx=0.5, rely=0.60, anchor='center')

boton_ver_Topm= tk.Button(medida, image=img_top10, command=leaderboard_command, width=180, height=40)
boton_ver_Topm.pack(pady=40, ipadx=20, ipady=5)
boton_ver_Topm.place(relx=0.5, rely=0.70, anchor='center')
medida.withdraw()


#Leaderboard
leaderboard=tk.Toplevel()
leaderboard.geometry("800x700")
leaderboard.title("Leaderboard")
background_ranking = tk.Label(leaderboard, image=img_fondoranking)
background_ranking.place(x=0, y=0, relwidth=1, relheight=1)

boton_enviar_medida_leaderboard= tk.Button(leaderboard, text='Enviar',command=salto_desde_leaderboard, width=30, height=10)
boton_enviar_medida_leaderboard.pack(pady=30)

boton_volverl= tk.Button(leaderboard, image=img_volver,  text='Volver', command=volver_opciones_l, width=180, height=50)
boton_volverl.pack(pady=30)
leaderboard.withdraw()

#Ventana créditos

ventana_creditos = tk.Toplevel()
ventana_creditos.geometry("800x700")
ventana_creditos.title("Créditos")
background_label2 = tk.Label(ventana_creditos, image=img_fondo_creditos)
background_label2.place(x=0, y=0, relwidth=1, relheight=1)
boton_volver_creditos = tk.Button(ventana_creditos, image=img_volver, command=lambda:volver(root,ventana_creditos), width=190, height=50)
boton_volver_creditos.pack(side="bottom", pady=60)
ventana_creditos.withdraw()

#Modo ventana
ventana_modo= tk.Toplevel()
ventana_modo.geometry("800x700")
ventana_modo.title("Modo")

background_label3 = tk.Label(ventana_modo, image=img_fondo_personajes)
background_label3.place(x=0, y=0, relwidth=1, relheight=1)

# Crear botones para cada personaje
botonjake = tk.Button(ventana_modo, image=img_botonjake, command=lambda: cambiar_tema(img_fondojake2))
botontricky = tk.Button(ventana_modo, image=img_botontricky, command=lambda: cambiar_tema(img_fondotricky2))
botonfresh = tk.Button(ventana_modo, image=img_botonfresh, command=lambda: cambiar_tema(img_fondofresh2))

# Posicionar los botones
botonjake.place(relx=0.5, rely=0.3, anchor="center")
botontricky.place(relx=0.5, rely=0.5, anchor="center")
botonfresh.place(relx=0.5, rely=0.7, anchor="center")

boton_volver = tk.Button(ventana_modo, image=img_volver, command=lambda:volver(root,ventana_modo), width=190,)  # Botón con imagen
boton_volver.place(relx=0.5, rely=0.9, anchor="center")
ventana_modo.withdraw()

#Ventana salto

#funciones ventana

grafica_limpio= tk.PhotoImage(file='foto blanco.png')

def labels(t,aceleracion_abs,aceleracion_y, masa):
    global a_correcta_sf
    global a_correcta_corr
    global v
    global potencia
    global fuerza
    a_correcta = calcular_aceleracion_correcta(aceleracion_abs, aceleracion_y)
    a_correcta_sf = sf(a_correcta, 20, 3)
    gravedad = calcular_gravedad(a_correcta_sf)
    gravedad_label = tk.Label(dg_ventana, text=f'Gravedad acelerómetro: {gravedad:.2}',fg='white',bg="#9D2C0E",font=bold_font1)
    gravedad_label.place(relx=0.5,rely=0.04, anchor='center')
    a_salto = a_correcta_sf -gravedad + 9.81
    fuerza = calcular_fuerza(a_salto, masa)
    fuerza_max = np.max(fuerza)
    fuerza_label = tk.Label(dg_ventana, text=f'Fuerza máxima: {fuerza_max:.2f}',fg='white',bg="#9D2C0E",font=bold_font1)
    fuerza_label.place(relx=0.5,rely=0.07, anchor='center')
    a_correcta_corr = calcular_aceleracion_corr(a_correcta_sf, gravedad)
    v = primitiva_numerica(a_correcta_corr, t, 0)
    v0 = calcular_velocidad_maxima(v)
    velocidad_label = tk.Label(dg_ventana, text=f'Velocidad máxima: {v0:.2f}',fg='white',bg="#9D2C0E",font=bold_font1)
    velocidad_label.place(relx=0.5,rely=0.1, anchor='center')
    potencia = calcular_potencia(fuerza, v)
    potencia_maxima = np.max(potencia[:np.argmax(v) + 1])
    potencia_label = tk.Label(dg_ventana, text=f'Potencia máxima: {potencia_maxima:.2f}',fg='white',bg="#9D2C0E",font=bold_font1)
    potencia_label.place(relx=0.5,rely=0.13, anchor='center')
    altura = calcular_altura(v0, gravedad)
    altura_label = tk.Label(dg_ventana, text=f'Altura del salto: {altura*1000:.2f}(mm)',fg='white',bg="#9D2C0E",font=bold_font1)
    altura_label.place(relx=0.5,rely=0.16, anchor='center')
    
def grafica_salto():
    global grafica_salto_f
    t_max_vel, t_min_vel, duracion_vuelo = calcular_duracion_vuelo(v, t)
    plt.figure(figsize=(5,3))
    plt.plot(t, a_correcta_sf, label='Aceleración')
    plt.axvspan(t_max_vel,t_min_vel, color='purple', alpha=0.3, label='Tiempo de vuelo')
    plt.grid('on')
    plt.xlim(0,3)
    plt.xlabel('$t$ [s]')
    plt.ylabel('$v$ [m/s]')
    plt.title('Salto')
    plt.savefig('grafica_salto')
    grafica_salto_f= tk.PhotoImage(file='grafica_salto.png')
    grafica.config(image=grafica_salto_f)

def grafica_velocidad():
    global grafica_velocidad_f
    plt.figure(figsize=(5, 3))
    plt.plot(t, v, color="orange", label='velocidad')
    plt.xlim(0,3)
    plt.xlabel('Tiempo')
    plt.ylabel('velocidad')
    plt.title('velocidad')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_velocidad')
    grafica_velocidad_f= tk.PhotoImage(file='grafica_velocidad.png')
    grafica.config(image=grafica_velocidad_f)
    

def grafica_potencia():
    global grafica_potencia_f
    plt.figure(figsize=(5, 3))
    plt.plot(t, potencia, color="orange", label='Potencia')
    plt.xlim(0,3)
    plt.xlabel('Tiempo')
    plt.ylabel('Potencia')
    plt.title('Potencia')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_potencia')
    grafica_potencia_f= tk.PhotoImage(file='grafica_potencia.png')
    grafica.config(image=grafica_potencia_f)

def grafica_fuerza():
    global grafica_fuerza_f
    plt.figure(figsize=(5, 3))
    plt.plot(t, fuerza, color="purple", label='Fuerza')
    plt.xlim(0,3)
    plt.xlabel('Tiempo')
    plt.ylabel('Fuerza')
    plt.title('Fuerza')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_fuerza')
    grafica_fuerza_f= tk.PhotoImage(file='grafica_fuerza.png')
    grafica.config(image=grafica_fuerza_f)
    
def obtener_salto():
    global t
    try:
        fichero = fichero_entrada.get()
        masa = float(peso_entrada.get())
        t, aceleracion_abs, aceleracion_y = cargar_datos(fichero)
        ventana_dg(t, aceleracion_abs, aceleracion_y, masa)
    except:
        messagebox.showerror(message="Algo salió mal. Comprueba si el archivo existe o está en la misma carpeta que la app, o mira si el peso es un número", title="Error de medida")


#Ventana salto
salto_ventana=tk.Toplevel()
salto_ventana.geometry("800x700")
salto_ventana.title("Salto")

backgroundsalto = tk.Label(salto_ventana, image=img_fondosalto)
backgroundsalto.place(x=0, y=0, relwidth=1, relheight=1)

boton_volver_salto= tk.Button(salto_ventana, image=img_volver,command=lambda:volver(root,salto_ventana), width=180, height=40)
boton_volver_salto.pack(pady=30)

fichero_entrada= tk.Entry(salto_ventana)
fichero_entrada.insert(0,'Fichero del salto(.xlsx)')
fichero_entrada.pack(pady=30)

peso_entrada= tk.Entry(salto_ventana)
peso_entrada.insert(0,'Peso del saltador (Kg)')
peso_entrada.pack(pady=30)

boton_analizar_salto= tk.Button(salto_ventana, image=img_analizarsalto, command=obtener_salto, width=195, height=40)
boton_analizar_salto.pack(pady=30)
salto_ventana.withdraw()

#Ventana datos y gráficos
def volver_dg():
    salto_ventana.deiconify()
    dg_ventana.destroy()
    grafica_limpio= tk.PhotoImage(file='foto blanco.png')
    
def ventana_dg(t, aceleracion_abs, aceleracion_y, masa):
    global dg_ventana
    global grafica
    salto_ventana.withdraw()
    dg_ventana=tk.Toplevel()
    dg_ventana.title("Resultados")
    dg_ventana.geometry("1000x900")
    
    background_resultados = tk.Label(dg_ventana, image=img_fondoresultados)
    background_resultados.place(x=0, y=0, relwidth=1, relheight=1)

    grafica= tk.Label(dg_ventana,image=grafica_limpio)
    grafica.place(relx=0.5, rely=0.5, anchor='center')
    boton_salto_g= tk.Button(dg_ventana, image=img_salto , command=grafica_salto, width=180, height=40)
    boton_salto_g.place(relx=0.21, rely=0.10, anchor='center')
    boton_velocidad_g= tk.Button(dg_ventana, image=img_velocidad ,command=grafica_velocidad, width=180, height=40)
    boton_velocidad_g.place(relx=0.21, rely=0.39, anchor='center')
    boton_potencia_g= tk.Button(dg_ventana, image= img_potencia,command=grafica_potencia, width=180, height=40)
    boton_potencia_g.place(relx=0.21, rely=0.61, anchor='center')
    boton_fuerza_g= tk.Button(dg_ventana, image= img_fuerza,command=grafica_fuerza, width=180, height=40)
    boton_fuerza_g.place(relx=0.21, rely=0.89, anchor='center')
    boton_volver_dg= tk.Button(dg_ventana, image= img_volver ,command=volver_dg, width=180, height=40)
    boton_volver_dg.place(relx=0.5, rely=0.84, anchor='center')

    labels(t, aceleracion_abs, aceleracion_y, masa)


root.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Llamar a la función cerrar_ventana cuando se cierre la ventana
# Ejecutar el bucle de la ventana
root.mainloop()


