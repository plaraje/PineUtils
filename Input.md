# Input and InputFormats Classes Documentation

## InputFormats Class

The `InputFormats` class defines various input formats using Chromify colors for enhanced visual presentation.

### Attributes:

- `TEXT`: Color for text input.
- `INT`: Color for integer input.
- `FLOAT`: Color for float input.
- `STRING`: Color for string input.
- `BOOL`: Color for boolean input.
- `CONFIRMATION`: Color for confirmation input.
- `LIST`: Color for list input.
- `NORMAL`: Normal text color.
- `FILE`: Color for file input.
- `DIRECTORY`: Color for directory input.
- `PATH`: Color for path input.
- `FILEDIRECTORY`: Color for file or directory input.
- `SELECT`: Color for select input.
- `CUSTOM`: Color for custom input.

---

## Input Class

The `Input` class provides various input prompts and types through its nested `Prompt` class.

### Nested Classes:

#### `Prompt` Class

Contains static methods for different input prompt types.

##### Static Methods:

- `prompt(inputType, prompt, custom_display="custom", custom_map=None, custom_func=None, file_types=None, select_list=None)`

    Generates a prompt based on the specified `inputType` and retrieves user input accordingly.

    - `inputType`: Type of input prompt to generate (from `Input.Prompt.Types`).
    - `prompt`: Prompt message to display to the user.
    - `custom_display`: Display name for custom input type (default: "custom").
    - `custom_map`: Mapping of custom input values to corresponding results (default: None).
    - `custom_func`: Custom function to process custom input (default: None).
    - `file_types`: List of file types for file input (default: None).
    - `select_list`: List or dictionary for select input (default: None).

    Returns the input value based on the specified `inputType` or `None` if input fails or `inputType` is invalid.

##### Nested Classes:

- `Types`

    Contains constants representing different input prompt types.

    - `NORMAL`: General text input.
    - `CONFIRMATION`: Yes/No confirmation.
    - `STRINGONLY`: Text input only.
    - `INTONLY`: Integer input only.
    - `FLOATONLY`: Float input only.
    - `BOOLONLY`: Boolean input only.
    - `LIST`: List input.
    - `ENTER`: Enter key prompt.
    - `FILE`: File selection prompt.
    - `DIRECTORY`: Directory selection prompt.
    - `PATH`: Path selection prompt.
    - `FILEDIRECTORY`: File or directory selection prompt.
    - `SELECT`: Selection prompt.
    - `CUSTOM`: Custom input prompt.

### Usage:

```python
from PineUtils.Files import FileDialog, File, Directory, Path
import PineUtils.Logger as LG

# Example usage to get integer input
value = Input.Prompt.prompt(Input.Prompt.Types.INTONLY, "Enter an integer:")

# Example usage to get file input
file = Input.Prompt.prompt(Input.Prompt.Types.FILE, "Select a file:", file_types=[("Text Files",".txt"), ("CSV Files",".csv")])

# Example usage to get directory input
directory = Input.Prompt.prompt(Input.Prompt.Types.DIRECTORY, "Select a directory:")

# Example usage to get custom input with a mapping
result = Input.Prompt.prompt(Input.Prompt.Types.CUSTOM, "Enter a fruit:", custom_map={("apple", "Choose red"): "red", ("banana","Choose yellow"): "yellow"})

# Example usage to get selection from a list
fruits = ["apple", "banana", "orange"]
selected_fruit = Input.Prompt.prompt(Input.Prompt.Types.SELECT, "Choose a fruit:", select_list=fruits)
```
