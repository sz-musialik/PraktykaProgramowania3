# Laboratorium 3 - Praktyczne przeglądy kodów i refaktoryzacja kodu
Przegląd i refaktoryzacja kodów z ćwiczenia Tennis Refactoring Kata.

## Opis ćwiczenia
Należało dokonać przeglądu kodu 3 wybranych przez siebie plików i wykonać w nich refaktoryzację kodu.

## tennis1.py

Wykonane refaktoryzacje:
- Opcje punktacji zapisano w tablicy `CLASS_NAME`, co ułatwiło zapis i odczyt punktacji,
- Pozbyto się zapisanych na sztywno nazw gracza i zastąpiono je bardziej uogólnionym zapisem,
- Uproszczono logikę wypisywania punktacji,
- Do istniejących i utworzonych metod dodano dokumentację w formie Docstrings.

## tennis2.py

Wykonane refaktoryzacje:
- Opcje punktacji zapisano w tablicy `CLASS_NAME`, co ułatwiło zapis i odczyt punktacji,
- Pozbyto się zapisanych na sztywno nazw gracza i zastąpiono je bardziej uogólnionym zapisem,
- Uproszczono logikę przyznawania punktów i ustawiania wyniku,
- Uproszczono logikę wypisywania wyniku przez pozbycie się powtórzeń i niepotrzebnie zagnieżdżonych instrukcji warunkowych,
- Do istniejących i utworzonych metod dodano dokumentację w formie Docstrings.

## tennis3.py

Wykonane refaktoryzacje:
- Opcje punktacji zapisano w tablicy `CLASS_NAME`, co ułatwiło zapis i odczyt punktacji,
- Poprawiono nazwenictwo zmiennych, które mogły być niejasne,
- Rozpisano jednolinijkowe instrukcje warunkowe 
- Do istniejących i utworzonych metod dodano dokumentację w formie Docstrings.

## Uruchomienie projektu
Przed uruchomieniem testów należy zainstalować pakiet `pytest` przy pomocy polecenia w konsoli:
```
pip install -r requirements.txt
```

Aby uruchomić testy, należy w konsoli wywołać polecenie:
```
python -m pytest
```
