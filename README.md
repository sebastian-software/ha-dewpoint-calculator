# Temperature Calculator für Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

A custom integration for Home Assistant that calculates the dew point based on temperature and humidity.

## Installation via HACS

1. Open HACS in Home Assistant
2. Go to “Integrations”
3. Click on the three dots in the top right corner
4. Select “Custom repositories”
5. Add the URL: `https://github.com/sebastian-software/ha-dewpoint-calculator`
6. Select category: “Integration”
7. Click on “Add”
8. Search for “Dewpoint Calculator” and install it
9. Restart Home Assistant

## Manual installation

1. Copy the `custom_components/dewpoint_calculator` folder to your `config/custom_components/` directory
2. Restart Home Assistant

## Parameters

- `temperature_entity`: Entity ID of your temperature sensor
- `humidity_entity`: Entity ID of your humidity sensor

## License

[Apache License; Version 2.0, January 2004](http://www.apache.org/licenses/LICENSE-2.0)

## Copyright

<img src="https://cdn.rawgit.com/sebastian-software/sebastian-software-brand/0d4ec9d6/sebastiansoftware-en.svg" alt="Logo of Sebastian Software GmbH, Mainz, Germany" width="460" height="160"/>

Copyright 2025<br/>[Sebastian Software GmbH](https://www.sebastian-software.de)
