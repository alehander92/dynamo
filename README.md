# dynamo

Translates your mypy annotated python3 sources to un-annotated, compatible with earler python.

```bash
dynamo a.py b.py
```

* Removes arg: t
* Removes -> t
* Removes from typing import t
* Removes import typing
