import Chromify

class LogType:
    def __init__(self, name: str):
        """
        Initialize a LogType instance with a name.

        Args:
        - name (str): The name of the log type.
        """
        self.name = name

class Types:
    ERROR = LogType("ERROR")
    WARNING = LogType("WARNING")
    INFO = LogType("INFO")
    SUCCESS = LogType("SUCCESS")
    DEBUG = LogType("DEBUG")
    CUSTOM = LogType("CUSTOM")

class Theme:
    def __init__(self, themeType: str | LogType, symbol: str, lightColor: Chromify.Color, mediumColor: Chromify.Color, darkColor: Chromify.Color):
        """
        Initialize a Theme instance with theme type, symbol, and colors.

        Args:
        - themeType (str or LogType): The type of the theme (either as a string or LogType instance).
        - symbol (str): The symbol representing the theme.
        - lightColor (Chromify.Color): The light color associated with the theme.
        - mediumColor (Chromify.Color): The medium color associated with the theme.
        - darkColor (Chromify.Color): The dark color associated with the theme.
        """
        self.theme_name = themeType.name if isinstance(themeType, LogType) else themeType
        self.symbol = symbol
        self.lightColor = lightColor
        self.mediumColor = mediumColor
        self.darkColor = darkColor

class Themes:
    ERROR = Theme(Types.ERROR, "!", Chromify.Color("#ff5555"), Chromify.Color("#ff2020"), Chromify.Color("#cc0000"))
    WARNING = Theme(Types.WARNING, "*", Chromify.Color("#ff9911"), Chromify.Color("#ff8000"), Chromify.Color("#ff6600"))
    INFO = Theme(Types.INFO, ">", Chromify.Color("#5555ff"), Chromify.Color("#2020ff"), Chromify.Color("#0000cc"))
    SUCCESS = Theme(Types.SUCCESS, "$", Chromify.Color("#55ff55"), Chromify.Color("#35ff35"), Chromify.Color("#00cc00"))
    DEBUG = Theme(Types.DEBUG, "?", Chromify.Color("#aaaaaa"), Chromify.Color("#808080"), Chromify.Color("#444444"))

    @staticmethod
    def CUSTOM(symbol: str, lightColor: Chromify.Color, mediumColor: Chromify.Color, darkColor: Chromify.Color, logtype: LogType = Types.CUSTOM):
        """
        Create a custom Theme instance.

        Args:
        - symbol (str): The symbol representing the theme.
        - lightColor (Chromify.Color): The light color associated with the theme.
        - mediumColor (Chromify.Color): The medium color associated with the theme.
        - darkColor (Chromify.Color): The dark color associated with the theme.
        - logtype (LogType, optional): The log type associated with the theme (default is Types.CUSTOM).

        Returns:
        - Theme: The created Theme instance.
        """
        return Theme(logtype, symbol, lightColor, mediumColor, darkColor)

class Logger:
    @staticmethod
    def error(message: str, name: str ="ERROR", theme: Theme = Themes.ERROR, preindentations: int = 0, prespaces: int = 0):
        """
        Log an error message with a specific theme.

        Args:
        - message (str): The error message to log.
        - name (str, optional): The name associated with the log message (default is "ERROR").
        - theme (Theme, optional): The theme used for formatting (default is Themes.ERROR).
        - preindentations (int, optional): Number of preceding tab characters (default is 0).
        - prespaces (int, optional): Number of preceding space characters (default is 0).
        """
        print("\t"*preindentations + " "*prespaces + f"{theme.darkColor.fore()}[{theme.mediumColor.fore()}{theme.symbol}{theme.darkColor.fore()}] {theme.mediumColor.fore()}{name}: {theme.lightColor.fore()}{message}{Chromify.Style.RESET_ALL}")

    @staticmethod
    def warn(message: str, name: str ="WARNING", theme: Theme = Themes.WARNING, preindentations: int = 0, prespaces: int = 0):
        """
        Log a warning message with a specific theme.

        Args:
        - message (str): The warning message to log.
        - name (str, optional): The name associated with the log message (default is "WARNING").
        - theme (Theme, optional): The theme used for formatting (default is Themes.WARNING).
        - preindentations (int, optional): Number of preceding tab characters (default is 0).
        - prespaces (int, optional): Number of preceding space characters (default is 0).
        """
        print("\t"*preindentations + " "*prespaces + f"{theme.darkColor.fore()}[{theme.mediumColor.fore()}{theme.symbol}{theme.darkColor.fore()}] {theme.mediumColor.fore()}{name}: {theme.lightColor.fore()}{message}{Chromify.Style.RESET_ALL}")

    @staticmethod
    def info(message: str, name: str ="INFO", theme: Theme = Themes.INFO, preindentations: int = 0, prespaces: int = 0):
        """
        Log an info message with a specific theme.

        Args:
        - message (str): The info message to log.
        - name (str, optional): The name associated with the log message (default is "INFO").
        - theme (Theme, optional): The theme used for formatting (default is Themes.INFO).
        - preindentations (int, optional): Number of preceding tab characters (default is 0).
        - prespaces (int, optional): Number of preceding space characters (default is 0).
        """
        print("\t"*preindentations + " "*prespaces + f"{theme.darkColor.fore()}[{theme.mediumColor.fore()}{theme.symbol}{theme.darkColor.fore()}] {theme.mediumColor.fore()}{name}: {theme.lightColor.fore()}{message}{Chromify.Style.RESET_ALL}")

    @staticmethod
    def success(message: str, name: str ="SUCCESS", theme: Theme = Themes.SUCCESS, preindentations: int = 0, prespaces: int = 0):
        """
        Log a success message with a specific theme.

        Args:
        - message (str): The success message to log.
        - name (str, optional): The name associated with the log message (default is "SUCCESS").
        - theme (Theme, optional): The theme used for formatting (default is Themes.SUCCESS).
        - preindentations (int, optional): Number of preceding tab characters (default is 0).
        - prespaces (int, optional): Number of preceding space characters (default is 0).
        """
        print("\t"*preindentations + " "*prespaces + f"{theme.darkColor.fore()}[{theme.mediumColor.fore()}{theme.symbol}{theme.darkColor.fore()}] {theme.mediumColor.fore()}{name}: {theme.lightColor.fore()}{message}{Chromify.Style.RESET_ALL}")

    @staticmethod
    def debug(message: str, name: str ="DEBUG", theme: Theme = Themes.DEBUG, preindentations: int = 0, prespaces: int = 0):
        """
        Log a debug message with a specific theme.

        Args:
        - message (str): The debug message to log.
        - name (str, optional): The name associated with the log message (default is "DEBUG").
        - theme (Theme, optional): The theme used for formatting (default is Themes.DEBUG).
        - preindentations (int, optional): Number of preceding tab characters (default is 0).
        - prespaces (int, optional): Number of preceding space characters (default is 0).
        """
        print("\t"*preindentations + " "*prespaces + f"{theme.darkColor.fore()}[{theme.mediumColor.fore()}{theme.symbol}{theme.darkColor.fore()}] {theme.mediumColor.fore()}{name}: {theme.lightColor.fore()}{message}{Chromify.Style.RESET_ALL}")

    @staticmethod
    def log(message: str, theme: Theme, name: str = None, preindentations: int = 0, prespaces: int = 0):
        """
        Log a message with a specific theme.

        Args:
        - message (str): The message to log.
        - theme (Theme): The theme used for formatting.
        - name (str, optional): The name associated with the log message (default is None).
        - preindentations (int, optional): Number of preceding tab characters (default is 0).
        - prespaces (int, optional): Number of preceding space characters (default is 0).
        """
        print("\t"*preindentations + " "*prespaces + f"{theme.darkColor.fore()}[{theme.mediumColor.fore()}{theme.symbol}{theme.darkColor.fore()}] {theme.mediumColor.fore()}{name if name != None else theme.theme_name}: {theme.lightColor.fore()}{message}{Chromify.Style.RESET_ALL}")

    @staticmethod
    def whiteLine(amount: int = 1):
        """
        Print a specified number of newline characters.

        Args:
        - amount (int, optional): Number of newline characters to print (default is 1).
        """
        print("\n"*amount, end="")
