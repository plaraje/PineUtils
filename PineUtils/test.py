from Chromify import init, Style
init() # For colors
# Importing Modules
import Logger, Input, Files

# Logger Module
from Logger import Logger, Themes

Logger.error("This is an error message")
Logger.warn("This is a warning message")
Logger.info("This is an info message")
Logger.success("This is a success message")
Logger.debug("This is a debug message")

from Input import Input

class Other:
    def __init__(self, value:str, *args, **kwargs) -> None:
        self.value = value
    def __str__(self):
        return f"Other({self.value})"
    def __repr__(self):
        return f"Other({self.value})"

# Example usage
value = Input.Prompt.prompt(Input.Prompt.Types.INTONLY, "Enter an integer:")
print(f"{Style.RESET_ALL}You entered: {value}")
print(type(value))

custom_map = {
    ("yes", "y", "t", "true", "1"): True,
    ("no", "n", "f", "false", "0"): False,
    ("other", "o", "none"): Other("This is a custom class")
}
result = Input.Prompt.prompt(Input.Prompt.Types.CUSTOM, "Enter a value:", custom_display="yes/no/other", custom_map=custom_map)
print(f"{Style.RESET_ALL}Result: {result}")

custom_func = lambda x: x.lower() == "true"
result = Input.Prompt.prompt(Input.Prompt.Types.CUSTOM, "Enter a value:", custom_display="true/false", custom_func=custom_func)
print(f"{Style.RESET_ALL}Result: {result}")

select_list = ["Option 1", "Option 2", "Option 3"]
result = Input.Prompt.prompt(Input.Prompt.Types.SELECT, "Choose an option:", select_list=select_list)
print(f"{Style.RESET_ALL}Result: {result}")

select_dict = {
    ("key1", "disp1"): "Value 1",
    ("key2", "disp2"): "Value 2",
    ("other", "other display"): Other("Any value")
}
result = Input.Prompt.prompt(Input.Prompt.Types.SELECT, "Choose an option:", select_list=select_dict)
print(f"{Style.RESET_ALL}Result: {result}")

# Files Module
from Files import File, Directory, Path, FileDialog

# Example usage
file = File(FileDialog.open(file_types=[
    ("Python Files", "*.py"),
    ("Text Files", "*.txt"),
    ("Image Files", "*.png, *.jpg, *.jpeg, *.gif"),
    ("All Files", "*.*"),
]))  # Only Tested in Windows 10!!
print(f"{Style.RESET_ALL}File extension: {file.extension}")
file.loaddata(8192)
file.save()
directory = Directory("C:/Users/Username/Documents")
directory.path = Path(FileDialog.openDirectory())
directory.open()
print(f"Directory path: {directory.path}, Files: {directory.data}")


def tree(dir, mother: str="/"):
    if isinstance(dir, Directory):
        for file in dir.data:
            if isinstance(file, File):
                Logger.info(f"{mother}File({file.fullname})")
            if isinstance(file, Directory):
                tree(file, dir.path)
    else:
        Logger.info(f"File({dir.fullname})")

tree(directory, directory.path)