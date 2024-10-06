from cs50 import SQL

db = SQL("sqlite:///favorite.db")

favorite = input("Favorites: ")

rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)
row = rows[0]

print(row["n"])
