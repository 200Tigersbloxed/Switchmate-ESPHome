from esphome.components import sensor, switch, ble_client
import esphome.codegen as cg

switchmate_ns = cg.esphome_ns.namespace("switchmate")

SwitchmateController = switchmate_ns.class_(
    "SwitchmateController",
    cg.PollingComponent,
    ble_client.BLEClientNode
)

SwitchmateSwitch = switchmate_ns.class_(
    "SwitchmateSwitch",
    switch.Switch
)

Sensor = sensor.Sensor
