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


class AccessUri(Model):
    """A disk access SAS uri.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar access_sas: A SAS uri for accessing a disk.
    :vartype access_sas: str
    """

    _validation = {
        'access_sas': {'readonly': True},
    }

    _attribute_map = {
        'access_sas': {'key': 'accessSAS', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(AccessUri, self).__init__(**kwargs)
        self.access_sas = None


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class CreationData(Model):
    """Data used when creating a disk.

    All required parameters must be populated in order to send to Azure.

    :param create_option: Required. This enumerates the possible sources of a
     disk's creation. Possible values include: 'Empty', 'Attach', 'FromImage',
     'Import', 'Copy', 'Restore', 'Upload'
    :type create_option: str or
     ~azure.mgmt.compute.v2018_09_30.models.DiskCreateOption
    :param storage_account_id: If createOption is Import, the Azure Resource
     Manager identifier of the storage account containing the blob to import as
     a disk. Required only if the blob is in a different subscription
    :type storage_account_id: str
    :param image_reference: Disk source information.
    :type image_reference:
     ~azure.mgmt.compute.v2018_09_30.models.ImageDiskReference
    :param source_uri: If createOption is Import, this is the URI of a blob to
     be imported into a managed disk.
    :type source_uri: str
    :param source_resource_id: If createOption is Copy, this is the ARM id of
     the source snapshot or disk.
    :type source_resource_id: str
    """

    _validation = {
        'create_option': {'required': True},
    }

    _attribute_map = {
        'create_option': {'key': 'createOption', 'type': 'str'},
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'image_reference': {'key': 'imageReference', 'type': 'ImageDiskReference'},
        'source_uri': {'key': 'sourceUri', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
    }

    def __init__(self, *, create_option, storage_account_id: str=None, image_reference=None, source_uri: str=None, source_resource_id: str=None, **kwargs) -> None:
        super(CreationData, self).__init__(**kwargs)
        self.create_option = create_option
        self.storage_account_id = storage_account_id
        self.image_reference = image_reference
        self.source_uri = source_uri
        self.source_resource_id = source_resource_id


class Resource(Model):
    """The Resource model definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, location: str, tags=None, **kwargs) -> None:
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class Disk(Resource):
    """Disk resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar managed_by: A relative URI containing the ID of the VM that has the
     disk attached.
    :vartype managed_by: str
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_09_30.models.DiskSku
    :param zones: The Logical zone list for Disk.
    :type zones: list[str]
    :ivar time_created: The time when the disk was created.
    :vartype time_created: datetime
    :param os_type: The Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_09_30.models.OperatingSystemTypes
    :param hyper_vgeneration: The hypervisor generation of the Virtual
     Machine. Applicable to OS disks only. Possible values include: 'V1', 'V2'
    :type hyper_vgeneration: str or
     ~azure.mgmt.compute.v2018_09_30.models.HyperVGeneration
    :param creation_data: Required. Disk source information. CreationData
     information cannot be changed after the disk has been created.
    :type creation_data: ~azure.mgmt.compute.v2018_09_30.models.CreationData
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings_collection: Encryption settings collection used
     for Azure Disk Encryption, can contain multiple encryption settings per
     disk or snapshot.
    :type encryption_settings_collection:
     ~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsCollection
    :ivar provisioning_state: The disk provisioning state.
    :vartype provisioning_state: str
    :param disk_iops_read_write: The number of IOPS allowed for this disk;
     only settable for UltraSSD disks. One operation can transfer between 4k
     and 256k bytes.
    :type disk_iops_read_write: long
    :param disk_mbps_read_write: The bandwidth allowed for this disk; only
     settable for UltraSSD disks. MBps means millions of bytes per second - MB
     here uses the ISO notation, of powers of 10.
    :type disk_mbps_read_write: int
    :ivar disk_state: The state of the disk. Possible values include:
     'Unattached', 'Attached', 'Reserved', 'ActiveSAS', 'ReadyToUpload',
     'ActiveUpload'
    :vartype disk_state: str or
     ~azure.mgmt.compute.v2018_09_30.models.DiskState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_by': {'readonly': True},
        'time_created': {'readonly': True},
        'creation_data': {'required': True},
        'provisioning_state': {'readonly': True},
        'disk_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'DiskSku'},
        'zones': {'key': 'zones', 'type': '[str]'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'hyper_vgeneration': {'key': 'properties.hyperVGeneration', 'type': 'str'},
        'creation_data': {'key': 'properties.creationData', 'type': 'CreationData'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings_collection': {'key': 'properties.encryptionSettingsCollection', 'type': 'EncryptionSettingsCollection'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'disk_iops_read_write': {'key': 'properties.diskIOPSReadWrite', 'type': 'long'},
        'disk_mbps_read_write': {'key': 'properties.diskMBpsReadWrite', 'type': 'int'},
        'disk_state': {'key': 'properties.diskState', 'type': 'str'},
    }

    def __init__(self, *, location: str, creation_data, tags=None, sku=None, zones=None, os_type=None, hyper_vgeneration=None, disk_size_gb: int=None, encryption_settings_collection=None, disk_iops_read_write: int=None, disk_mbps_read_write: int=None, **kwargs) -> None:
        super(Disk, self).__init__(location=location, tags=tags, **kwargs)
        self.managed_by = None
        self.sku = sku
        self.zones = zones
        self.time_created = None
        self.os_type = os_type
        self.hyper_vgeneration = hyper_vgeneration
        self.creation_data = creation_data
        self.disk_size_gb = disk_size_gb
        self.encryption_settings_collection = encryption_settings_collection
        self.provisioning_state = None
        self.disk_iops_read_write = disk_iops_read_write
        self.disk_mbps_read_write = disk_mbps_read_write
        self.disk_state = None


class DiskSku(Model):
    """The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, or
    UltraSSD_LRS.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The sku name. Possible values include: 'Standard_LRS',
     'Premium_LRS', 'StandardSSD_LRS', 'UltraSSD_LRS'
    :type name: str or
     ~azure.mgmt.compute.v2018_09_30.models.DiskStorageAccountTypes
    :ivar tier: The sku tier. Default value: "Standard" .
    :vartype tier: str
    """

    _validation = {
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name=None, **kwargs) -> None:
        super(DiskSku, self).__init__(**kwargs)
        self.name = name
        self.tier = None


class DiskUpdate(Model):
    """Disk update resource.

    :param os_type: the Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_09_30.models.OperatingSystemTypes
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings_collection: Encryption settings collection used
     be Azure Disk Encryption, can contain multiple encryption settings per
     disk or snapshot.
    :type encryption_settings_collection:
     ~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsCollection
    :param disk_iops_read_write: The number of IOPS allowed for this disk;
     only settable for UltraSSD disks. One operation can transfer between 4k
     and 256k bytes.
    :type disk_iops_read_write: long
    :param disk_mbps_read_write: The bandwidth allowed for this disk; only
     settable for UltraSSD disks. MBps means millions of bytes per second - MB
     here uses the ISO notation, of powers of 10.
    :type disk_mbps_read_write: int
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_09_30.models.DiskSku
    """

    _attribute_map = {
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings_collection': {'key': 'properties.encryptionSettingsCollection', 'type': 'EncryptionSettingsCollection'},
        'disk_iops_read_write': {'key': 'properties.diskIOPSReadWrite', 'type': 'long'},
        'disk_mbps_read_write': {'key': 'properties.diskMBpsReadWrite', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'DiskSku'},
    }

    def __init__(self, *, os_type=None, disk_size_gb: int=None, encryption_settings_collection=None, disk_iops_read_write: int=None, disk_mbps_read_write: int=None, tags=None, sku=None, **kwargs) -> None:
        super(DiskUpdate, self).__init__(**kwargs)
        self.os_type = os_type
        self.disk_size_gb = disk_size_gb
        self.encryption_settings_collection = encryption_settings_collection
        self.disk_iops_read_write = disk_iops_read_write
        self.disk_mbps_read_write = disk_mbps_read_write
        self.tags = tags
        self.sku = sku


class EncryptionSettingsCollection(Model):
    """Encryption settings for disk or snapshot.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Set this flag to true and provide
     DiskEncryptionKey and optional KeyEncryptionKey to enable encryption. Set
     this flag to false and remove DiskEncryptionKey and KeyEncryptionKey to
     disable encryption. If EncryptionSettings is null in the request object,
     the existing settings remain unchanged.
    :type enabled: bool
    :param encryption_settings: A collection of encryption settings, one for
     each disk volume.
    :type encryption_settings:
     list[~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsElement]
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'encryption_settings': {'key': 'encryptionSettings', 'type': '[EncryptionSettingsElement]'},
    }

    def __init__(self, *, enabled: bool, encryption_settings=None, **kwargs) -> None:
        super(EncryptionSettingsCollection, self).__init__(**kwargs)
        self.enabled = enabled
        self.encryption_settings = encryption_settings


class EncryptionSettingsElement(Model):
    """Encryption settings for one disk volume.

    :param disk_encryption_key: Key Vault Secret Url and vault id of the disk
     encryption key
    :type disk_encryption_key:
     ~azure.mgmt.compute.v2018_09_30.models.KeyVaultAndSecretReference
    :param key_encryption_key: Key Vault Key Url and vault id of the key
     encryption key. KeyEncryptionKey is optional and when provided is used to
     unwrap the disk encryption key.
    :type key_encryption_key:
     ~azure.mgmt.compute.v2018_09_30.models.KeyVaultAndKeyReference
    """

    _attribute_map = {
        'disk_encryption_key': {'key': 'diskEncryptionKey', 'type': 'KeyVaultAndSecretReference'},
        'key_encryption_key': {'key': 'keyEncryptionKey', 'type': 'KeyVaultAndKeyReference'},
    }

    def __init__(self, *, disk_encryption_key=None, key_encryption_key=None, **kwargs) -> None:
        super(EncryptionSettingsElement, self).__init__(**kwargs)
        self.disk_encryption_key = disk_encryption_key
        self.key_encryption_key = key_encryption_key


class GrantAccessData(Model):
    """Data used for requesting a SAS.

    All required parameters must be populated in order to send to Azure.

    :param access: Required. Possible values include: 'None', 'Read', 'Write'
    :type access: str or ~azure.mgmt.compute.v2018_09_30.models.AccessLevel
    :param duration_in_seconds: Required. Time duration in seconds until the
     SAS access expires.
    :type duration_in_seconds: int
    """

    _validation = {
        'access': {'required': True},
        'duration_in_seconds': {'required': True},
    }

    _attribute_map = {
        'access': {'key': 'access', 'type': 'str'},
        'duration_in_seconds': {'key': 'durationInSeconds', 'type': 'int'},
    }

    def __init__(self, *, access, duration_in_seconds: int, **kwargs) -> None:
        super(GrantAccessData, self).__init__(**kwargs)
        self.access = access
        self.duration_in_seconds = duration_in_seconds


class ImageDiskReference(Model):
    """The source image used for creating the disk.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. A relative uri containing either a Platform Image
     Repository or user image reference.
    :type id: str
    :param lun: If the disk is created from an image's data disk, this is an
     index that indicates which of the data disks in the image to use. For OS
     disks, this field is null.
    :type lun: int
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'lun': {'key': 'lun', 'type': 'int'},
    }

    def __init__(self, *, id: str, lun: int=None, **kwargs) -> None:
        super(ImageDiskReference, self).__init__(**kwargs)
        self.id = id
        self.lun = lun


class KeyVaultAndKeyReference(Model):
    """Key Vault Key Url and vault id of KeK, KeK is optional and when provided is
    used to unwrap the encryptionKey.

    All required parameters must be populated in order to send to Azure.

    :param source_vault: Required. Resource id of the KeyVault containing the
     key or secret
    :type source_vault: ~azure.mgmt.compute.v2018_09_30.models.SourceVault
    :param key_url: Required. Url pointing to a key or secret in KeyVault
    :type key_url: str
    """

    _validation = {
        'source_vault': {'required': True},
        'key_url': {'required': True},
    }

    _attribute_map = {
        'source_vault': {'key': 'sourceVault', 'type': 'SourceVault'},
        'key_url': {'key': 'keyUrl', 'type': 'str'},
    }

    def __init__(self, *, source_vault, key_url: str, **kwargs) -> None:
        super(KeyVaultAndKeyReference, self).__init__(**kwargs)
        self.source_vault = source_vault
        self.key_url = key_url


class KeyVaultAndSecretReference(Model):
    """Key Vault Secret Url and vault id of the encryption key .

    All required parameters must be populated in order to send to Azure.

    :param source_vault: Required. Resource id of the KeyVault containing the
     key or secret
    :type source_vault: ~azure.mgmt.compute.v2018_09_30.models.SourceVault
    :param secret_url: Required. Url pointing to a key or secret in KeyVault
    :type secret_url: str
    """

    _validation = {
        'source_vault': {'required': True},
        'secret_url': {'required': True},
    }

    _attribute_map = {
        'source_vault': {'key': 'sourceVault', 'type': 'SourceVault'},
        'secret_url': {'key': 'secretUrl', 'type': 'str'},
    }

    def __init__(self, *, source_vault, secret_url: str, **kwargs) -> None:
        super(KeyVaultAndSecretReference, self).__init__(**kwargs)
        self.source_vault = source_vault
        self.secret_url = secret_url


class Snapshot(Resource):
    """Snapshot resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Required. Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :ivar managed_by: Unused. Always Null.
    :vartype managed_by: str
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_09_30.models.SnapshotSku
    :ivar time_created: The time when the disk was created.
    :vartype time_created: datetime
    :param os_type: The Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_09_30.models.OperatingSystemTypes
    :param hyper_vgeneration: The hypervisor generation of the Virtual
     Machine. Applicable to OS disks only. Possible values include: 'V1', 'V2'
    :type hyper_vgeneration: str or
     ~azure.mgmt.compute.v2018_09_30.models.HyperVGeneration
    :param creation_data: Required. Disk source information. CreationData
     information cannot be changed after the disk has been created.
    :type creation_data: ~azure.mgmt.compute.v2018_09_30.models.CreationData
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings_collection: Encryption settings collection used
     be Azure Disk Encryption, can contain multiple encryption settings per
     disk or snapshot.
    :type encryption_settings_collection:
     ~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsCollection
    :ivar provisioning_state: The disk provisioning state.
    :vartype provisioning_state: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'managed_by': {'readonly': True},
        'time_created': {'readonly': True},
        'creation_data': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'SnapshotSku'},
        'time_created': {'key': 'properties.timeCreated', 'type': 'iso-8601'},
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'hyper_vgeneration': {'key': 'properties.hyperVGeneration', 'type': 'str'},
        'creation_data': {'key': 'properties.creationData', 'type': 'CreationData'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings_collection': {'key': 'properties.encryptionSettingsCollection', 'type': 'EncryptionSettingsCollection'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, location: str, creation_data, tags=None, sku=None, os_type=None, hyper_vgeneration=None, disk_size_gb: int=None, encryption_settings_collection=None, **kwargs) -> None:
        super(Snapshot, self).__init__(location=location, tags=tags, **kwargs)
        self.managed_by = None
        self.sku = sku
        self.time_created = None
        self.os_type = os_type
        self.hyper_vgeneration = hyper_vgeneration
        self.creation_data = creation_data
        self.disk_size_gb = disk_size_gb
        self.encryption_settings_collection = encryption_settings_collection
        self.provisioning_state = None


class SnapshotSku(Model):
    """The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: The sku name. Possible values include: 'Standard_LRS',
     'Premium_LRS', 'Standard_ZRS'
    :type name: str or
     ~azure.mgmt.compute.v2018_09_30.models.SnapshotStorageAccountTypes
    :ivar tier: The sku tier. Default value: "Standard" .
    :vartype tier: str
    """

    _validation = {
        'tier': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, *, name=None, **kwargs) -> None:
        super(SnapshotSku, self).__init__(**kwargs)
        self.name = name
        self.tier = None


class SnapshotUpdate(Model):
    """Snapshot update resource.

    :param os_type: the Operating System type. Possible values include:
     'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_09_30.models.OperatingSystemTypes
    :param disk_size_gb: If creationData.createOption is Empty, this field is
     mandatory and it indicates the size of the VHD to create. If this field is
     present for updates or creation with other options, it indicates a resize.
     Resizes are only allowed if the disk is not attached to a running VM, and
     can only increase the disk's size.
    :type disk_size_gb: int
    :param encryption_settings_collection: Encryption settings collection used
     be Azure Disk Encryption, can contain multiple encryption settings per
     disk or snapshot.
    :type encryption_settings_collection:
     ~azure.mgmt.compute.v2018_09_30.models.EncryptionSettingsCollection
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku:
    :type sku: ~azure.mgmt.compute.v2018_09_30.models.SnapshotSku
    """

    _attribute_map = {
        'os_type': {'key': 'properties.osType', 'type': 'OperatingSystemTypes'},
        'disk_size_gb': {'key': 'properties.diskSizeGB', 'type': 'int'},
        'encryption_settings_collection': {'key': 'properties.encryptionSettingsCollection', 'type': 'EncryptionSettingsCollection'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'SnapshotSku'},
    }

    def __init__(self, *, os_type=None, disk_size_gb: int=None, encryption_settings_collection=None, tags=None, sku=None, **kwargs) -> None:
        super(SnapshotUpdate, self).__init__(**kwargs)
        self.os_type = os_type
        self.disk_size_gb = disk_size_gb
        self.encryption_settings_collection = encryption_settings_collection
        self.tags = tags
        self.sku = sku


class SourceVault(Model):
    """The vault id is an Azure Resource Manager Resource id in the form
    /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.KeyVault/vaults/{vaultName}.

    :param id: Resource Id
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(SourceVault, self).__init__(**kwargs)
        self.id = id
