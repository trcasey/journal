
def print_header():
    print('-------------------------------------')
    print('            DAILY JOURNAL')
    print('-------------------------------------')

def run_event_loop():
    pass

def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = None

    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            print('L')
        elif cmd == 'a':
            print('A')
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'.".format(cmd))

    print('Goodbye.')

def list_entries():
    print('Listing...')

def add_entry():
    print('Adding...')

def main():
    print_header()
    run_event_loop()

main()