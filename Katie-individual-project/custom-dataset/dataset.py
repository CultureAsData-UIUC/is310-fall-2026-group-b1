import json
from pathlib import Path
output_file = Path("a_thousand_covers.json")

from rich.console import Console
console = Console()
from rich.table import Table

book_covers = [
    {
        "title": "Iliad",
        "translator": "Richard Lattimore",
        "cover_image": "https://press.uchicago.edu/.imaging/mte/ucp/medium/dam/ucp/books/jacket/978/02/26/47/9780226470481.jpg/jcr:content/9780226470481.jpg",
        "publication_year": 2011,
        "publishing_company": "Univeristy of Chicago Press",
        "isbn_13": 9780226470498,
        "cover_type": "example"
    },
    {
        "title": "Iliad",
        "translator": "Richard Lattimore",
        "cover_image": "https://www.lib.uchicago.edu/media/images/lattimore_SoftcoverLattimore.original.jpg",
        "publication_year": 1961,
        "publishing_company": "Univeristy of Chicago Press",
        "isbn_13": 0,
        "cover_type": "example"
    },
    {
        "title": "Iliad",
        "translator": "Richard Lattimore",
        "cover_image": "https://www.lib.uchicago.edu/media/images/lattimore_odysessey.original.jpg",
        "publication_year": 0,
        "publishing_company": "University of Chicago Press",
        "isbn_13": 0,
        "cover_type": "example"
    },
    {
        "title": "Iliad",
        "translator": "Barry B. Powell",
        "cover_image": "https://images.isbndb.com/covers/26347473482258.jpg",
        "publication_year": 2013,
        "publishing_company": "Oxford University Press",
        "isbn_13": 9780199326129,
        "cover_type": "Ebook"
    },
    {
        "title": "Iliad",
        "translator": "Stanley Lombardo",
        "cover_image": "https://images.isbndb.com/covers/14531833482498.jpg",
        "publication_year": 1997,
        "publishing_company": "Hackett Pub. Co",
        "isbn_13": 9780872203525,
        "cover_type": "Paperback"
    },
    {
        "title": "Iliad",
        "translator": "Robert Fitzgerald",
        "cover_image": "https://images.isbndb.com/covers/24523603482429.jpg",
        "publication_year": 1992,
        "publishing_company": "Knopf",
        "isbn_13": 9780679410751,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fitzgerald",
        "cover_image": "https://images.isbndb.com/covers/8971963482321.jpg",
        "publication_year": 2004,
        "publishing_company": "Macmillan",
        "isbn_13": 9780374529055,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Emily Wilson",
        "cover_image": "https://m.media-amazon.com/images/I/91R3cB3kQGL._SY522_.jpg",
        "publication_year": 2024,
        "publishing_company": "WW Norton & Co",
        "isbn_13": 9781324076148,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Emily Wilson",
        "cover_image": "https://m.media-amazon.com/images/I/71XGV6a9MHL._SY522_.jpg",
        "publication_year": 2023,
        "publishing_company": "WW Norton & Co",
        "isbn_13": 9781324001805,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Caroline Alexander",
        "cover_image": "https://images.isbndb.com/covers/1666873482210.jpg",
        "publication_year": 2015,
        "publishing_company": "Ecco",
        "isbn_13": 9780062046277,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fagles",
        "cover_image": "https://images.isbndb.com/covers/23024483482426.jpg",
        "publication_year": 1991,
        "publishing_company": "Penguin",
        "isbn_13": 9780670835102,
        "cover_type": "Hardcovers"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fagles",
        "cover_image": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1625333695i/1371.jpg",
        "publication_year": 1999,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140275360,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fagles",
        "cover_image": "https://m.media-amazon.com/images/I/71r2FXvlR6L._SY522_.jpg",
        "publication_year": 1991,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140445923,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Peter Green",
        "cover_image": "https://images.isbndb.com/covers/6034643482373.jpg",
        "publication_year": 2015,
        "publishing_company": "University of California Press",
        "isbn_13": 9780520281431,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "W. H. D. Rouse",
        "cover_image": "https://images.isbndb.com/covers/20108543482348.jpg",
        "publication_year": 2015,
        "publishing_company": "Signet",
        "isbn_13": 9780451474346,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Alexander Pope",
        "cover_image": "https://images.isbndb.com/covers/26449423482714.jpg",
        "publication_year": 2012,
        "publishing_company": "CreateSpace Independent Publishing Platform",
        "isbn_13": 9781480048348,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Alexander Pope",
        "cover_image": "https://images.isbndb.com/covers/1633463488843.jpg",
        "publication_year": 2020,
        "publishing_company": "Independently Published",
        "isbn_13": 9798691347443,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "George Chapman",
        "cover_image": "https://m.media-amazon.com/images/I/91+OIDfAebL._SY522_.jpg",
        "publication_year": 1998,
        "publishing_company": "Princeton University Press",
        "isbn_13": 9780691002361,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "George Chapman",
        "cover_image": "https://m.media-amazon.com/images/I/81UkqIgdrWL._SY522_.jpg",
        "publication_year": 2003,
        "publishing_company": "Wordsworth Editions Ltd",
        "isbn_13": 9781853262425,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "W. H. D. Rouse",
        "cover_image": "https://images.isbndb.com/covers/15230993482703.jpg",
        "publication_year": 1964,
        "publishing_company": "GROSSET UNIVERSAL LIBRARY",
        "isbn_13": 9781448032136,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Stephen Mitchell",
        "cover_image": "https://m.media-amazon.com/images/I/61Tmf9pRPYL._SY522_.jpg",
        "publication_year": 2013,
        "publishing_company": "Weidenfeld & Nicolson",
        "isbn_13": 9780753827772,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Caroline Alexander",
        "cover_image": "https://m.media-amazon.com/images/I/A1a06Bv9AbL._SY522_.jpg",
        "publication_year": 2017,
        "publishing_company": "Vintage Classics",
        "isbn_13": 9781784870577,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "Anthony Verity",
        "cover_image": "https://m.media-amazon.com/images/I/81QElTQ5RRL._SY466_.jpg",
        "publication_year": 2012,
        "publishing_company": "Oxford University press",
        "isbn_13": 9780199645213,
        "cover_type": "Paperback"
    },    
    {
        "title": "Iliad",
        "translator": "E. V. Rieu",
        "cover_image": "https://m.media-amazon.com/images/I/91sK23D9A4L._SY522_.jpg",
        "publication_year": 2014,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780141394657,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Martin Hammond",
        "cover_image": "https://m.media-amazon.com/images/I/81K5OtgQOGL._SY522_.jpg",
        "publication_year": 1987,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140444445,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "Emily Wilson",
        "cover_image": "https://m.media-amazon.com/images/I/71rp7o5oTnL._SY522_.jpg",
        "publication_year": 2018,
        "publishing_company": "WW Norton & Co",
        "isbn_13": 9780393356250,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "Robert Fagles",
        "cover_image": "https://www.amazon.sg/Odyssey-Homer/dp/0393356256/ref=sr_1_1?crid=255930X4XJZAP&dib=eyJ2IjoiMSJ9.VSvdahgCg6_Yy4KMrXXSyqI9XuFSQBGTtM0Kzj982VkExcfJZ_GaMI8XCaOOFn8zuUqf6HexDof5Qd3sf7F8RaI8lKdt1GWHUbzWk6UD4Vq4BcvNVAGdsEv4B3RkBDxfStp51BLdYUWp_ipS4c3qEZKF_ipD5k6tEcLpd3jPeDhf-jtKe3_9N05m6ATRhUAqNvxF0C6TIE9igFBUle6D3snXZtOxFm4HQFHG4Vj3c1wVEa_2aA7CZvj-BLeg7k8GluTpcr5WlldB7J41Qj_KQWTusnqLM_Wac8yLik6UovE.eeHv2KX3mBohFEm9G-dB85fC0sbVBqOEjU0cM0Tf-TI&dib_tag=se&keywords=odyssey+book&qid=1793687269&sprefix=odyssey+book%2Caps%2C420&sr=8-1",
        "publication_year": 1997,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140268867,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "E. V. Rieu",
        "cover_image": "https://m.media-amazon.com/images/I/91tJdfOKReL._SY522_.jpg",
        "publication_year": 2010,
        "publishing_company": "Penguin UK Classics",
        "isbn_13": 9780141192444,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Odyssey",
        "translator": "E. V. Rieu",
        "cover_image": "https://m.media-amazon.com/images/I/71GRVFSo-hL._SY522_.jpg",
        "publication_year": 203,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780140449112,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "Robert Fitzgerald",
        "cover_image": "https://m.media-amazon.com/images/I/61iBukByAdL._SY522_.jpg",
        "publication_year": 2026,
        "publishing_company": "Picador USA",
        "isbn_13": 9781250375445,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "Robert Fagles",
        "cover_image": "https://m.media-amazon.com/images/I/81-ghHO6JyL._SY522_.jpg",
        "publication_year": 2006,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780143039952,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "Samuel Butler",
        "cover_image": "https://m.media-amazon.com/images/I/617xdL4cjWL._SY466_.jpg",
        "publication_year": 2026,
        "publishing_company": "Thomas Nelson Inc",
        "isbn_13": 9781400356683,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Odyssey",
        "translator": "Alexander Pope",
        "cover_image": "https://m.media-amazon.com/images/I/91U0S2T6EyL._SY522_.jpg",
        "publication_year": 2025,
        "publishing_company": "Chiltern Publishing",
        "isbn_13": 9781914602726,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Odyssey",
        "translator": "Richmond Lattimore",
        "cover_image": "https://m.media-amazon.com/images/I/81NgHUJUQjL._SY522_.jpg",
        "publication_year": 2007,
        "publishing_company": "Harper Perennial Modern Classics",
        "isbn_13": 9780061244186,
        "cover_type": "Paperback"
    },    
    {
        "title": "Odyssey",
        "translator": "Daniel Mendelsohn",
        "cover_image": "https://m.media-amazon.com/images/I/81R4opASwAL._SY522_.jpg",
        "publication_year": 2025,
        "publishing_company": "University of Chicago Press",
        "isbn_13": 9780226604428,
        "cover_type": "Hardcover"
    },    
    {
        "title": "Iliad",
        "translator": "Robert Fitzgerald",
        "cover_image": "https://m.media-amazon.com/images/I/51dEwQigNNL._SY522_.jpg",
        "publication_year": 2007,
        "publishing_company": "Vintage Classics",
        "isbn_13": 9780099511687,
        "cover_type": "Unknown"
    },    
    {
        "title": "Odyssey",
        "translator": "Walter Shewring",
        "cover_image": "https://m.media-amazon.com/images/I/61y4iEwsfgL._SY522_.jpg",
        "publication_year": 2008,
        "publishing_company": "Oxford University Press",
        "isbn_13": 9780199536788,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "W. H. D. Rouse",
        "cover_image": "https://m.media-amazon.com/images/I/61yK5aJBkRL._SY522_.jpg",
        "publication_year": 2015,
        "publishing_company": "Turtleback books",
        "isbn_13": 9781680656565,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "A. T. Murray",
        "cover_image": "https://m.media-amazon.com/images/I/41w5hbt6lQL._SY466_.jpg",
        "publication_year": 2026,
        "publishing_company": "Ithaca Classics",
        "isbn_13": 9798994744840,
        "cover_type": "Paperback"
    },
    {
        "title": "Iliad",
        "translator": "A. T. Murray",
        "cover_image": "https://m.media-amazon.com/images/I/41ZoVGh4HlL._SY466_.jpg",
        "publication_year": 2026,
        "publishing_company": "Ithaca Classics",
        "isbn_13": 9798994744833,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Anthony Verity",
        "cover_image": "https://m.media-amazon.com/images/I/61S8o5L-XIL._SY466_.jpg",
        "publication_year": 2018,
        "publishing_company": "Oxford University Press",
        "isbn_13": 9780198736479,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Samuel Butler",
        "cover_image": "https://m.media-amazon.com/images/I/816a4U+cXqL._SY522_.jpg",
        "publication_year": 2026,
        "publishing_company": "Cantebury Classics",
        "isbn_13": 9781667212166,
        "cover_type": "Flexibound"
    },
    {
        "title": "Odyssey",
        "translator": "Peter Green",
        "cover_image": "https://m.media-amazon.com/images/I/81HlkYrAp8L._SY522_.jpg",
        "publication_year": 2019,
        "publishing_company": "University of California Press",
        "isbn_13": 9780520303362,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Robert Fagles",
        "cover_image": "https://images.isbndb.com/covers/26195773482238.jpg",
        "publication_year": 2020,
        "publishing_company": "Penguin Classics",
        "isbn_13": 9780143139379,
        "cover_type": "example"
    },
    {
        "title": "Odyssey",
        "translator": "Robert Henry Dawson",
        "cover_image": "https://images.isbndb.com/covers/18666473488699.jpg",
        "publication_year": 2025,
        "publishing_company": "Independently Publised",
        "isbn_13": 9798288615368,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Michael Solot",
        "cover_image": "https://images.isbndb.com/covers/17586883482806.jpg",
        "publication_year": 2025,
        "publishing_company": "Society of Classical Poets",
        "isbn_13": 9781737551362,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Robin Lister",
        "cover_image": "https://images.isbndb.com/covers/6886833482456.jpg",
        "publication_year": 2022,
        "publishing_company": "Kingfisher",
        "isbn_13": 9780753478707,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Stephen Mitchell",
        "cover_image": "https://images.isbndb.com/covers/23565713482704.jpg",
        "publication_year": 2014,
        "publishing_company": "Simon and Schuster",
        "isbn_13": 9781451674187,
        "cover_type": "Paperback"
    },
    {
        "title": "Odyssey",
        "translator": "Daniel Mendelsohn",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2026/07/homer-odyssey-mendelsohn-penguin-classics-HB-666x1024.jpg",
        "publication_year": 2026,
        "publishing_company": "Penguin",
        "isbn_13": 9780241733585,
        "cover_type": "Clothbound"
    },
    {
        "title": "Odyssey",
        "translator": "Robert Fitzgerald",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2026/07/homer-odyssey-everymans-library-HB-637x1024.jpg",
        "publication_year": 1992,
        "publishing_company": "Everyman's Library",
        "isbn_13": 9780679410478,
        "cover_type": "Hardcover"
    },
    {
        "title": "Odyssey",
        "translator": "T. E. Lawrence",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2026/07/homer-odyssey-macmillan-collectors-library-632x1024.jpg",
        "publication_year": 2016,
        "publishing_company": "Macmillan Collector's Library",
        "isbn_13": 9781909621459,
        "cover_type": "Hardcover"
    },
    {
        "title": "Odyssey",
        "translator": "Samuel Butler",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2026/04/union-square-deluxe-illustrated-odyssey-homer-2026-612x1024.jpg",
        "publication_year": 2026,
        "publishing_company": "Union Square & Co.",
        "isbn_13": 9781454968047,
        "cover_type": "Hardcover"
    },
    {
        "title": "Odyssey",
        "translator": "T. E. Shaw",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2026/07/homer-odyssey-locked-library-2026-661x1024.jpg",
        "publication_year": 2026,
        "publishing_company": "Harper Collins/The Locked Library",
        "isbn_13": 9780008837723,
        "cover_type": "Hardcover"
    },
    {
        "title": "Odyssey",
        "translator": "Alexander Pope",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2025/05/arcturus-epic-odyssey-homer-2025.jpg",
        "publication_year": 2026,
        "publishing_company": "Sirius/Acturus",
        "isbn_13": 9781398862487,
        "cover_type": "Hardcover"
    },
    {
        "title": "Odyssey",
        "translator": "William Cullen Bryant",
        "cover_image": "https://beautifulbooks.info/wp-content/uploads/2020/09/calla-homer-odyssey-300.jpg",
        "publication_year": 2015,
        "publishing_company": "Calla Editions/Dover",
        "isbn_13": 9781606600771,
        "cover_type": "Hardcover"
    },
]

"""    {
        "title": "title",
        "translator": "example",
        "cover_image": "example",
        "publication_year": 0,
        "publishing_company": "example",
        "isbn_13": 0,
        "cover_type": "example"
    },
"""

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

output_file.write_text(json.dumps(book_covers, indent=4), encoding="utf-8")
console.print(f"File saved in {output_file.resolve()}")