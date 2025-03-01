from populatepublic import populate_public
from generatepage import generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1]
    populate_public("docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
