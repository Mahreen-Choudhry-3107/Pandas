## Installation of Pandas

If you have Python and PIP already installed on a system, then installation of Pandas is very easy.

Install it using this command:

```bash
C:\Users\Your Name>pip install pandas
```

If this command fails, then use a Python distribution that already has Pandas installed like, Anaconda, Spyder etc.

---

## Import Pandas

Once Pandas is installed, import it in your applications by adding the `import` keyword:

```python
import pandas
```

Now Pandas is imported and ready to use.

### Example

```python
import pandas

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)
```