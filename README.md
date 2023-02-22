# texual-timer-driven-demo
This repository holds a basic [Textual](https://textual.textualize.io/) application
that demonstrates how a timer can be used to asynchronously update UI elements. 

## Getting started
It is recommended to create a new python enviroment either via venv or conda
before getting started. This command set should help do that:

```
$ conda create -n textual-demo "python=>3.10"
$ conda activate textual-demo
```

Following this, install all requirements as follows:

```
(textual-demo) $ pip install -r requirements.txt
```

To launch the app run:
```
$ textual run display.py
```

Alternatively to develop with ease do:
```
$ textual run --dev display.py
```
and in a seperate terminal run:
```
$ textual console
```
to get a debug log. 
