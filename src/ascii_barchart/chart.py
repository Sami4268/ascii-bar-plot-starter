from rich.console import Console
from rich.text import Text

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}


def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)


def render_bar_chart(values, width=40):
    console = Console()
    maximum = max((value for _label, value in values), default=0)

    console.print("Average value1 by type\n")

    for label, value in values:
        length = scale_bar(value, maximum, width)
        line = Text(f"{label} | ")
        line.append("█" * length, style=STYLES.get(label, "bold white"))
        line.append(" " * (width - length))
        line.append(f" {value:.2f}")
        console.print(line)