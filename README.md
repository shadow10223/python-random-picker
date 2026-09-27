# Random Picker with History

A small Python tool that picks a random option from a list and logs each pick with a timestamp.

## What It Does

- Reads a list of options from `options.txt`
- Randomly picks one option each time it runs
- Displays the pick and the current date-time
- Appends every pick to `history.txt` with a timestamp

## How to Run

1. Make sure Python 3 is installed
2. Make sure `options.txt` exists in the same folder (one option per line)
3. Run:
python3 picker.py

## Technologies Used

- Python 3
- `random` module — for `random.choice()`
- `datetime` module — for timestamps
- `os` module — for portable file paths
- File I/O — reading options, appending history

## What I Learned

- Importing and using multiple modules in one program
- The difference between `import X` and `from X import Y`
- Using `random.choice()` to pick from a list
- Getting the current date-time with `datetime.datetime.now()`
- Building portable file paths with `os.path.dirname` and `os.path.join`
- Appending to a file without overwriting it (`"a"` mode)
- Using f-strings to format output

## Future Improvements

- Add a menu to view/clear history
- Support multiple option files (e.g., `food.txt`, `movies.txt`)
- Add a `--count` flag to pick multiple options at once
- Save history in CSV or JSON format for easier analysis