# Standard modules.
from pathlib import Path
from typing import Callable
from datetime import datetime
from logging import getLogger, setLoggerClass

# Third-party modules.
import typer
from colorama import Fore

# Custom modules.
from logger import CustomLogger


app = typer.Typer()
setLoggerClass(CustomLogger)
logger = getLogger(__name__)

COLORS = {
    'INFO': Fore.LIGHTGREEN_EX,
    'DEBUG': Fore.LIGHTMAGENTA_EX,
    'ERROR': Fore.LIGHTRED_EX,
    'STATUS': Fore.LIGHTCYAN_EX,
    'WARNING': Fore.LIGHTYELLOW_EX
}


def echo_log(level: str, msg: str):
    level = level.upper()
    color = COLORS.get(level, '')
    level_str = f'{color}{level:^8}{Fore.WHITE}'
    timestamp = datetime.now().strftime('%H:%M')
    formatted = f'[{level_str}] {timestamp} - {msg}'
    typer.echo(formatted)


def _register_commands(aliases: dict[str | tuple[str, ...], Callable]) -> None:
    """
    Registers commands in the Typer application with support for multiple aliases per function.

    Each key in `aliases` can either be:
        - a string (single alias), or
        - a tuple of strings (multiple aliases)

    Each value must be a callable (function) that is registered as a command in Typer.

    Example:
        ```
        _register_commands({
            ("clear", "clr"): {
                clear_logs,
                "Description of command here"
            },
            ...
        })
        ```

    Args:
        aliases (dict[str | tuple[str, ...], Callable]): Mapping of alias names to command functions.
    """
    if not isinstance(aliases, dict):
        logger.error(f'Invalid type for aliases. Expected dict[str | tuple[str, ...], Callable], got {type(aliases)}')
        return

    for keys, command_info in aliases.items():
        func = command_info.get('func')
        help_text = command_info.get('help', '')

        if not callable(func):
            logger.error(f'Invalid command handler for {keys}: expected callable, got {type(func)}')
            continue

        if isinstance(keys, str):
            keys = (keys,)  # Make it a tuple for consistency

        # We find all aliases that are shorter than the longest one.
        # This is because they should have hidden=True so they are not shown in --help.
        hidden_commands = [
            key for key in keys
            if len(key) < max([len(key) for key in keys])
        ]

        for name in keys:
            try:
                if name in hidden_commands:
                    app.command(name=name, hidden=True)(func)
                else:
                    app.command(name=name, help=help_text)(func)
            except Exception as e:
                logger.error(f'Error registering command "{name}": {e}')


def backup(task: str, format: str, save_path: str) -> None:
    pass

def sync() -> None:
    pass

def transfer(id: str, data_type: str) -> None:
    pass

def set_token(token: str) -> None:
    pass

def list_projects() -> None:
    pass

def list_tasks(id: str, data_type: str) -> None:
    pass


#* Instead of using the app.command() decorator we register all commands at the bottom.
#* This makes it possible to provide aliases for commands since otherwise you'd have to copy function definitions
#* and use app.command() multiple times. It's a mess.
_register_commands(
    {
        ('b', 'backup'): {
            'func': backup,
            'help': 'Creates a backup of of either a single task, project or everything and saves it in the given path with the specified format.'
        },
        ('s', 'sync'): {
            'func': sync,
            'help': 'Synchronizes your local version of your Todoist data with the cloud.'
        },
        ('t', 'trans', 'transfer'): {
            'func': transfer,
            'help': 'Transfers a single task or project to the specified destination.'
        },
        ('st', 'set-token'): {
            'func': set_token,
            'help': 'Sets the API token.'
        },
        ('lp', 'proj', 'projects'): {
            'func': list_projects,
            'help': 'Lists all available projects.'
        },
        ('lt', 'tasks'): {
            'func': list_tasks,
            'help': 'Lists either all tasks in a single project or across all projects.'
        }
    }
)
