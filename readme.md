# testapp — CPTD Shortcut Test Command

This command is created for testing the behavior of desktop shortcuts generated via the `installapp` utility in the CPTD CLI system.

## Purpose

To verify that:

- Shortcuts created by `installapp` execute correctly
- Terminal opens and runs the command
- Icons and paths are correctly applied
- Add Icon

## Usage

To run the command:

    cptd testapp

Expected result:

    [✓] The program has been successfully installed as an aplication!.

## Installation

Add this command to CPTD CLI using:

    cptd command --add testapp.zip

Then use `installapp`:

    cptd installapp --add testapp

after installapp run icon testapp

Expected result:
[✓] The program has been successfully installed as an aplication!.

## Removal

    cptd installapp --delete testapp
    cptd command --del testapp

## Requirements

- CPTD CLI installed
- Supported OS: All

