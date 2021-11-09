# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/linux/protocol/frr/iproute.yaml
#
# DONOT EDIT - generated by diligent bots

from dent_os_testbed.lib.test_lib_object import TestLibObject


class LinuxFrrIpRoute(TestLibObject):
    """
    vtysh

    """

    def format_show(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_show(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_add(self, command, *argv, **kwarg):
        raise NotImplementedError

    def parse_add(self, command, output, *argv, **kwarg):
        raise NotImplementedError

    def format_command(self, command, *argv, **kwarg):
        if command in ["show"]:
            return self.format_show(command, *argv, **kwarg)

        if command in ["add"]:
            return self.format_add(command, *argv, **kwarg)

        raise NameError("Cannot find command " + command)

    def parse_output(self, command, output, *argv, **kwarg):
        if command in ["show"]:
            return self.parse_show(command, output, *argv, **kwarg)

        if command in ["add"]:
            return self.parse_add(command, output, *argv, **kwarg)

        raise NameError("Cannot find command " + command)
