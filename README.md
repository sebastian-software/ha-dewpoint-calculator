# Dewpoint Calculator für Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

A custom integration for Home Assistant that calculates the dew point based on temperature and humidity sensors.

## What is Dew Point?

The **dew point** is the temperature at which air becomes saturated with moisture and water vapor begins to condense into liquid water (dew). It's a key indicator of humidity and comfort levels in your home.

### Why is this useful?

- **Mold Prevention**: When surfaces in your home (walls, windows, etc.) fall below the dew point temperature, condensation forms, creating ideal conditions for mold growth. By monitoring the dew point, you can take preventive action.
- **Comfort Assessment**: Unlike relative humidity, dew point provides an absolute measure of moisture in the air. A dew point above 20°C (68°F) feels muggy, while below 10°C (50°F) feels dry and comfortable.
- **Climate Control Optimization**: Understanding dew point helps you optimize your heating, cooling, and dehumidification systems (HVAC) to maintain a healthy indoor environment.
- **Window Condensation**: Compare room dew point with window surface temperatures to predict and prevent condensation issues.

### How does it work?

This integration uses existing temperature and humidity sensors in your Home Assistant setup to automatically calculate and display the dew point as a new sensor entity. The calculation updates whenever your source sensors change, giving you real-time monitoring of moisture conditions.

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

Copyright 2025–2026<br/>[Sebastian Software GmbH](https://www.sebastian-software.de)
