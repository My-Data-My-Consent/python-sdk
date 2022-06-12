"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mydatamyconsent.model_utils import (  # noqa: F401
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
    OpenApiModel
)
from mydatamyconsent.exceptions import ApiAttributeError


def lazy_import():
    from mydatamyconsent.model.data_consent_status import DataConsentStatus
    globals()['DataConsentStatus'] = DataConsentStatus


class DataConsentDetails(ModelNormal):
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
            'request_id': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'status': (DataConsentStatus,),  # noqa: E501
            'requested_at_utc': (datetime,),  # noqa: E501
            'approved_at_utc': (datetime,),  # noqa: E501
            'data_access_expires_at_utc': (datetime,),  # noqa: E501
            'template_id': (str, none_type,),  # noqa: E501
            'purpose': (str, none_type,),  # noqa: E501
            'transaction_id': (str, none_type,),  # noqa: E501
            'revoked_at_utc': (datetime, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'request_id': 'requestId',  # noqa: E501
        'title': 'title',  # noqa: E501
        'description': 'description',  # noqa: E501
        'status': 'status',  # noqa: E501
        'requested_at_utc': 'requestedAtUtc',  # noqa: E501
        'approved_at_utc': 'approvedAtUtc',  # noqa: E501
        'data_access_expires_at_utc': 'dataAccessExpiresAtUtc',  # noqa: E501
        'template_id': 'templateId',  # noqa: E501
        'purpose': 'purpose',  # noqa: E501
        'transaction_id': 'transactionId',  # noqa: E501
        'revoked_at_utc': 'revokedAtUtc',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, request_id, title, description, status, requested_at_utc, approved_at_utc, data_access_expires_at_utc, *args, **kwargs):  # noqa: E501
        """DataConsentDetails - a model defined in OpenAPI

        Args:
            id (str): Data consent id.
            request_id (str): Consent request id.
            title (str): Consent title.
            description (str): Consent description.
            status (DataConsentStatus):
            requested_at_utc (datetime): Consent requested datetime in UTC timezone.
            approved_at_utc (datetime): Consent approval datetime in UTC timezone.
            data_access_expires_at_utc (datetime): Data access expiration datetime in UTC timezone.

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
            template_id (str, none_type): Consent template id.. [optional]  # noqa: E501
            purpose (str, none_type): Consent purpose.. [optional]  # noqa: E501
            transaction_id (str, none_type): Transaction id.. [optional]  # noqa: E501
            revoked_at_utc (datetime, none_type): Consent revocation datetime in UTC timezone.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.id = id
        self.request_id = request_id
        self.title = title
        self.description = description
        self.status = status
        self.requested_at_utc = requested_at_utc
        self.approved_at_utc = approved_at_utc
        self.data_access_expires_at_utc = data_access_expires_at_utc
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
    def __init__(self, id, request_id, title, description, status, requested_at_utc, approved_at_utc, data_access_expires_at_utc, *args, **kwargs):  # noqa: E501
        """DataConsentDetails - a model defined in OpenAPI

        Args:
            id (str): Data consent id.
            request_id (str): Consent request id.
            title (str): Consent title.
            description (str): Consent description.
            status (DataConsentStatus):
            requested_at_utc (datetime): Consent requested datetime in UTC timezone.
            approved_at_utc (datetime): Consent approval datetime in UTC timezone.
            data_access_expires_at_utc (datetime): Data access expiration datetime in UTC timezone.

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
            template_id (str, none_type): Consent template id.. [optional]  # noqa: E501
            purpose (str, none_type): Consent purpose.. [optional]  # noqa: E501
            transaction_id (str, none_type): Transaction id.. [optional]  # noqa: E501
            revoked_at_utc (datetime, none_type): Consent revocation datetime in UTC timezone.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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

        self.id = id
        self.request_id = request_id
        self.title = title
        self.description = description
        self.status = status
        self.requested_at_utc = requested_at_utc
        self.approved_at_utc = approved_at_utc
        self.data_access_expires_at_utc = data_access_expires_at_utc
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
