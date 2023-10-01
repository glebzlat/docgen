---
title: Getting started
subject: Tutorial
subtitle: DocGen basics
short_title: Getting started with DocGen
author: Gleb Zlatanov
copyright: 2023 (c) Gleb Zlatanov
keywords: test, markdown, myst
---

```{admonition} Non standard Markdown
:class: warning

This is a MyST Markdown extension.
```

## Introduction

This is an example of how to generate C++ documentation with [Sphinx](https://www.sphinx-doc.org/en/master/)
using [Doxygen](https://www.doxygen.nl/) with [Breathe](https://breathe.readthedocs.io/),
[MyST](https://myst-parser.readthedocs.io) for [CommonMark](https://commonmark.org)
support and [bytefield-svg](https://bytefield-svg.deepsymmetry.org) for
bytefield diagrams.

This example is heavily inspired by
[this article](https://medium.com/practical-coding/c-documentation-with-doxygen-cmake-sphinx-breathe-for-those-of-use-who-are-totally-lost-part-2-21f4fb1abd9f).

See [Get started with MyST and Sphinx](https://myst-parser.readthedocs.io/en/v0.17.1/sphinx/intro.html),
[MyST syntax](https://myst-parser.readthedocs.io/en/v0.17.1/syntax/syntax.html)
and [MyST directives](https://myst-parser.readthedocs.io/en/v0.17.1/syntax/syntax.html#syntax-directives).
Also see [Jupiter book syntax cheatsheet](https://jupyterbook.org/en/stable/reference/cheatsheet.html).

This is a sample article, which main purpose is to demonstrate MyST CommonMark
capabilities. I will place CommonMark code after all samples. Maybe I write
an extension for Sphinx to create spoilers using html `<details>` tag to hide
things like this sample code. You also can open source of this page to see,
how it is written.

### Inserting figures

I can easily create figures with images:

```{figure} https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png
:name: linux-mascot-tux
:alt: Tux Linux mascot
:align: center

Tux
```

    ```{figure} https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png
    :name: linux-mascot-tux
    :alt: Tux Linux mascot
    :align: center

    Tux
    ```

### Creating admonitions:

```{admonition} MyST syntax peculiarities
Default directive syntax is using backticks '`' fence. But I've seen in a
couple sources that people using a colon ':' fence. It didn't work for me, and I
was wondering, how they do it. Then I've found that MyST has its own extensions,
(extension for an extension, you know) that allows to write directives using
colon fence.

    :::{directive}
    text
    :::

This is the default syntax:

    ```{directive}
    text
    \```

You see the backslash in the code example above, because my default Neovim
Markdown highlight engine does not display this correctly.

```

In the sample above I've used `admonition` directive.

:::{note}

Directives with colon fence allow to nest directives and code blocks, written
with backtick fence, without indenting them with 4 spaces. Though in the sample
above I've used `admonition` directive and placed code example that contains
backticks with the help of 4-space indentation.

```sh
echo "Backtick fenced code blocks work inside the colon blocks without indentation"
```
:::

### Reference to figures

I can reference to figures. See the figure Tux in the example 1.

[Tux](linux-mascot-tux) is a Linux mascot.

Using link syntax: `[Tux](linux-mascot-tux)`.

### Generating diagrams with bytefield-svg

I finally added `bytefield-svg` to this example. Now I can create beautiful
bytefield diagrams by writting them in Clojure. `bytefield-svg` is a utility,
written in Clojure, that "translates" Clojure code into an SVG format.

```{figure} bytefields/packet.svg
:name: packet
:alt: packet
:align: center
```

I've inserted the figure above using the `figure` directive already denoted in
previous examples. See `doc/bytefield/packet.clj` for the source code of this
picture.

```{raw} html
:file: bytefields/packet.svg
```


## Requirements

```{note}
Currently I'm running Alpine Linux, so here I will mention Alpine Package Keeper
(APK) package manager. Some packages may have another names in other repos, so
check the name of the package for your distro.
```

### Various admonitions

It is easy to create various types of admonitions. In the example above I
used `note` directive.

```{warning}
And this is the `warning` admonition.
```

```{attention}
`attention` admonition
```

```{caution}
`caution` admonition
```

```{danger}
`danger` admonition
```

```{error}
`error` admonition
```

```{hint}
`hint` admonition
```

```{important}
`important` admonition
```

### Actual requirements

Here I suppose that you already have installed Python3 and py3-pip. Also you
should have some C++ compiler in your system.

For Python packages see the `requirements.txt` file.

```sh
apk add doxygen cmake py3-sphinx
pip3 install --user -r requirements.txt
```

## Features

Do not forget that it is a _documentaton for C++ code_, and let me say a few
about the C++ code example.

### Link code documentation

This is the main class of a library: {cpp:class}`hello::hello_world`. This class
has ability to generate and print greetings (such functionality). Is has two
methods: {cpp:func}`hello::hello_world::get_greeting` and
{cpp:func}`hello::hello_world::print_greeting`.

Also the library has pretty template function, that allows you to inspect types.
{cpp:func}`template <typename T> void hello::inspect_type()`

In two paragraphs above I link documentation placed on another page using
`{cpp:func}` Sphinx role.

```{note}
{cpp:func}`template <typename T> void hello::inspect_type()` uses C++
`__PRETTY_FUNCTION__` extension and won't work for MSVC.
```

```{tip}
Use Linux instead of Windows as it is a great system without bloatware with
divine powers.
```

Note the another admonition type - `tip`.

MyST uses [Pygments](https://pygments.org/) for syntax highlighting, so
you don't need to link external JavaScript like Highlight.js. So cool!

```cpp
#include <iostream>

int main() {
  std::cout << "Hello World!" << std::endl;
  return 0;
}
```

Insert code examples is straightforward:

    ```cpp
    code
    ```

### Glossary

Well, Sphinx offers `{glossary}` directive, but it looks pretty poor. I
don't know, why - maybe theme I've used does not style it properly.

```{glossary}
LOL
: Laugh out loud
```

    ```{glossary}
    LOL
    : Laugh out loud
    ```

For adding custom extensions to Sphinx see
[Hello World extension](https://www.sphinx-doc.org/en/master/development/tutorials/helloworld.html),
[Creating RST Directives](https://docutils.sourceforge.io/docs/howto/rst-directives.html),
[Writing Sphinx Extensions](https://www.sphinx-doc.org/en/master/development/index.html),
[Writing a simple extension](https://sphinx-rtd-trial.readthedocs.io/en/latest/ext/tutorial.html).

## Custom extension

Yeah, I've already wrote a bunch of extensions for Sphinx. I _love_ to code
~~(and I have no many friends also and I have nothing to do)~~. Well, CommonMark
has no strikethrough text, so you see tildes in the previous sentence.

This is a simple `{helloworld}` directive that creates html `<p>Hello World</>`
code and does nothing except.

```{helloworld}
```

    ```{helloworld}
    ```

### includefile

The following directive, `{includefile}`, inserts code from a file. Pretty
useful functionality. Initially I wanted to use Doxygen to embed code, because
it reads source files and can do it. But it does it badly, so I've decided to do
it my way.

```{includefile} ../examples/print_greeting.cpp
:lang: cpp
:begin: 7
```

This is the code:

    ```{includefile} ../examples/print_greeting.cpp
    :lang: cpp
    :begin: 7
    ```

Here I used `begin` parameter, that specifies the line, from which the code will
be inserted. I can get only part of a file by specifying `:begin:` and `:end:`:

```{includefile} ../examples/print_greeting.cpp
:lang: cpp
:begin: 11
:end: 12
```

    ```{includefile} ../examples/print_greeting.cpp
    :lang: cpp
    :begin: 11
    :end: 12
    ```

It is not so comfortable to count lines, so I added tag functionality. You need
to place single line comments with opening and closing tag:

```
// <<opening-tag>>
... code ...
// <</closing-tag>>
```

And the code between tags will be inserted into a documentation. Doxygen has
similar functionality, but i did it cooler >:)

See the file `examples/type_inspect.cpp`.

These two code blocks illustrate `tag` usage. Here is the block with
`simple-example` tag:

    ```{includefile} ../examples/type_inspect.cpp
    :lang: cpp
    :tag: simple-example
    ```

Output:

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: simple-example
```

And with `complicated-example` tag:

    ```{includefile} ../examples/type_inspect.cpp
    :lang: cpp
    :tag: complicated-example
    ```

Output:

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: complicated-example
```

This extension also handles nested tags. If the tag-like line appears inside
code, it will be removed. In the following example I will insert code
inside `sample-1` tag, which has nested `type-pack-sample` tag. For this example
I took part of my [type-pack code](https://glebzlat.github.io/type_pack) code.

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: sample-1
```

How it is inserted:

    ```{includefile} ../examples/type_inspect.cpp
    :lang: cpp
    :tag: sample-1
    ```

Pay attention that the code that you see on the page has not tag-like lines.
They're removed.

Nested tag inside the `sample-1`.

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: type-pack-sample
```

I can use `begin` and `end` parameters inside tags. In this case, I count lines
from the opening tag. In the following example I use `end`.

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: type-pack-impl
:end: 12
```

How it is inserted:

    ```{includefile} ../examples/type_inspect.cpp
    :lang: cpp
    :tag: type-pack-impl
    :end: 12
    ```

And here I use `begin`:

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: type-pack-impl
:begin: 13
```

How it is inserted:

    ```{includefile} ../examples/type_inspect.cpp
    :lang: cpp
    :tag: type-pack-impl
    :begin: 13
    ```

Well, I found that Sphinx offers directives for including code from files:
`include` and `literalinclude`. But I am unstoppable, so I continue to use my
own directive. I've added a possibility to emphasize lines. So I can create
fancy explanations of my code:

"If the unspecified `at_helper` is called, it will try to evaluate 
`Error_Type_Pack_Out_Of_Range::type`. As this struct has no definition, the
compilation error will occur."

```{includefile} ../examples/type_inspect.cpp
:lang: cpp
:tag: type-pack-impl
:begin: 13
:emphasize: 3-6
```

Pay attention that emphasize line count starts from the `begin` line.

### Theme extending

Also pay attention that all code samples has the Copy button on the top-right.
So professional. And do not forget to use "scroll to top" button (it appears
on the bottom-right side of a page, when you far enough from the top.

In Sphinx you can easily extend themes and "inject" your custom functionality.
See [Sphinx theming](https://www.sphinx-doc.org/en/master/development/theming.html).
