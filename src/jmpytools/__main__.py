"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """jmpytools."""


if __name__ == "__main__":
    main(prog_name="jmpytools")  # pragma: no cover
