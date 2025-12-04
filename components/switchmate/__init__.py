from esphome.components import ble_client, switch, sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID, CONF_NAME

from .switchmate import (
    SwitchmateController,
    SwitchmateSwitch
)

AUTO_LOAD = ["sensor", "switch", "ble_client"]

CONFIG_SCHEMA = (
    switch.SWITCH_SCHEMA.extend({
        cv.GenerateID(): cv.declare_id(SwitchmateController),
        cv.Required("ble_client_id"): cv.use_id(ble_client.BLEClient),
        cv.Optional("notify", default=False): cv.boolean,
        cv.Optional("update_interval", default="1s"): cv.update_interval,
    })
)

@switch.register_switch("switchmate", SwitchmateSwitch, CONFIG_SCHEMA)
async def to_code(config):
    var = cg.new_Pvariable(
        config[CONF_ID],
        config[CONF_NAME],
        config["notify"],
        config["update_interval"]
    )

    await cg.register_component(var, config)

    client = await cg.get_variable(config["ble_client_id"])
    cg.add(client.register_ble_node(var))

    # Battery sensor
    batt = await sensor.new_sensor({
        "name": f"{config[CONF_NAME]} Battery",
        "icon": "mdi:battery",
        "unit_of_measurement": "%",
    })
    cg.add(var.set_battery_sensor(batt))

    # State switch
    sw = await switch.new_switch({
        "name": config[CONF_NAME],
        "icon": "mdi:light-switch",
    })
    cg.add(var.set_state_switch(sw))
