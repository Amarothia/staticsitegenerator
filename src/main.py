from populatepublic import populate_public
from generatepage import generate_page

def main():
    populate_public()
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
