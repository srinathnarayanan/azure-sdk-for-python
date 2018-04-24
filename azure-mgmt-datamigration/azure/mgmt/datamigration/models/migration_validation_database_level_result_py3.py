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


class MigrationValidationDatabaseLevelResult(Model):
    """Database level validation results.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Result identifier
    :vartype id: str
    :ivar migration_id: Migration Identifier
    :vartype migration_id: str
    :ivar source_database_name: Name of the source database
    :vartype source_database_name: str
    :ivar target_database_name: Name of the target database
    :vartype target_database_name: str
    :ivar started_on: Validation start time
    :vartype started_on: datetime
    :ivar ended_on: Validation end time
    :vartype ended_on: datetime
    :ivar data_integrity_validation_result: Provides data integrity validation
     result between the source and target tables that are migrated.
    :vartype data_integrity_validation_result:
     ~azure.mgmt.datamigration.models.DataIntegrityValidationResult
    :ivar schema_validation_result: Provides schema comparison result between
     source and target database
    :vartype schema_validation_result:
     ~azure.mgmt.datamigration.models.SchemaComparisonValidationResult
    :ivar query_analysis_validation_result: Results of some of the query
     execution result between source and target database
    :vartype query_analysis_validation_result:
     ~azure.mgmt.datamigration.models.QueryAnalysisValidationResult
    :ivar status: Current status of validation at the database level. Possible
     values include: 'Default', 'NotStarted', 'Initialized', 'InProgress',
     'Completed', 'CompletedWithIssues', 'Failed', 'Stopped'
    :vartype status: str or ~azure.mgmt.datamigration.models.ValidationStatus
    """

    _validation = {
        'id': {'readonly': True},
        'migration_id': {'readonly': True},
        'source_database_name': {'readonly': True},
        'target_database_name': {'readonly': True},
        'started_on': {'readonly': True},
        'ended_on': {'readonly': True},
        'data_integrity_validation_result': {'readonly': True},
        'schema_validation_result': {'readonly': True},
        'query_analysis_validation_result': {'readonly': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'migration_id': {'key': 'migrationId', 'type': 'str'},
        'source_database_name': {'key': 'sourceDatabaseName', 'type': 'str'},
        'target_database_name': {'key': 'targetDatabaseName', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'ended_on': {'key': 'endedOn', 'type': 'iso-8601'},
        'data_integrity_validation_result': {'key': 'dataIntegrityValidationResult', 'type': 'DataIntegrityValidationResult'},
        'schema_validation_result': {'key': 'schemaValidationResult', 'type': 'SchemaComparisonValidationResult'},
        'query_analysis_validation_result': {'key': 'queryAnalysisValidationResult', 'type': 'QueryAnalysisValidationResult'},
        'status': {'key': 'status', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(MigrationValidationDatabaseLevelResult, self).__init__(**kwargs)
        self.id = None
        self.migration_id = None
        self.source_database_name = None
        self.target_database_name = None
        self.started_on = None
        self.ended_on = None
        self.data_integrity_validation_result = None
        self.schema_validation_result = None
        self.query_analysis_validation_result = None
        self.status = None