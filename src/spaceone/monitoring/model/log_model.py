from schematics import Model
from schematics.types import ModelType, StringType, DateTimeType, ListType, DictType, BaseType


class AdditionalProperty(Model):
    channels = StringType(serialize_when_none=False)


class Property(Model):
    entity = StringType(serialize_when_none=False)
    event_category = StringType(deserialize_from="eventCategory", serialize_when_none=False)
    hierarchy = StringType(serialize_when_none=False)
    message = StringType(serialize_when_none=False)
    service_request_id = StringType(deserialize_from="serviceRequestId", serialize_when_none=False)
    status_code = StringType(deserialize_from="statusCode", serialize_when_none=False)


class ObjectName(Model):
    additional_properties = ModelType(AdditionalProperty, default={})
    localized_value = StringType(serialize_when_none=False)
    value = StringType(serialize_when_none=False)


class Claim(Model):
    aio = StringType(serialize_when_none=False)
    appid = StringType(serialize_when_none=False)
    appidacr = StringType(serialize_when_none=False)
    aud = StringType(serialize_when_none=False)
    exp = StringType(serialize_when_none=False)
    groups = StringType(serialize_when_none=False)
    iat = StringType(serialize_when_none=False)
    ipaddr = StringType(serialize_when_none=False)
    iss = StringType(serialize_when_none=False)
    name = StringType(serialize_when_none=False)
    nbf = StringType(serialize_when_none=False)
    puid = StringType(serialize_when_none=False)
    rh = StringType(serialize_when_none=False)
    uti = StringType(serialize_when_none=False)
    ver = StringType(serialize_when_none=False)
    wids = StringType(serialize_when_none=False)
    xms_tcdt = StringType(serialize_when_none=False)
    auth_n_class_reference = StringType(deserialize_from="http://schemas.microsoft.com/claims/authnclassreference",
                                        serialize_when_none=False)
    auth_n_methods_references = StringType(deserialize_from="http://schemas.microsoft.com/claims/authnmethodsreferences",
                                           serialize_when_none=False)
    object_identifier = StringType(deserialize_from="http://schemas.microsoft.com/identity/claims/objectidentifier",
                                   serialize_when_none=False)
    scope = StringType(deserialize_from="http://schemas.microsoft.com/identity/claims/scope",
                       serialize_when_none=False)
    tenant_id = StringType(deserialize_from="http://schemas.microsoft.com/identity/claims/tenantid",
                           serialize_when_none=False)
    given_name = StringType(deserialize_from="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname",
                            serialize_when_none=False)
    _name = StringType(deserialize_from="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
                       serialize_when_none=False)
    name_identifier = StringType(deserialize_from="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",
                                 serialize_when_none=False)
    surname = StringType(deserialize_from="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname",
                         serialize_when_none=False)
    upn = StringType(deserialize_from="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn",
                     serialize_when_none=False)


class HTTPRequest(Model):
    additional_properties = ModelType(AdditionalProperty, default={})
    client_ip_address = StringType(serialize_when_none=False)
    client_request_id = StringType(serialize_when_none=False)
    method = StringType(serialize_when_none=False)
    uri = StringType(default=None)


class Category(Model):
    additional_properties = ModelType(AdditionalProperty, default={})
    localized_value = StringType(serialize_when_none=False)
    value = StringType(serialize_when_none=False)


class Authorization(Model):
    action = StringType(serialize_when_none=False)
    additional_properties = ModelType(AdditionalProperty, default={})
    role = StringType(default=None)
    scope = StringType(serialize_when_none=False)


class ActivityLogInfo(Model):
    id = StringType(serialize_when_none=False)
    level = StringType(serialize_when_none=False)
    operation_id = StringType(serialize_when_none=False)
    operation_name = ModelType(ObjectName, default={})
    properties = ModelType(Property, default={})
    resource_group_name = StringType(serialize_when_none=False)
    resource_id = StringType(serialize_when_none=False)
    resource_provider_name = ModelType(ObjectName, default={})
    resource_type = ModelType(ObjectName, default={})
    status = ModelType(ObjectName, default={})
    sub_status = ModelType(ObjectName, default={})
    submission_timestamp = DateTimeType(serialize_when_none=False)
    subscription_id = StringType(serialize_when_none=False)
    tenant_id = StringType(serialize_when_none=False)
    caller = StringType(serialize_when_none=False)
    correlation_id = StringType(serialize_when_none=False)
    description = StringType(serialize_when_none=False)
    event_data_id = StringType(serialize_when_none=False)
    event_name = ModelType(ObjectName, default={})
    http_request = ModelType(HTTPRequest, default={})
    additional_properties = ModelType(AdditionalProperty, default={})
    authorization = ModelType(Authorization, default={})
    category = ModelType(Category, default={})
    claims = ModelType(Claim, default={})
    event_timestamp = DateTimeType(serialize_when_none=False)


class Log(Model):
    results = ListType(ModelType(ActivityLogInfo), default=[])
