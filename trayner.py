# (c) 2026 Ryanhtech Labs.
#
# This file is part of Trayner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import os
import sys


def get_default_pdf_directory_absolute_path() -> str:
    """
    Returns the absolute path to the default PDF save directory.
    The default directory is the 'pdf' directory located in this script's directory. Please be aware that this directory
    might not be writeable.
    :return: the absolute path to the default PDF save directory.
    """
    # Use the os module to determine the path to the script's directory, and add the default PDF save directory name
    # which is obviously 'pdf'
    script_directory_path = os.path.abspath(os.path.dirname(__file__))

    # Thank you very much Micro$oft
    if sys.platform == "win32":
        return script_directory_path + "\\pdf"
    return script_directory_path + "/pdf"

def init_pdf_directory(pdf_dir_path: str):
    """
    Initialises the PDF directory. If it doesn't exist, this function creates it.
    :raise IOError: If the directory isn't writeable or if it cannot be created.
    :raise FileExistsError: If the provided path is a file.
    :param pdf_dir_path: The absolute path to the PDF directory.
    """
    if os.path.isfile(pdf_dir_path):
        # The file is not a directory
        raise FileExistsError(f"The file '{pdf_dir_path}' is not a directory")
    elif os.path.isdir(pdf_dir_path):
        # Check if the directory is writeable (write and execute permissions)
        if not os.access(pdf_dir_path, os.W_OK | os.X_OK):
            raise IOError(f"The directory '{pdf_dir_path}' doesn't seem to be writeable")
        return

    # The directory doesn't exist; create it
    try:
        os.mkdir(pdf_dir_path)
    except:
        raise IOError(f"The directory '{pdf_dir_path}' couldn't be created.")

def init_parse_arguments() -> argparse.Namespace:
    """
    Parses the command-line arguments that were provided to the programme.
    :return: The parsed command-line arguments.
    """
    # Create an ArgumentParser object that we'll populate with the supported command-line arguments
    argument_parser = argparse.ArgumentParser(prog="trayner")
    argument_parser.add_argument("--pdf_directory", default=get_default_pdf_directory_absolute_path())

    # Return the parsed arguments
    return argument_parser.parse_args()

def main():
    """
    Main routine.
    :return: exit code
    """
    # Parse the command-line arguments
    arguments = init_parse_arguments()

    # Initialise the PDF directory
    init_pdf_directory(arguments.pdf_directory)

    return 0

if __name__ == "__main__":
    # Execute the main routine, and get its exit code
    exit_code = main()

    # Exit with the specified exit code
    sys.exit(exit_code)
