import Chromify
from Files import FileDialog, File, Directory, Path
import Logger as LG

class InputFormats:
    """
    Defines various input formats using Chromify colors.

    Attributes:
    - TEXT: Color for text input.
    - INT: Color for integer input.
    - FLOAT: Color for float input.
    - STRING: Color for string input.
    - BOOL: Color for boolean input.
    - CONFIRMATION: Color for confirmation input.
    - LIST: Color for list input.
    - NORMAL: Normal text color.
    - FILE: Color for file input.
    - DIRECTORY: Color for directory input.
    - PATH: Color for path input.
    - FILEDIRECTORY: Color for file or directory input.
    - SELECT: Color for select input.
    - CUSTOM: Color for custom input.
    """
    TEXT = Chromify.Color("#ffff33")
    INT = Chromify.Color("#e33529")
    FLOAT = Chromify.Color("#00ffff")
    STRING = Chromify.Color("#fff000")
    BOOL = Chromify.Color("#11ff11")
    CONFIRMATION = Chromify.Color("#ff2222")
    LIST = Chromify.Color("#ff00ff")
    NORMAL = Chromify.Color("#dfdfdf")
    FILE = Chromify.Color("#ff9900")
    DIRECTORY = Chromify.Color("#99ff99")
    PATH = Chromify.Color("#9999ff")
    FILEDIRECTORY = Chromify.Color("#ff99a3")
    SELECT = Chromify.Color("#33ccff")
    CUSTOM = Chromify.Color("#ff6699")

class Input:
    """
    Class providing various input prompts and types.

    Nested Classes:
    - Prompt: Class containing static methods for different input prompt types.

    Methods:
    - __init__: Initializes an instance of Input.
    """
    class Prompt:
        """
        Nested class providing static methods for different input prompt types.

        Static Methods:
        - prompt: Generates a prompt based on the specified inputType and retrieves user input accordingly.
        """
        class Types:
            """
            Nested class containing constants representing different input prompt types.
            """
            NORMAL = {"type": "1"}
            CONFIRMATION = {"type": "2"}
            STRINGONLY = {"type": "3"}
            INTONLY = {"type": "4"}
            FLOATONLY = {"type": "5"}
            BOOLONLY = {"type": "6"}
            LIST = {"type": "7"}
            ENTER = {"type": "8"}
            FILE = {"type": "9"}
            DIRECTORY = {"type": "10"}
            PATH = {"type": "11"}
            FILEDIRECTORY = {"type": "12"}
            SELECT = {"type": "13"}
            CUSTOM = {"type": "14"}

        @staticmethod
        def prompt(inputType, prompt, custom_display="custom", custom_map=None, custom_func=None, file_types=None, select_list=None):
            """
            Generates a prompt based on the specified inputType and retrieves user input accordingly.

            Args:
            - inputType: Type of input prompt to generate (from Input.Prompt.Types).
            - prompt: Prompt message to display to the user.
            - custom_display: Display name for custom input type (default: "custom").
            - custom_map: Mapping of custom input values to corresponding results (default: None).
            - custom_func: Custom function to process custom input (default: None).
            - file_types: List of file types for file input (default: None).
            - select_list: List or dictionary for select input (default: None).

            Returns:
            - Input value based on the specified inputType or None if inputType is invalid or input fails.
            """

            if inputType == Input.Prompt.Types.CONFIRMATION:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.CONFIRMATION.fore()}(YES/NO){InputFormats.TEXT.fore()}> {InputFormats.CONFIRMATION.fore()}")
                if value.lower() in ["yes", "y"]:
                    return True
                elif value.lower() in ["no", "n"]:
                    return False
                else:
                    return None
            elif inputType == Input.Prompt.Types.STRINGONLY:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.STRING.fore()}(text){InputFormats.TEXT.fore()}> {InputFormats.STRING.fore()}")
                return value
            elif inputType == Input.Prompt.Types.INTONLY:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.INT.fore()}(int){InputFormats.TEXT.fore()}> {InputFormats.INT.fore()}")
                try:
                    value = int(value)
                except Exception:
                    value = None
                return value
            elif inputType == Input.Prompt.Types.FLOATONLY:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.FLOAT.fore()}(num){InputFormats.TEXT.fore()}> {InputFormats.FLOAT.fore()}")
                try:
                    value = float(value.replace(",", "."))
                except Exception:
                    value = None
                return value
            elif inputType == Input.Prompt.Types.BOOLONLY:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.BOOL.fore()}(bool){InputFormats.TEXT.fore()}> {InputFormats.BOOL.fore()}")
                if value.lower() in ["y", "yes", "1", "true", "t"]:
                    return True
                elif value.lower() in ["n", "no", "0", "false", "f"]:
                    return False
                else:
                    return None
            elif inputType == Input.Prompt.Types.LIST:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.LIST.fore()}(list){InputFormats.TEXT.fore()}> {InputFormats.LIST.fore()}")
                value = value.strip(" ").split(",")
                lst = list()
                for e in value:
                    lst.append(e.strip(" "))
                return lst
            elif inputType == Input.Prompt.Types.FILE:
                print(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.FILE.fore()}(file){InputFormats.TEXT.fore()}> {InputFormats.FILE.fore()}")
                file = File(FileDialog.open(file_types))
                return file
            elif inputType == Input.Prompt.Types.DIRECTORY:
                print(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.DIRECTORY.fore()}(directory){InputFormats.TEXT.fore()}> {InputFormats.DIRECTORY.fore()}")
                directory = Directory(FileDialog.openDirectory())
                return directory
            elif inputType == Input.Prompt.Types.PATH:
                print(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.PATH.fore()}(path){InputFormats.TEXT.fore()}> {InputFormats.PATH.fore()}")
                path_type = Input.Prompt.prompt(Input.Prompt.Types.NORMAL, f"{InputFormats.TEXT.fore()}\t  > Choose path type {InputFormats.PATH.fore()}({InputFormats.FILE.fore()}file{InputFormats.PATH.fore()}/{InputFormats.DIRECTORY.fore()}directory{InputFormats.PATH.fore()}): ").lower()
                if path_type in ["file", "f", "0"]:
                    return FileDialog.open(file_types)
                elif path_type in ["directory", "d", "1", "dir"] or path_type.startswith("dir"):
                    return FileDialog.openDirectory()
                else:
                    return None
            elif inputType == Input.Prompt.Types.FILEDIRECTORY:
                print(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.FILEDIRECTORY.fore()}(file/directory){InputFormats.TEXT.fore()}> {InputFormats.FILEDIRECTORY.fore()}")
                path_type = Input.Prompt.prompt(Input.Prompt.Types.NORMAL, f"{InputFormats.TEXT.fore()}\t  > Choose path type {InputFormats.FILEDIRECTORY.fore()}({InputFormats.FILE.fore()}file{InputFormats.FILEDIRECTORY.fore()}/{InputFormats.DIRECTORY.fore()}directory{InputFormats.FILEDIRECTORY.fore()}): ").lower()
                if path_type in ["file", "f", "0"]:
                    return File(FileDialog.open(file_types))
                elif path_type in ["directory", "d", "1", "dir"] or path_type.startswith("dir"):
                    return Directory(FileDialog.openDirectory())
                else:
                    return None
            elif inputType == Input.Prompt.Types.SELECT:
                if isinstance(select_list, list):
                    for index, item in enumerate(select_list):
                        print(f"[{index}] - {item}")
                elif isinstance(select_list, dict):
                    for key, display in select_list.keys():
                        print(f"[{key}] - {display}")
                else:
                    return None

                while True:
                    value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:> {InputFormats.NORMAL.fore()}")
                    if isinstance(select_list, list):
                        try:
                            value = int(value)
                            if 0 <= value < len(select_list):
                                return select_list[value]
                        except ValueError:
                            pass
                    elif isinstance(select_list, dict):
                        for key, display in select_list.keys():
                            if value.lower() == key.lower() or value.lower() == display.lower():
                                return select_list[(key, display)]
                    LG.Logger.whiteLine()
                    LG.Logger.error("Invalid selection. Please enter a valid option.", "INPUT ERROR", preindentations=1)
                    LG.Logger.whiteLine()
            elif inputType == Input.Prompt.Types.CUSTOM:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:{InputFormats.CUSTOM.fore()}({custom_display}){InputFormats.TEXT.fore()}> {InputFormats.CUSTOM.fore()}")
                if custom_map:
                    for key, result in custom_map.items():
                        if isinstance(key, (list, tuple)) and value in key:
                            return result
                        elif value == key:
                            return result
                if custom_func:
                    return custom_func(value)
                return value
            else:
                value = input(f"\t{prompt} {InputFormats.TEXT.fore()}:> {InputFormats.NORMAL.fore()}")
                return value

