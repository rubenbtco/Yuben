"""
    Ce fichier contient la classe DatabaseManager qui est utilisée pour gérer les opérations de base de données.
"""

import mysql.connector

class DatabaseManager:
    def __init__(self, host, user, password, database):
        """
            Constructeur de la classe DatabaseManager.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        """
            Méthode pour obtenir une connexion à la base de données.
        """
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)

    def check_user(self, username, password):
        """
            Méthode pour vérifier si un utilisateur existe dans la base de données.
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utilisateurs WHERE pseudonyme = %s AND mot_de_passe = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    def create_user(self, nom, prenom, pseudonyme, mot_de_passe):
        """
            Méthode pour créer un nouvel utilisateur dans la base de données.
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO utilisateurs (nom, prenom, pseudonyme, mot_de_passe) VALUES (%s, %s, %s, %s)",
                (nom, prenom, pseudonyme, mot_de_passe))
            conn.commit()
            return True
        except Exception as e:
            print(f"Failed to register user: {e}")
            return False
        finally:
            cursor.close()
            conn.close()

    def send_message(self, user_id, message):
        """
            Méthode pour envoyer un message dans le chat, dans la base de données.
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chat (id_eleve, message) VALUES (%s,%s)", (user_id, message,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_messages(self):
        """
            Méthode pour obtenir les messages du chat depuis la base de données.
        """
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                    SELECT utilisateurs.pseudonyme, chat.message 
                    FROM chat
                    JOIN utilisateurs ON chat.id_eleve = utilisateurs.id
                    ORDER BY chat.id DESC LIMIT 3
                """)
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
        return messages