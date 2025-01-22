import os
import subprocess

def create_markdown_with_code_chunks(directory, output_file):
    """
    Creates a .qmd file where the README.md file (if present) is added first,
    followed by the contents of .yml files in each folder and subfolder within the given directory as code chunks,
    and finally converts the .qmd file to a PDF using Quarto.

    Args:
        directory (str): Path to the directory containing the folders and subfolders.
        output_file (str): Path to the output .qmd file.
    """
    def process_directory(path, depth=0):
        """Processes each folder and its subfolders before moving onto the next folder."""
        indent = "#" * (depth + 1)  # Adjust header level based on depth

        # Creates a list of all the folders in the directory, including sub folders
        entries = sorted(os.listdir(path))
        folders_to_process = [e for e in entries if os.path.isdir(os.path.join(path, e)) and (depth > 0 or e[0].isdigit())]

        for entry in folders_to_process:
            entry_path = os.path.join(path, entry)

            if os.path.isdir(entry_path):
                # Write a header for the folder, includes a hyperlink  to the folder section within the laTEX code
                qmd_file.write(f"{indent} Folder: {entry}\n\n")
                path_clean = entry_path.replace('\\', r'\textbackslash ')
                path_clean = path_clean.replace('_', r'\_')
                link = "folder-" + entry.lower()
                link = link.replace(' ', '').replace(':', '-')
                qmd_file.write(f"\\lohead{{\\hyperref[{link}]{{{path_clean}}}}}\n\n")

                # Process README.md if present
                # For each file, they are read into a code chuck with four `. Three are usually used but the markdown
                # files that are read have code chunks themselves with three `. Increase the number for four if the
                # files use more to create code chunks. 
                readme_path = os.path.join(entry_path, 'README.md')
                if os.path.isfile(readme_path):
                    with open(readme_path, 'r') as readme_file:
                        # Writes the header for the README.md file with a hyperlink
                        path_clean = readme_path.replace('\\', r'\textbackslash ')
                        path_clean = path_clean.replace('_', r'\_')
                        qmd_file.write(f"\\lohead{{{path_clean}}}\n\n")

                        # Creates the section for the README.md and creates a code chunk in markdown
                        qmd_file.write(f"{indent}# README.md\n\n")
                        qmd_file.write("````md\n")
                        qmd_file.write(readme_file.read())
                        qmd_file.write("\n````\n")

                # Process .yml and .md files in the folder
                for sub_entry in sorted(os.listdir(entry_path)):
                    sub_entry_path = os.path.join(entry_path, sub_entry)
                    
                    path_clean = sub_entry_path.replace('\\', r'\textbackslash ')
                    path_clean = path_clean.replace('_', r'\_')

                    # .md and .yml files are read seperatly, first .md files than .yml files
                    if os.path.isfile(sub_entry_path) and sub_entry.endswith('.md') and sub_entry != "README.md":
                        qmd_file.write(f"{indent}# {sub_entry}\n\n")
                        # Additional steps required to clean up the hyperlink references for .md files
                        # References are written automatically when stiching the .qmd file to laTEX file by quarto
                        link = sub_entry.lower()
                        link = ''.join([i for i in link if not i.isdigit()])
                        if link[0] == '_':
                            link = link[1:]
                        link = link.replace(' ', '')
                        link = link.replace(':', '-')
                        qmd_file.write(f"\\lohead{{\\hyperref[{link}]{{{path_clean}}}}}\n\n")
                        with open(sub_entry_path, 'r') as md_file:
                            qmd_file.write("````md\n")
                            qmd_file.write(md_file.read())
                            qmd_file.write("\n````\n")

                    if os.path.isfile(sub_entry_path) and sub_entry.endswith('.yml'):
                        qmd_file.write(f"{indent}# {sub_entry}\n\n")
                        # Additional steps required to clean up the hyperlink references for .yml files
                        # References are written automatically when stiching the .qmd file to laTEX file by quarto
                        link = sub_entry.lower()
                        link = ''.join([i for i in link if not i.isdigit()])
                        if link[0] == '_':
                            link = link[1:]
                        link = link.replace(' ', '')
                        link = link.replace(':', '-')
                        qmd_file.write(f"\\lohead{{\\hyperref[{link}]{{{path_clean}}}}}\n\n")
                        with open(sub_entry_path, 'r') as yml_file:
                            qmd_file.write("````yaml\n")
                            qmd_file.write(yml_file.read())
                            qmd_file.write("\n````\n")

                # Recurse into subdirectories before moving to the next folder
                process_directory(entry_path, depth + 1)

    try:
        with open(output_file, 'w') as qmd_file:
            # Add YAML metadata to configure text wrapping and line numbers for code chunks
            qmd_file.write("---\n")
            qmd_file.write("title: 'Toronto Water WMS Configuration Schema'\n")
            qmd_file.write("format:\n")
            qmd_file.write("    pdf:\n")
# The next line is added to debug the laTEX .tex file as it can be difficult understanding how quarto will interpret custom laTEX code
#            qmd_file.write("        keep-tex: true\n")
            qmd_file.write("        toc: true\n")
            qmd_file.write("        code-line-numbers: true\n")
            qmd_file.write("        header-includes:\n")
            # A list of custom laTEX code that changes the formatting of the pdf file
            qmd_file.write("            - |\n")
            qmd_file.write("                \\usepackage{fvextra}\n")
            qmd_file.write("                \\usepackage{geometry}\n")
            # Use this to change the size of the pages and the different margins
            qmd_file.write("                \\geometry{a4paper, total={170mm,257mm}, left=20mm,top=20mm}\n")
            # This loads a package which is needed to customize the header
            qmd_file.write("                \\usepackage[autooneside=false]{scrlayer-scrpage}\n")
            # Clears the default header options and introduces the footer title and page numbering
            qmd_file.write("                \\lohead{}\n")
            qmd_file.write("                \\cohead{}\n")
            qmd_file.write("                \\cfoot{Toronto Water WMS Configuration Schema}\n")
            qmd_file.write("                \\rofoot{\\thepage}\n")
            # The following code enables text wrapping in the code chunks, unclear on the specifics 
            qmd_file.write("                \\DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\\\\{\\}}\n")
            qmd_file.write("---\n\n")
            qmd_file.write("\\pagebreak\n")

            # Start processing the main directory
            process_directory(directory)

        print(f"Quarto file created at: {output_file}")

        # Convert the .qmd file to a PDF using Quarto
        output_pdf_file = output_file.replace('.qmd', '.pdf')
        subprocess.run(["quarto", "render", output_file, "--to", "pdf"], check=True)
        print(f"PDF file created at: {output_pdf_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function call, change the directory of the file names here 
directory_path = "."
output_qmd_file = "output.qmd"
create_markdown_with_code_chunks(directory_path, output_qmd_file)
