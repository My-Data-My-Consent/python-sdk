"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from com.mydatamyconsent.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from com.mydatamyconsent.exceptions import ApiAttributeError


def lazy_import():
    from com.mydatamyconsent.model.data_consent_requested_account_dto import DataConsentRequestedAccountDto
    from com.mydatamyconsent.model.data_consent_requested_document import DataConsentRequestedDocument
    from com.mydatamyconsent.model.data_consent_requested_document_dto import DataConsentRequestedDocumentDto
    from com.mydatamyconsent.model.data_consent_requester_dto import DataConsentRequesterDto
    from com.mydatamyconsent.model.data_consent_status import DataConsentStatus
    from com.mydatamyconsent.model.data_fetch_frequency_unit import DataFetchFrequencyUnit
    from com.mydatamyconsent.model.data_fetch_type import DataFetchType
    from com.mydatamyconsent.model.data_life_unit import DataLifeUnit
    from com.mydatamyconsent.model.json_schema import JsonSchema
    globals()['DataConsentRequestedAccountDto'] = DataConsentRequestedAccountDto
    globals()['DataConsentRequestedDocument'] = DataConsentRequestedDocument
    globals()['DataConsentRequestedDocumentDto'] = DataConsentRequestedDocumentDto
    globals()['DataConsentRequesterDto'] = DataConsentRequesterDto
    globals()['DataConsentStatus'] = DataConsentStatus
    globals()['DataFetchFrequencyUnit'] = DataFetchFrequencyUnit
    globals()['DataFetchType'] = DataFetchType
    globals()['DataLifeUnit'] = DataLifeUnit
    globals()['JsonSchema'] = JsonSchema


class DataConsentDetailsDto(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'requester': (DataConsentRequesterDto,),  # noqa: E501
            'location': (str, none_type,),  # noqa: E501
            'personal_info_requested': (bool,),  # noqa: E501
            'documents': (int,),  # noqa: E501
            'financial_accounts': (int,),  # noqa: E501
            'transaction_id': (str, none_type,),  # noqa: E501
            'ip_address': (str, none_type,),  # noqa: E501
            'description': (str, none_type,),  # noqa: E501
            'purpose_code': (str, none_type,),  # noqa: E501
            'purpose_link': (str, none_type,),  # noqa: E501
            'agreement_id': (str, none_type,),  # noqa: E501
            'data_life_unit': (DataLifeUnit,),  # noqa: E501
            'data_life_value': (int,),  # noqa: E501
            'data_fetch_frequency_unit': (DataFetchFrequencyUnit,),  # noqa: E501
            'data_fetch_frequency_unit_value': (int,),  # noqa: E501
            'data_fetch_type': (DataFetchType,),  # noqa: E501
            'status': (DataConsentStatus,),  # noqa: E501
            'approved_at_utc': (datetime, none_type,),  # noqa: E501
            'rejected_at_utc': (datetime, none_type,),  # noqa: E501
            'expires_at_utc': (datetime,),  # noqa: E501
            'requested_at_utc': (datetime,),  # noqa: E501
            'requested_financial_accounts': ([DataConsentRequestedAccountDto], none_type,),  # noqa: E501
            'requested_documents': ([DataConsentRequestedDocumentDto], none_type,),  # noqa: E501
            'requested_health_data': ([DataConsentRequestedDocument], none_type,),  # noqa: E501
            'requested_identity_details': (JsonSchema,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'requester': 'requester',  # noqa: E501
        'location': 'location',  # noqa: E501
        'personal_info_requested': 'personalInfoRequested',  # noqa: E501
        'documents': 'documents',  # noqa: E501
        'financial_accounts': 'financialAccounts',  # noqa: E501
        'transaction_id': 'transactionId',  # noqa: E501
        'ip_address': 'ipAddress',  # noqa: E501
        'description': 'description',  # noqa: E501
        'purpose_code': 'purposeCode',  # noqa: E501
        'purpose_link': 'purposeLink',  # noqa: E501
        'agreement_id': 'agreementId',  # noqa: E501
        'data_life_unit': 'dataLifeUnit',  # noqa: E501
        'data_life_value': 'dataLifeValue',  # noqa: E501
        'data_fetch_frequency_unit': 'dataFetchFrequencyUnit',  # noqa: E501
        'data_fetch_frequency_unit_value': 'dataFetchFrequencyUnitValue',  # noqa: E501
        'data_fetch_type': 'dataFetchType',  # noqa: E501
        'status': 'status',  # noqa: E501
        'approved_at_utc': 'approvedAtUtc',  # noqa: E501
        'rejected_at_utc': 'rejectedAtUtc',  # noqa: E501
        'expires_at_utc': 'expiresAtUtc',  # noqa: E501
        'requested_at_utc': 'requestedAtUtc',  # noqa: E501
        'requested_financial_accounts': 'requestedFinancialAccounts',  # noqa: E501
        'requested_documents': 'requestedDocuments',  # noqa: E501
        'requested_health_data': 'requestedHealthData',  # noqa: E501
        'requested_identity_details': 'requestedIdentityDetails',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """DataConsentDetailsDto - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            requester (DataConsentRequesterDto): [optional]  # noqa: E501
            location (str, none_type): [optional]  # noqa: E501
            personal_info_requested (bool): [optional]  # noqa: E501
            documents (int): [optional]  # noqa: E501
            financial_accounts (int): [optional]  # noqa: E501
            transaction_id (str, none_type): [optional]  # noqa: E501
            ip_address (str, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            purpose_code (str, none_type): [optional]  # noqa: E501
            purpose_link (str, none_type): [optional]  # noqa: E501
            agreement_id (str, none_type): [optional]  # noqa: E501
            data_life_unit (DataLifeUnit): [optional]  # noqa: E501
            data_life_value (int): [optional]  # noqa: E501
            data_fetch_frequency_unit (DataFetchFrequencyUnit): [optional]  # noqa: E501
            data_fetch_frequency_unit_value (int): [optional]  # noqa: E501
            data_fetch_type (DataFetchType): [optional]  # noqa: E501
            status (DataConsentStatus): [optional]  # noqa: E501
            approved_at_utc (datetime, none_type): [optional]  # noqa: E501
            rejected_at_utc (datetime, none_type): [optional]  # noqa: E501
            expires_at_utc (datetime): [optional]  # noqa: E501
            requested_at_utc (datetime): [optional]  # noqa: E501
            requested_financial_accounts ([DataConsentRequestedAccountDto], none_type): [optional]  # noqa: E501
            requested_documents ([DataConsentRequestedDocumentDto], none_type): [optional]  # noqa: E501
            requested_health_data ([DataConsentRequestedDocument], none_type): [optional]  # noqa: E501
            requested_identity_details (JsonSchema): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """DataConsentDetailsDto - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            requester (DataConsentRequesterDto): [optional]  # noqa: E501
            location (str, none_type): [optional]  # noqa: E501
            personal_info_requested (bool): [optional]  # noqa: E501
            documents (int): [optional]  # noqa: E501
            financial_accounts (int): [optional]  # noqa: E501
            transaction_id (str, none_type): [optional]  # noqa: E501
            ip_address (str, none_type): [optional]  # noqa: E501
            description (str, none_type): [optional]  # noqa: E501
            purpose_code (str, none_type): [optional]  # noqa: E501
            purpose_link (str, none_type): [optional]  # noqa: E501
            agreement_id (str, none_type): [optional]  # noqa: E501
            data_life_unit (DataLifeUnit): [optional]  # noqa: E501
            data_life_value (int): [optional]  # noqa: E501
            data_fetch_frequency_unit (DataFetchFrequencyUnit): [optional]  # noqa: E501
            data_fetch_frequency_unit_value (int): [optional]  # noqa: E501
            data_fetch_type (DataFetchType): [optional]  # noqa: E501
            status (DataConsentStatus): [optional]  # noqa: E501
            approved_at_utc (datetime, none_type): [optional]  # noqa: E501
            rejected_at_utc (datetime, none_type): [optional]  # noqa: E501
            expires_at_utc (datetime): [optional]  # noqa: E501
            requested_at_utc (datetime): [optional]  # noqa: E501
            requested_financial_accounts ([DataConsentRequestedAccountDto], none_type): [optional]  # noqa: E501
            requested_documents ([DataConsentRequestedDocumentDto], none_type): [optional]  # noqa: E501
            requested_health_data ([DataConsentRequestedDocument], none_type): [optional]  # noqa: E501
            requested_identity_details (JsonSchema): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
