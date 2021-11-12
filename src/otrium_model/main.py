import click
import uvicorn
from otrium_model.logger.root_logger import log_config


@click.group()
@click.version_option()
def cli() -> None:
    """Command line interface for the sales prediction model."""


@cli.command()
@click.option("--host", default="127.0.0.1")
@click.option("--port", default=8000)
@click.option("--debug/--no-debug", default=False)
def serve(host: str, port: int, debug: bool) -> None:
    """
    Serves a fitted model in FastAPI
    """
    uvicorn.run(app="otrium_model.app:app", host=host, port=port, debug=debug, reload=False, log_config=log_config)


if __name__ == "__main__":
    cli()
