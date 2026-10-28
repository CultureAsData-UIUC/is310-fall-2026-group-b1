from rich.console import Console
console = Console()
from rich.table import Table

book_covers = [
    {
        "title": "Iliad",
        "translator": "Richard Lattimore",
        "cover_image": "example",
        "publication_year": 2011,
        "publishing_company": "Univeristy of Chicago Press",
        "isbn_13": 9780226470498,
        "cover_type": "example"
    },
    {
        "title": "Iliad",
        "translator": "Richard Lattimore",
        "cover_image": "example",
        "publication_year": 1961,
        "publishing_company": "Univeristy of Chicago Press",
        "isbn_13": 0,
        "cover_type": "example"
    },
    {
        "title": "Iliad",
        "translator": "Richard Lattimore",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "University of Chicago Press",
        "isbn_13": 0,
        "cover_type": "example"
    },
    {
        "title": "Iliad",
        "translator": "Barry B. Powell",
        "cover_image": "example",
        "publication_year": 2013,
        "publishing_company": "Oxford University Press",
        "isbn_13": 9780199326129,
        "cover_type": "Ebook"
    },
    {
        "title": "Iliad",
        "translator": "Stanley Lombardo",
        "cover_image": "example",
        "publication_year": 1997,
        "publishing_company": "Hackett Pub. Co",
        "isbn_13": 9780872203525,
        "cover_type": "Paperback"
    },
    {
        "title": "Iliad",
        "translator": "Robert Fitzgerald",
        "cover_image": "example",
        "publication_year": 1992,
        "publishing_company": "Knopf",
        "isbn_13": 9780679410751,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fitzgerald",
        "cover_image": "example",
        "publication_year": 2004,
        "publishing_company": "Macmillan",
        "isbn_13": 9780374529055,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Emily Wilson",
        "cover_image": "example",
        "publication_year": 2024,
        "publishing_company": "WW Norton & Co",
        "isbn_13": 9781324076148,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Emily Wilson",
        "cover_image": "example",
        "publication_year": 2023,
        "publishing_company": "WW Norton & Co",
        "isbn_13": 9781324001805,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Caroline Alexander",
        "cover_image": "example",
        "publication_year": 2015,
        "publishing_company": "Ecco",
        "isbn_13": 9780062046277,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fagles",
        "cover_image": "example",
        "publication_year": 1991,
        "publishing_company": "Penguin",
        "isbn_13": 9780670835102,
        "cover_type": "Hardcovers"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fagles",
        "cover_image": "example",
        "publication_year": 1999,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140275360,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fagles",
        "cover_image": "example",
        "publication_year": 1991,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140445923,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Peter Green",
        "cover_image": "example",
        "publication_year": 2015,
        "publishing_company": "University of California Press",
        "isbn_13": 9780520281431,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "W. H. D. Rouse",
        "cover_image": "example",
        "publication_year": 2015,
        "publishing_company": "Signet",
        "isbn_13": 9780451474346,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Alexander Pope",
        "cover_image": "example",
        "publication_year": 2012,
        "publishing_company": "CreateSpace Independent Publishing Platform",
        "isbn_13": 9781480048348,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Alexander Pope",
        "cover_image": "example",
        "publication_year": 2020,
        "publishing_company": "Independently Published",
        "isbn_13": 9798691347443,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "George Chapman",
        "cover_image": "example",
        "publication_year": 1998,
        "publishing_company": "Princeton University Press",
        "isbn_13": 9780691002361,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "george Chapman",
        "cover_image": "example",
        "publication_year": 2003,
        "publishing_company": "Wordsworth Editions Ltd",
        "isbn_13": 9781853262425,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },    
    {
        "title": "Iliad",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },
]

def initial_table(book_list):
    table = Table(title="Iliad and Odyssey Dataset", style="dark_blue")
    table.add_column("Title", justify="center")
    table.add_column("Translator", justify="center")
    table.add_column("Cover Image", justify="center")
    table.add_column("Publication Year", justify="center")
    table.add_column("Publishing Company", justify="center")
    table.add_column("ISBN-13", justify="center")
    table.add_column("Cover Type", justify="center")
    for book in book_list:
        table.add_row(book["title"], book["translator"], book["cover_image"], 
        str(book["publication_year"]), book["publishing_company"],
        str(book["isbn_13"]), book["cover_type"])

    console.print(table)
    
initial_table(book_covers)
