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

## Configuration

Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: dewpoint_calculator
    temperature_entity: sensor.your_temperature
    humidity_entity: sensor.your_humidity
```

## Parameter

- `temperature_entity`: Entity-ID deines Temperatursensors
- `humidity_entity`: Entity-ID deines Feuchtigkeitssensors

## License

Copyright (C) 2025 Sebastian Software GmbH, Germany

MIT License
