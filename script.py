#   **--Settings--**

# Import
import tkinter as tk
import webbrowser
from tkinter import font
from PIL import ImageTk, Image, ImageFont, ImageDraw
import requests
from tkinter.scrolledtext import ScrolledText
import os


# Create App
SkinIDApp = tk.Tk()
SkinIDApp.geometry("350x450")
SkinIDApp.title("MC WiiU Skin ID Checker")
icon_path = os.path.abspath("assets/icon.ico")
SkinIDApp.iconbitmap(icon_path)

# Disable window resizing
SkinIDApp.resizable(False, False)

# Load images
youtube_path = os.path.abspath("assets/youtube.png")
YoutubeImage = Image.open(youtube_path)
YoutubeImageSize = YoutubeImage.resize((23, 20), Image.LANCZOS)
YoutubePhotoImage = ImageTk.PhotoImage(YoutubeImageSize)

discord_path = os.path.abspath("assets/discord.png")
DiscordImage = Image.open(discord_path)
DiscordImageSize = DiscordImage.resize((23, 20), Image.LANCZOS)
DiscordPhotoImage = ImageTk.PhotoImage(DiscordImageSize)

github_path = os.path.abspath("assets/github.png")
GitHubImage = Image.open(github_path)
GitHubImageSize = GitHubImage.resize((23, 20), Image.LANCZOS)
GitHubPhotoImage = ImageTk.PhotoImage(GitHubImageSize)

# Load Font 
FontLuckiestGuy = os.path.abspath("assets/LuckiestGuy-Regular.ttf")

# ------------------------------------------

#   **--Background--**

# Global Background
Background = tk.Label(SkinIDApp, bg="#383838")
Background.place(x=0, y=0, width=350, height=450)

# Title Border Background
BorderBackgroundTitleApp = tk.Label(SkinIDApp, bg="#000000")
BorderBackgroundTitleApp.place(x=0, y=49, width=350, height=2)
BorderBackgroundTitleApp.lift()

# Background Youtube Discord
BackgroundYoutubeDiscord = tk.Label(SkinIDApp, bg="#585858")
BackgroundYoutubeDiscord.place(x=0, y=420, width=350, height=30)
BackgroundYoutubeDiscord.lift()
BorderBackgroundYoutubeDiscord = tk.Label(SkinIDApp, bg="#000000")
BorderBackgroundYoutubeDiscord.place(x=0, y=419, width=350, height=2)
BorderBackgroundYoutubeDiscord.lift()

# ------------------------------------------

def send_to_discord():
    webhook_url = "something"
    input_text = input_entry.get()
    # Vérifier si le message contient exactement 8 chiffres
    if input_text.isdigit() and len(input_text) == 8:
        # Vérifier si le nombre est déjà dans le fichier
        with open('fichier.txt', 'r') as f:
            numeros = f.readlines()
        if input_text+'\n' in numeros:
            console_text.insert(tk.INSERT, "ERROR : The number already exists in the database.\n")
            console_text.insert(tk.INSERT, "------------------------------\n")
        else:
            # Ajouter le nombre à la fin du fichier
            with open('fichier.txt', 'a') as f:
                f.write(input_text+'\n')
            console_text.insert(tk.INSERT, "The number is correct.\n")
            # Envoyer le message à Discord
            data = {
                "content": input_text
            }
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                console_text.insert(tk.INSERT, "Message validated and sent : {}\n".format(input_text))
                console_text.insert(tk.INSERT, "------------------------------\n")
            else:
                console_text.insert(tk.INSERT, "ERROR : connection not established.\n")
                console_text.insert(tk.INSERT, "------------------------------\n")
    else:
        console_text.insert(tk.INSERT, "ERROR : enter an 8-digit message.\n")
        console_text.insert(tk.INSERT, "------------------------------\n")

    # Faire défiler automatiquement vers le bas
    console_text.see(tk.END)

def validate_input(char):
    # Vérifier si le caractère est un chiffre
    if char.isdigit():
        return True
    else:
        return False

# Zone de texte
validate_input_func = SkinIDApp.register(validate_input)
input_entry = tk.Entry(SkinIDApp, width=15, font=("Arial", 12), validate="key", validatecommand=(validate_input_func, '%S'))
input_entry.place(x=100, y=100)
input_entry.configure(relief="solid", bd=1)

# Bouton Valider
validate_button = tk.Button(SkinIDApp, text="Validate", command=send_to_discord)
validate_button.place(x=140, y=150)

# Console
console_text = ScrolledText(SkinIDApp, width=30, height=10)
console_text.place(x=50, y=230)
console_text.insert(tk.INSERT, "Version : 1.0.0 - Check if any updates have been made.\n")
console_text.insert(tk.INSERT, "------------------------------\n")

# ------------------------------------------

#   **--Title and Background--** 

TitleAppText = "MC WiiU Skin ID Checker"
TitleAppFontSize = 25
TitleAppFont = ImageFont.truetype(FontLuckiestGuy, TitleAppFontSize)

# Image and Border
TitleAppImageWidth = 400
TitleAppImageHeight = 45
TitleAppImage = Image.new("RGBA", (TitleAppImageWidth, TitleAppImageHeight), (255, 255, 255, 0))
TitleAppDraw = ImageDraw.Draw(TitleAppImage)
TitleAppOutlineColor = (0, 0, 0)
TitleAppOutlinePosition = (33.5, 17)
TitleAppDraw.text(TitleAppOutlinePosition, TitleAppText, font=TitleAppFont, fill=TitleAppOutlineColor)

# Draw Text
TitleAppTextColor = (255, 255, 255)
TitleAppTextPosition = (32.5, 15)
TitleAppDraw.text(TitleAppTextPosition, TitleAppText, font=TitleAppFont, fill=TitleAppTextColor)

# Convert Image to tk
TitleAppImagetk = ImageTk.PhotoImage(TitleAppImage)

# Show Image
TitleApp = tk.Label(SkinIDApp, image=TitleAppImagetk, bg="#585858")
TitleApp.place(x=0, y=0)

# ------------------------------------------

#    **--YouTube Button--**

# Image
YoutubeIMG = tk.Label(SkinIDApp, image=YoutubePhotoImage, bg="#585858", bd=1, relief="solid")
YoutubeIMG.place(x=201, y=SkinIDApp.winfo_height() - 3, anchor="sw")

# Text
YoutubeText = tk.Label(SkinIDApp, text="Jerem2206", bg="#585858", fg="#FFFFFF")
YoutubeText.place(x=188, y=SkinIDApp.winfo_height() - 25, anchor="sw")
YoutubeText.place_forget()

# Display text
def YoutubeShowText(event):
    YoutubeText.place(x=188, y=SkinIDApp.winfo_height() - 25, anchor="sw")

# Hide text
def YoutubeHideText(event):
    YoutubeText.place_forget()

# Link
def YoutubeLink(event):
    webbrowser.open("https://www.youtube.com/channel/UC004A2sK0Pr0dD6MJzy6cTQ")

# Bind events
YoutubeIMG.bind("<Enter>", YoutubeShowText)
YoutubeIMG.bind("<Leave>", YoutubeHideText)
YoutubeIMG.bind("<Button-1>", YoutubeLink)

# ------------------------------------------

#   **--Discord Button--**

# Image
DiscordIMG = tk.Label(SkinIDApp, image=DiscordPhotoImage, bg="#585858", bd=1, relief="solid")
DiscordIMG.place(x=118, y=SkinIDApp.winfo_height() - 3, anchor="sw")

# Text
DiscordText = tk.Label(SkinIDApp, text="jeremestici", bg="#585858", fg="#FFFFFF")
DiscordText.place(x=101, y=SkinIDApp.winfo_height() - 25, anchor="sw")
DiscordText.place_forget()

# Display text
def DiscordShowText(event):
    DiscordText.place(x=101, y=SkinIDApp.winfo_height() - 25, anchor="sw")

# Hide text
def DiscordHideText(event):
    DiscordText.place_forget()

# Bind events
DiscordIMG.bind("<Enter>", DiscordShowText)
DiscordIMG.bind("<Leave>", DiscordHideText)

# ------------------------------------------

#    **--GitHub Button--**

# Image
GitHubIMG = tk.Label(SkinIDApp, image=GitHubPhotoImage, bg="#585858", bd=1, relief="solid")
GitHubIMG.place(x=159, y=SkinIDApp.winfo_height() - 3, anchor="sw")

# Text
GitHubText = tk.Label(SkinIDApp, text="jeremy2206", bg="#585858", fg="#FFFFFF")
GitHubText.place(x=139, y=SkinIDApp.winfo_height() - 25, anchor="sw")
GitHubText.place_forget()

# Display text
def GitHubShowText(event):
    GitHubText.place(x=139, y=SkinIDApp.winfo_height() - 25, anchor="sw")

# Hide text
def GitHubHideText(event):
    GitHubText.place_forget()

# Link
def GitHubLink(event):
    webbrowser.open("https://github.com/jeremy2206")

# Bind events
GitHubIMG.bind("<Enter>", GitHubShowText)
GitHubIMG.bind("<Leave>", GitHubHideText)
GitHubIMG.bind("<Button-1>", GitHubLink)

# ------------------------------------------

#   **--Run App--**
SkinIDApp.mainloop()
