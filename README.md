# PineUtils

PineUtils is a Python module designed to provide various utility functionalities, primarily targeted for use on Windows 10. Feedback and contributions are welcome to improve compatibility and features across different platforms.

## Installation

You can install PineUtils using pip:

```bash
pip install PineUtils
```

## Usage

### Importing Modules

```python
from PineUtils import Logger, Input, Files
```

### Classes and Functionalities

#### Logger Module

The `Logger` module provides logging functionalities with themed output.

```python
from PineUtils.Logger import Logger, Themes

Logger.error("This is an error message")
Logger.warn("This is a warning message")
Logger.info("This is an info message")
Logger.success("This is a success message")
Logger.debug("This is a debug message")
```

#### Input Module

The `Input` module provides various prompt types for user input.

```python
from PineUtils.Input import Input

# Example usage
value = Input.Prompt.prompt(Input.Prompt.Types.INTONLY, "Enter an integer:")
print(f"You entered: {value}")
print(type(value))  #: It will be int

custom_map = {
    ("yes", "y", "t", "true", "1"): True,
    ("no", "n", "f", "false", "0"): False,
    ("other", "o", "none"): Other("This is a custom class")
}
result = Input.Prompt.prompt(Input.Prompt.Types.CUSTOM, "Enter a value:", custom_display="yes/no/other", custom_map=custom_map)
print(f"{Chromify.Style.RESET_ALL}Result: {result}")
#: In case the user enter yes, y, t, true, 1. It will return True (bool)
#: In case the user enters no, n, .... result will be False (bool)
#: In case the user enters other, o, none. result will be an instance of the class Other

# Custom input type with lambda
custom_func = lambda x: x.lower() == "true"
result = Input.Prompt.prompt(Input.Prompt.Types.CUSTOM, "Enter a value:", custom_display="true/false", custom_func=custom_func)
print(f"{Chromify.Style.RESET_ALL}Result: {result}")
#: the input will be considered as x, so if x is equal to true (not case sensitive) the result will be True else it will be False
#: for example for a YES confirmation it could be labda m: m == "YES", so the input have to be exactly "YES" case sensitive.

# Solicitando una entrada tipo SELECT con una lista
select_list = ["Option 1", "Option 2", "Option 3"]
result = Input.Prompt.prompt(Input.Prompt.Types.SELECT, "Choose an option:", select_list=select_list)
print(f"{Chromify.Style.RESET_ALL}Result: {result}")
#: Thiw will display a list with their index and the index entered will be the option choosed, in this case:
#> [0] - Option 1
#> [1] - Option 2
#> [2] - Option 3
#: If the user chooses 1 for example, result will be Option 2

# Solicitando una entrada tipo SELECT con un diccionario
select_dict = {
    ("key1", "disp1"): "Value 1",
    ("key2", "disp2"): "Value 2",
    ("other", "other display"): Other("Any value")
}
result = Input.Prompt.prompt(Input.Prompt.Types.SELECT, "Choose an option:", select_list=select_dict)
print(f"{Chromify.Style.RESET_ALL}Result: {result}")
#: Thiw will display a list with their key and display details and the key entered will be then the value
#> [key1] - disp1 * If choosen the result will be "Value 1"
#> [key2] - disp2 * If choosen the result will be "Value 2"
#> [other] - other display * If choosen the result will be an instance of Other()

```

#### Files Module

The `Files` module provides classes related to file operations.

```python
from PineUtils.Files import File, Directory, Path, FileDialog

# Example usage
file = File(FileDialog.open(file_types=[
    ("Python Files", "*.py"),
    ("Text Files", "*.txt"),
    ("Image Files", "*.png, *.jpg, *.jpeg, *.gif")
    ("All Files", "*.*"),
])) # Only Tested in Windows 10!!
print(f"File extension: {file.extension}")
file.loaddata(8192) # this will load all the data of the file into file.bytes[] divided in chunks of 8192 bytes
file.save() # this will save the data into the same file
directory = Directory("C:/Users/Username/Documents")
directory.open() #: Load all the data into the directory.data
print(f"Directory path: {directory.path}, Files: {directory.data}")
#: You can also use File.open(path) this will open the file from that path loading all the data
#: Also do FileDialog.openDirectory() this will return the path to a selected folder (in string)
```

## Contributors

- Author: [Plaraje](mailto:plaraje@proton.me)

## Version

Current version: `0.0.1`

## Feedback

Feedback and bug reports can be submitted via GitHub issues or by contacting the author directly.
This was specially tested in Windows 10 so any feedback is welcome

## More Specific Docs

For more specific docs see also:
- [Logger Class](Logger.md)
- [Input Class](Input.md)
- [Files Class](Files.md)
- [Array2D Class](Array2D.md)