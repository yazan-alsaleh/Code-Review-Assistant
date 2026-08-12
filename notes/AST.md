# Abstract Syntax Tree (AST)

A built-in tool that allows Python to understand the structure of Python code.


Example
```
x = 10
```

`ast` can turn that into a structured tree representing:

```
Assignment
├── x
└── 10
```

So:
```
ast.parse(code)
```
means: "Take this Python source code and build an AST from it."
