The author of an elementary school algebra text book has approached you to write a program to solve simple arithmetic equations. The author wants to use a program to avoid human errors in preparing the solutions manual. The text book author will provide a string containing the arithmetic problem.

For example:

```text
12 - 4 * 3
```

You are asked to create a function that will output the result. For the above input line, the corresponding output would be:

```text
0.00
```

The simple problems are limited to integer values with multiplication, division, addition and subtraction operations (though the result may be a decimal). As in the above example, the computation must follow the standard order of precedence for arithmetic operations. All multiplications and divisions are performed, from left to right, before any additions and subtractions, and then all additions and subtractions are performed from left to right.

The signature of your function should be, depending on the language:

```python
def solve(text_equation: str) -> str
```

You may implement other functions called by your `solve` function if you wish.

## Input Spec

The input data is a string containing the equation. Spaces are used to delimit the integers and the operators.

## Output Spec

The return value should be the result, formatted as a string with two decimal places.

**NOTE**: If the input contains an error or results in a division by zero, your function is expected to return "ERROR".

## Sample Input & Output

| Sample number | Input (str)               | Output (str) |
| ------------- | ------------------------- | ------------ |
| 1             | `"3 * 2 - 4 * 2 / 3 - 0"` | `"3.33"`     |
| 2             | `"4"`                     | `"4.00"`     |
| 3             | `"1 + 1"`                 | `"2.00"`     |
| 4             | `"2 * 2 * 2 * 2 * 2"`     | `"32.00"`    |
| 5             | `"2 \* 2 / 0 - 2"`        | `"ERROR"`    |
