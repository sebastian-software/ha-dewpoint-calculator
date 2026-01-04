# Dewpoint Calculator for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub Release](https://img.shields.io/github/v/release/sebastian-software/ha-dewpoint-calculator)](https://github.com/sebastian-software/ha-dewpoint-calculator/releases)
[![License](https://img.shields.io/github/license/sebastian-software/ha-dewpoint-calculator)](https://github.com/sebastian-software/ha-dewpoint-calculator/blob/main/LICENSE)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2023.1.0+-blue.svg)](https://www.home-assistant.io/)
[![GitHub issues](https://img.shields.io/github/issues/sebastian-software/ha-dewpoint-calculator)](https://github.com/sebastian-software/ha-dewpoint-calculator/issues)
[![Validate](https://github.com/sebastian-software/ha-dewpoint-calculator/actions/workflows/validate.yaml/badge.svg)](https://github.com/sebastian-software/ha-dewpoint-calculator/actions/workflows/validate.yaml)

A custom integration for Home Assistant that calculates the dewpoint based on temperature and humidity sensors.

## What is dewpoint?

The **dewpoint** is the temperature at which air becomes saturated with moisture and water vapor begins to condense into liquid water (dew). It's a key indicator of humidity and comfort levels in your home.

### Why is this useful?

- **Mold Prevention**: When surfaces in your home (walls, windows, etc.) fall below the dewpoint temperature, condensation forms, creating ideal conditions for mold growth. By monitoring the dewpoint, you can take preventive action.
- **Comfort Assessment**: Unlike relative humidity, dewpoint provides an absolute measure of moisture in the air. A dewpoint above 20°C (68°F) feels muggy, while below 10°C (50°F) feels dry and comfortable.
- **Climate Control Optimization**: Understanding dewpoint helps you optimize your heating, cooling, and dehumidification systems to maintain a healthy indoor environment.
- **Window Condensation**: Compare room dewpoint with window surface temperatures to predict and prevent condensation issues.

### How does it work?

This integration uses existing temperature and humidity sensors in your Home Assistant setup to automatically calculate and display the dewpoint as a new sensor entity. The calculation updates whenever your source sensors change, giving you real-time monitoring of moisture conditions.

## Installation via HACS

[HACS](https://hacs.xyz/) (Home Assistant Community Store) makes it easy to install custom integrations. If you don't have HACS yet, install it first from [hacs.xyz](https://hacs.xyz/).

1. Open **HACS** in Home Assistant
2. Go to **Integrations**
3. Click the **three dots** in the top right corner
4. Select **Custom repositories**
5. Add the repository URL: `https://github.com/sebastian-software/ha-dewpoint-calculator`
6. Select category: **Integration**
7. Click **Add**
8. Search for **Dewpoint Calculator** and click **Download**
9. **Restart Home Assistant** to complete installation

## Manual installation

If you prefer not to use HACS:

1. Download the latest release from the [releases page](https://github.com/sebastian-software/ha-dewpoint-calculator/releases)
2. Copy the `custom_components/dewpoint_calculator` folder to your `config/custom_components/` directory
3. **Restart Home Assistant** to complete installation

> **Note:** Your final path should be `config/custom_components/dewpoint_calculator/manifest.json`

## Creating a dewpoint sensor

After installation, you can create one or more dewpoint sensors. Each sensor requires an existing temperature sensor and humidity sensor as data sources.

1. In Home Assistant, navigate to **Settings** → **Devices & services**
2. Click the **Integrations** tab at the top
3. Click the **+ Add Integration** button in the bottom right corner
4. Search for and select **Dewpoint Calculator**
5. Enter a descriptive name for your sensor (e.g., "Living Room Dewpoint")
6. Select the **temperature sensor** you want to use as a source
7. Select the **humidity sensor** you want to use as a source
8. Click **Submit** to create the sensor

> **Tip:** You can repeat these steps to create multiple dewpoint sensors for different rooms or areas in your home.

## License

[Apache License; Version 2.0, January 2004](http://www.apache.org/licenses/LICENSE-2.0)

## Copyright

<img src="https://cdn.rawgit.com/sebastian-software/sebastian-software-brand/0d4ec9d6/sebastiansoftware-en.svg" alt="Logo of Sebastian Software GmbH, Mainz, Germany" width="460" height="160"/>

Copyright 2025–2026<br/>[Sebastian Software GmbH](https://www.sebastian-software.de)
