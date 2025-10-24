import os
import tkinter as tk
from tkinter import PhotoImage
import pygame
import keyboard
import threading
import time
import random
import sys


def get_path(rel_path):
    """Retourne le chemin absolu, compatible PyInstaller"""
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

# ======== Initialiser pygame mixer ======== 
pygame.mixer.init()

# ======== Dictionnaire des sons avec nom d'affichage et nom de fichier ========

sons_1= {
    "&" : ("Thunder", "thunder.wav"),               # 1
    "é" : ("Gun 1", "gun_1.wav"),                   # 2
    '"' : ("Gun 2", "gun_2.wav"),                   # 3
    "'" : ("Wind", "wind.wav"),                     # 4
    "(" : ("Rain", "rain.wav"),                     # 5
    "-" : ("Explosion", "explosion.wav"),           # 6
    "è" : ("Explosion", "explosion_bis.wav"),       # 7
    "_" : ("coin", "coin.wav"),                     # 8
    "ç" : ("Heart Beat", "Heart_beat.wav"),         # 9
    "à" : ("Pressure", "pressure.wav"),             # 0
    "=" : ("Stop", "stop.wav") # =======================
    }

sons_2 = {
    "&" : ("Fracture", "fallbig.wav"),              # 1
    "é" : ("Plouf", "water_splash3.wav"),           # 2
    '"' : ("Craft", "craft.wav"),                   # 3
    "'" : ("Lock", "locking.wav"),                  # 4
    "(" : ("Alien Door", "alien.wav"),              # 5
    "-" : ("Vault", "vault.wav"),                   # 6
    "è" : ("Old Door", "olddooropen.wav"),          # 7
    "_" : ("Door Slam", "close.wav"),               # 8
    "ç" : ("Crow", "crow.wav"),                     # 9
    "à" : ("KwaKwa", "kwakwa.wav"),                 # 0
    "=" : ("Stop", "stop.wav") # =======================
    }

sons_3 = {
    "&" : ("Steve", "Steve.mp3"),                   # 1
    "é" : ("Crystal", "bottle_break.wav"),#------------------
    '"' : ("Drop", "drop.wav"),                     # 3
    "'" : ("Missing", "Missing.wav"),#------------------
    "(" : ("Missing", "Missing.wav"),#------------------
    "-" : ("Missing", "Missing.wav"),#------------------
    "è" : ("Missing", "Missing.wav"),#------------------
    "_" : ("Missing", "Missing.wav"),#------------------
    "ç" : ("Missing", "Missing.wav"),#------------------
    "à" : ("Missing", "Missing.wav"),#------------------
    "=" : ("Stop", "stop.wav") # =======================
    }

sons_4 = {
    "&" : ("cave 1", "Cave3.wav"),                  # 1
    "é" : ("cave 2", "Cave4.wav"),                  # 2
    '"' : ("cave 3", "Cave5.wav"),                  # 3
    "'" : ("Walking", "step_1.wav"),                # 4
    "(" : ("Step2", "step_2.wav"),                  # 5
    "-" : ("Groupe", "group_run.wav"),              # 6
    "è" : ("Alarm", "alarm.wav"),                   # 7
    "_" : ("Alarm Bis ", "alarm_bis.wav"),          # 8
    "ç" : ("Creak", "creak03.wav"),                 # 9
    "à" : ("wave", "wave.wav"),                     # 0
    "=" : ("Stop", "stop.wav") # =======================
    }


sons = sons_1

# ======== Préparation des Sets =========

sound_sets = [sons_1, sons_2, sons_3, sons_4]
current_set_index = 0
sons = sound_sets[current_set_index]

# ======== Préparation du Switch ======== 

def switch():
    global sons
    if sons == sons_1:
        sons = sons_2
    elif sons == sons_2:
        sons = sons_3
    elif sons == sons_3:
        sons = sons_4
    else:
        sons = sons_1
    print("🎛️ Switch de set effectué.")


# ======== Fonction pour jouer un son ========
def jouer_son(fichier):
    try:
        # pygame.mixer.music.load(f"se/{fichier}")
        pygame.mixer.music.load(get_path(os.path.join("se", fichier)))
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Erreur en jouant le son {fichier} : {e}")

# ======== Écoute des touches clavier même en arrière-plan ========

hotkeys_active = True
hotkeys_thread = None

def toggle_hotkeys():
    global hotkeys_active, hotkeys_thread

    if hotkeys_active:
        hotkeys_active = False
        print("⛔️ Détection clavier désactivée")
        btn_toggle_hotkeys.config(text="⛔️ Ecoute du clavier", fg="red",bg="#ff9999",activebackground="#ff0000")
        # jouer_son("buttonclick.mp3")
    else:
        hotkeys_active = True
        print("✅ Détection clavier activée")
        hotkeys_thread = threading.Thread(target=boucle_hotkeys, daemon=True)
        hotkeys_thread.start()
        btn_toggle_hotkeys.config(text="✅ Ecoute du clavier", fg="green",bg="#99ffa7",activebackground="#00ff26")
        # jouer_son("buttonclick.mp3")

def switch():
    global sons, current_set_index
    current_set_index = (current_set_index + 1) % len(sound_sets)
    sons = sound_sets[current_set_index]
    print(f"🎛️ Passage au set {current_set_index + 1}")
    charger_boutons()

def boucle_hotkeys():
    last_state_2 = False  # Suivi de l'état de la touche ²
    while hotkeys_active:
        # Gestion du switch par la touche ²
        pressed_2 = keyboard.is_pressed("²")
        if pressed_2 and not last_state_2:  # Touche vient d'être pressée
            switch()
        last_state_2 = pressed_2

        # Gestion des autres touches du set
        for scancode in sons:
            if keyboard.is_pressed(scancode):
                nom, fichier = sons[scancode]
                print(f"→→→ {nom}")
                jouer_son(fichier)
                while keyboard.is_pressed(scancode):
                    time.sleep(0.05)
        time.sleep(0.05)

# ===== Dark Mod =====

light_index = 0
def dark_mod():
    """Change le mode clair / sombre"""
    global light_index

    # Inversion du mode
    light_index = 1 - light_index  # 0 -> 1 ou 1 -> 0

    if light_index == 1:
        # 🌙 Mode sombre
        app.configure(bg="#24202d")
        conteneur_boutons.configure(bg="#24202d")
        conteneur_divers.configure(bg="#24202d")
        contener_slider.configure(bg="#24202d")
        contener_sets.configure(bg="#24202d")
        volume_label.configure(bg="#24202d", fg="white")
        volume_slider.configure(bg="#FFC266", troughcolor="#FFAD33")
        build_label.configure(bg="#24202d", fg="white")
        label.configure(bg="#24202d", fg="white")
        light_toggle_hotkeys.config(text="☀ Light mod", fg="orange",bg="#ffe6af", activebackground="#ffd572")
        print("🎛️ Passage au mode sombre")
    else:
        # ☀️ Mode clair
        app.configure(bg="SystemButtonFace")  
        conteneur_boutons.configure(bg="SystemButtonFace")
        conteneur_divers.configure(bg="SystemButtonFace")
        contener_slider.configure(bg="SystemButtonFace")
        contener_sets.configure(bg="SystemButtonFace")
        volume_label.configure(bg="SystemButtonFace", fg="black")
        volume_slider.configure(bg="#66CCFF", troughcolor="#3399FF")
        build_label.configure(bg="SystemButtonFace", fg="grey")
        label.configure(bg="SystemButtonFace", fg="black")
        light_toggle_hotkeys.config(text="🌙 Dark mod", fg="blue",bg="#a099ff", activebackground="#0000ff")
        print("🎛️ Passage au mode clair")

    jouer_son("buttonclick.mp3")


# ===== Slider de volume =====
def changer_volume(val):
    volume = float(val) / 100  # convertir en 0.0 - 1.0
    pygame.mixer.music.set_volume(volume)
    print(f"🔊 Volume : {int(float(val))}%")


def charger_boutons():
    global images

    # Vider les anciens widgets
    for widget in conteneur_boutons.winfo_children():
        widget.destroy()

    images = {}
    for i, (key, (name, file)) in enumerate(sons.items()):
        nom_sans_ext = os.path.splitext(file)[0]
        # chemin_image = os.path.join("img", f"{nom_sans_ext}.png")
        chemin_image = get_path(os.path.join("img", f"{nom_sans_ext}.png"))
        if os.path.exists(chemin_image):
            images[nom_sans_ext] = PhotoImage(file=chemin_image)
        else:
            images[nom_sans_ext] = None

        img = images[nom_sans_ext]
        btn = tk.Button(conteneur_boutons,
                        text=f"{name}",
                        image=img,
                        compound="top",
                        font=police_perso,
                        anchor="w",
                        padx=5,
                        width=50,
                        bg="#ff7373",
                        activebackground="#ff0000",
                        command=lambda f=file, n=name: [print(f"→→→ {n}"), jouer_son(f)])

        row = i // 12
        col = i % 12
        btn.grid(row=row, column=col, padx=10, pady=5, sticky="w")

def set_sons(index):
    """Change directement le set courant"""
    global sons, current_set_index
    current_set_index = index
    sons = sound_sets[current_set_index]
    print(f"🎛️ Passage manuel au set {current_set_index + 1}")
    #jouer_son("buttonclick.mp3")
    charger_boutons()



# ====== Création de la fenêtre principale ========
app = tk.Tk()
app.title("🔊 Soundboard")
app.geometry("1100x270")
#app.configure(bg="#171c2c")  # gris foncé  



# ======== Charger la police personnalisée ========
police_perso = ("Time New Roman", 8)


label = tk.Label(app, text="Table game Ready Soundboard", font=("Time New Roman",12))
label.pack(pady=10)

# ======== Image pour les boutons ========
images = {}  # Dictionnaire pour stocker les images

for _, (_, fichier) in sons.items():
    nom_sans_ext = os.path.splitext(fichier)[0]
    # chemin_image = os.path.join("img", f"{nom_sans_ext}.png")
    chemin_image = get_path(os.path.join("img", f"{nom_sans_ext}.png"))
    if os.path.exists(chemin_image):
        images[nom_sans_ext] = PhotoImage(file=chemin_image)
    else:
        images[nom_sans_ext] = None  # Pas d’image pour ce son


# ======== Conteneur pour les boutons ========
conteneur_boutons = tk.Frame(app)
conteneur_boutons.pack()

# ======== Création des boutons côte à côte ========
for i, (key, (name, file)) in enumerate(sons.items()):
    nom_sans_ext = os.path.splitext(file)[0]
    img = images.get(nom_sans_ext)

    btn = tk.Button(conteneur_boutons,
                    # text=f"[{i}] {name}",
                    text=f"{name}",
                    image=img,
                    compound="top",
                    font=police_perso,
                    anchor="w",
                    padx=5,
                    width=50,
                    bg="#ff7373",
                    activebackground="#a34040",
                    command=lambda f=file, n=name: [print(f"→→→ {n}"), jouer_son(f)])
    
    # Disposition sur 12 colonnes
    row = i // 12
    col = i % 12
    btn.grid(row=row, column=col, padx=10, pady=5, sticky="w")


# ======== Boutons de sélection de Set ========

contener_sets = tk.Frame(app)
contener_sets.pack(pady=5)

for i in range(4):
    btn_set = tk.Button(
        contener_sets,
        text=f"🦊 Set {i+1}",
        width=10,
        font=police_perso,
        bg="#cc73ff",
        activebackground="#8400ff",
        command=lambda i=i: set_sons(i)
    )
    btn_set.grid(row=0, column=i, padx=5, pady=5)


# ======== Slider Volume ===========

# ligne_horizontale = tk.Frame(app, height=1, bg="Dark red", bd=0)
# ligne_horizontale.pack(fill="x", padx=10, pady=10)

contener_slider = tk.Frame(app)
contener_slider.pack(pady=1)

volume_label = tk.Label(
    contener_slider,
    text="Volume",
    font=(police_perso)
)
volume_label.grid(row=0, column=0, columnspan=2, padx=0, pady=0)

volume_slider = tk.Scale(
    contener_slider,
    from_=0,
    to=100,
    orient="horizontal",
    length=500,
    showvalue=0,
    troughcolor="#3399FF",    # couleur de la barre
    bg="#66CCFF",             # fond du widget
    highlightthickness=0,       # pas de bordure claire
    bd=1,              
    command=changer_volume
)
volume_slider.set(50)
volume_slider.grid(row=1, column=1, padx=0, pady=0)  

# ======== Bouton Quitter et détection ========
# ligne_horizontale = tk.Frame(app, height=1, bg="Dark red", bd=0)
# ligne_horizontale.pack(fill="x", padx=20, pady=10)

conteneur_divers = tk.Frame(app)
conteneur_divers.pack(pady=10)

# Bouton pour activer/désactiver l'écoute clavier
light_toggle_hotkeys = tk.Button(
    conteneur_divers,
    text="🌙 Dark mod", fg="blue",
    bg="#a099ff",
    activebackground="#0000ff",
    font=police_perso,
    width=25,
    command=dark_mod
)
light_toggle_hotkeys.grid(row=0, column=0, padx=5, pady=5)

# Bouton pour activer/désactiver l'écoute clavier
btn_toggle_hotkeys = tk.Button(
    conteneur_divers,
    text="✅ Ecoute du clavier", fg="green",
    font=police_perso,
    width=25,
    bg="#99ffa7",
    activebackground="#00ff26",
    command=toggle_hotkeys
)
btn_toggle_hotkeys.grid(row=0, column=1, padx=5, pady=5)

# Bouton pour quitter
bouton_quit = tk.Button(
    conteneur_divers,
    text="❌ Quitter",
    width=25,
    font=police_perso,
    bg="#adadad",
    activebackground="#232323",
    command=app.destroy
)
bouton_quit.grid(row=0, column=2, padx=5, pady=5)

# ======== Lancement de l'écoute des touches dans un thread séparé ========
threading.Thread(target=boucle_hotkeys, daemon=True).start()

# ======== Affichage du numéro de build en bas à droite ========
build_label = tk.Label(
    app,
    text="Beta 4.2",
    font=("Arial", 8),
    fg="gray",
    anchor="se"
)
build_label.place(relx=1.0, rely=1.0, anchor="se", x=-5, y=-5)

app.mainloop()


