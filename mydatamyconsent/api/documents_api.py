"""
    My Data My Consent - Developer API

    Unleashing the power of data consent by establishing trust. The Platform Core Developer API defines a set of capabilities that can be used to request, issue, manage and update data, documents and credentials by organizations. The API can be used to request, manage and update Decentralised Identifiers, Financial Data, Health Data issue Documents, Credentials directly or using OpenID Connect flows, and verify Messages signed with DIDs and much more.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@mydatamyconsent.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from mydatamyconsent.api_client import ApiClient, Endpoint as _Endpoint
from mydatamyconsent.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from mydatamyconsent.model.document_issue_request import DocumentIssueRequest
from mydatamyconsent.model.document_issue_request_details import DocumentIssueRequestDetails
from mydatamyconsent.model.document_type_paginated_list import DocumentTypePaginatedList
from mydatamyconsent.model.error import Error
from mydatamyconsent.model.issued_document_details import IssuedDocumentDetails
from mydatamyconsent.model.issued_document_paginated_list import IssuedDocumentPaginatedList
from mydatamyconsent.model.problem_details import ProblemDetails
from mydatamyconsent.model.supported_entity_type import SupportedEntityType


class DocumentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_issued_document_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (IssuedDocumentDetails,),
                'auth': [],
                'endpoint_path': '/v1/documents/issued/{documentId}',
                'operation_id': 'get_issued_document_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_id',
                ],
                'required': [
                    'document_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_id':
                        (str,),
                },
                'attribute_map': {
                    'document_id': 'documentId',
                },
                'location_map': {
                    'document_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_issued_documents_endpoint = _Endpoint(
            settings={
                'response_type': (IssuedDocumentPaginatedList,),
                'auth': [],
                'endpoint_path': '/v1/documents/issued',
                'operation_id': 'get_issued_documents',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_type_id',
                    'from_date_time',
                    'to_date_time',
                    'page_no',
                    'page_size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_type_id':
                        (str,),
                    'from_date_time':
                        (datetime,),
                    'to_date_time':
                        (datetime,),
                    'page_no':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'document_type_id': 'documentTypeId',
                    'from_date_time': 'fromDateTime',
                    'to_date_time': 'toDateTime',
                    'page_no': 'pageNo',
                    'page_size': 'pageSize',
                },
                'location_map': {
                    'document_type_id': 'query',
                    'from_date_time': 'query',
                    'to_date_time': 'query',
                    'page_no': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_registered_document_types_endpoint = _Endpoint(
            settings={
                'response_type': (DocumentTypePaginatedList,),
                'auth': [],
                'endpoint_path': '/v1/documents/types',
                'operation_id': 'get_registered_document_types',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'supported_entity_type',
                    'page_no',
                    'page_size',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'supported_entity_type':
                        (SupportedEntityType,),
                    'page_no':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'supported_entity_type': 'supportedEntityType',
                    'page_no': 'pageNo',
                    'page_size': 'pageSize',
                },
                'location_map': {
                    'supported_entity_type': 'query',
                    'page_no': 'query',
                    'page_size': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.issue_document_to_individual_endpoint = _Endpoint(
            settings={
                'response_type': (DocumentIssueRequestDetails,),
                'auth': [],
                'endpoint_path': '/v1/documents/issue/individual',
                'operation_id': 'issue_document_to_individual',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_issue_request',
                ],
                'required': [
                    'document_issue_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_issue_request':
                        (DocumentIssueRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'document_issue_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.issue_document_to_organization_endpoint = _Endpoint(
            settings={
                'response_type': (DocumentIssueRequestDetails,),
                'auth': [],
                'endpoint_path': '/v1/documents/issue/organization',
                'operation_id': 'issue_document_to_organization',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'document_issue_request',
                ],
                'required': [
                    'document_issue_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'document_issue_request':
                        (DocumentIssueRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'document_issue_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.upload_document_for_individual_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/documents/issue/individual/upload/{issueRequestId}',
                'operation_id': 'upload_document_for_individual',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'issue_request_id',
                    'form_file',
                ],
                'required': [
                    'issue_request_id',
                    'form_file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'issue_request_id':
                        (str,),
                    'form_file':
                        (file_type,),
                },
                'attribute_map': {
                    'issue_request_id': 'issueRequestId',
                    'form_file': 'formFile',
                },
                'location_map': {
                    'issue_request_id': 'path',
                    'form_file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.upload_document_for_organization_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/v1/documents/issue/organization/upload/{issueRequestId}',
                'operation_id': 'upload_document_for_organization',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'issue_request_id',
                    'form_file',
                ],
                'required': [
                    'issue_request_id',
                    'form_file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'issue_request_id':
                        (str,),
                    'form_file':
                        (file_type,),
                },
                'attribute_map': {
                    'issue_request_id': 'issueRequestId',
                    'form_file': 'formFile',
                },
                'location_map': {
                    'issue_request_id': 'path',
                    'form_file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def get_issued_document_by_id(
        self,
        document_id,
        **kwargs
    ):
        """Get issued document.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_issued_document_by_id(document_id, async_req=True)
        >>> result = thread.get()

        Args:
            document_id (str): Document id.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            IssuedDocumentDetails
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['document_id'] = \
            document_id
        return self.get_issued_document_by_id_endpoint.call_with_http_info(**kwargs)

    def get_issued_documents(
        self,
        **kwargs
    ):
        """Get paginated list of issued documents of given document type.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_issued_documents(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            document_type_id (str): Document type id.. [optional]
            from_date_time (datetime): From DateTime in UTC timezone.. [optional]
            to_date_time (datetime): To DateTime in UTC timezone.. [optional]
            page_no (int): Page number.. [optional] if omitted the server will use the default value of 1
            page_size (int): Number of items to return.. [optional] if omitted the server will use the default value of 25
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            IssuedDocumentPaginatedList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_issued_documents_endpoint.call_with_http_info(**kwargs)

    def get_registered_document_types(
        self,
        **kwargs
    ):
        """Get paginated list of registered document types.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_registered_document_types(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            supported_entity_type (SupportedEntityType): Supported entity type.. [optional]
            page_no (int): Page number.. [optional] if omitted the server will use the default value of 1
            page_size (int): Number of items to return.. [optional] if omitted the server will use the default value of 25
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DocumentTypePaginatedList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_registered_document_types_endpoint.call_with_http_info(**kwargs)

    def issue_document_to_individual(
        self,
        document_issue_request,
        **kwargs
    ):
        """Issue a new document to an individual user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_document_to_individual(document_issue_request, async_req=True)
        >>> result = thread.get()

        Args:
            document_issue_request (DocumentIssueRequest): Document issue request payload

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DocumentIssueRequestDetails
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['document_issue_request'] = \
            document_issue_request
        return self.issue_document_to_individual_endpoint.call_with_http_info(**kwargs)

    def issue_document_to_organization(
        self,
        document_issue_request,
        **kwargs
    ):
        """Issue a new document to an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_document_to_organization(document_issue_request, async_req=True)
        >>> result = thread.get()

        Args:
            document_issue_request (DocumentIssueRequest): Document issue request payload

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DocumentIssueRequestDetails
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['document_issue_request'] = \
            document_issue_request
        return self.issue_document_to_organization_endpoint.call_with_http_info(**kwargs)

    def upload_document_for_individual(
        self,
        issue_request_id,
        form_file,
        **kwargs
    ):
        """Upload a document for issuance request of individual.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_document_for_individual(issue_request_id, form_file, async_req=True)
        >>> result = thread.get()

        Args:
            issue_request_id (str): Document issue request id.
            form_file (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['issue_request_id'] = \
            issue_request_id
        kwargs['form_file'] = \
            form_file
        return self.upload_document_for_individual_endpoint.call_with_http_info(**kwargs)

    def upload_document_for_organization(
        self,
        issue_request_id,
        form_file,
        **kwargs
    ):
        """Upload a document for issuance request of organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_document_for_organization(issue_request_id, form_file, async_req=True)
        >>> result = thread.get()

        Args:
            issue_request_id (str): Document issue request id System.Guid.
            form_file (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['issue_request_id'] = \
            issue_request_id
        kwargs['form_file'] = \
            form_file
        return self.upload_document_for_organization_endpoint.call_with_http_info(**kwargs)

