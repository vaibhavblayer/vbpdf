
import click
import os
import sys
import PyPDF2
import time
from rich.console import Console
from .functions_pdf import pages_pdf
from .functions_pdf import extract_png_pdf
from .blur import blur
from .stack import stack
from .topng import topng
from .addbg import addbg

bg_path = "/Users/vaibhavblayer/10xphysics/backgrounds/bg_instagram.jpg"


@click.command(
        help="Converts pdf pages into pngs"
        )
@click.option(
        '-i',
        '--inputfile',
        type=click.Path(),
        default="./main.pdf",
        show_default=True,
        help="Input file name"
        )
@click.option(
        '-o',
        '--opacity',
        type=click.FLOAT,
        default=0.35,
        show_default=True,
        help="Opacity of blur layer"
        )
@click.option(
        '-d',
        '--dpi',
        default=320,
        type=click.INT,
        show_default=True,
        help="DPI -> density per inch for png"
        )
@click.option(
        '-b',
        '--background',
        type=click.Path(),
        default=bg_path,
        show_default=True,
        help="Path of the background image"
        )
@click.option(
        '-r',
        '--ranges',
        nargs=2,
        default=([1, 1]),
        type=click.Tuple([int, int]),
        show_default=True,
        help="Page range to be converted into png"
        )
@click.option(
        '-R',
        '--radius',
        default=2,
        show_default=True,
        help="Radius of gaussian-blur"
        )
@click.pass_context
def instagram(ctx, inputfile, opacity, dpi, background, ranges, radius):
    ctx.invoke(topng, inputfile=inputfile, ranges=ranges, transparent=True, dpi=dpi)

    for i in range(ranges[0], ranges[1]+1):
        ctx.invoke(blur, inputimage=f'main-{i}.png', outputimage=f'main-{i}b.png', opacity=opacity, radius=radius)

    for i in range(ranges[0], ranges[1]+1):
        ctx.invoke(stack, image=f'main-{i}.png', background=f'main-{i}b.png', outputfile=f'main-{i}bs.png', position=(-2, -2))

    if not os.path.exists('./downloads'):
        os.mkdir('./downloads')

    for i in range(ranges[0], ranges[1]+1):
        ctx.invoke(addbg, image=f'main-{i}bs.png', background=background, outputfile=f'./downloads/main-{i}f.png')