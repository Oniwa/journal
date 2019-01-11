"""
This module handles the journal data.
"""
import os


def load(name):
    """
    This method creates and loads a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fn:
            for entry in fn.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """
    This method saves a journal entry to the journal file.

    :param name: The base name of the journal to save.
    :param journal_data:  The data of the journal entry to save
    :return: None
    """
    filename = get_full_pathname(name)
    print(f'..... saving to: {filename}')

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    """
    This method gets the path for the journal saves.
    :param name: The base name of the journal file.
    :return: Full path of the journal file
    """
    filename = os.path.abspath(os.path.join('.', 'journals', f'{name}.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    This method adds a journal entry to the journal data.
    :param text: The journal entry.
    :param journal_data: The data of the journal
    :return: None
    """
    journal_data.append(text)

# todo: could model as a class
# todo: convert to pathlib
