Regex (short for regular expression) is a pattern used to search, match, and manipulate text.

For example

Suppose you have this text:
```
Alice has 3 cats and 12 dogs.
```

| Regex    | Matches               | Meaning                       |
| -------- | --------------------- | ----------------------------- |
| `cat`    | `cat`                 | Finds the exact word "cat"    |
| `\d`     | `3`, `1`, `2`         | Any single digit              |
| `\d+`    | `3`, `12`             | One or more digits            |
| `[A-Z]`  | `A`                   | Any uppercase letter          |
| `[a-z]+` | `lice`, `has`, `cats` | One or more lowercase letters |
