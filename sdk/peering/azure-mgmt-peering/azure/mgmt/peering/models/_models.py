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
from msrest.exceptions import HttpOperationError


class BgpSession(Model):
    """The properties that define a BGP session.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param session_prefix_v4: The IPv4 prefix that contains both ends' IPv4
     addresses.
    :type session_prefix_v4: str
    :param session_prefix_v6: The IPv6 prefix that contains both ends' IPv6
     addresses.
    :type session_prefix_v6: str
    :ivar microsoft_session_ipv4_address: The IPv4 session address on
     Microsoft's end.
    :vartype microsoft_session_ipv4_address: str
    :ivar microsoft_session_ipv6_address: The IPv6 session address on
     Microsoft's end.
    :vartype microsoft_session_ipv6_address: str
    :param peer_session_ipv4_address: The IPv4 session address on peer's end.
    :type peer_session_ipv4_address: str
    :param peer_session_ipv6_address: The IPv6 session address on peer's end.
    :type peer_session_ipv6_address: str
    :ivar session_state_v4: The state of the IPv4 session. Possible values
     include: 'None', 'Idle', 'Connect', 'Active', 'OpenSent', 'OpenConfirm',
     'OpenReceived', 'Established', 'PendingAdd', 'PendingUpdate',
     'PendingRemove'
    :vartype session_state_v4: str or
     ~azure.mgmt.peering.models.SessionStateV4
    :ivar session_state_v6: The state of the IPv6 session. Possible values
     include: 'None', 'Idle', 'Connect', 'Active', 'OpenSent', 'OpenConfirm',
     'OpenReceived', 'Established', 'PendingAdd', 'PendingUpdate',
     'PendingRemove'
    :vartype session_state_v6: str or
     ~azure.mgmt.peering.models.SessionStateV6
    :param max_prefixes_advertised_v4: The maximum number of prefixes
     advertised over the IPv4 session.
    :type max_prefixes_advertised_v4: int
    :param max_prefixes_advertised_v6: The maximum number of prefixes
     advertised over the IPv6 session.
    :type max_prefixes_advertised_v6: int
    :param md5_authentication_key: The MD5 authentication key of the session.
    :type md5_authentication_key: str
    """

    _validation = {
        'microsoft_session_ipv4_address': {'readonly': True},
        'microsoft_session_ipv6_address': {'readonly': True},
        'session_state_v4': {'readonly': True},
        'session_state_v6': {'readonly': True},
    }

    _attribute_map = {
        'session_prefix_v4': {'key': 'sessionPrefixV4', 'type': 'str'},
        'session_prefix_v6': {'key': 'sessionPrefixV6', 'type': 'str'},
        'microsoft_session_ipv4_address': {'key': 'microsoftSessionIPv4Address', 'type': 'str'},
        'microsoft_session_ipv6_address': {'key': 'microsoftSessionIPv6Address', 'type': 'str'},
        'peer_session_ipv4_address': {'key': 'peerSessionIPv4Address', 'type': 'str'},
        'peer_session_ipv6_address': {'key': 'peerSessionIPv6Address', 'type': 'str'},
        'session_state_v4': {'key': 'sessionStateV4', 'type': 'str'},
        'session_state_v6': {'key': 'sessionStateV6', 'type': 'str'},
        'max_prefixes_advertised_v4': {'key': 'maxPrefixesAdvertisedV4', 'type': 'int'},
        'max_prefixes_advertised_v6': {'key': 'maxPrefixesAdvertisedV6', 'type': 'int'},
        'md5_authentication_key': {'key': 'md5AuthenticationKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BgpSession, self).__init__(**kwargs)
        self.session_prefix_v4 = kwargs.get('session_prefix_v4', None)
        self.session_prefix_v6 = kwargs.get('session_prefix_v6', None)
        self.microsoft_session_ipv4_address = None
        self.microsoft_session_ipv6_address = None
        self.peer_session_ipv4_address = kwargs.get('peer_session_ipv4_address', None)
        self.peer_session_ipv6_address = kwargs.get('peer_session_ipv6_address', None)
        self.session_state_v4 = None
        self.session_state_v6 = None
        self.max_prefixes_advertised_v4 = kwargs.get('max_prefixes_advertised_v4', None)
        self.max_prefixes_advertised_v6 = kwargs.get('max_prefixes_advertised_v6', None)
        self.md5_authentication_key = kwargs.get('md5_authentication_key', None)


class CheckServiceProviderAvailabilityInput(Model):
    """Class for CheckServiceProviderAvailabilityInput.

    :param peering_service_location: Gets or sets the PeeringServiceLocation
    :type peering_service_location: str
    :param peering_service_provider: Gets or sets the PeeringServiceProvider
    :type peering_service_provider: str
    """

    _attribute_map = {
        'peering_service_location': {'key': 'peeringServiceLocation', 'type': 'str'},
        'peering_service_provider': {'key': 'peeringServiceProvider', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CheckServiceProviderAvailabilityInput, self).__init__(**kwargs)
        self.peering_service_location = kwargs.get('peering_service_location', None)
        self.peering_service_provider = kwargs.get('peering_service_provider', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ContactInfo(Model):
    """The contact information of the peer.

    :param emails: The list of email addresses.
    :type emails: list[str]
    :param phone: The list of contact numbers.
    :type phone: list[str]
    """

    _attribute_map = {
        'emails': {'key': 'emails', 'type': '[str]'},
        'phone': {'key': 'phone', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ContactInfo, self).__init__(**kwargs)
        self.emails = kwargs.get('emails', None)
        self.phone = kwargs.get('phone', None)


class DirectConnection(Model):
    """The properties that define a direct connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param bandwidth_in_mbps: The bandwidth of the connection.
    :type bandwidth_in_mbps: int
    :param provisioned_bandwidth_in_mbps: The bandwidth that is actually
     provisioned.
    :type provisioned_bandwidth_in_mbps: int
    :param session_address_provider: The field indicating if Microsoft
     provides session ip addresses. Possible values include: 'Microsoft',
     'Peer'
    :type session_address_provider: str or
     ~azure.mgmt.peering.models.SessionAddressProvider
    :param use_for_peering_service: The flag that indicates whether or not the
     connection is used for peering service.
    :type use_for_peering_service: bool
    :param peering_db_facility_id: The PeeringDB.com ID of the facility at
     which the connection has to be set up.
    :type peering_db_facility_id: int
    :ivar connection_state: The state of the connection. Possible values
     include: 'None', 'PendingApproval', 'Approved', 'ProvisioningStarted',
     'ProvisioningFailed', 'ProvisioningCompleted', 'Validating', 'Active'
    :vartype connection_state: str or
     ~azure.mgmt.peering.models.ConnectionState
    :param bgp_session: The BGP session associated with the connection.
    :type bgp_session: ~azure.mgmt.peering.models.BgpSession
    :param connection_identifier: The unique identifier (GUID) for the
     connection.
    :type connection_identifier: str
    """

    _validation = {
        'connection_state': {'readonly': True},
    }

    _attribute_map = {
        'bandwidth_in_mbps': {'key': 'bandwidthInMbps', 'type': 'int'},
        'provisioned_bandwidth_in_mbps': {'key': 'provisionedBandwidthInMbps', 'type': 'int'},
        'session_address_provider': {'key': 'sessionAddressProvider', 'type': 'str'},
        'use_for_peering_service': {'key': 'useForPeeringService', 'type': 'bool'},
        'peering_db_facility_id': {'key': 'peeringDBFacilityId', 'type': 'int'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'bgp_session': {'key': 'bgpSession', 'type': 'BgpSession'},
        'connection_identifier': {'key': 'connectionIdentifier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DirectConnection, self).__init__(**kwargs)
        self.bandwidth_in_mbps = kwargs.get('bandwidth_in_mbps', None)
        self.provisioned_bandwidth_in_mbps = kwargs.get('provisioned_bandwidth_in_mbps', None)
        self.session_address_provider = kwargs.get('session_address_provider', None)
        self.use_for_peering_service = kwargs.get('use_for_peering_service', None)
        self.peering_db_facility_id = kwargs.get('peering_db_facility_id', None)
        self.connection_state = None
        self.bgp_session = kwargs.get('bgp_session', None)
        self.connection_identifier = kwargs.get('connection_identifier', None)


class DirectPeeringFacility(Model):
    """The properties that define a direct peering facility.

    :param address: The address of the direct peering facility.
    :type address: str
    :param direct_peering_type: The type of the direct peering. Possible
     values include: 'Edge', 'Transit', 'Cdn', 'Internal'
    :type direct_peering_type: str or
     ~azure.mgmt.peering.models.DirectPeeringType
    :param peering_db_facility_id: The PeeringDB.com ID of the facility.
    :type peering_db_facility_id: int
    :param peering_db_facility_link: The PeeringDB.com URL of the facility.
    :type peering_db_facility_link: str
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'direct_peering_type': {'key': 'directPeeringType', 'type': 'str'},
        'peering_db_facility_id': {'key': 'peeringDBFacilityId', 'type': 'int'},
        'peering_db_facility_link': {'key': 'peeringDBFacilityLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DirectPeeringFacility, self).__init__(**kwargs)
        self.address = kwargs.get('address', None)
        self.direct_peering_type = kwargs.get('direct_peering_type', None)
        self.peering_db_facility_id = kwargs.get('peering_db_facility_id', None)
        self.peering_db_facility_link = kwargs.get('peering_db_facility_link', None)


class ErrorResponse(Model):
    """The error response that indicates why an operation has failed.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = None
        self.message = None


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ExchangeConnection(Model):
    """The properties that define an exchange connection.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param peering_db_facility_id: The PeeringDB.com ID of the facility at
     which the connection has to be set up.
    :type peering_db_facility_id: int
    :ivar connection_state: The state of the connection. Possible values
     include: 'None', 'PendingApproval', 'Approved', 'ProvisioningStarted',
     'ProvisioningFailed', 'ProvisioningCompleted', 'Validating', 'Active'
    :vartype connection_state: str or
     ~azure.mgmt.peering.models.ConnectionState
    :param bgp_session: The BGP session associated with the connection.
    :type bgp_session: ~azure.mgmt.peering.models.BgpSession
    :param connection_identifier: The unique identifier (GUID) for the
     connection.
    :type connection_identifier: str
    """

    _validation = {
        'connection_state': {'readonly': True},
    }

    _attribute_map = {
        'peering_db_facility_id': {'key': 'peeringDBFacilityId', 'type': 'int'},
        'connection_state': {'key': 'connectionState', 'type': 'str'},
        'bgp_session': {'key': 'bgpSession', 'type': 'BgpSession'},
        'connection_identifier': {'key': 'connectionIdentifier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExchangeConnection, self).__init__(**kwargs)
        self.peering_db_facility_id = kwargs.get('peering_db_facility_id', None)
        self.connection_state = None
        self.bgp_session = kwargs.get('bgp_session', None)
        self.connection_identifier = kwargs.get('connection_identifier', None)


class ExchangePeeringFacility(Model):
    """The properties that define an exchange peering facility.

    :param exchange_name: The name of the exchange peering facility.
    :type exchange_name: str
    :param bandwidth_in_mbps: The bandwidth of the connection between
     Microsoft and the exchange peering facility.
    :type bandwidth_in_mbps: int
    :param microsoft_ipv4_address: The IPv4 address of Microsoft at the
     exchange peering facility.
    :type microsoft_ipv4_address: str
    :param microsoft_ipv6_address: The IPv6 address of Microsoft at the
     exchange peering facility.
    :type microsoft_ipv6_address: str
    :param facility_ipv4_prefix: The IPv4 prefixes associated with the
     exchange peering facility.
    :type facility_ipv4_prefix: str
    :param facility_ipv6_prefix: The IPv6 prefixes associated with the
     exchange peering facility.
    :type facility_ipv6_prefix: str
    :param peering_db_facility_id: The PeeringDB.com ID of the facility.
    :type peering_db_facility_id: int
    :param peering_db_facility_link: The PeeringDB.com URL of the facility.
    :type peering_db_facility_link: str
    """

    _attribute_map = {
        'exchange_name': {'key': 'exchangeName', 'type': 'str'},
        'bandwidth_in_mbps': {'key': 'bandwidthInMbps', 'type': 'int'},
        'microsoft_ipv4_address': {'key': 'microsoftIPv4Address', 'type': 'str'},
        'microsoft_ipv6_address': {'key': 'microsoftIPv6Address', 'type': 'str'},
        'facility_ipv4_prefix': {'key': 'facilityIPv4Prefix', 'type': 'str'},
        'facility_ipv6_prefix': {'key': 'facilityIPv6Prefix', 'type': 'str'},
        'peering_db_facility_id': {'key': 'peeringDBFacilityId', 'type': 'int'},
        'peering_db_facility_link': {'key': 'peeringDBFacilityLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExchangePeeringFacility, self).__init__(**kwargs)
        self.exchange_name = kwargs.get('exchange_name', None)
        self.bandwidth_in_mbps = kwargs.get('bandwidth_in_mbps', None)
        self.microsoft_ipv4_address = kwargs.get('microsoft_ipv4_address', None)
        self.microsoft_ipv6_address = kwargs.get('microsoft_ipv6_address', None)
        self.facility_ipv4_prefix = kwargs.get('facility_ipv4_prefix', None)
        self.facility_ipv6_prefix = kwargs.get('facility_ipv6_prefix', None)
        self.peering_db_facility_id = kwargs.get('peering_db_facility_id', None)
        self.peering_db_facility_link = kwargs.get('peering_db_facility_link', None)


class Operation(Model):
    """The peering API operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the operation.
    :vartype name: str
    :ivar display: The information related to the operation.
    :vartype display: ~azure.mgmt.peering.models.OperationDisplayInfo
    :ivar is_data_action: The flag that indicates whether the operation
     applies to data plane.
    :vartype is_data_action: bool
    """

    _validation = {
        'name': {'readonly': True},
        'display': {'readonly': True},
        'is_data_action': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplayInfo'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = None
        self.is_data_action = None


class OperationDisplayInfo(Model):
    """The information related to the operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provider: The name of the resource provider.
    :vartype provider: str
    :ivar resource: The type of the resource.
    :vartype resource: str
    :ivar operation: The name of the operation.
    :vartype operation: str
    :ivar description: The description of the operation.
    :vartype description: str
    """

    _validation = {
        'provider': {'readonly': True},
        'resource': {'readonly': True},
        'operation': {'readonly': True},
        'description': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplayInfo, self).__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class Resource(Model):
    """The ARM resource class.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None


class PeerAsn(Resource):
    """The essential information related to the peer's ASN.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param peer_asn: The Autonomous System Number (ASN) of the peer.
    :type peer_asn: int
    :param peer_contact_info: The contact information of the peer.
    :type peer_contact_info: ~azure.mgmt.peering.models.ContactInfo
    :param peer_name: The name of the peer.
    :type peer_name: str
    :param validation_state: The validation state of the ASN associated with
     the peer. Possible values include: 'None', 'Pending', 'Approved', 'Failed'
    :type validation_state: str or ~azure.mgmt.peering.models.ValidationState
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'peer_asn': {'key': 'properties.peerAsn', 'type': 'int'},
        'peer_contact_info': {'key': 'properties.peerContactInfo', 'type': 'ContactInfo'},
        'peer_name': {'key': 'properties.peerName', 'type': 'str'},
        'validation_state': {'key': 'properties.validationState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeerAsn, self).__init__(**kwargs)
        self.peer_asn = kwargs.get('peer_asn', None)
        self.peer_contact_info = kwargs.get('peer_contact_info', None)
        self.peer_name = kwargs.get('peer_name', None)
        self.validation_state = kwargs.get('validation_state', None)


class Peering(Resource):
    """Peering is a logical representation of a set of connections to the
    Microsoft Cloud Edge at a location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param sku: Required. The SKU that defines the tier and kind of the
     peering.
    :type sku: ~azure.mgmt.peering.models.PeeringSku
    :param kind: Required. The kind of the peering. Possible values include:
     'Direct', 'Exchange'
    :type kind: str or ~azure.mgmt.peering.models.Kind
    :param direct: The properties that define a direct peering.
    :type direct: ~azure.mgmt.peering.models.PeeringPropertiesDirect
    :param exchange: The properties that define an exchange peering.
    :type exchange: ~azure.mgmt.peering.models.PeeringPropertiesExchange
    :param peering_location: The location of the peering.
    :type peering_location: str
    :ivar provisioning_state: The provisioning state of the resource. Possible
     values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.peering.models.ProvisioningState
    :param location: Required. The location of the resource.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'sku': {'required': True},
        'kind': {'required': True},
        'provisioning_state': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'PeeringSku'},
        'kind': {'key': 'kind', 'type': 'str'},
        'direct': {'key': 'properties.direct', 'type': 'PeeringPropertiesDirect'},
        'exchange': {'key': 'properties.exchange', 'type': 'PeeringPropertiesExchange'},
        'peering_location': {'key': 'properties.peeringLocation', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Peering, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.kind = kwargs.get('kind', None)
        self.direct = kwargs.get('direct', None)
        self.exchange = kwargs.get('exchange', None)
        self.peering_location = kwargs.get('peering_location', None)
        self.provisioning_state = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class PeeringBandwidthOffer(Model):
    """The properties that define a peering bandwidth offer.

    :param offer_name: The name of the bandwidth offer.
    :type offer_name: str
    :param value_in_mbps: The value of the bandwidth offer in Mbps.
    :type value_in_mbps: int
    """

    _attribute_map = {
        'offer_name': {'key': 'offerName', 'type': 'str'},
        'value_in_mbps': {'key': 'valueInMbps', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(PeeringBandwidthOffer, self).__init__(**kwargs)
        self.offer_name = kwargs.get('offer_name', None)
        self.value_in_mbps = kwargs.get('value_in_mbps', None)


class PeeringLocation(Resource):
    """Peering location is where connectivity could be established to the
    Microsoft Cloud Edge.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param kind: The kind of peering that the peering location supports.
     Possible values include: 'Direct', 'Exchange'
    :type kind: str or ~azure.mgmt.peering.models.Kind
    :param direct: The properties that define a direct peering location.
    :type direct: ~azure.mgmt.peering.models.PeeringLocationPropertiesDirect
    :param exchange: The properties that define an exchange peering location.
    :type exchange:
     ~azure.mgmt.peering.models.PeeringLocationPropertiesExchange
    :param peering_location: The name of the peering location.
    :type peering_location: str
    :param country: The country in which the peering location exists.
    :type country: str
    :param azure_region: The Azure region associated with the peering
     location.
    :type azure_region: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'direct': {'key': 'properties.direct', 'type': 'PeeringLocationPropertiesDirect'},
        'exchange': {'key': 'properties.exchange', 'type': 'PeeringLocationPropertiesExchange'},
        'peering_location': {'key': 'properties.peeringLocation', 'type': 'str'},
        'country': {'key': 'properties.country', 'type': 'str'},
        'azure_region': {'key': 'properties.azureRegion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringLocation, self).__init__(**kwargs)
        self.kind = kwargs.get('kind', None)
        self.direct = kwargs.get('direct', None)
        self.exchange = kwargs.get('exchange', None)
        self.peering_location = kwargs.get('peering_location', None)
        self.country = kwargs.get('country', None)
        self.azure_region = kwargs.get('azure_region', None)


class PeeringLocationPropertiesDirect(Model):
    """The properties that define a direct peering location.

    :param peering_facilities: The list of direct peering facilities at the
     peering location.
    :type peering_facilities:
     list[~azure.mgmt.peering.models.DirectPeeringFacility]
    :param bandwidth_offers: The list of bandwidth offers available at the
     peering location.
    :type bandwidth_offers:
     list[~azure.mgmt.peering.models.PeeringBandwidthOffer]
    """

    _attribute_map = {
        'peering_facilities': {'key': 'peeringFacilities', 'type': '[DirectPeeringFacility]'},
        'bandwidth_offers': {'key': 'bandwidthOffers', 'type': '[PeeringBandwidthOffer]'},
    }

    def __init__(self, **kwargs):
        super(PeeringLocationPropertiesDirect, self).__init__(**kwargs)
        self.peering_facilities = kwargs.get('peering_facilities', None)
        self.bandwidth_offers = kwargs.get('bandwidth_offers', None)


class PeeringLocationPropertiesExchange(Model):
    """The properties that define an exchange peering location.

    :param peering_facilities: The list of exchange peering facilities at the
     peering location.
    :type peering_facilities:
     list[~azure.mgmt.peering.models.ExchangePeeringFacility]
    """

    _attribute_map = {
        'peering_facilities': {'key': 'peeringFacilities', 'type': '[ExchangePeeringFacility]'},
    }

    def __init__(self, **kwargs):
        super(PeeringLocationPropertiesExchange, self).__init__(**kwargs)
        self.peering_facilities = kwargs.get('peering_facilities', None)


class PeeringPropertiesDirect(Model):
    """The properties that define a direct peering.

    :param connections: The set of connections that constitute a direct
     peering.
    :type connections: list[~azure.mgmt.peering.models.DirectConnection]
    :param use_for_peering_service: The flag that indicates whether or not the
     peering is used for peering service.
    :type use_for_peering_service: bool
    :param peer_asn: The reference of the peer ASN.
    :type peer_asn: ~azure.mgmt.peering.models.SubResource
    :param direct_peering_type: The type of direct peering. Possible values
     include: 'Edge', 'Transit', 'Cdn', 'Internal'
    :type direct_peering_type: str or
     ~azure.mgmt.peering.models.DirectPeeringType
    """

    _attribute_map = {
        'connections': {'key': 'connections', 'type': '[DirectConnection]'},
        'use_for_peering_service': {'key': 'useForPeeringService', 'type': 'bool'},
        'peer_asn': {'key': 'peerAsn', 'type': 'SubResource'},
        'direct_peering_type': {'key': 'directPeeringType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringPropertiesDirect, self).__init__(**kwargs)
        self.connections = kwargs.get('connections', None)
        self.use_for_peering_service = kwargs.get('use_for_peering_service', None)
        self.peer_asn = kwargs.get('peer_asn', None)
        self.direct_peering_type = kwargs.get('direct_peering_type', None)


class PeeringPropertiesExchange(Model):
    """The properties that define an exchange peering.

    :param connections: The set of connections that constitute an exchange
     peering.
    :type connections: list[~azure.mgmt.peering.models.ExchangeConnection]
    :param peer_asn: The reference of the peer ASN.
    :type peer_asn: ~azure.mgmt.peering.models.SubResource
    """

    _attribute_map = {
        'connections': {'key': 'connections', 'type': '[ExchangeConnection]'},
        'peer_asn': {'key': 'peerAsn', 'type': 'SubResource'},
    }

    def __init__(self, **kwargs):
        super(PeeringPropertiesExchange, self).__init__(**kwargs)
        self.connections = kwargs.get('connections', None)
        self.peer_asn = kwargs.get('peer_asn', None)


class PeeringService(Resource):
    """Peering Service.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param peering_service_location: The PeeringServiceLocation of the
     Customer.
    :type peering_service_location: str
    :param peering_service_provider: The MAPS Provider Name.
    :type peering_service_provider: str
    :ivar provisioning_state: The provisioning state of the resource. Possible
     values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.peering.models.ProvisioningState
    :param location: Required. The location of the resource.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'peering_service_location': {'key': 'properties.peeringServiceLocation', 'type': 'str'},
        'peering_service_provider': {'key': 'properties.peeringServiceProvider', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(PeeringService, self).__init__(**kwargs)
        self.peering_service_location = kwargs.get('peering_service_location', None)
        self.peering_service_provider = kwargs.get('peering_service_provider', None)
        self.provisioning_state = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class PeeringServiceLocation(Resource):
    """PeeringService location.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param country: Country of the customer
    :type country: str
    :param state: State of the customer
    :type state: str
    :param azure_region: Azure region for the location
    :type azure_region: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'country': {'key': 'properties.country', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'azure_region': {'key': 'properties.azureRegion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringServiceLocation, self).__init__(**kwargs)
        self.country = kwargs.get('country', None)
        self.state = kwargs.get('state', None)
        self.azure_region = kwargs.get('azure_region', None)


class PeeringServicePrefix(Resource):
    """The peering service prefix class.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param prefix: Valid route prefix
    :type prefix: str
    :param prefix_validation_state: The prefix validation state. Possible
     values include: 'None', 'Invalid', 'Verified', 'Failed', 'Pending',
     'Unknown'
    :type prefix_validation_state: str or
     ~azure.mgmt.peering.models.PrefixValidationState
    :param learned_type: The prefix learned type. Possible values include:
     'None', 'ViaPartner', 'ViaSession'
    :type learned_type: str or ~azure.mgmt.peering.models.LearnedType
    :ivar provisioning_state: The provisioning state of the resource. Possible
     values include: 'Succeeded', 'Updating', 'Deleting', 'Failed'
    :vartype provisioning_state: str or
     ~azure.mgmt.peering.models.ProvisioningState
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'prefix': {'key': 'properties.prefix', 'type': 'str'},
        'prefix_validation_state': {'key': 'properties.prefixValidationState', 'type': 'str'},
        'learned_type': {'key': 'properties.learnedType', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringServicePrefix, self).__init__(**kwargs)
        self.prefix = kwargs.get('prefix', None)
        self.prefix_validation_state = kwargs.get('prefix_validation_state', None)
        self.learned_type = kwargs.get('learned_type', None)
        self.provisioning_state = None


class PeeringServiceProvider(Resource):
    """PeeringService provider.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param service_provider_name: The name of the service provider.
    :type service_provider_name: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'service_provider_name': {'key': 'properties.serviceProviderName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringServiceProvider, self).__init__(**kwargs)
        self.service_provider_name = kwargs.get('service_provider_name', None)


class PeeringSku(Model):
    """The SKU that defines the tier and kind of the peering.

    :param name: The name of the peering SKU. Possible values include:
     'Basic_Exchange_Free', 'Basic_Direct_Free', 'Premium_Direct_Free',
     'Premium_Exchange_Metered', 'Premium_Direct_Metered',
     'Premium_Direct_Unlimited'
    :type name: str or ~azure.mgmt.peering.models.Name
    :param tier: The tier of the peering SKU. Possible values include:
     'Basic', 'Premium'
    :type tier: str or ~azure.mgmt.peering.models.Tier
    :param family: The family of the peering SKU. Possible values include:
     'Direct', 'Exchange'
    :type family: str or ~azure.mgmt.peering.models.Family
    :param size: The size of the peering SKU. Possible values include: 'Free',
     'Metered', 'Unlimited'
    :type size: str or ~azure.mgmt.peering.models.Size
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PeeringSku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
        self.family = kwargs.get('family', None)
        self.size = kwargs.get('size', None)


class ResourceTags(Model):
    """The resource tags.

    :param tags: Gets or sets the tags, a dictionary of descriptors arm object
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ResourceTags, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class SubResource(Model):
    """The sub resource.

    :param id: The identifier of the referenced resource.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubResource, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
