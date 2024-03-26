from datetime import datetime

current_year = datetime.now().year


def send_wishes():
    recipient = input('Podaj imie solenizanta/ki: ')
    recipient = recipient.capitalize()
    birth_year = int(input('Podaj Jego/Jej rok urodzenia: '))
    message = input('Wpisz zyczenia: ')
    sender = input('Podaj swoje imie: ')
    sender = sender.capitalize()

    wishes = (
        f'{recipient}, wszystkiego najlepszego z okazji '
        f'{current_year - birth_year} urodzin!\n{message}\n{sender}'
    )

    print(wishes)


send_wishes()
