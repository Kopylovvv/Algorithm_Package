# Алгоритмический пакет

Консольный алгоритмический мини‑пакет на Python: 
функции вычисления факториала числа и чисел Фибоначчи, 
различные алгоритмы сортировок и 
стек, с которым можно работать прямо в консоли.

CLI через `typer` и запуск через `uv`.

## Структура
```
├── src
│   ├── __init__.py
│   ├── algopack
│   │   ├── __init__.py
│   │   ├── math_funcs.py
│   │   ├── sorting_algorithms
│   │   │   ├── __init__.py
│   │   │   ├── bubble.py
│   │   │   ├── bucket.py
│   │   │   ├── count.py
│   │   │   ├── heap.py
│   │   │   ├── quick.py
│   │   │   └── radix.py
│   │   ├── stack_list.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── benchmark.py
│   │       └── generators.py
│   └── cli
│       ├── __init__.py
│       ├── benchmark_cmd.py
│       ├── factorial_cmd.py
│       ├── fibo_cmd.py
│       ├── sort_cmd.py
│       └── stack_cmd.py
├── tests
│   ├── __init__.py
│   ├── test_math_funcs.py
│   ├── test_sorting_algorithms.py
│   └── test_stack.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```
## Установка и запуск
1. Клонировать репозиторий и перейти в папку проекта
```commandline
git clone https://github.com/Kopylovvv/Algorithm_Package.git
cd Algorithm_Package
```
2. Создать и активировать окружение `uv`
```commandline
uv venv
source .venv/bin/activate
```
3. Установить зависимости
```commandline
uv sync
```
4. Вызов команд
```commandline
python -m main <command_name> [options] [flags] 
```
5. Запуск тестов
```commandline
uv run pytest
```



## Модули и функции

### `algopack.math_funcs`

- `factorial`, `factorial_recursive` — факториал `n` для `n >= 0`, при отрицательных `n` выбрасывают `ValueError`
- `fibo`, `fibo_recursive` — n-е число Фибоначчи, итеративная и рекурсивная версии с одинаковым результатом для тех же `n`

### `algopack.sorting_algorithms`

- `bubble_sort`, `quick_sort`, `heap_sort` — классические сортировки списков целых чисел
- `counting_sort` — сортировка целых с произвольным диапазоном (включая отрицательные)
- `radix_sort` — LSD radix sort для неотрицательных целых, при отрицательных выбрасывает `ValueError`
- `bucket_sort` — сортировка `float`

Все сортировки тестируются сравнением с результатом `sorted` на разных массивах

### `algopack.stack_list.Stack`

- Методы: `push`, `pop`, `peek`, `min`, `is_empty`, `__len__`.  
- При некорректных операциях (`pop`/`peek`/`min` на пустом стеке) выбрасывает `IndexError`; минимум поддерживается за O(1) за счёт дополнительного стека

### `algopack.utils.generators` и `benchmark`

- Генераторы: `randint_array`, `nearly_sorted`, `many_duplicates`, `reverse_sorted`, `randfloat_array` — создают массивы для разных сценариев (случайные, почти отсортированные, с большим числом дублей, по убыванию, `float` для bucket sort)  
- Бенчмарк: `benchmark_sorts` принимает словари `{имя_массива: данные}` и `{имя_алгоритма: функция}`, прогоняет все сортировки и возвращает времена выполнения для последующей печати в CLI





## CLI: команды и примеры

CLI реализован на библиотеке Typer: команды и опции описаны через аннотации типов, `--help` генерируется автоматически

### Общий help
```commandline
python -m main --help
```

### `factorial`
```commandline
python -m main factorial 10
python -m main factorial 10 --recursive
```


- Позиционный аргумент `n: int` — значение, для которого считается факториал.  
- Опция `--recursive` / `-r` — использовать рекурсивную версию вместо итеративной.

### `fibo`

```commandline
python -m main sort --algo quick --size 100 --case random
python -m main sort --algo counting --size 50 --case many_duplicates
python -m main sort --algo heap --size 20 --case reverse
```

Опции:

- `--algo` / `-a` — алгоритм: `bubble|quick|counting|radix|bucket|heap`.  
- `--size` / `-n` — размер генерируемого массива.  
- `--case` / `-c` — сценарий генерации:
  - `random` — случайный массив целых.  
  - `nearly_sorted` — почти отсортированный массив.  
  - `many_duplicates` — много повторяющихся значений.  
  - `reverse` — массив, отсортированный по убыванию.

Для `bucket` используется массив `float` (через генератор для `float`), для остальных — массивы целых чисел

### `benchmark`

```commandline
python -m main benchmark --size 1000
```


- Опция `--size` — размер массивов для бенчмарка.

Команда генерирует несколько наборов (`random`, `nearly_sorted`, `many_duplicates`, `reverse_sorted`), прогоняет на них все сортировки и выводит в консоль таблицу с усреднённым временем работы каждой сортировки на каждом наборе данных

### `stack`

```commandline
python -m main stack
```


Запускает интерактивный режим работы со стеком. Доступные команды внутри режима:

- `push <x>` — положить целое число `x` в стек.  
- `pop` — снять верхний элемент (при пустом стеке — сообщение об ошибке).  
- `peek` — посмотреть верхний элемент, не снимая его.  
- `min` — получить текущий минимум за \(O(1)\).  
- `size` — текущий размер стека.  
- `empty` — проверка, пуст ли стек.  
- `exit` — выход из режима.

Ошибки (`pop`/`peek`/`min` на пустом стеке, неверный формат `push`) обрабатываются и выводятся как понятные текстовые сообщения.

---

## Инструменты и особенности

- **Python + src‑layout**: исходники лежат в `src/algopack`, тесты — в `tests`; это упрощает изоляцию зависимостей и работу с путями импорта
- **Typer**: библиотека для удобного создания CLI, использует type hints, автоматически строит help и парсит аргументы командной строки 
- **uv**: менеджер окружений и зависимостей; через `uv venv` создаётся виртуальное окружение, `uv sync` устанавливает зависимости, 
- **pytest**: тесты запускаются командой `uv run pytest`, покрытие кода настраивается через `pyproject.toml` (`--cov=algopack`, `--cov-report=term-missing`)

