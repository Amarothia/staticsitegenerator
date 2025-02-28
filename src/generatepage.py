from markdowntohtmlnode import markdown_to_html_node
from extracttitle import extract_title
import os, shutil

# os.path.exists
# os.listdir
# os.path.join
# os.path.isfile
# os.mkdir
# os.path.dirname
# os.makedirs
# shutil.copy
# shutil.rmtree

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown_text = f.read()
    with open(template_path) as f:
        template_html = f.read()
    html_string = markdown_to_html_node(markdown_text).to_html()
    title = extract_title(markdown_text)
    revised_html = template_html.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    directory_of_final_html_file = os.path.dirname(dest_path)
    if os.path.exists(directory_of_final_html_file) == False:
        os.makedirs(directory_of_final_html_file)
    with open(dest_path, 'w') as f:
        f.write(revised_html)
    