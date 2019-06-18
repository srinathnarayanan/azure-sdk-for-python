# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import map_error

from ... import models


class ShareOperations:
    """ShareOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar restype: . Constant value: "share".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.restype = "share"

    async def create(self, timeout=None, metadata=None, quota=None, *, cls=None, **kwargs):
        """Creates a new share under the specified account. If the share with the
        same name already exists, the operation fails.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param metadata: A name-value pair to associate with a file storage
         object.
        :type metadata: str
        :param quota: Specifies the maximum size of the share, in gigabytes.
        :type quota: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')

        # Construct headers
        header_parameters = {}
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        if quota is not None:
            header_parameters['x-ms-share-quota'] = self._serialize.header("quota", quota, 'int', minimum=1)
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    create.metadata = {'url': '/{shareName}'}

    async def get_properties(self, sharesnapshot=None, timeout=None, *, cls=None, **kwargs):
        """Returns all user-defined metadata and system properties for the
        specified share or share snapshot. The data returned does not include
        the share's list of files.

        :param sharesnapshot: The snapshot parameter is an opaque DateTime
         value that, when present, specifies the share snapshot to query.
        :type sharesnapshot: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_properties.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sharesnapshot is not None:
            query_parameters['sharesnapshot'] = self._serialize.query("sharesnapshot", sharesnapshot, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-meta': self._deserialize('{str}', response.headers.get('x-ms-meta')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-share-quota': self._deserialize('int', response.headers.get('x-ms-share-quota')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    get_properties.metadata = {'url': '/{shareName}'}

    async def delete(self, sharesnapshot=None, timeout=None, delete_snapshots=None, *, cls=None, **kwargs):
        """Operation marks the specified share or share snapshot for deletion. The
        share or share snapshot and any files contained within it are later
        deleted during garbage collection.

        :param sharesnapshot: The snapshot parameter is an opaque DateTime
         value that, when present, specifies the share snapshot to query.
        :type sharesnapshot: str
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param delete_snapshots: Specifies the option include to delete the
         base share and all of its snapshots. Possible values include:
         'include'
        :type delete_snapshots: str or ~file.models.DeleteSnapshotsOptionType
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if sharesnapshot is not None:
            query_parameters['sharesnapshot'] = self._serialize.query("sharesnapshot", sharesnapshot, 'str')
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if delete_snapshots is not None:
            header_parameters['x-ms-delete-snapshots'] = self._serialize.header("delete_snapshots", delete_snapshots, 'DeleteSnapshotsOptionType')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    delete.metadata = {'url': '/{shareName}'}

    async def create_snapshot(self, timeout=None, metadata=None, *, cls=None, **kwargs):
        """Creates a read-only snapshot of a share.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param metadata: A name-value pair to associate with a file storage
         object.
        :type metadata: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "snapshot"

        # Construct URL
        url = self.create_snapshot.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'x-ms-snapshot': self._deserialize('str', response.headers.get('x-ms-snapshot')),
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    create_snapshot.metadata = {'url': '/{shareName}'}

    async def set_quota(self, timeout=None, quota=None, *, cls=None, **kwargs):
        """Sets quota for the specified share.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param quota: Specifies the maximum size of the share, in gigabytes.
        :type quota: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "properties"

        # Construct URL
        url = self.set_quota.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')
        if quota is not None:
            header_parameters['x-ms-share-quota'] = self._serialize.header("quota", quota, 'int', minimum=1)

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_quota.metadata = {'url': '/{shareName}'}

    async def set_metadata(self, timeout=None, metadata=None, *, cls=None, **kwargs):
        """Sets one or more user-defined name-value pairs for the specified share.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param metadata: A name-value pair to associate with a file storage
         object.
        :type metadata: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "metadata"

        # Construct URL
        url = self.set_metadata.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        if metadata is not None:
            header_parameters['x-ms-meta'] = self._serialize.header("metadata", metadata, 'str')
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_metadata.metadata = {'url': '/{shareName}'}

    async def get_access_policy(self, timeout=None, *, cls=None, **kwargs):
        """Returns information about stored access policies specified on the
        share.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: list or the result of cls(response)
        :rtype: list[~file.models.SignedIdentifier]
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "acl"

        # Construct URL
        url = self.get_access_policy.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('[SignedIdentifier]', response)
            header_dict = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    get_access_policy.metadata = {'url': '/{shareName}'}

    async def set_access_policy(self, share_acl=None, timeout=None, *, cls=None, **kwargs):
        """Sets a stored access policy for use with shared access signatures.

        :param share_acl: The ACL for the share.
        :type share_acl: list[~file.models.SignedIdentifier]
        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "acl"

        # Construct URL
        url = self.set_access_policy.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/xml; charset=utf-8'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct body
        if share_acl is not None:
            body_content = self._serialize.body(share_acl, '[SignedIdentifier]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        if cls:
            response_headers = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }
            return cls(response, None, response_headers)
    set_access_policy.metadata = {'url': '/{shareName}'}

    async def get_statistics(self, timeout=None, *, cls=None, **kwargs):
        """Retrieves statistics related to the share.

        :param timeout: The timeout parameter is expressed in seconds. For
         more information, see <a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>
        :type timeout: int
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: ShareStats or the result of cls(response)
        :rtype: ~file.models.ShareStats
        :raises:
         :class:`StorageErrorException<file.models.StorageErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        comp = "stats"

        # Construct URL
        url = self.get_statistics.metadata['url']
        path_format_arguments = {
            'url': self._serialize.url("self._config.url", self._config.url, 'str', skip_quote=True)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if timeout is not None:
            query_parameters['timeout'] = self._serialize.query("timeout", timeout, 'int', minimum=0)
        query_parameters['restype'] = self._serialize.query("self.restype", self.restype, 'str')
        query_parameters['comp'] = self._serialize.query("comp", comp, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/xml'
        header_parameters['x-ms-version'] = self._serialize.header("self._config.version", self._config.version, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.StorageErrorException(response, self._deserialize)

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ShareStats', response)
            header_dict = {
                'ETag': self._deserialize('str', response.headers.get('ETag')),
                'Last-Modified': self._deserialize('rfc-1123', response.headers.get('Last-Modified')),
                'x-ms-request-id': self._deserialize('str', response.headers.get('x-ms-request-id')),
                'x-ms-version': self._deserialize('str', response.headers.get('x-ms-version')),
                'Date': self._deserialize('rfc-1123', response.headers.get('Date')),
                'x-ms-error-code': self._deserialize('str', response.headers.get('x-ms-error-code')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    get_statistics.metadata = {'url': '/{shareName}'}
