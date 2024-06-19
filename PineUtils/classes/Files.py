from typing import Union, Generator, List, Optional
import platform
import subprocess
import zipfile
import os
import re
import struct

class Path:
    """
    Represents a path object with utility methods for handling paths.

    Attributes:
    - path (str): The path string.

    Methods:
    - __init__: Initializes the Path object.
    - filename: Returns the filename from the path.
    - extension: Returns the file extension from the path.
    - fullname: Returns the full name (filename) from the path.
    - name: Returns the name of the last directory in the path.
    - mother: Returns the parent directory of the path.
    - disk: Returns the disk drive of the path.
    - __str__: Returns the string representation of the Path object.
    - __repr__: Returns the official string representation of the Path object.
    """

    def __init__(self, path: str = None):
        """
        Initializes the Path object.

        Args:
        - path (str): The path string.
        """
        self.path: str = None
        if isinstance(path, Path):
            self.path = path.path
        else:
            self.path = path

    @property
    def filename(self) -> str:
        """
        Returns the filename from the path.

        Returns:
        - str: Filename from the path.
        """
        return os.path.basename(self.path)

    @property
    def extension(self) -> str:
        """
        Returns the file extension from the path.

        Returns:
        - str: File extension from the path.
        """
        return os.path.splitext(self.path)[1]

    @property
    def fullname(self) -> str:
        """
        Returns the full name (filename) from the path.

        Returns:
        - str: Full name (filename) from the path.
        """
        return os.path.basename(self.path)

    @property
    def name(self) -> str:
        """
        Returns the name of the last directory in the path.

        Returns:
        - str: Name of the last directory.
        """
        return os.path.basename(os.path.dirname(self.path))

    @property
    def mother(self) -> 'Path':
        """
        Returns the parent directory of the path.

        Returns:
        - Path: Parent directory.
        """
        return Path(os.path.dirname(self.path))

    @property
    def disk(self) -> str:
        """
        Returns the disk drive of the path.

        Returns:
        - str: Disk drive.
        """
        return os.path.splitdrive(self.path)[0]

    def __str__(self):
        """
        Returns the string representation of the Path object.

        Returns:
        - str: String representation of the Path object.
        """
        return str(self.path)

    def __repr__(self):
        """
        Returns the official string representation of the Path object.

        Returns:
        - str: Official string representation of the Path object.
        """
        return f"Path({str(self.path)!r})"


class File:
    """
    Represents a file object with methods for file operations.

    Attributes:
    - path (Path): The Path object representing the file path.

    Methods:
    - __init__: Initializes the File object.
    - filename: Returns the filename from the file path.
    - extension: Returns the file extension from the file path.
    - fullname: Returns the full name (filename) from the file path.
    - read_in_chunks: Generator to read the file in chunks.
    - loaddata: Loads the entire file into memory.
    - write: Writes content to a specific position in the file.
    - save: Saves the file with the current content.
    - open: Static method to open a File object from a path.
    - mother: Returns the parent directory of the current file.
    - disk: Returns the disk drive of the current file.
    - rename: Sets a new name for the file.
    - compare: Compares the current file with another file.
    """


    def __init__(self, path: Union[Path, str] = None):
        """
        Initializes the File object.

        Args:
        - path (Union[Path, str]): Path object or string representing the file path.
        """
        self.path = path if isinstance(path, Path) else Path(path)
        self.new_name = None

    @property
    def filename(self) -> str:
        """
        Returns the filename from the file path.

        Returns:
        - str: Filename from the file path.
        """
        return os.path.basename(self.path.path)

    @property
    def extension(self) -> str:
        """
        Returns the file extension from the file path.

        Returns:
        - str: File extension from the file path.
        """
        return os.path.splitext(self.path.path)[1]

    @property
    def fullname(self) -> str:
        """
        Returns the full name (filename) from the file path.

        Returns:
        - str: Full name (filename) from the file path.
        """
        return os.path.basename(self.path.path)
    
    @property
    def mother(self) -> Union['Directory', None]:
        """
        Returns the parent directory of the current file.

        Returns:
        - Union[Directory, None]: Parent Directory object or None if at the root.
        """
        parent_path = self.path.path.parent
        return Directory(parent_path) if parent_path else None

    @property
    def disk(self) -> str:
        """
        Returns the disk drive of the current file.

        Returns:
        - str: Disk drive of the current file.
        """
        return self.path.path.drive

    def read_in_chunks(self, chunksize: int = 8192) -> Generator[bytes, None, None]:
        """
        Generator to read the file in chunks.

        Args:
        - chunksize (int): Size of each chunk to read.

        Yields:
        - bytes: Chunk of data read from the file.
        """
        if self.path is not None and self.path.path is not None:
            with open(self.path.path, 'rb') as f:
                while chunk := f.read(chunksize):
                    yield chunk

    def loaddata(self, chunksize: int = 8192) -> List[bytes]:
        """
        Loads the entire file into memory.

        Args:
        - chunksize (int): Size of each chunk to read.

        Returns:
        - List[bytes]: List of bytes read from the file.
        """
        self.bytes = []
        for chunk in self.read_in_chunks(chunksize):
            self.bytes.append(chunk)
        return self.bytes
    
    def write(self, content: bytes, chunk: int, position: int):
        """
        Writes content to a specific position in the file.

        Args:
        - content (bytes): Content to write to the file.
        - chunk (int): Index of the chunk to write to.
        - position (int): Position within the chunk to write the content.
        """
        if self.bytes:
            self.bytes[chunk][position] = content

    def save(self):
        """
        Saves the file with the current content and applies any pending name change.

        If a new name has been set, renames the file.
        """

        if self.path is not None and self.path.path is not None and self.bytes:
            if self.new_name:
                new_path = os.path.join(self.path.mother.path, self.new_name)
                os.rename(self.path.path, new_path)
                self.path = Path(new_path)
                self.new_name = None
            with open(self.path.path, 'wb') as f:
                for chunk in self.bytes:
                    f.write(chunk)
    
    def rename(self, new_name: str):
        """
        Sets a new name for the file.

        Args:
        - new_name (str): The new name for the file.
        """
        self.new_name = new_name

    @staticmethod
    def open(path: Union[Path, str], chunksize: int = 8192) -> 'File':
        """
        Static method to open a File object from a path.

        Args:
        - path (Union[Path, str]): Path object or string representing the file path.
        - chunksize (int): Size of each chunk to read.

        Returns:
        - File: File object initialized with the content from the file.
        """
        file = File(path=path)
        file.loaddata(chunksize)
        return file
    
    def compare(self, other: 'File') -> Union[bool, None]:
        """
        Compares the current file with another file.

        Args:
        - other (File): The other file to compare with.

        Returns:
        - bool: True if the files are identical, False otherwise.
        """
        if self.path.path == other.path.path:
            return True

        try:
            if len(self.bytes) == len(other.bytes) and len(self.bytes) == 0:
                return None
            if len(self.bytes) > 0 and len(other.bytes) > 0:
                if len(self.bytes) != len(other.bytes):
                    return False
                for chunk1, chunk2 in zip(self.bytes, other.bytes):
                    if chunk1 != chunk2:
                        return False
                return True
        except IOError as e:
            print(f"Error comparing files: {e}")
            return False


class Directory:
    """
    Represents a directory object with methods for directory operations.

    Attributes:
    - path (Path): The Path object representing the directory path.
    - data (List[Union[File, Directory]]): List of files and subdirectories in the directory.

    Methods:
    - __init__: Initializes the Directory object.
    - __getitem__: Retrieves an item from the data list.
    - __setitem__: Sets an item in the data list.
    - __repr__: Returns the official string representation of the Directory object.
    - open: Opens the directory and populates the data list with files and subdirectories.
    - name: Returns the name of the directory.
    - mother: Returns the parent directory of the current directory.
    - disk: Returns the disk drive of the current directory.
    - iterate: Iterates through all files and directories within the current directory.
    - rename: Sets a new name for the file.
    - compare: Compares the current directory with another directory.
    - find: Finds files and directories matching a pattern within the directory.
    - get_metadata: Retrieves metadata for the directory.
    - extract_exif: Extracts basic EXIF data from a JPEG file.
    """


    @property
    def name(self) -> str:
        """
        Returns the name of the directory.

        Returns:
        - str: Name of the directory.
        """
        return os.path.basename(self.path.path)

    @property
    def mother(self) -> Union['Directory', None]:
        """
        Returns the parent directory of the current directory.

        Returns:
        - Union[Directory, None]: Parent Directory object or None if at the root.
        """
        parent_path = self.path.path.parent
        return Directory(parent_path) if parent_path else None

    @property
    def disk(self) -> str:
        """
        Returns the disk drive of the current directory.

        Returns:
        - str: Disk drive of the current directory.
        """
        return self.path.path.drive

    def __init__(self, path: Union[Path, str] = None):
        """
        Initializes the Directory object.

        Args:
        - path (Union[Path, str]): Path object or string representing the directory path.
        """
        self.path = path if isinstance(path, Path) else Path(path)
        self.data = []
        self.new_name = None

    def __getitem__(self, item):
        """
        Retrieves an item from the data list.

        Args:
        - item: Index or key to retrieve from the data list.

        Returns:
        - Union[File, Directory]: File or Directory object from the data list.
        """
        return self.data[item]

    def __setitem__(self, key, value):
        """
        Sets an item in the data list.

        Args:
        - key: Index or key to set in the data list.
        - value: Value to set in the data list (File or Directory object).
        """
        self.data[key] = value

    def __repr__(self):
        """
        Returns the official string representation of the Directory object.

        Returns:
        - str: Official string representation of the Directory object.
        """
        return f"Directory({self.data})"

    def open(self):
        """
        Opens the directory and populates the data list with files and subdirectories.

        Returns:
        - List[Union[File, Directory]]: List of File and Directory objects in the directory.
        """
        self.data = []
        for root, dirs, files in os.walk(self.path.path):
            for file in files:
                file_path = os.path.join(root, file)
                self.data.append(File(Path(file_path)))
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                self.data.append(Directory(Path(dir_path)))
        return self.data
    
    def iterate(self) -> Generator[Union[File, 'Directory'], None, None]:
        """
        Iterates through all files and directories within the current directory.

        Yields:
        - Union[File, Directory]: Yields File and Directory objects found in the current directory and its subdirectories.
        """
        for root, dirs, files in os.walk(self.path.path):
            for file in files:
                file_path = os.path.join(root, file)
                yield File(Path(file_path))
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                yield Directory(Path(dir_path))
    
    def rename(self, new_name: str):
        """
        Sets a new name for the directory.

        Args:
        - new_name (str): The new name for the directory.
        """
        self.new_name = new_name

    def save(self):
        """
        Applies any pending name change to the directory.

        If a new name has been set, renames the directory.
        """
        if self.new_name:
            new_path = os.path.join(self.path.mother.path, self.new_name)
            os.rename(self.path.path, new_path)
            self.path = Path(new_path)
            self.new_name = None
    
    def compare(self, other: 'Directory') -> bool:
        """
        Compares the current directory with another directory.

        Args:
        - other (Directory): The other directory to compare with.

        Returns:
        - bool: True if the directories are identical, False otherwise.
        """
        return self._compare_directories(self.path.path, other.path.path)

    def _compare_directories(self, dir1: str, dir2: str) -> bool:
        """
        Helper method to recursively compare directories.

        Args:
        - dir1 (str): The path of the first directory.
        - dir2 (str): The path of the second directory.

        Returns:
        - bool: True if the directories are identical, False otherwise.
        """
        for item in os.listdir(dir1):
            item1 = os.path.join(dir1, item)
            item2 = os.path.join(dir2, item)

            if os.path.isdir(item1):
                if not os.path.isdir(item2):
                    return False
                if not self._compare_directories(item1, item2):
                    return False
            else:
                if not os.path.isfile(item2):
                    return False
                if not self._compare_files(item1, item2):
                    return False

        for item in os.listdir(dir2):
            if item not in os.listdir(dir1):
                return False

        return True

    def _compare_files(self, file1: str, file2: str) -> Union[bool, None]:
        """
        Helper method to compare two files.

        Args:
        - file1 (str): The path of the first file.
        - file2 (str): The path of the second file.

        Returns:
        - bool: True if the files are identical, False otherwise.
        """
        f1 = File(Path(file1))
        f2 = File(Path(file2))
        f1.loaddata()
        f2.loaddata()
        return f1.compare(f2)
    
    def find(self, pattern: str) -> Generator[Union['File', 'Directory'], None, None]:
        """
        Finds files and directories matching a pattern within the directory.

        Args:
        - pattern (str): Pattern to search for (supports wildcards * and ?).

        Yields:
        - Union[File, Directory]: Generates File and Directory objects matching the pattern.
        """
        pattern = pattern.replace('*', '.*').replace('?', '.') + '$'
        regex = re.compile(pattern)
        
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if regex.match(file):
                    yield File(os.path.join(root, file))
            for dir in dirs:
                if regex.match(dir):
                    yield Directory(os.path.join(root, dir))

    def get_metadata(self) -> dict:
        """
        Retrieves metadata for the directory.

        Returns:
        - dict: Dictionary containing metadata information.
        """
        metadata = {}

        # Basic directory properties
        metadata['name'] = self.name
        metadata['path'] = str(self.path)
        metadata['total_items'] = len(self.data)

        # Extract EXIF data from JPEG files if present
        jpeg_files = [file for file in self.data if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg')]
        exif_data = {}
        for file in jpeg_files:
            try:
                file_path = os.path.join(self.path, file)
                exif = self.extract_exif(file_path)
                exif_data[file] = exif
            except Exception as e:
                exif_data[file] = {'Error': str(e)}

        metadata['exif_data'] = exif_data

        return metadata

    @staticmethod
    def extract_exif(filename):
        """
        Extracts basic EXIF data from a JPEG file.

        WARNING ONLY WORKS WITH JPEG files, really unhandled.

        Args:
        - filename (str): Path to the JPEG file.

        Returns:
        - dict: Dictionary containing extracted EXIF tags and values.
        """
        exif_data = {}

        with open(filename, 'rb') as f:
            data = f.read()

            # Check for JPEG SOI marker
            if data[0:2] != b'\xFF\xD8':
                raise ValueError("Not a valid JPEG file")

            # Find APP1 marker
            app1_marker_pos = data.find(b'\xFF\xE1')

            if app1_marker_pos == -1:
                raise ValueError("No EXIF data found")

            # Read APP1 length
            app1_length = struct.unpack('>H', data[app1_marker_pos + 2:app1_marker_pos + 4])[0]

            # Read EXIF identifier 'Exif\0\0'
            exif_identifier = data[app1_marker_pos + 4:app1_marker_pos + 10]
            if exif_identifier != b'Exif\x00\x00':
                raise ValueError("No EXIF data found")

            # Read TIFF header
            tiff_header = data[app1_marker_pos + 10:app1_marker_pos + 14]
            if tiff_header != b'II*\x00' and tiff_header != b'MM\x00*':
                raise ValueError("Invalid TIFF header")

            # Read TIFF data offset
            tiff_offset = struct.unpack_from('>I', data, app1_marker_pos + 14)[0]

            # Read number of entries in IFD0 (usually 12)
            num_entries = struct.unpack_from('>H', data, tiff_offset)[0]

            # Read each entry
            offset = tiff_offset + 2

            for _ in range(num_entries):
                tag = struct.unpack_from('>H', data, offset)[0]
                field_type = struct.unpack_from('>H', data, offset + 2)[0]
                num_values = struct.unpack_from('>I', data, offset + 4)[0]

                if field_type == 2 or field_type == 7:  # ASCII or UNDEFINED
                    value_offset = struct.unpack_from('>I', data, offset + 8)[0]
                    value = data[offset + 8:offset + 8 + num_values].decode('utf-8')
                else:
                    value = struct.unpack_from('>{0}L'.format(num_values), data, offset + 8)

                exif_data[tag] = value

                offset += 12

        return exif_data
    
class FileDialog:
    """
    Provides static methods for opening file dialogs based on the operating system.

    Methods:
    - open: Opens a file dialog to select a file based on the operating system.
    - _open_file_dialog_windows: Opens a file dialog on Windows using PowerShell.
    - _open_file_dialog_mac: Opens a file dialog on macOS using AppleScript.
    - _open_file_dialog_linux: Opens a file dialog on Linux using Zenity.
    - openDirectory: Opens a directory selection dialog based on the operating system.
    - _select_directory_windows: Opens a directory selection dialog on Windows using PowerShell.
    - _select_directory_mac: Opens a directory selection dialog on macOS using AppleScript.
    - _select_directory_linux: Opens a directory selection dialog on Linux using Zenity.
    """

    @staticmethod
    def open(file_types=None):
        """
        Opens a file dialog to select a file based on the operating system.

        Args:
        - file_types (Optional[List[Tuple[str, str]]]): List of file types with names and patterns.

        Returns:
        - Union[Path, None]: Path object representing the selected file path or None if selection fails.
        """
        system_os = platform.system()

        if system_os == "Windows":
            return FileDialog._open_file_dialog_windows(file_types)
        elif system_os == "Darwin":
            return FileDialog._open_file_dialog_mac(file_types)
        elif system_os == "Linux":
            return FileDialog._open_file_dialog_linux(file_types)
        else:
            print(f"Unsupported operating system: {system_os}")
            return None

    @staticmethod
    def _open_file_dialog_windows(file_types=None):
        """
        Opens a file dialog on Windows using PowerShell.

        Args:
        - file_types (Optional[List[Tuple[str, str]]]): List of file types with names and patterns.

        Returns:
        - Union[Path, None]: Path object representing the selected file path or None if selection fails.
        """
        try:
            # Build file filter
            filters = []
            if file_types:
                for name, pattern in file_types:
                    filters.append(f"{name} ({pattern.replace(',', ';')})|{pattern.replace(',', ';')}")

                filter_str = "|".join(filters)
            else:
                filter_str = "All files (*.*)|*.*"

            # Execute a PowerShell script to open the dialog
            command = [
                "powershell", "-Command",
                f"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; " +
                f"$fileDialog = New-Object System.Windows.Forms.OpenFileDialog; " +
                f"$fileDialog.Filter = '{filter_str}'; " +
                f"$fileDialog.FilterIndex = 1; " +  # Set the initial filter index
                f"if ($fileDialog.ShowDialog() -eq 'OK') {{ $fileDialog.FileName }}"
            ]
            file_path = subprocess.check_output(command, universal_newlines=True).strip()
            if file_path:
                return Path(file_path)
            else:
                return None
        except Exception as e:
            print(f"Error opening file dialog on Windows: {e}")
            return None

    @staticmethod
    def _open_file_dialog_mac(file_types=None):
        """
        Opens a file dialog on macOS using AppleScript.

        Args:
        - file_types (Optional[List[Tuple[str, str]]]): List of file types with names and patterns.

        Returns:
        - Union[Path, None]: Path object representing the selected file path or None if selection fails.
        """
        try:
            # Use AppleScript to open the dialog
            filter_str = ""
            if file_types:
                filter_str = "{" + ", ".join([f"\"{ext.strip()}\"" for _, pattern in file_types for ext in pattern.split(',')]) + "}"

            apple_script = f'''
                set file_path to POSIX path of (choose file of type {filter_str} with prompt "Select a file")
                return file_path
            '''
            command = ["osascript", "-e", apple_script]
            file_path = subprocess.check_output(command, universal_newlines=True).strip()
            if file_path:
                return Path(file_path)
            else:
                return None
        except Exception as e:
            print(f"Error opening file dialog on macOS: {e}")
            return None

    @staticmethod
    def _open_file_dialog_linux(file_types=None):
        """
        Opens a file dialog on Linux using Zenity.

        Args:
        - file_types (Optional[List[Tuple[str, str]]]): List of file types with names and patterns.

        Returns:
        - Union[Path, None]: Path object representing the selected file path or None if selection fails.
        """
        try:
            # Use Zenity to open the dialog
            filter_str = ""
            if file_types:
                filter_str = " --file-filter=".join([f"\"{name} | {pattern.replace(',', ' ')}\"" for name, pattern in file_types])

            command = ["zenity", "--file-selection", "--file-filter=" + filter_str]
            file_path = subprocess.check_output(command, universal_newlines=True).strip()
            if file_path:
                return Path(file_path)
            else:
                return None
        except Exception as e:
            print(f"Error opening file dialog on Linux: {e}")
            return None

    @staticmethod
    def openDirectory():
        """
        Opens a directory selection dialog based on the operating system.

        Returns:
        - Union[Path, None]: Path object representing the selected directory path or None if selection fails.
        """
        system_os = platform.system()

        if system_os == "Windows":
            return FileDialog._select_directory_windows()
        elif system_os == "Darwin":
            return FileDialog._select_directory_mac()
        elif system_os == "Linux":
            return FileDialog._select_directory_linux()
        else:
            print(f"Unsupported operating system: {system_os}")
            return None

    @staticmethod
    def _select_directory_windows():
        """
        Opens a directory selection dialog on Windows using PowerShell.

        Returns:
        - Union[Path, None]: Path object representing the selected directory path or None if selection fails.
        """
        try:
            command = [
                "powershell", "-Command",
                "[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms') | Out-Null; " +
                "$folderDialog = New-Object System.Windows.Forms.FolderBrowserDialog; " +
                "if ($folderDialog.ShowDialog() -eq 'OK') { $folderDialog.SelectedPath }"
            ]
            folder_path = subprocess.check_output(command, universal_newlines=True).strip()
            if folder_path:
                return Path(folder_path)
            else:
                return None
        except Exception as e:
            print(f"Error selecting directory on Windows: {e}")
            return None

    @staticmethod
    def _select_directory_mac():
        """
        Opens a directory selection dialog on macOS using AppleScript.

        Returns:
        - Union[Path, None]: Path object representing the selected directory path or None if selection fails.
        """
        try:
            apple_script = '''
                set folder_path to POSIX path of (choose folder with prompt "Select a folder")
                return folder_path
            '''
            command = ["osascript", "-e", apple_script]
            folder_path = subprocess.check_output(command, universal_newlines=True).strip()
            if folder_path:
                return Path(folder_path)
            else:
                return None
        except Exception as e:
            print(f"Error selecting directory on macOS: {e}")
            return None

    @staticmethod
    def _select_directory_linux():
        """
        Opens a directory selection dialog on Linux using Zenity.

        Returns:
        - Union[Path, None]: Path object representing the selected directory path or None if selection fails.
        """
        try:
            command = ["zenity", "--file-selection", "--directory"]
            folder_path = subprocess.check_output(command, universal_newlines=True).strip()
            if folder_path:
                return Path(folder_path)
            else:
                return None
        except Exception as e:
            print(f"Error selecting directory on Linux: {e}")
            return None
        

class ZipUtil:
    """
    Provides static methods for compressing and decompressing files and directories.

    Methods:
    - compress: Compresses a list of File and Directory objects into a ZIP file.
    - decompress: Decompresses a ZIP file into a specified directory.

    """

    @staticmethod
    def compress(files_to_compress: List[Union[File, Directory]], zip_file_path: str) -> str:
        """
        Compresses a list of File and Directory objects into a ZIP file.

        Args:
        - files_to_compress (List[Union[File, Directory]]): List of File and Directory objects to compress.
        - zip_file_path (str): Path to the output ZIP file.

        Returns:
        - str: Path to the compressed ZIP file or None if compression fails.
        """
        try:
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for item in files_to_compress:
                    if isinstance(item, File) and os.path.isfile(item.path.path):
                        zipf.write(item.path.path, arcname=os.path.basename(item.path.path))
                    elif isinstance(item, Directory) and os.path.isdir(item.path.path):
                        for root, dirs, files in os.walk(item.path.path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                zipf.write(file_path, arcname=os.path.relpath(file_path, os.path.dirname(item.path.path)))
            return zip_file_path
        except Exception as e:
            print(f"Error compressing files to ZIP: {e}")
            return None

    @staticmethod
    def decompress(zip_file: Union[File, str], extract_to: Union[Directory, str]) -> Optional[str]:
        """
        Decompresses a ZIP file into a specified directory.

        Args:
        - zip_file (Union[File, str]): Path to the ZIP file or File object representing the ZIP file.
        - extract_to (Union[Directory, str]): Path to the directory or Directory object to extract the ZIP file contents.

        Returns:
        - Optional[str]: Path to the directory where files were extracted or None if extraction fails.
        """
        try:
            zip_file_path = zip_file.path.path if isinstance(zip_file, File) else zip_file
            extract_to_path = extract_to.path.path if isinstance(extract_to, Directory) else extract_to

            with zipfile.ZipFile(zip_file_path, 'r') as zipf:
                zipf.extractall(extract_to_path)
            return extract_to_path
        except Exception as e:
            print(f"Error decompressing ZIP file: {e}")
            return None