# vbpdf
Install using pip

```sh
pip install vbpdf
```

## Usage
```sh
vbpdf -h
```
```sh
Usage: vbpdf [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  overlay  Annotates any pdf file.
  split    Splits any pdf file.
  topng    Converts pdf pages into pngs

```

```sh
vbpdf split -h
```
```sh
Usage: vbpdf split [OPTIONS]

  Splits any pdf file.

Options:
  -i, --inputfile PATH            Input file  [default: ./main.pdf]
  -o, --outputfile PATH           Output file  [default: ./main_splited.pdf]
  -p, --pages <INTEGER INTEGER>...
                                  Pages range  [default: 0, 0]
  -h, --help                      Show this message and exit.
  
```
