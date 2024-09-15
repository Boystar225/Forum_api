# API Rest Gestion d'un Forum
Développement d'une API REST pour la gestion d'un forum avec Django

## Les étapes d'installation de l'application :
- Ouvrer un terminal puis cloner le lien github de l'application : git clone https://github.com/Boystar225/Forum_api.git
- Créer un environnement virtuel dans le repertoire ( python ou python3 pour Unix -m venv venv ou env)
- Naviguer vers le fichier activate.bat soit dans scripts ou bin, puis activer l'environnement (source activate ou activate pour windows)
- Revener au repertoire de votre projet puis installer les dépendances de l'application à partir du fichier requirements.txt (pip ou pip3 install -r requirements.txt)
- Installez et configurez une base de données Postgresql 'forum_db' configurer les accès dans le fichier settings.py
- Naviguez vers le repertoire source (src) puis créer et appliquer les migrations : python manage.py makemigrations ensuite python manage.py migrate
  
## Les instructions de démarrage :
- Naviguez vers le repertoire source (src) puis lancer le server : python manage.py runserver, vous pouvez preciser le port python manage.py runserver numeros_port ( exple : python manage.py runserver 7879)
- Vous pouvez tester avec le navigateur ou avec Postman 
  
## Description des fonctionnalités principales de l'application :

### Gestion des forums
- Création d'un nouveau forum
- Liste des forums existants
- Récupération des détails d'un forum
### Gestion des sujets
- Création d'un nouveau sujet dans un forum
- Liste des sujets d'un forum
- Récupération des détails d'un sujet
### Gestion des messages 
- Création d'un nouveau message dans un sujet
- Liste des messages d'un sujet


