## Path Class

Represents a path object with utility methods for handling paths.

### Attributes

- **path** (str): The path string.

### Methods

- **__init__(path: str = None)**:
  Initializes the Path object.

- **filename() -> str**:
  Returns the filename from the path.

- **extension() -> str**:
  Returns the file extension from the path.

- **fullname() -> str**:
  Returns the full name (filename) from the path.

- **name() -> str**:
  Returns the name of the last directory in the path.

- **mother() -> Path**:
  Returns the parent directory of the path.

- **disk() -> str**:
  Returns the disk drive of the path.

- **__str__() -> str**:
  Returns the string representation of the Path object.

- **__repr__() -> str**:
  Returns the official string representation of the Path object.
```

### File Class

Represents a file object with methods for file operations.

### Attributes

- **path** (Path): The Path object representing the file path.

### Methods

- **__init__(path: Union[Path, str] = None)**:
  Initializes the File object.

- **filename() -> str**:
  Returns the filename from the file path.

- **extension() -> str**:
  Returns the file extension from the file path.

- **fullname() -> str**:
  Returns the full name (filename) from the file path.

- **mother() -> Union[Directory, None]**:
  Returns the parent directory of the current file.

- **disk() -> str**:
  Returns the disk drive of the current file.

- **read_in_chunks(chunksize: int = 8192) -> Generator[bytes, None, None]**:
  Generator to read the file in chunks.

- **loaddata(chunksize: int = 8192) -> List[bytes]**:
  Loads the entire file into memory.

- **write(content: bytes, chunk: int, position: int)**:
  Writes content to a specific position in the file.

- **save()**:
  Saves the file with the current content.

- **rename(new_name: str)**:
  Sets a new name for the file.

- **compare(other: 'File') -> Union[bool, None]**:
  Compares the current file with another file.

- **open(path: Union[Path, str], chunksize: int = 8192) -> 'File'**:
  Static method to open a File object from a path.
```

### Directory Class

```markdown
## Directory Class

Represents a directory object with methods for directory operations.

### Attributes

- **path** (Path): The Path object representing the directory path.
- **data** (List[Union[File, Directory]]): List of files and subdirectories in the directory.

### Methods

- **__init__(path: Union[Path, str] = None)**:
  Initializes the Directory object.

- **name() -> str**:
  Returns the name of the directory.

- **mother() -> Union[Directory, None]**:
  Returns the parent directory of the current directory.

- **disk() -> str**:
  Returns the disk drive of the current directory.

- **__getitem__(item)**:
  Retrieves an item from the data list.

- **__setitem__(key, value)**:
  Sets an item in the data list.

- **__repr__() -> str**:
  Returns the official string representation of the Directory object.

- **open() -> List[Union[File, Directory]]**:
  Opens the directory and populates the data list with files and subdirectories.

- **iterate() -> Generator[Union[File, Directory], None, None]**:
  Iterates through all files and directories within the current directory.

- **rename(new_name: str)**:
  Sets a new name for the directory.

- **save()**:
  Applies any pending name change to the directory.

- **compare(other: 'Directory') -> bool**:
  Compares the current directory with another directory.

- **find(pattern: str) -> Generator[Union['File', 'Directory'], None, None]**:
  Finds files and directories matching a pattern within the directory.

- **get_metadata() -> dict**:
  Retrieves metadata for the directory.
```

### FileDialog Class

```markdown
## FileDialog Class

Provides static methods for opening file dialogs based on the operating system.

### Methods

- **open(file_types=None)**:
  Opens a file dialog to select a file based on the operating system.

  - `file_types` (Optional[List[Tuple[str, str]]]): List of file types with names and patterns.
  - Returns: Union[Path, None]: Path object representing the selected file path or None if selection fails.

- **openDirectory()**:
  Opens a directory selection dialog based on the operating system.

  - Returns: Union[Path, None]: Path object representing the selected directory path or None if selection fails.
```

### ZipUtil Class

```markdown
## ZipUtil Class

Provides static methods for compressing and decompressing files and directories.

### Methods

- **compress(files_to_compress: List[Union[File, Directory]], zip_file_path: str) -> str**:
  Compresses a list of File and Directory objects into a ZIP file.

  - `files_to_compress` (List[Union[File, Directory]]): List of File and Directory objects to compress.
  - `zip_file_path` (str): Path to the output ZIP file.
  - Returns: str: Path to the compressed ZIP file or None if compression fails.

- **decompress(zip_file: Union[File, str], extract_to: Union[Directory, str]) -> Optional[str]**:
  Decompresses a ZIP file into a specified directory.

  - `zip_file` (Union[File, str]): Path to the ZIP file or File object representing the ZIP file.
  - `extract_to` (Union[Directory, str]): Path to the directory or Directory object to extract the ZIP file contents.
  - Returns: Optional[str]: Path to the directory where files were extracted or None if extraction fails.
