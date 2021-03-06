# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServiceProperties(Model):
    """The properties of a service.

    All required parameters must be populated in order to send to Azure.

    :param target_location: Required. The Azure location to which the
     resources in the service belong to or should be deployed to.
    :type target_location: str
    :param target_subscription_id: Required. The subscription to which the
     resources in the service belong to or should be deployed to.
    :type target_subscription_id: str
    """

    _validation = {
        'target_location': {'required': True},
        'target_subscription_id': {'required': True},
    }

    _attribute_map = {
        'target_location': {'key': 'targetLocation', 'type': 'str'},
        'target_subscription_id': {'key': 'targetSubscriptionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceProperties, self).__init__(**kwargs)
        self.target_location = kwargs.get('target_location', None)
        self.target_subscription_id = kwargs.get('target_subscription_id', None)
