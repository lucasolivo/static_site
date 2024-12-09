import os
import shutil
from markdown_blocks import *
from pathlib import Path
from inline_markdown import *

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
file_path_template = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    print("Generating content...")
    generate_pages_recursive(dir_path_content, file_path_template, dir_path_public)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path) as f:
        from_file = f.read()
    with open(template_path) as f:
        template_file = f.read()
    print(f'from the garden: {from_file}')
    html_node = markdown_to_html_node(from_file)
  #  if not html_node.value:
 #       print("Full node structure:")
 #       print_node_structure(html_node)
  #      return
    html = html_node.to_html()
    title = extract_title(from_file)
    template_file = template_file.replace('{{ Title }}', title)
    template_file = template_file.replace('{{ Content }}', html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, 'w') as f:
        f.write(template_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if not filename.endswith('md'):
                continue
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

def print_node_structure(node, indent=0):
    if node is None:
        print(" " * indent + "Node is None!")
        return
        
    print(" " * indent + f"Type: {type(node)}")
    print(" " * indent + f"Tag: {node.tag}")
    print(" " * indent + f"Value: {node.value}")
    print(" " * indent + f"Props: {node.props}")
    
    children = getattr(node, 'children', None)
    if children is not None:
        print(" " * indent + f"Children count: {len(children)}")
        for child in children:
            print_node_structure(child, indent + 2)

main()
