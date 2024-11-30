import mysql.connector
import os

# Database connection details
db_config = {
    "host": "db",
    "user": os.getenv("MYSQL_USER", "test_user"),
    "password": os.getenv("MYSQL_PASSWORD", "test_password"),
    "database": os.getenv("MYSQL_DATABASE", "test_db"),
}

def query_database():
    try:
       
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create a sample table and insert data
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));")
        cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');")
        conn.commit()
        
        # Query the database
        cursor.execute("SELECT * FROM users;")
        results = cursor.fetchall()
        
        # Print results
        print("User data from the database:")
        for row in results:
            print(row)
        
        # Close the connection
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    query_database()
