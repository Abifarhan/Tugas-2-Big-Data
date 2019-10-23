from pathlib import Path

path = Path('data/')

pathlist = path.rglob('*.txt')

# Untuk membersihkan tanda petik pada teks agar data bisa diproses
for path in pathlist:
    with open(path, 'r') as file:
        data = file.readlines()
        if not data:
            continue
        title, content = data[0], data[1:]
        title = title.replace("'", '')
        content.insert(0, title)

    with open(path, 'w') as file:
        file.writelines(content)
