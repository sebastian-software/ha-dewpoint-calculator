from __future__ import annotations

import math
from typing import Any, cast

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import CONF_HUMIDITY_ENTITY, CONF_TEMPERATURE_ENTITY, CONF_NAME


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the sensor platform."""
    temp_entity_config: Any = config.get(CONF_TEMPERATURE_ENTITY)
    humidity_entity_config: Any = config.get(CONF_HUMIDITY_ENTITY)
    name_config: Any = config.get(CONF_NAME, "Dewpoint")

    if not isinstance(temp_entity_config, str) or not isinstance(
        humidity_entity_config, str
    ):
        raise ValueError("Temperature and humidity entities must both be strings")

    if not isinstance(name_config, str):
        raise ValueError("Name must be a string")

    temp_entity = cast(str, temp_entity_config)
    humidity_entity = cast(str, humidity_entity_config)
    name = cast(str, name_config)

    async_add_entities(
        [DewpointCalculatorSensor(hass, temp_entity, humidity_entity, name)]
    )


class DewpointCalculatorSensor(SensorEntity):
    """Sensor that calculates dewpoint based on temperature and humidity."""

    def __init__(
        self, hass: HomeAssistant, temp_entity: str, humidity_entity: str, name: str
    ):
        """Initialize the sensor."""
        self.hass = hass
        self._temp_entity = temp_entity
        self._humidity_entity = humidity_entity
        self._attr_name = name
        self._attr_unique_id = f"dewpoint_{temp_entity}_{humidity_entity}"
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._state = None

    async def async_added_to_hass(self):
        """Register callbacks."""

        @callback
        def sensor_state_listener(event):
            """Handle state changes."""
            self.async_schedule_update_ha_state(True)

        async_track_state_change_event(
            self.hass,
            [self._temp_entity, self._humidity_entity],
            sensor_state_listener,
        )

        # Initial calculation
        self.async_schedule_update_ha_state(True)

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Calculate new state."""
        temp_state = self.hass.states.get(self._temp_entity)
        humidity_state = self.hass.states.get(self._humidity_entity)

        if temp_state is None or humidity_state is None:
            self._state = None
            return

        try:
            temperature = float(temp_state.state)
            relativeHumidity = float(humidity_state.state)

            K2 = 17.62
            K3 = 243.12

            # Magnus formula
            # https://de.wikipedia.org/wiki/Taupunkt#Abh%C3%A4ngigkeit_der_Taupunkttemperatur_von_relativer_Luftfeuchtigkeit_und_Lufttemperatur
            self._state = (
                K3
                * (
                    (K2 * temperature) / (K3 + temperature)
                    + math.log(relativeHumidity / 100)
                )
                / ((K2 * K3) / (K3 + temperature) - math.log(relativeHumidity / 100))
            )

        except (ValueError, TypeError, ZeroDivisionError):
            self._state = None
