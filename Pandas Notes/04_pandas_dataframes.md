## What is a DataFrame?

A Pandas DataFrame is a **2-dimensional data structure**, like a 2-dimensional array, or a table with rows and columns.

### Example

Create a simple Pandas DataFrame:

```python
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Load data into a DataFrame object
df = pd.DataFrame(data)

print(df)
```

### Result

```text
   calories  duration
0       420        50
1       380        40
2       390        45
```

---

## Locate Row

As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas uses the `loc` attribute to return one or more specified rows.

### Example

Return row `0`:

```python
# Refer to the row index
print(df.loc[0])
```

### Result

```text
calories    420
duration     50
Name: 0, dtype: int64
```

**Note:** This example returns a Pandas **Series**.

### Example

Return rows `0` and `1`:

```python
# Use a list of indexes
print(df.loc[[0, 1]])
```

### Result

```text
   calories  duration
0       420        50
1       380        40
```

**Note:** When using `[]`, the result is a Pandas **DataFrame**.