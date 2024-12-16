


# 🦊 HO MY FOX - ADVANCED NETWORK ATTACK TOOL 🌐

Bienvenue dans le **HO MY FOX**, un outil d'attaque réseau ultra-secret conçu pour impressionner même les plus grands hackers et faire rougir ton prof de Python ! 😎

Ce projet a été réalisé dans le cadre d'un défi pour mon cours de Python, mais je dois avouer que ce n'est pas encore aussi classe que je le voudrais. C'est pourquoi **j'ai besoin de ton aide pour l'améliorer et le rendre encore plus "hacker"**, avec des options cool, des blagues de hacker et des fonctionnalités sympas qui feront lever les sourcils du professeur ! 💻⚡

### 📸 Voici ce que fait **HO MY FOX** :
1. **Écoute les commandes réseau** : Ce programme se connecte à un serveur et attend tes commandes comme un hacker dans un film.
2. **Commandes de hacking** : T'es prêt à exécuter des commandes système, envoyer des fichiers, et même obtenir des informations sur le système à distance.
3. **Blagues de hacker** : Parce qu'un bon hacker sait qu'il faut toujours rigoler ! (J'en ai quelques-unes à te faire découvrir) 😜
4. **Transfert de fichiers sécurisés** : Tu peux envoyer des fichiers cryptés comme un pro et prouver que ton espionnage est au top niveau !
5. **Interface d’attaque ASCII** : Ouais, c'est classe, un peu comme dans un film de hacking des années 90. 🖥️

### 🚀 Comment démarrer ?
1. Clone ce repo sur ta machine (duh).
   ```bash
   git clone https://github.com/tonutilisateur/ho-my-fox.git
   cd ho-my-fox
   ```

2. Exécute le serveur ou le client en fonction de ton rôle :
   - **Serveur** : Pour recevoir des connexions.
     ```bash
     python ho_my_fox_server.py
     ```
   - **Client** : Pour te connecter au serveur et démarrer les attaques.
     ```bash
     python ho_my_fox.py


### 🎮 Commandes disponibles :
- **exit** : Fermer la connexion (L'honneur est sauf, mais il est temps de partir).
- **help** : Obtenir l'aide (Pas besoin d'être un hacker pour ça !).
- **sysinfo** : Obtenez des informations système détaillées (Savoir ce qui se cache sous le capot, comme un vrai hacker).
- **send_file <nom_fichier>** : Envoie un fichier, mais pas n'importe comment, il est crypté en Base64 pour que ça fasse sérieux.
- **joke** : Obtenez une blague de hacker pour détendre l'atmosphère. (Pas de bug, juste des blagues !)
- **[commande système]** : Exécute une commande système. Très pratique quand tu veux faire croire que tu contrôles tout.

### 🔥 Features à venir :
- **Plus de blagues** : Parce qu'un hacker rigole toujours, même sous la pression.
- **Plus de commandes d'attaque** : Je veux rendre ce projet plus impressionnant avec des fonctionnalités encore plus "darknet" 😈.
- **Améliorations graphiques** : L'interface ASCII mérite un petit relooking pour impressionner encore plus.

### 🦊 "Pourquoi ce nom ?"  
Parce qu'un hacker, c'est comme un renard. Il est rapide, rusé, et souvent imprévisible. C'est pour ça que j'ai appelé ce projet **"HO MY FOX"**. En plus, j'adore les renards, ils sont trop cool. 🦊

### 📌 Quelques lignes de code pour te donner le ton :

```python
import socket

class HoMyFox:
    def __init__(self, host='127.0.0.1', port=4444):
        self.HOST = host
        self.PORT = port
        self.client = None
        self.hacker_jokes = [
            "Why do hackers prefer dark mode? Because light attracts bugs! 🐛",
            "I don't always test my code, but when I do, I do it in production. 😎",
            "sudo make me a sandwich? Nah, I'll just hack one instead! 🥪",
            "Debugging is like being a detective in a crime movie where you're also the murderer. 🕵️‍♂️",
            "Real programmers count from 0. Fight me! 👊",
        ]
    
    def display_ascii_art(self):
        fox_art = r"""
        ██████╗  ██████╗      ███╗   ███╗██╗   ██╗    ███████╗ ██████╗ ██╗  ██╗
       ██╔═══██╗██╔═══██╗     ████╗ ████║╚██╗ ██╔╝    ██╔════╝██╔═══██╗╚██╗██╔╝
       ██║   ██║██║   ██║     ██╔████╔██║ ╚████╔╝     █████╗  ██║   ██║ ╚███╔╝ 
       ██║   ██║██║   ██║     ██║╚██╔╝██║  ╚██╔╝      ██╔══╝  ██║   ██║ ██╔██╗ 
       ╚██████╔╝╚██████╔╝     ██║ ╚═╝ ██║   ██║       ██║     ╚██████╔╝██╔╝ ██╗
        ╚═════╝  ╚═════╝      ╚═╝     ╚═╝   ╚═╝       ╚═╝      ╚═════╝ ╚═╝  ╚═╝
                       🦊 ADVANCED NETWORK ATTACK TOOL 🌐
        """
        print(fox_art)
        print(f"[🦊] System: {platform.system()} | Python: {platform.python_version()}\n")
```

### 🚨 Disclaimer :
Ce projet est une **simulation de hacking** et n'est **pas destiné à être utilisé de manière malveillante**. Utilise-le uniquement dans un environnement contrôlé (par exemple, avec ton propre réseau ou dans le cadre d'un projet éducatif). **L'usage de cet outil à des fins non éthiques est totalement interdit.**

Si tu as des suggestions, des blagues encore plus drôles ou des idées pour rendre ce projet plus épique, n'hésite pas à ouvrir une **issue** ou envoyer une **pull request** !

### 📢 Suis-moi sur [INSTA](https://www.instagram.com/i_am_the_fox_coder/) pour plus de blagues et de projets cool !
