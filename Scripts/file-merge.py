import os

def merge_edges_files(folder_path, output_file):
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    edges_files = [file for file in os.listdir(folder_path) if file.endswith('_edges.txt')]

    with open(output_file, 'w') as output:
        for edges_file in edges_files:
            file_path = os.path.join(folder_path, edges_file)
            with open(file_path, 'r') as input_file:
                output.write(input_file.read())
                output.write('')
    print(f"Merged {len(edges_files)} files into '{output_file}'.")

folder_path = r''
output_file = 'network.txt'

merge_edges_files(folder_path, output_file)
