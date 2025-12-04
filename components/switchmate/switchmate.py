from esphome.components import sensor, switch, ble_client
import esphome.codegen as cg
from esphome.const import CONF_ID, CONF_NAME, CONF_ICON, ENTITY_CATEGORY_DIAGNOSTIC

switchmate_ns = cg.esphome_ns.namespace("switchmate")
SwitchmateController = switchmate_ns.class_("SwitchmateController", cg.PollingComponent, ble_client.BLEClientNode)
SwitchmateSwitch = switchmate_ns.class_("SwitchmateSwitch", switch.Switch)
Sensor = sensor.Sensor

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_NAME], config["notify"], config["update_interval"])
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
