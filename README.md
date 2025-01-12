# Blocky Game

## Podsumowanie

Projekt zawiera formalny model w PDDL i implementację narzędzia
umożliwiającego interakcję z systemem opartym o autorskie rozwinięcie
gry logicznej N-Puzzle. Dodatkowo, możliwe jest przeprowadzenie
procesu generowania nowych instancji problemów w oparciu o zdefiniowane
przez użytkownika parametry, import i eksport instancji problemów oraz 
przeprowadzenie procesu ich rozwiązywania za pomocą
gotowych narzędzi planistycznych, takich jak [Fast Downward](https://www.fast-downward.org/HomePage).

## Proces przygotowania środowiska

Czynnością konieczną do uruchomienia projektu jest zainstalowanie interpretera języka [Python](https://www.python.org/)
w wersji 3.12 lub nowszej wraz z menedżerem pakietów [pip](https://pypi.org/project/pip/).
Następnie, należy zainstalować biblioteki wymagane do działania narzędzia.
W tym celu należy wykonać poniższe polecenie:

```bash
pip install -r requirements.txt
```

## Uruchomienie programu

W celu uruchomienia programu należy wykonać poniższe polecenie:

```bash
python main.py
```

Na ekranie powinno pojawić się okno programu, w którym dostępne są
przyciski umożliwiające interakcję z systemem. Program automatycznie
zakończy działanie po zamknięciu okna lub w przypadku rozwiązania
instancji problemu.

## Konfiguracja

Wszystkie parametry związane z generowaniem, importem i eksportem
instancji problemów i ustawieniami graficznymi można znaleźć i skonfigurować
w `blocky_game/config/config.py`. W pliku tym znajdują się
dwie klasy: `PyGameConfig` oraz `BlockyGameConfig`. Pierwsza z nich
zawiera parametry związane z ustawieniami graficznymi, takimi jak
rozmiar okna, oczekiwana liczba klatek na sekundę,
szybkość animacji, itp. Druga klasa zawiera parametry związane z
generowaniem instancji problemów, takie jak rozmiar planszy, liczba
kluczy oraz wszystkie parametry umożliwiające konfigurację
ścieżek do plików i katalogów związanych z importem i eksportem.

```python
@dataclass
class PyGameConfig:
    # Liczba klatek na sekundę
    frames_per_second: int = 30
    # Szerokość okna
    screen_width: int = 1200 
    # Wysokość okna
    screen_height: int = 750 
    # Tytuł okna
    screen_title: str = "Blocky Game" 
    size_ratio: float = 0.9 
    # Czas oczekiwania na wykonanie kolejnej akcji
    actions_delay = 250.0 
    # Czas trwania animacji
    animation_duration = 500.0 
    # Tryb pełnoekranowy
    fullscreen = False 
    # Czy używać natywnej rozdzielczości ekranu zamiast określonej w konfiguracji
    use_native_screen_resolution = False 


@dataclass
class BlockyGameConfig:
    # Nazwa definicji domeny, musi być zgodna z nazwą pliku w katalogu domain
    domain_definition_name: str = "blocky_game"
    # Ńazwa pliku z definicją problemu, musi być umieszczona w katalogu problems
    problem_definition_path: str = "problem-experiment_6x6_6_60_2/problem-experiment_6x6_6_60_2-subproblem-4.pddl"
    # Określa nazwę pliku (bez rozszerzenia), do którego zostanie zapisana lista akcji
    state_serialization_name: str | None = "problem-experiment_7x7_6_150_48"
    # Nazwa pliku z sekwencją akcji, opcjonalna, w przypadku podania None akcje będą wprowadzane przez użytkownika
    actions_list_name: str | None = None # "problem2-solution"
    # Konfiguracja generatora instancji problemów (zobacz `blocky_game/config/config_helper.py`)
    generator_config: GeneratorConfig | None = \
        GeneratorConfig(7, 7, 6, 150, SimpleProblemGenerator)
```

Projekt umożliwia również możliwość wczytywania i zapisu
sekwencji wykonanych akcji i ich odtwarzania, uwzględniając
przy tym animację ruchów. W celu wczytania sekwencji akcji
należy określić ścieżkę do pliku z sekwencją w pliku konfiguracyjnym.
Format pliku z sekwencją akcji można znaleźć w pliku `solutions/problem1-solution.actions`. 

## Dodatkowe informacje

Projekt został zrealizowany w ramach projektu dyplomowego
na Akademii Górniczo-Hutniczej w Krakowie w 2025 roku.
