# akvelon_test_task

The NumberFormatter class has a parse_int method that takes a string as 
input. assuming all characters in the string are between 0 and 9, returns an integer. If an argument other than a string integer is passed to the method input, a warning is returned.

```python
>>> obj = NumberFormatter()
>>> obj.parse_int('123')
123
```

```python
>>> obj.parse_int('-123')
-123
```
```python
>>> obj.parse_int('')
'The argument cannot be an empty string'
```
```python
>>> obj.parse_int('123o')
'Wrong symbol in string'
```