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


class SignalRCreateOrUpdateProperties(Model):
    """Settings used to provision or configure the resource.

    :param host_name_prefix: Prefix for the hostName of the SignalR service.
     Retained for future use.
     The hostname will be of format:
     &lt;hostNamePrefix&gt;.service.signalr.net.
    :type host_name_prefix: str
    :param features: List of SignalR featureFlags. e.g. ServiceMode.
     FeatureFlags that are not included in the parameters for the update
     operation will not be modified.
     And the response will only include featureFlags that are explicitly set.
     When a featureFlag is not explicitly set, SignalR service will use its
     globally default value.
     But keep in mind, the default value doesn't mean "false". It varies in
     terms of different FeatureFlags.
    :type features: list[~azure.mgmt.signalr.models.SignalRFeature]
    """

    _attribute_map = {
        'host_name_prefix': {'key': 'hostNamePrefix', 'type': 'str'},
        'features': {'key': 'features', 'type': '[SignalRFeature]'},
    }

    def __init__(self, **kwargs):
        super(SignalRCreateOrUpdateProperties, self).__init__(**kwargs)
        self.host_name_prefix = kwargs.get('host_name_prefix', None)
        self.features = kwargs.get('features', None)
