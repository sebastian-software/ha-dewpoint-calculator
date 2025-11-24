# Temperature Calculator

Calculates the dew point based upon one temperature sensor and one humidity sensor.

## Installation

1. Install this integration via HACS
2. Restart Home Assistant
3. Add configuration to `configuration.yaml`

## Configuration

```yaml
sensor:
  - platform: dewpoint_calculator
    temperature_entity: sensor.your_temperature
    humidity_entity: sensor.your_humidity
```

## Support

If you encounter any problems, please create an issue on GitHub.
