import os


def load(name):
    # todo: populate from file if it exists
    return []


def save(name, journal_data):
    filename = get_full_pathname(name)
    print(f'..... saving to: {filename}')

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', f'{name}.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)

# todo: could model as a class
# todo: convert to pathlib