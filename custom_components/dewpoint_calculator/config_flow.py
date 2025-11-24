"""Config flow for Dewpoint Calculator integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import selector
from homeassistant.helpers.translation import async_get_translations

from .const import DOMAIN, CONF_TEMPERATURE_ENTITY, CONF_HUMIDITY_ENTITY

_LOGGER = logging.getLogger(__name__)


class DewpointCalculatorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Dewpoint Calculator."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        # Get translations
        translations = await async_get_translations(
            self.hass, self.hass.config.language, "config", [DOMAIN]
        )
        domain_strings: dict[str, Any] | str = translations.get(DOMAIN, {})
        if isinstance(domain_strings, dict):
            config_strings: dict[str, Any] | str = domain_strings.get("config", {})
            if isinstance(config_strings, dict):
                step_strings: dict[str, Any] = config_strings.get("step", {}).get(
                    "user", {}
                )
            else:
                step_strings = {}
        else:
            step_strings = {}

        if user_input is not None:
            # Unique ID based on the selected sensors
            unique_id = f"{user_input[CONF_TEMPERATURE_ENTITY]}_{user_input[CONF_HUMIDITY_ENTITY]}"
            await self.async_set_unique_id(unique_id)
            self._abort_if_unique_id_configured()

            # Create title from the name
            default_title = (
                step_strings.get("title", "Dewpoint")
                if isinstance(step_strings, dict)
                else "Dewpoint"
            )
            title = user_input.get("name", default_title)

            return self.async_create_entry(
                title=title,
                data=user_input,
            )

        # Schema with nice dropdown selectors
        data_schema = vol.Schema(
            {
                vol.Required("name", default="Dewpoint"): str,
                vol.Required(CONF_TEMPERATURE_ENTITY): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="sensor",
                        device_class="temperature",
                    )
                ),
                vol.Required(CONF_HUMIDITY_ENTITY): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="sensor",
                        device_class="humidity",
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Dewpoint Calculator."""

    def __init__(self, config_entry: config_entries.ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> config_entries.ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            # Update config entry
            self.hass.config_entries.async_update_entry(
                self.config_entry,
                data={**self.config_entry.data, **user_input},
            )
            return self.async_create_entry(title="", data={})

        # Current values as default
        data_schema = vol.Schema(
            {
                vol.Required(
                    "name",
                    default=self.config_entry.data.get("name", "Dewpoint"),
                ): str,
                vol.Required(
                    CONF_TEMPERATURE_ENTITY,
                    default=self.config_entry.data.get(CONF_TEMPERATURE_ENTITY),
                ): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="sensor",
                        device_class="temperature",
                    )
                ),
                vol.Required(
                    CONF_HUMIDITY_ENTITY,
                    default=self.config_entry.data.get(CONF_HUMIDITY_ENTITY),
                ): selector.EntitySelector(
                    selector.EntitySelectorConfig(
                        domain="sensor",
                        device_class="humidity",
                    )
                ),
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=data_schema,
        )
