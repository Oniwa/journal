"""
This is the journal module.
"""
import journal


def main():
    """
    This method is the main function for the program.
    :return: None
    """
    print_header()
    run_event_loop()


def print_header():
    """
    This method prints the program header.
    :return: None
    """
    print('-----------------------------')
    print('        JOURNAL APP')
    print('-----------------------------')


def run_event_loop():
    """
    This method is the event loop for the program.
    :return: None
    """
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, or E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f'Sorry, we don\'t understand \'{cmd}\'.')

    print("Done, goodbye.")
    journal.save(journal_name, journal_data)


def list_entries(data):
    """
    This method lists all of the journal entries.
    :param data: This is the journal data.
    :return: None
    """
    print('Your journal entries: ')

    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(f'* [{idx + 1}] {entry}')


def add_entry(data):
    """
    This method adds an entry to the journal data
    :param data: This is a journal entry
    :return: None
    """
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, data)


if __name__ == "__main__":
    main()
