💰 Smart Finance App – INF232 EC2

📌 Description

Smart Finance App est une application web développée en Python avec Flask dans le cadre du TP INF232 EC2 en analyse de données. Elle permet de gérer des clients 

⸻

🎯 Objectif du projet

L’objectif principal est de concevoir une application de collecte de données financières en ligne capable de :
	•	enregistrer des clients
	•	suivre leurs transactions (revenus et dépenses)
	•	analyser les données de manière descriptive
	•	introduire une prédiction simple basée sur le machine learning

⸻

👤 Gestion des clients

L’application permet d’ajouter des clients avec leurs informations de base (nom, contact). Ces données sont stockées dans une base SQLite et peuvent être consultées à tout moment.

⸻

💰 Gestion des transactions financières

Chaque client peut effectuer des transactions de type revenu ou dépense. L’application enregistre ces opérations et calcule automatiquement le suivi du solde global.

⸻

📊 Analyse des données

Une analyse descriptive est intégrée afin de calculer :
	•	le total des revenus
	•	le total des dépenses
	•	le solde final

Ces résultats permettent de visualiser la situation financière globale des données enregistrées.

⸻

🤖 Prédiction (Machine Learning)

Un module de régression linéaire est utilisé pour effectuer une prédiction simple des valeurs futures des transactions, ajoutant une dimension d’analyse intelligente au projet.

⸻

⚙️ Technologies utilisées
	•	Python
	•	Flask
	•	Pandas
	•	NumPy
	•	Scikit-learn
	•	SQLite

⸻

🧠 Structure du projet

Le projet est structuré de manière simple et claire :
	•	app.py : application principale Flask
	•	base de données SQLite : stockage des données
	•	templates : interface utilisateur
	•	requirements.txt : dépendances du projet

⸻

🚀 Déploiement

L’application peut être exécutée localement ou déployée sur une plateforme en ligne afin de générer un lien accessible, comme exigé dans le cadre du TP INF232 EC2.

⸻

👨‍💻 Auteur

Nom : Kenne Mbasso Yvan
Matricule : 24F2736
Projet : INF232 EC2 – Analyse de données

⸻

📌 Conclusion

Ce projet combine la collecte de données, la gestion financière, l’analyse statistique et une introduction au machine learning, dans le but de proposer une application simple, fonctionnelle et pédagogique conforme aux exigences académiques.
