# Logger Documentation

## LogType Class

The `LogType` class represents a type of log with a name.

### Constructor:

```python
class LogType:
    def __init__(self, name: str):
        """
        Initialize a LogType instance with a name.

        Args:
        - name (str): The name of the log type.
        """
        self.name = name

#: Or just import it
from PineUtils.Logger import LogType
```

---

## Types Class

The `Types` class defines constants for different log types using instances of `LogType`.

### Attributes:

- `ERROR`: Represents an error log.
- `WARNING`: Represents a warning log.
- `INFO`: Represents an informational log.
- `SUCCESS`: Represents a success log.
- `DEBUG`: Represents a debug log.
- `CUSTOM`: Represents a custom log type.

---

## Theme Class

The `Theme` class represents a log theme with a type, symbol, and colors.

### Constructor:

```python
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

#: You can import it using:
from PineUtils.Logger import Theme
```

---

## Themes Class

The `Themes` class provides predefined themes for different log types using the `Theme` class.

### Attributes:

- `ERROR`: Predefined theme for error logs.
- `WARNING`: Predefined theme for warning logs.
- `INFO`: Predefined theme for informational logs.
- `SUCCESS`: Predefined theme for success logs.
- `DEBUG`: Predefined theme for debug logs.

### Static Method:

- `CUSTOM(symbol, lightColor, mediumColor, darkColor, logtype=Types.CUSTOM)`: Create a custom theme instance.

---

## Logger Class

The `Logger` class provides methods to log messages with specified themes and formats.

### Static Methods:

- `error(message, name="ERROR", theme=Themes.ERROR, preindentations=0, prespaces=0)`: Log an error message.
- `warn(message, name="WARNING", theme=Themes.WARNING, preindentations=0, prespaces=0)`: Log a warning message.
- `info(message, name="INFO", theme=Themes.INFO, preindentations=0, prespaces=0)`: Log an informational message.
- `success(message, name="SUCCESS", theme=Themes.SUCCESS, preindentations=0, prespaces=0)`: Log a success message.
- `debug(message, name="DEBUG", theme=Themes.DEBUG, preindentations=0, prespaces=0)`: Log a debug message.
- `log(message, theme, name=None, preindentations=0, prespaces=0)`: Log a message with a specified theme.
- `whiteLine(amount=1)`: Print a specified number of newline characters.

### Usage:

```python
# Example usage
Logger.error("This is an error message.")
Logger.warn("This is a warning message.")
Logger.info("This is an informational message.")
Logger.success("This is a success message.")
Logger.debug("This is a debug message.")
```
