# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# generated using file ./gen/model/dent/network/tc/tc.yaml
#
# DONOT EDIT - generated by diligent bots

import asyncio

from dent_os_testbed.lib.tc.tc_chain import TcChain

from .utils import TestDevice


def test_that_tc_chain_add(capfd):

    dv1 = TestDevice(platform='dentos')
    dv2 = TestDevice(platform='dentos')
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.add(
            input_data=[
                {
                    # device 1
                    'test_dev': [{}],
                }
            ],
            device_obj={'test_dev': dv1},
        )
    )
    print(out)
    assert 'command' in out[0]['test_dev'].keys()
    assert 'result' in out[0]['test_dev'].keys()
    # check the rc
    assert out[0]['test_dev']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.add(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            # command 1
                            'parent': 227,
                            'root': True,
                            'block': 1340,
                            'filtertype': 'hghovvyh',
                            'options': 'soleycsj',
                        },
                        {
                            # command 2
                            'parent': 6203,
                            'root': True,
                            'block': 3045,
                            'filtertype': 'rayvqtwx',
                            'options': 'trqjgsfn',
                        },
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.add(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            'parent': 227,
                            'root': True,
                            'block': 1340,
                            'filtertype': 'hghovvyh',
                            'options': 'soleycsj',
                        }
                    ],
                    # device 2
                    'test_dev2': [
                        {
                            'parent': 6203,
                            'root': True,
                            'block': 3045,
                            'filtertype': 'rayvqtwx',
                            'options': 'trqjgsfn',
                        }
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    assert 'command' in out[1]['test_dev2'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    assert 'result' in out[1]['test_dev2'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0
    assert out[1]['test_dev2']['rc'] == 0


def test_that_tc_chain_delete(capfd):

    dv1 = TestDevice(platform='dentos')
    dv2 = TestDevice(platform='dentos')
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.delete(
            input_data=[
                {
                    # device 1
                    'test_dev': [{}],
                }
            ],
            device_obj={'test_dev': dv1},
        )
    )
    print(out)
    assert 'command' in out[0]['test_dev'].keys()
    assert 'result' in out[0]['test_dev'].keys()
    # check the rc
    assert out[0]['test_dev']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.delete(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            # command 1
                            'parent': 3150,
                            'root': False,
                            'block': 9151,
                            'filtertype': 'tkoionev',
                            'options': 'mewuqsdn',
                        },
                        {
                            # command 2
                            'parent': 1548,
                            'root': True,
                            'block': 5145,
                            'filtertype': 'ctezvngy',
                            'options': 'nyohorwj',
                        },
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.delete(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            'parent': 3150,
                            'root': False,
                            'block': 9151,
                            'filtertype': 'tkoionev',
                            'options': 'mewuqsdn',
                        }
                    ],
                    # device 2
                    'test_dev2': [
                        {
                            'parent': 1548,
                            'root': True,
                            'block': 5145,
                            'filtertype': 'ctezvngy',
                            'options': 'nyohorwj',
                        }
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    assert 'command' in out[1]['test_dev2'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    assert 'result' in out[1]['test_dev2'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0
    assert out[1]['test_dev2']['rc'] == 0


def test_that_tc_chain_get(capfd):

    dv1 = TestDevice(platform='dentos')
    dv2 = TestDevice(platform='dentos')
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.get(
            input_data=[
                {
                    # device 1
                    'test_dev': [{}],
                }
            ],
            device_obj={'test_dev': dv1},
        )
    )
    print(out)
    assert 'command' in out[0]['test_dev'].keys()
    assert 'result' in out[0]['test_dev'].keys()
    # check the rc
    assert out[0]['test_dev']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.get(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            # command 1
                            'parent': 8524,
                            'root': False,
                            'block': 3895,
                            'filtertype': 'tvzoatae',
                            'options': 'syxfnfzg',
                        },
                        {
                            # command 2
                            'parent': 9170,
                            'root': True,
                            'block': 5252,
                            'filtertype': 'skkknymo',
                            'options': 'twnkwgjz',
                        },
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.get(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            'parent': 8524,
                            'root': False,
                            'block': 3895,
                            'filtertype': 'tvzoatae',
                            'options': 'syxfnfzg',
                        }
                    ],
                    # device 2
                    'test_dev2': [
                        {
                            'parent': 9170,
                            'root': True,
                            'block': 5252,
                            'filtertype': 'skkknymo',
                            'options': 'twnkwgjz',
                        }
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    assert 'command' in out[1]['test_dev2'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    assert 'result' in out[1]['test_dev2'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0
    assert out[1]['test_dev2']['rc'] == 0


def test_that_tc_chain_show(capfd):

    dv1 = TestDevice(platform='dentos')
    dv2 = TestDevice(platform='dentos')
    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.show(
            input_data=[
                {
                    # device 1
                    'test_dev': [{}],
                }
            ],
            device_obj={'test_dev': dv1},
        )
    )
    print(out)
    assert 'command' in out[0]['test_dev'].keys()
    assert 'result' in out[0]['test_dev'].keys()
    # check the rc
    assert out[0]['test_dev']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.show(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            # command 1
                            'block': 4131,
                            'options': 'qikdpaan',
                        },
                        {
                            # command 2
                            'block': 9110,
                            'options': 'qseurzsd',
                        },
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0

    loop = asyncio.get_event_loop()
    out = loop.run_until_complete(
        TcChain.show(
            input_data=[
                {
                    # device 1
                    'test_dev1': [
                        {
                            'block': 4131,
                            'options': 'qikdpaan',
                        }
                    ],
                    # device 2
                    'test_dev2': [
                        {
                            'block': 9110,
                            'options': 'qseurzsd',
                        }
                    ],
                }
            ],
            device_obj={'test_dev1': dv1, 'test_dev2': dv2},
        )
    )
    print(out)
    # check if the command was formed
    assert 'command' in out[0]['test_dev1'].keys()
    assert 'command' in out[1]['test_dev2'].keys()
    # check if the result was formed
    assert 'result' in out[0]['test_dev1'].keys()
    assert 'result' in out[1]['test_dev2'].keys()
    # check the rc
    assert out[0]['test_dev1']['rc'] == 0
    assert out[1]['test_dev2']['rc'] == 0
