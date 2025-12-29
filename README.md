# Templite — A Minimal Python Template Engine

This project is an educational implementation of a **minimal template engine in Python**, inspired by the book ***500 Lines or Less*** by **A. Jesse Jiryu Davis and Guido van Rossum**.

The goal is to demonstrate how a simple templating language can be **parsed, compiled into Python code, and executed dynamically**, providing a deep understanding of how template engines like Jinja or Django Templates work internally.

## ✨ Features

* Variable interpolation: `{{ variable }}`
* Filters using pipe syntax: `{{ name|upper }}`
* Control flow:

  * `if` / `endif`
  * `for` / `endfor`
* Comments: `{# this is ignored #}`
* Dot access for attributes and dictionary keys
* Runtime compilation into a Python function
* Clear separation between **compile-time** and **render-time**

## 📖 Inspiration

This implementation is based on the **Templite** example from the book:

> ***500 Lines or Less***
> *Experience how real systems are built, one small program at a time.*

The book focuses on building real software systems from scratch in a compact and educational way. This project closely follows that philosophy.

## 🧠 How It Works (High-Level)

1. **Parsing**

   * The template text is split into tokens using regular expressions.
   * Tokens are classified as:

     * Literal text
     * Expressions (`{{ ... }}`)
     * Control tags (`{% ... %}`)
     * Comments (`{# ... #}`)

2. **Compilation**

   * The template is compiled into a **Python function** using the `CodeBuilder` helper.
   * Indentation is managed explicitly to generate valid Python code.
   * Expressions are translated into Python expressions that access a unified context.

3. **Execution**

   * The generated Python function is executed using `exec`.
   * Rendering is done by calling the compiled function with a context dictionary.

## 🧩 Code Structure

### `CodeBuilder`

A helper class responsible for:

* Managing indentation levels
* Building Python source code incrementally
* Executing generated code safely
* Ensuring all blocks are properly closed

### `Templite`

The core template engine:

* Parses template syntax
* Tracks variables and loop variables
* Generates Python code for expressions and control flow
* Renders the final output using a merged context

### `TempliteSyntaxError`

A custom exception raised when the template syntax is invalid.

## ▶️ Example Usage

```python
from Templite import Templite

templite = Templite(
    '''
    <h1>Hello {{name|upper}}!</h1>
    {% for topic in topics %}
        <p>You are interested in {{topic}}.</p>
    {% endfor %}
    ''',
    {'upper': str.upper},
)

text = templite.render({
    'name': "Mirian",
    'topics': ['Python', 'Java', 'Watercolor', 'Amigurumi'],
})

print(text)
```

### Output

```html
<h1>Hello MIRIAN!</h1>
<p>You are interested in Python.</p>
<p>You are interested in Java.</p>
<p>You are interested in Watercolor.</p>
<p>You are interested in Amigurumi.</p>
```

## 🚧 Limitations

* Limited expression support (`if` only supports a single variable)
* No escaping or security protections
* No template inheritance
* No sandboxing

These limitations are deliberate and aligned with the educational goals.

## 📚 References

* ***500 Lines or Less*** — A. Jesse Jiryu Davis, Guido van Rossum
* Python documentation: `exec`, `re`, and dynamic code execution
* Jinja and Django Templates (for comparison)
