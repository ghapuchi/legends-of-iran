import glob

legend_paths = glob.glob('legends/*.md')

readme_str = '# Legends who gave their life in the fight against the evil of the Islamic Republic in Iran.\n\n'
for path in legends_path:
    with open(path, 'r') as fs:
        readme_str += fs.read()

with open('README.md', 'w+') as fs:
    fs.write(readme_str)
