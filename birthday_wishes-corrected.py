from datetime import datetime

recipient = input('Podaj imie solenizanta: ')
birth_year = int(input('Podaj Jego rok urodzenia: '))
message = input('Napisz wiadomosc z zyczeniami: ')
sender = input('Podaj swoje imie: ')
current_year = datetime.now().year
age = current_year - birth_year

print(f'{recipient}, wszystkiego najlepszego z okazji {age} urodzin!\n'
      f'{message}\n{sender}')
