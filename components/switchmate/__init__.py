from esphome.components import ble_client
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import CONF_ID

AUTO_LOAD = ["sensor", "switch", "ble_client"]

switchmate_ns = cg.esphome_ns.namespace("switchmate")

SwitchmateController = switchmate_ns.class_("SwitchmateController", cg.PollingComponent, ble_client.BLEClientNode)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SwitchmateController),
    cv.Required("ble_client_id"): cv.use_id(ble_client.BLEClient),
    cv.Required("name"): cv.string,
    cv.Optional("notify", default=False): cv.boolean,
    cv.Optional("update_interval", default="1s"): cv.update_interval,
})
