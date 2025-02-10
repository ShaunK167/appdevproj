import os

# Path to the shelve database file
db_path = 'marketplace.db.dat'

# Check if the file exists and delete it
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Database {db_path} has been cleared.")
else:
    print(f"Database {db_path} does not exist.")