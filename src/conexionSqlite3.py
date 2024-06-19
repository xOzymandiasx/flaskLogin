import sqlite3;

try:
  miConexion = sqlite3.connect("db/Usuarios.db");
  cursor = miConexion.cursor();
  cursor.execute("SELECT * FROM personas");
  misUsers = cursor.fetchall();
  for users in misUsers:
    print(users);
except Exception as ex:
  print(ex);