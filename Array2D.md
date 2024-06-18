```markdown
# Array2D Documentation

## Array2D Class

The `Array2D` class represents a two-dimensional array extended from a list.

### Constructor:

```python
class Array2D(list):
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
```

### Public Methods:

- `get_element(row, col)`: Retrieves a specific element in the array.
- `set_element(row, col, value)`: Sets a value for a specific element in the array.
- `get_rows()`: Returns the number of rows in the array.
- `get_cols()`: Returns the number of columns in the array.
- `display()`: Prints the array in a readable format.
- `copy()`: Returns a deep copy of the array.
- `transpose()`: Returns the transpose of the array.
- `scalar_multiply(scalar)`: Multiplies the array by a scalar.
- `sum_row(row)`: Returns the sum of a specific row.
- `sum_col(col)`: Returns the sum of a specific column.
- `max_value()`: Returns the maximum value in the array.
- `min_value()`: Returns the minimum value in the array.
- `is_square()`: Checks if the array is square.
- `fill_random(low, high)`: Fills the array with random numbers within a given range.

### Usage Examples:

```python
# Example usage
array = Array2D(rows=3, cols=3, fill=0)
array.display()

array.set_element(0, 0, 1)
print(array.get_element(0, 0))

transposed = array.transpose()
transposed.display()

array_filled = Array2D(rows=2, cols=2)
array_filled.fill_random(1, 10)
print(array_filled)

array_copy = array.copy()
print(array == array_copy)

sum_row = array.sum_row(0)
sum_col = array.sum_col(0)

max_value = array.max_value()
min_value = array.min_value()

is_square = array.is_square()
```