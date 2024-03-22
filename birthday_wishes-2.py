def send_wishes(recipient=str, birth_year=int, message=str, sender=str):
    print(f'{recipient}, wszystkiego najlepszego z okazji {2024 - birth_year} '
          f'urodzin!\n{message}\n{sender}')


send_wishes('Heniek', 1978, '100 lat!', 'Piotr')
