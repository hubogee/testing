# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/tc/tc.yaml
#
# DONOT EDIT - generated by diligent bots

import pytest
from dent_os_testbed.lib.test_lib_object import TestLibObject
from dent_os_testbed.lib.tc.linux.linux_tc_class_impl import LinuxTcClassImpl
class TcClass(TestLibObject):
    """
        - tc [ OPTIONS ] [ FORMAT ] class show dev DEV
        - tc [ OPTIONS ] class [ add | change | replace | delete ] dev DEV parent qdisc-id
         [ classid class-id ] qdisc [ qdisc specific parameters ]
        OPTIONS := { [ -force ] -b[atch] [ filename ] | [ -n[etns] name ] | [ -nm | -nam[es] ] |
          [ { -cf | -c[onf] } [ filename ] ] [ -t[imestamp] ] | [ -t[short] | [ -o[neline] ] }
        FORMAT := { -s[tatistics] | -d[etails] | -r[aw] | -i[ec] | -g[raph] | -j[json] | -p[retty] | -col[or] }

    """
    async def _run_command(api, *argv, **kwarg):
        devices = kwarg['input_data']
        result = list()
        for device in devices:
            for device_name in device:
                device_result = {
                    device_name : dict()
                }
                # device lookup
                if 'device_obj' in kwarg:
                    device_obj = kwarg.get('device_obj', None)[device_name]
                else:
                    if device_name not in pytest.testbed.devices_dict:
                        device_result[device_name] =  'No matching device '+ device_name
                        result.append(device_result)
                        return result
                    device_obj = pytest.testbed.devices_dict[device_name]
                commands = ''
                if device_obj.os in ['dentos', 'cumulus']:
                    impl_obj = LinuxTcClassImpl()
                    for command in device[device_name]:
                        commands += impl_obj.format_command(command=api, params=command)
                        commands += '&& '
                    commands = commands[:-3]

                else:
                    device_result[device_name]['rc'] = -1
                    device_result[device_name]['result'] = 'No matching device OS '+ device_obj.os
                    result.append(device_result)
                    return result
                device_result[device_name]['command'] = commands
                try:
                    rc, output = await device_obj.run_cmd(('sudo ' if device_obj.ssh_conn_params.pssh else '') + commands)
                    device_result[device_name]['rc'] = rc
                    device_result[device_name]['result'] = output
                    if 'parse_output' in kwarg:
                        parse_output = impl_obj.parse_output(command=api, output=output, commands=commands)
                        device_result[device_name]['parsed_output'] = parse_output
                except Exception as e:
                    device_result[device_name]['rc'] = -1
                    device_result[device_name]['result'] = str(e)
                result.append(device_result)
        return result

    async def add(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcClass.add(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'classid':'int',
                        'qdisc':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] class [ add | change | replace | delete ] dev DEV parent qdisc-id [
        classid class-id ] qdisc [ qdisc specific parameters ]

        """
        return await TcClass._run_command('add', *argv, **kwarg)

    async def change(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcClass.change(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'classid':'int',
                        'qdisc':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] class [ add | change | replace | delete ] dev DEV parent qdisc-id [
        classid class-id ] qdisc [ qdisc specific parameters ]

        """
        return await TcClass._run_command('change', *argv, **kwarg)

    async def replace(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcClass.replace(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'classid':'int',
                        'qdisc':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] class [ add | change | replace | delete ] dev DEV parent qdisc-id [
        classid class-id ] qdisc [ qdisc specific parameters ]

        """
        return await TcClass._run_command('replace', *argv, **kwarg)

    async def delete(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcClass.delete(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'parent':'int',
                        'classid':'int',
                        'qdisc':'int',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] class [ add | change | replace | delete ] dev DEV parent qdisc-id [
        classid class-id ] qdisc [ qdisc specific parameters ]

        """
        return await TcClass._run_command('delete', *argv, **kwarg)

    async def show(*argv, **kwarg):
        """
        Platforms: ['dentos', 'cumulus']
        Usage:
        TcClass.show(
            input_data = [{
                # device 1
                'dev1' : [{
                    # command 1
                        'dev':'string',
                        'format':'string',
                        'options':'string',
                }],
            }],
        )
        Description:
        tc [ OPTIONS ] [ FORMAT ] class show dev DEV

        """
        return await TcClass._run_command('show', *argv, **kwarg)
