def ispresent(person):
    names = ['N2', 'bn', 'TS']
    if person in names:
        return True
    else:
        return False


def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False
