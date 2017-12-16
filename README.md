# dynamo

Compiles your python3 source to compatible with python2.7 source.

Mostly useful for removing mypy annotation and for using f'' literals in earlier python

Notice: it doesn't deal with str/bytecode and most other changes. It's a good helper for some usecases, if somebody
is interested in others, feel free to open issue/fork.

```bash
dynamo a.py a_27.py
```

* Removes var: t
* Removes arg: t
* Removes -> t
* Removes from typing import t
* Removes from mypy_extensions import t
* Replaces TypedDict with class t: pass
* Removes import typing
* Replaces f'' strings with valid python2 syntax

## install

```bash
pip install dynamo-py
```

## why

In some cases we **need** python scripts compatible with python2 systems. dynamo is mostly geared for little scripts and libs.

## but

yep, please, if possible: upgrade to Python3. (but sometimes there are additional requirements)
