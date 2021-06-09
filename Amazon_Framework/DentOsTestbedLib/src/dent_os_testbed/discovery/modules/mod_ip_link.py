# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/ip/link.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.discovery.Module import Module
from dent_os_testbed.lib.ip.ip_link import IpLink


class IpLinkMod(Module):
    """"""

    def set_ip_link(self, src, dst):

        for i, ip_link in enumerate(src):
            if "ifindex" in ip_link:
                dst[i].ifindex = ip_link.get("ifindex")
            if "ifname" in ip_link:
                dst[i].ifname = ip_link.get("ifname")
            if "mtu" in ip_link:
                dst[i].mtu = ip_link.get("mtu")
            if "qdisc" in ip_link:
                dst[i].qdisc = ip_link.get("qdisc")
            if "operstate" in ip_link:
                dst[i].operstate = ip_link.get("operstate")
            if "linkmode" in ip_link:
                dst[i].linkmode = ip_link.get("linkmode")
            if "group" in ip_link:
                dst[i].group = ip_link.get("group")
            if "txqlen" in ip_link:
                dst[i].txqlen = ip_link.get("txqlen")
            if "link_type" in ip_link:
                dst[i].link_type = ip_link.get("link_type")
            if "address" in ip_link:
                dst[i].address = ip_link.get("address")
            if "broadcast" in ip_link:
                dst[i].broadcast = ip_link.get("broadcast")
            if "promiscuity" in ip_link:
                dst[i].promiscuity = ip_link.get("promiscuity")
            if "min_mtu" in ip_link:
                dst[i].min_mtu = ip_link.get("min_mtu")
            if "max_mtu" in ip_link:
                dst[i].max_mtu = ip_link.get("max_mtu")
            if "inet6_addr_gen_mode" in ip_link:
                dst[i].inet6_addr_gen_mode = ip_link.get("inet6_addr_gen_mode")
            if "num_tx_queues" in ip_link:
                dst[i].num_tx_queues = ip_link.get("num_tx_queues")
            if "num_rx_queues" in ip_link:
                dst[i].num_rx_queues = ip_link.get("num_rx_queues")
            if "gso_max_size" in ip_link:
                dst[i].gso_max_size = ip_link.get("gso_max_size")
            if "gso_max_segs" in ip_link:
                dst[i].gso_max_segs = ip_link.get("gso_max_segs")
            if "phys_port_name" in ip_link:
                dst[i].phys_port_name = ip_link.get("phys_port_name")
            if "phys_switch_id" in ip_link:
                dst[i].phys_switch_id = ip_link.get("phys_switch_id")
            if "device" in ip_link:
                dst[i].device = ip_link.get("device")
            if "txqueuelen" in ip_link:
                dst[i].txqueuelen = ip_link.get("txqueuelen")
            if "name" in ip_link:
                dst[i].name = ip_link.get("name")
            if "netns" in ip_link:
                dst[i].netns = ip_link.get("netns")
            if "alias" in ip_link:
                dst[i].alias = ip_link.get("alias")
            if "vf" in ip_link:
                dst[i].vf = ip_link.get("vf")
            if "mac" in ip_link:
                dst[i].mac = ip_link.get("mac")
            if "qos" in ip_link:
                dst[i].qos = ip_link.get("qos")
            if "vlan" in ip_link:
                dst[i].vlan = ip_link.get("vlan")
            if "rate" in ip_link:
                dst[i].rate = ip_link.get("rate")
            if "max_tx_rate" in ip_link:
                dst[i].max_tx_rate = ip_link.get("max_tx_rate")
            if "min_tx_rate" in ip_link:
                dst[i].min_tx_rate = ip_link.get("min_tx_rate")
            if "spoofchk" in ip_link:
                dst[i].spoofchk = ip_link.get("spoofchk")
            if "state" in ip_link:
                dst[i].state = ip_link.get("state")
            if "master" in ip_link:
                dst[i].master = ip_link.get("master")
            if "options" in ip_link:
                dst[i].options = ip_link.get("options")

    async def discover(self):
        # need to get device instance to get the data from
        #
        for i, dut in enumerate(self.report.duts):
            if not dut.device_id:
                continue
            dev = self.ctx.devices_dict[dut.device_id]
            if dev.os == "ixnetwork" or not await dev.is_connected():
                print("Device not connected skipping ip_link discovery")
                continue
            print("Running ip_link Discovery on " + dev.host_name)
            out = await IpLink.show(
                input_data=[{dev.host_name: [{"dut_discovery": True}]}],
                device_obj={dev.host_name: dev},
                parse_output=True,
            )
            if out[0][dev.host_name]["rc"] != 0:
                print(out)
                print("Failed to get ip_link")
                continue
            if "parsed_output" not in out[0][dev.host_name]:
                print("Failed to get parsed_output ip_link")
                print(out)
                continue
            self.set_ip_link(
                out[0][dev.host_name]["parsed_output"], self.report.duts[i].network.layer1.links
            )
            print(
                "Finished ip_link Discovery on {} with {} entries".format(
                    dev.host_name, len(self.report.duts[i].network.layer1.links)
                )
            )
