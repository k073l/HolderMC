# HolderMC
Program that lets you farm mobs in Minecraft by using your crossbow, while you can do other things on your computer.

## Features
- GUI
- Adjustable delays through `options.yml`
- Does not require focus on Minecraft window
- Autosaves your delay config

## Usage
`python main.py`

Input delay between shots or leave blank to use `options.yml` settings. Click run to start and ALT+TAB from Minecraft window (may require F3+P to disable pause on lost focus).
To stop simply click stop.

## Dependencies
- PySimpleGUIQt (`pip install PySimpleGUIQt`)
- PyYAML (`pip install PyYAML`)
- ahk (See [here](https://pypi.org/project/ahk/))

