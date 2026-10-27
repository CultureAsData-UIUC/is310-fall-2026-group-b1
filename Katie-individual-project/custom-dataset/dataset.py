from rich.console import Console
console = Console()
from rich.table import Table

book_covers = [
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
