# The Decorators excercise - difficult to understand to me for now


The *args and **kwargs syntax is great for decorators that are intended to work on functions with different signatures.
https://developer.mozilla.org/en-US/docs/Glossary/Signature/Function

The log_call_count function below doesn't care about the number or type of the decorated
function's (func_to_decorate) arguments. It just wants to count how many times the
function is called. However, it still needs to pass any arguments through to the wrapped function.

```
def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper
```

Complete the markdown_to_text_decorator function. It can decorate a function with any
number of string arguments, no matter if they're positional or keyword args.
It will run the decorated function, but first strip out any Markdown heading symbols
(see below for an explanation of Markdown headings).

It should return a wrapper function that takes *args and **kwargs. The wrapper should:

Map the *args to a new list where each string is converted to plain text using convert_md_to_txt.
Map the **kwargs to a new dictionary where each "value" is converted to plain text using
convert_md_to_txt. The "key" should remain the same.
Return the result of calling the decorated function with the new arguments.

Tips
Take a look at the editor's formatters.py file tab to see what the formatter functions do.
What arguments are they expecting? You can use * tuple unpacking and **
dictionary unpacking operators to pass variables as the correct arguments.

The map function with a new function passed in access the tuple values
Use the list() function to convert map results to a list
Use the dict() function to convert map results to a dictionary
The .items() method can be used on a dictionary to get an iterable of key-value tuple pairs
The provided convert_md_to_txt function takes a string of Markdown text and returns a string of text with any "heading" symbols removed. For example:
