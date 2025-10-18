# 🔊 Table Game Ready Soundboard
🇬🇧 🇨🇦 🇺🇸
A simple, fast, ready-to-use soundboard for role-playing or board games.  
🎲 Controllable with the mouse or keyboard (top 12 keys on AZERTY keyboard).  
🎛️ Graphical interface via Tkinter, audio playback with pygame.

---

## 🖼️ Visual Preview

![Application Preview](img/preview.png)

---

## ⌨️ Active Keys (AZERTY keyboard)
```| Page 1 | :--------- |
| `²`    | Switch page|
| `&`    | Thunder    |
| `é`    | Gun 1      |
| `"`    | Gun 2      |
| `'`    | Wind       |
| `(`    | Rain       |
| `-`    | Explosion  |
| `è`    | Explosion  |
| `_`    | coin       |
| `ç`    | Heart Beat |
| `à`    | Pressure   |
| `=`    | Stop       |

| Touche | Nom du son |
| Page 2 | :--------- |
| `²`    | Switch page|
| `&`    | Fracture   |
| `é`    | Plouf      |
| `"`    | Craft      |
| `'`    | Lock       |
| `(`    | Alien Door |
| `-`    | Vault      |
| `è`    | Old Door   |
| `_`    | Door Slam  |
| `ç`    | Crow       |
| `à`    | KwaKwa     |
| `=`    | Stop       |

| Touche | Nom du son |
| Page 3 | :--------- |
| `²`    | Switch page|
| `&`    | Steve      |
| `é`    | Missing    |
| `"`    | Drop       |
| `'`    | Missing    |
| `(`    | Missing    |
| `-`    | Missing    |
| `è`    | Missing    |
| `_`    | Missing    |
| `ç`    | Missing    |
| `à`    | Missing    |
| `=`    | Stop       |

| Touche | Nom du son |
| Page 4 | :--------- |
| `²`    | Switch page|
| `&`    | cave 1     |
| `é`    | cave 2     |
| `"`    | cave 3     |
| `'`    | Walking    |
| `(`    | Step2      |
| `-`    | Groupe     |
| `è`    | Alarm      |
| `_`    | Alarm Bis  |
| `ç`    | Creak      |
| `à`    | wave       |
| `=`    | Stop       |
```
---

## 🚀 Launch the Application

1. Install Python 3.10 or higher  
2. Install dependencies:

```
pip install pygame keyboard
```
### Lancer l'application :
```
python app.py
```
### Launch the application:
```
python app.py
```
🎵 Sounds must be placed in a `se/` folder

🖼️ Images in an `img/` folder

## 🧊 Create a Windows Executable (.exe)

1. Install PyInstaller:

``` 
pip install pyinstaller
``` 
2. Generate the executable (on Windows):

``` 
pyinstaller --noconfirm --onefile --windowed --add-data "img;img" --add-data "se;se" app.py
```
📦 The final .exe will be in `dist/app.exe`

💡 On Linux/macOS, replace `;` with `:` in paths (img:img, se:se)

🔐 Note: Antivirus software may flag the program as a threat on first run. A preliminary launch is recommended before use.

# 📁 Recommended File Structure
        soundboard/
        ├── app.py
        ├── img/
        │   ├── thunder.png
        │   └── ...
        ├── se/
        │   ├── thunder.wav
        │   └── ...
        ├── README.md


## ⚙️ Technical Info

    🖼️ GUI: Tkinter

    🔉 Audio: pygame.mixer.music

    🎧 Only one sound played at a time (no overlap)

    🎹 Keyboard shortcuts active even without focus (via keyboard)

    ✅ Enable/disable keyboard listening via button

    🎚️ Integrated volume slider

### ☝ License

    Open-source project under MIT License. No warranty.

### 👤 Author

DBZ-V



🇫🇷 🇨🇦 🇧🇪
Une soundboard simple, rapide et prête à l’emploi pour les jeux de rôle ou de plateau.  
🎲 Contrôlable à la souris ou avec le clavier (12 touches supérieures du clavier AZERTY).  
🎛️ Interface graphique via Tkinter, lecture audio avec pygame.

---

## 🖼️ Aperçu visuel

![Aperçu de l'application](img/preview.png)

---
## ⌨️ Touches actives (clavier AZERTY)
```
| Touche | Son déclenché |
| Page 1 | :--------- |
| `²`    | Switch page|
| `&`    | Thunder    |
| `é`    | Gun 1      |
| `"`    | Gun 2      |
| `'`    | Wind       |
| `(`    | Rain       |
| `-`    | Explosion  |
| `è`    | Explosion  |
| `_`    | coin       |
| `ç`    | Heart Beat |
| `à`    | Pressure   |
| `=`    | Stop       |

| Touche | Nom du son |
| Page 2 | :--------- |
| `²`    | Switch page|
| `&`    | Fracture   |
| `é`    | Plouf      |
| `"`    | Craft      |
| `'`    | Lock       |
| `(`    | Alien Door |
| `-`    | Vault      |
| `è`    | Old Door   |
| `_`    | Door Slam  |
| `ç`    | Crow       |
| `à`    | KwaKwa     |
| `=`    | Stop       |

| Touche | Nom du son |
| Page 3 | :--------- |
| `²`    | Switch page|
| `&`    | Steve      |
| `é`    | Missing    |
| `"`    | Drop       |
| `'`    | Missing    |
| `(`    | Missing    |
| `-`    | Missing    |
| `è`    | Missing    |
| `_`    | Missing    |
| `ç`    | Missing    |
| `à`    | Missing    |
| `=`    | Stop       |

| Touche | Nom du son |
| Page 4 | :--------- |
| `²`    | Switch page|
| `&`    | cave 1     |
| `é`    | cave 2     |
| `"`    | cave 3     |
| `'`    | Walking    |
| `(`    | Step2      |
| `-`    | Groupe     |
| `è`    | Alarm      |
| `_`    | Alarm Bis  |
| `ç`    | Creak      |
| `à`    | wave       |
| `=`    | Stop       |
```
---

## 🚀 Lancer l’application

1. Installer Python 3.10 ou plus
2. Installer les dépendances :

```
pip install pygame keyboard
```
### Lancer l'application :
```
python app.py
```
🎵 Les sons doivent être placés dans un dossier se/

🖼️ Les images dans un dossier img/

## 🧊 Créer un exécutable Windows (.exe)

1.Installer PyInstaller :
``` 
pip install pyinstaller
``` 
2.Générer l’exécutable (Sous Windows) :
``` 
pyinstaller --noconfirm --onefile --windowed --add-data "img;img" --add-data "se;se" app.py
``` 
📦 Le .exe final sera dans dist/app.exe

💡 Sous Linux/macOS, remplacer ; par : dans les chemins (img:img, se:se)

🔐 nota: les antivirus peuvent percevoir le programme comme menace à la premiere execution, prévoir donc une execution préliminaire avant utilisation.

# 📁 Arborescence recommandée
        soundboard/
        ├── app.py
        ├── img/
        │   ├── thunder.png
        │   └── ...
        ├── se/
        │   ├── thunder.wav
        │   └── ...
        ├── README.md


## ⚙️ Infos techniques

    🖼️ Interface graphique : Tkinter

    🔉 Audio : pygame.mixer.music

    🎧 Un seul son joué à la fois (non superposables)

    🎹 Raccourcis clavier actifs même sans focus (via keyboard)

    ✅ Activation/désactivation de l’écoute clavier via bouton

    🎚️ Curseur de volume intégré

### ☝ Licence

    Projet open-source sous licence MIT. Aucune garantie.

### 👤 Auteur

DBZ-V


