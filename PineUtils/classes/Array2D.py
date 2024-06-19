import copy
import random

class Array2D(list):
    """
    Class representing a two-dimensional array extended from a list.

    Public methods:
    - __init__: Initializes the array.
    - get_element: Retrieves a specific element in the array.
    - set_element: Sets a value for a specific element in the array.
    - get_rows: Returns the number of rows in the array.
    - get_cols: Returns the number of columns in the array.
    - display: Prints the array in a readable format.
    - copy: Returns a deep copy of the array.
    - __eq__: Compares two arrays for equality.
    - transpose: Returns the transpose of the array.
    - __add__: Adds two arrays of the same size.
    - scalar_multiply: Multiplies the array by a scalar.
    - sum_row: Returns the sum of a specific row.
    - sum_col: Returns the sum of a specific column.
    - max_value: Returns the maximum value in the array.
    - min_value: Returns the minimum value in the array.
    - is_square: Checks if the array is square.
    - fill_random: Fills the array with random numbers within a given range.
    """

    def __init__(self, data=None, rows=None, cols=None, fill=None):
        """
        Initializes the array.

        Args:
        - data: List of lists representing the data of the array.
        - rows: Number of rows for an empty array.
        - cols: Number of columns for an empty array.
        - fill: Fill value for an empty array.

        Raises:
        - ValueError: If neither 'data' nor ('rows' and 'cols') are provided.
        """
        if data is not None:
            super().__init__(data)
            self.rows = len(data)
            self.cols = len(data[0])
        elif rows is not None and cols is not None:
            super().__init__([[fill] * cols for _ in range(rows)])
            self.rows = rows
            self.cols = cols
        else:
            raise ValueError("Must provide either 'data' or 'rows' and 'cols'")
    
    def get_element(self, row, col):
        """
        Retrieves a specific element in the array.

        Args:
        - row: Index of the row of the element.
        - col: Index of the column of the element.

        Returns:
        - Value of the element at position (row, col).
        """
        return self[row][col]

    def set_element(self, row, col, value):
        """
        Sets a value for a specific element in the array.

        Args:
        - row: Index of the row of the element.
        - col: Index of the column of the element.
        - value: Value to set at position (row, col).
        """
        self[row][col] = value

    def get_rows(self):
        """
        Returns the number of rows in the array.

        Returns:
        - Number of rows.
        """
        return self.rows

    def get_cols(self):
        """
        Returns the number of columns in the array.

        Returns:
        - Number of columns.
        """
        return self.cols
    
    def display(self):
        """
        Prints the array in a readable format.
        """
        for row in self:
            for item in row:
                print(item, "  ", end="")
            print()

    def copy(self):
        """
        Returns a deep copy of the array.

        Returns:
        - Deep copy of the array.
        """
        return copy.deepcopy(self)

    def transpose(self):
        """
        Returns the transpose of the array.

        Returns:
        - Transposed array.
        """
        transposed_array = Array2D(rows=self.cols, cols=self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_array[j][i] = self[i][j]
        return transposed_array

    def scalar_multiply(self, scalar):
        """
        Multiplies the array by a scalar.

        Args:
        - scalar: Scalar to multiply the array.

        Returns:
        - Resulting array after scalar multiplication.
        """
        result = Array2D(rows=self.rows, cols=self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result[i][j] = self[i][j] * scalar
        return result

    def sum_row(self, row):
        """
        Returns the sum of a specific row.

        Args:
        - row: Index of the row to sum.

        Returns:
        - Sum of the elements in the specified row.
        """
        return sum(self[row])

    def sum_col(self, col):
        """
        Returns the sum of a specific column.

        Args:
        - col: Index of the column to sum.

        Returns:
        - Sum of the elements in the specified column.
        """
        return sum(row[col] for row in self)

    def max_value(self):
        """
        Returns the maximum value in the array.

        Returns:
        - Maximum value in the array.
        """
        return max(max(row) for row in self)

    def min_value(self):
        """
        Returns the minimum value in the array.

        Returns:
        - Minimum value in the array.
        """
        return min(min(row) for row in self)
    
    def is_square(self):
        """
        Checks if the array is square.

        Returns:
        - True if the array is square, False otherwise.
        """
        return self.rows == self.cols

    def fill_random(self, low, high):
        """
        Fills the array with random numbers within a given range.

        Args:
        - low: Lower bound of the range for random numbers.
        - high: Upper bound of the range for random numbers.
        """
        for i in range(self.rows):
            for j in range(self.cols):
                self[i][j] = random.randint(low, high)
