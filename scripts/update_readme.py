import glob

legend_paths = glob.glob('legends/*.md')

readme_str = '# Legends of Iran\nIn memory of the women, men, and children of Iran who lost their lives to the evil Islamic Republic.\n'
for path in legend_paths:
    with open(path, 'r') as fs:
        readme_str += fs.read()

with open('README.md', 'w+') as fs:
    fs.write(readme_str)
