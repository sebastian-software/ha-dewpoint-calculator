"""Sensor platform for Dewpoint Calculator."""

from __future__ import annotations

import logging
import math

from homeassistant.components.sensor import SensorDeviceClass, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event

from .const import DOMAIN, CONF_TEMPERATURE_ENTITY, CONF_HUMIDITY_ENTITY

_LOGGER = logging.getLogger(__name__)

# Magnus formula constants
K2 = 17.62
K3 = 243.12


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Dewpoint Calculator sensor from a config entry."""
    name = entry.data.get("name", "Dewpoint")
    temp_entity = entry.data.get(CONF_TEMPERATURE_ENTITY)
    humidity_entity = entry.data.get(CONF_HUMIDITY_ENTITY)

    if not isinstance(temp_entity, str) or not isinstance(humidity_entity, str):
        _LOGGER.error(
            "Invalid entity ids for entry %s: temp=%s humidity=%s",
            entry.entry_id,
            temp_entity,
            humidity_entity,
        )
        return

    async_add_entities(
        [DewpointCalculatorSensor(hass, entry, temp_entity, humidity_entity, name)],
        True,
    )


class DewpointCalculatorSensor(SensorEntity):
    """Representation of a Dewpoint Calculator sensor."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
        temp_entity: str,
        humidity_entity: str,
        name: str,
    ) -> None:
        """Initialize the sensor."""
        self.hass = hass
        self._entry = entry
        self._temp_entity = temp_entity
        self._humidity_entity = humidity_entity

        # Sensor properties
        self._attr_name = name
        self._attr_unique_id = f"{DOMAIN}_{entry.entry_id}"
        self._attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
        self._attr_device_class = SensorDeviceClass.TEMPERATURE
        self._attr_suggested_display_precision = 1
        self._attr_icon = "mdi:water-thermometer"
        self._state: float | None = None

        # Additional attributes for debugging
        self._attr_extra_state_attributes = {}

    async def async_added_to_hass(self) -> None:
        """Register callbacks."""

        @callback
        def sensor_state_listener(event):
            """Handle state changes of source sensors."""
            self.async_schedule_update_ha_state(True)

        # Listen to changes of both sensors
        self.async_on_remove(
            async_track_state_change_event(
                self.hass,
                [self._temp_entity, self._humidity_entity],
                sensor_state_listener,
            )
        )

        # Initial calculation
        await self.async_update()

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self) -> None:
        """Calculate dewpoint."""
        temp_state = self.hass.states.get(self._temp_entity)
        humidity_state = self.hass.states.get(self._humidity_entity)

        if temp_state is None or humidity_state is None:
            self._state = None
            self._attr_extra_state_attributes = {"error": "Sensor not available"}
            return

        if temp_state.state in ("unknown", "unavailable") or humidity_state.state in ("unknown", "unavailable"):
            self._state = None
            self._attr_extra_state_attributes = {"error": "Source sensor unavailable"}
            return

        try:
            temp = float(temp_state.state)
            rh = float(humidity_state.state)

            # Magnus formula for dewpoint
            # dewpoint = (K3 * ((K2*temp)/(K3+temp) + ln(rh/100))) /
            #            ((K2*K3)/(K3+temp) - ln(rh/100))

            if rh <= 0 or rh > 100:
                raise ValueError(f"Invalid humidity: {rh}%")

            ln_rh = math.log(rh / 100)
            numerator = K3 * ((K2 * temp) / (K3 + temp) + ln_rh)
            denominator = (K2 * K3) / (K3 + temp) - ln_rh

            if denominator == 0:
                raise ZeroDivisionError("Division by zero in formula")

            self._state = numerator / denominator

            # Additional information
            self._attr_extra_state_attributes = {
                "temperature": temp,
                "humidity": rh,
                "temperature_entity": self._temp_entity,
                "humidity_entity": self._humidity_entity,
            }

        except (ValueError, TypeError, ZeroDivisionError) as err:
            _LOGGER.warning("Error calculating dewpoint for %s: %s", self._attr_name, err)
            self._state = None
            self._attr_extra_state_attributes = {"error": str(err)}
