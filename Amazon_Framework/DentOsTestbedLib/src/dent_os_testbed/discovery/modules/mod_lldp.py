# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/platform/lldp/lldp.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.discovery.Module import Module
from dent_os_testbed.lib.lldp.lldp import Lldp


class LldpMod(Module):
    """"""

    def set_lldp(self, src, dst):

        for i, lldp in enumerate(src):
            if "interface" in lldp:
                dst[i].interface = lldp.get("interface")
            if "options" in lldp:
                dst[i].options = lldp.get("options")
            if "remote_host" in lldp:
                dst[i].remote_host = lldp.get("remote_host")
            if "remote_interface" in lldp:
                dst[i].remote_interface = lldp.get("remote_interface")

    async def discover(self):
        # need to get device instance to get the data from
        #
        for i, dut in enumerate(self.report.duts):
            if not dut.device_id:
                continue
            dev = self.ctx.devices_dict[dut.device_id]
            if dev.os == "ixnetwork" or not await dev.is_connected():
                print("Device not connected skipping lldp discovery")
                continue
            print("Running lldp Discovery on " + dev.host_name)
            out = await Lldp.show(
                input_data=[{dev.host_name: [{"dut_discovery": True}]}],
                device_obj={dev.host_name: dev},
                parse_output=True,
            )
            if out[0][dev.host_name]["rc"] != 0:
                print(out)
                print("Failed to get lldp")
                continue
            if "parsed_output" not in out[0][dev.host_name]:
                print("Failed to get parsed_output lldp")
                print(out)
                continue
            self.set_lldp(
                out[0][dev.host_name]["parsed_output"], self.report.duts[i].platform.lldp.interfaces
            )
            print(
                "Finished lldp Discovery on {} with {} entries".format(
                    dev.host_name, len(self.report.duts[i].platform.lldp.interfaces)
                )
            )