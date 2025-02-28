from populatepublic import populate_public
from generatepage import generate_pages_recursive

def main():
    populate_public()
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
