"""Sensor calculations use only synthetic Home Assistant source states."""

from types import SimpleNamespace

import pytest
from homeassistant.core import HomeAssistant

from custom_components.dewpoint_calculator.sensor import DewpointCalculatorSensor


@pytest.mark.asyncio
@pytest.mark.parametrize("source", ["sensor.temperature", "sensor.humidity"])
@pytest.mark.parametrize("reading", ["NaN", "Infinity", "-Infinity"])
async def test_nonfinite_readings_are_rejected_and_recover(tmp_path, source, reading):
    hass = HomeAssistant(str(tmp_path))
    hass.states.async_set("sensor.temperature", "20")
    hass.states.async_set("sensor.humidity", "50")
    sensor = DewpointCalculatorSensor(
        hass,
        SimpleNamespace(entry_id="synthetic"),
        "sensor.temperature",
        "sensor.humidity",
        "Test dewpoint",
    )
    await sensor.async_update()
    expected = sensor.native_value
    assert expected == pytest.approx(9.255, abs=0.001)

    hass.states.async_set(source, reading)
    await sensor.async_update()
    assert sensor.native_value is None
    assert sensor.extra_state_attributes["error"] == "calculation_error"
    assert sensor.extra_state_attributes["error_details"]

    hass.states.async_set(source, "20" if source == "sensor.temperature" else "50")
    await sensor.async_update()
    assert sensor.native_value == pytest.approx(expected)
    assert "error" not in sensor.extra_state_attributes


@pytest.mark.asyncio
@pytest.mark.parametrize("humidity", ["0", "101", "-1", "unavailable", "not-a-number"])
async def test_invalid_humidity_keeps_existing_error_handling(tmp_path, humidity):
    hass = HomeAssistant(str(tmp_path))
    hass.states.async_set("sensor.temperature", "20")
    hass.states.async_set("sensor.humidity", humidity)
    sensor = DewpointCalculatorSensor(
        hass,
        SimpleNamespace(entry_id="synthetic"),
        "sensor.temperature",
        "sensor.humidity",
        "Test dewpoint",
    )
    await sensor.async_update()
    assert sensor.native_value is None
    assert "error" in sensor.extra_state_attributes
