import csv
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))

def main():
    # We use the sys library to open a csv file on our local computer via terminal
    csv_file = open(f"{sys.argv[1]}")

    print("Epale")
    # We read the csv file
    reader = csv.reader(csv_file)

    for isbn,title,author,year in reader:

       # db.execute("INSERT INTO flights (ISBN_number, title, author, publication_year) VALUES (:isbn, :title, :author, :year)",
        #{"isbn": isbn, "title": title, "author": author, "year": year})

        print(f"ISBN {isbn}, Title {title}, Author {author}, Year {year}.")

    #db.commit()

if __name__ == "__main__":
    main()
