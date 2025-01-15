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

        entries = sorted(os.listdir(path))
        folders_to_process = [e for e in entries if os.path.isdir(os.path.join(path, e)) and (depth > 0 or e[0].isdigit())]

        for entry in folders_to_process:
            entry_path = os.path.join(path, entry)

            if os.path.isdir(entry_path):
                # Write a header for the folder
                qmd_file.write(f"{indent} Folder: {entry}\n\n")

                # Process README.md if present
                readme_path = os.path.join(entry_path, 'README.md')
                if os.path.isfile(readme_path):
                    with open(readme_path, 'r') as readme_file:
                        qmd_file.write(f"{indent}# README.md\n\n")
                        qmd_file.write("```md\n")
                        qmd_file.write(readme_file.read())
                        qmd_file.write("```\n\n")

                # Process .yml files in the folder
                for sub_entry in sorted(os.listdir(entry_path)):
                    sub_entry_path = os.path.join(entry_path, sub_entry)

                    if os.path.isfile(sub_entry_path) and sub_entry.endswith('.yml'):
                        qmd_file.write(f"{indent}# {sub_entry}\n\n")
                        with open(sub_entry_path, 'r') as yml_file:
                            qmd_file.write("```yaml\n")
                            qmd_file.write(yml_file.read())
                            qmd_file.write("\n```\n")

                # Recurse into subdirectories before moving to the next folder
                process_directory(entry_path, depth + 1)

    try:
        with open(output_file, 'w') as qmd_file:
            # Add YAML metadata to configure text wrapping and line numbers for code chunks
            qmd_file.write("---\n")
            qmd_file.write("title: 'Toronto Water WMS Configuration Schema'\n")
            qmd_file.write("format:\n")
            qmd_file.write("    pdf:\n")
            qmd_file.write("        toc: true\n")
            qmd_file.write("        code-line-numbers: true\n")
            qmd_file.write("        header-includes:\n")
            qmd_file.write("            - |\n")
            qmd_file.write("                \\usepackage{fvextra}\n")
            qmd_file.write("                \\usepackage[autooneside=false, automark]{scrlayer-scrpage}\n")
            qmd_file.write("                \\automark[subsection]{section}\n")
            qmd_file.write("                \\lohead{/\\leftmark/}\n")
            qmd_file.write("                \\cohead{}\n")
            qmd_file.write("                \\cfoot{Toronto Water WMS Configuration Schema}\n")
            qmd_file.write("                \\rofoot{\\thepage}\n")
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

# Function call 
directory_path = "."
output_qmd_file = "output.qmd"
create_markdown_with_code_chunks(directory_path, output_qmd_file)
