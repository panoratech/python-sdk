# PanoraSDK Services
A list of all services and services methods.
- Services

    - [Main](#main)

    - [Auth](#auth)

    - [Connections](#connections)

    - [Webhook](#webhook)

    - [LinkedUsers](#linkedusers)

    - [Organisations](#organisations)

    - [Projects](#projects)

    - [FieldMapping](#fieldmapping)

    - [Events](#events)

    - [MagicLink](#magiclink)

    - [Passthrough](#passthrough)

    - [CrmContact](#crmcontact)
- [All Methods](#all-methods)


## Main

| Method    | Description|
| :-------- | :----------| 
| [app_controller_get_hello](#app_controller_get_hello) |  |


## Auth

| Method    | Description|
| :-------- | :----------| 
| [sign_up](#sign_up) | Register |
| [sign_in](#sign_in) | Log In |
| [get_users](#get_users) | Get users |
| [get_api_keys](#get_api_keys) | Retrieve API Keys |
| [generate_api_key](#generate_api_key) | Create API Key |


## Connections

| Method    | Description|
| :-------- | :----------| 
| [handle_o_auth_callback](#handle_o_auth_callback) | Capture oAuth Callback |
| [get_connections](#get_connections) | Retrieve Connections |


## Webhook

| Method    | Description|
| :-------- | :----------| 
| [create_webhook_metadata](#create_webhook_metadata) | Add webhook metadata |
| [get_webhooks_metadata](#get_webhooks_metadata) | Retrieve webhooks metadata  |
| [update_webhook_status](#update_webhook_status) | Update webhook status |


## LinkedUsers

| Method    | Description|
| :-------- | :----------| 
| [add_linked_user](#add_linked_user) | Add Linked User |
| [get_linked_users](#get_linked_users) | Retrieve Linked Users |
| [get_linked_user](#get_linked_user) | Retrieve a Linked User |


## Organisations

| Method    | Description|
| :-------- | :----------| 
| [get_organisations](#get_organisations) | Retrieve Organisations |
| [create_organisation](#create_organisation) | Create an Organisation |


## Projects

| Method    | Description|
| :-------- | :----------| 
| [get_projects](#get_projects) | Retrieve projects |
| [create_project](#create_project) | Create a project |


## FieldMapping

| Method    | Description|
| :-------- | :----------| 
| [get_field_mappings_entities](#get_field_mappings_entities) | Retrieve field mapping entities |
| [get_field_mappings](#get_field_mappings) | Retrieve field mappings |
| [get_field_mapping_values](#get_field_mapping_values) | Retrieve field mappings values |
| [define_target_field](#define_target_field) | Define target Field |
| [map_field](#map_field) | Map Custom Field |
| [get_custom_provider_properties](#get_custom_provider_properties) | Retrieve Custom Properties |


## Events

| Method    | Description|
| :-------- | :----------| 
| [get_events](#get_events) | Retrieve Events |


## MagicLink

| Method    | Description|
| :-------- | :----------| 
| [create_magic_link](#create_magic_link) | Create a Magic Link |
| [get_magic_links](#get_magic_links) | Retrieve Magic Links |
| [get_magic_link](#get_magic_link) | Retrieve a Magic Link |


## Passthrough

| Method    | Description|
| :-------- | :----------| 
| [passthrough_request](#passthrough_request) | Make a passthrough request |


## CrmContact

| Method    | Description|
| :-------- | :----------| 
| [add_contact](#add_contact) | Create CRM Contact |
| [get_contacts](#get_contacts) | Retrieve a batch of CRM Contacts |
| [update_contact](#update_contact) | Update a CRM Contact |
| [get_contact](#get_contact) | Retrieve a CRM Contact |
| [add_contacts](#add_contacts) | Add a batch of CRM Contacts |




## All Methods


### **app_controller_get_hello**

- HTTP Method: GET
- Endpoint: /

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.main.app_controller_get_hello()

pprint(vars(results))

```


### **sign_up**
Register
- HTTP Method: POST
- Endpoint: /auth/register

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateUserDto](/src/panorasdk/models/README.md#createuserdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'email': 'email',
	'first_name': 'first_name',
	'last_name': 'last_name',
	'password_hash': 'password_hash'
}
results = sdk.auth.sign_up(request_input = request_body)

pprint(vars(results))

```

### **sign_in**
Log In
- HTTP Method: POST
- Endpoint: /auth/login

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [LoginDto](/src/panorasdk/models/README.md#logindto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'email': 'email',
	'id_user': 'id_user',
	'password_hash': 'password_hash'
}
results = sdk.auth.sign_in(request_input = request_body)

pprint(vars(results))

```

### **get_users**
Get users
- HTTP Method: GET
- Endpoint: /auth/users

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.auth.get_users()

pprint(vars(results))

```

### **get_api_keys**
Retrieve API Keys
- HTTP Method: GET
- Endpoint: /auth/api-keys

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.auth.get_api_keys()

pprint(vars(results))

```

### **generate_api_key**
Create API Key
- HTTP Method: POST
- Endpoint: /auth/generate-apikey

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [ApiKeyDto](/src/panorasdk/models/README.md#apikeydto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'keyName': 'keyName',
	'projectId': 'projectId',
	'userId': 'userId'
}
results = sdk.auth.generate_api_key(request_input = request_body)

pprint(vars(results))

```


### **handle_o_auth_callback**
Capture oAuth Callback
- HTTP Method: GET
- Endpoint: /connections/oauth/callback

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| state | str | Required |  |
| code | str | Required |  |
| location | str | Required |  |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.connections.handle_o_auth_callback(
	state = 'state',
	code = 'code',
	location = 'location'
)

pprint(vars(results))

```

### **get_connections**
Retrieve Connections
- HTTP Method: GET
- Endpoint: /connections

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.connections.get_connections()

pprint(vars(results))

```


### **create_webhook_metadata**
Add webhook metadata
- HTTP Method: POST
- Endpoint: /webhook

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [WebhookDto](/src/panorasdk/models/README.md#webhookdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'description': 'description',
	'id_project': 'id_project',
	'scope': 'scope',
	'url': 'url'
}
results = sdk.webhook.create_webhook_metadata(request_input = request_body)

pprint(vars(results))

```

### **get_webhooks_metadata**
Retrieve webhooks metadata 
- HTTP Method: GET
- Endpoint: /webhook

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.webhook.get_webhooks_metadata()

pprint(vars(results))

```

### **update_webhook_status**
Update webhook status
- HTTP Method: PUT
- Endpoint: /webhook/{id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.webhook.update_webhook_status(id = 'id')

pprint(vars(results))

```


### **add_linked_user**
Add Linked User
- HTTP Method: POST
- Endpoint: /linked-users/create

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateLinkedUserDto](/src/panorasdk/models/README.md#createlinkeduserdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'alias': 'alias',
	'id_project': 'id_project',
	'linked_user_origin_id': 'linked_user_origin_id'
}
results = sdk.linked_users.add_linked_user(request_input = request_body)

pprint(vars(results))

```

### **get_linked_users**
Retrieve Linked Users
- HTTP Method: GET
- Endpoint: /linked-users

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.linked_users.get_linked_users()

pprint(vars(results))

```

### **get_linked_user**
Retrieve a Linked User
- HTTP Method: GET
- Endpoint: /linked-users/single

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.linked_users.get_linked_user(id = 'id')

pprint(vars(results))

```


### **get_organisations**
Retrieve Organisations
- HTTP Method: GET
- Endpoint: /organisations

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.organisations.get_organisations()

pprint(vars(results))

```

### **create_organisation**
Create an Organisation
- HTTP Method: POST
- Endpoint: /organisations/create

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateOrganizationDto](/src/panorasdk/models/README.md#createorganizationdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'name': 'name',
	'stripe_customer_id': 'stripe_customer_id'
}
results = sdk.organisations.create_organisation(request_input = request_body)

pprint(vars(results))

```


### **get_projects**
Retrieve projects
- HTTP Method: GET
- Endpoint: /projects

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.projects.get_projects()

pprint(vars(results))

```

### **create_project**
Create a project
- HTTP Method: POST
- Endpoint: /projects/create

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateProjectDto](/src/panorasdk/models/README.md#createprojectdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'id_organization': 'id_organization',
	'name': 'name'
}
results = sdk.projects.create_project(request_input = request_body)

pprint(vars(results))

```


### **get_field_mappings_entities**
Retrieve field mapping entities
- HTTP Method: GET
- Endpoint: /field-mapping/entities

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.field_mapping.get_field_mappings_entities()

pprint(vars(results))

```

### **get_field_mappings**
Retrieve field mappings
- HTTP Method: GET
- Endpoint: /field-mapping/attribute

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.field_mapping.get_field_mappings()

pprint(vars(results))

```

### **get_field_mapping_values**
Retrieve field mappings values
- HTTP Method: GET
- Endpoint: /field-mapping/value

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.field_mapping.get_field_mapping_values()

pprint(vars(results))

```

### **define_target_field**
Define target Field
- HTTP Method: POST
- Endpoint: /field-mapping/define

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [DefineTargetFieldDto](/src/panorasdk/models/README.md#definetargetfielddto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'data_type': 'data_type',
	'description': 'description',
	'name': 'name',
	'object_type_owner': 'object_type_owner'
}
results = sdk.field_mapping.define_target_field(request_input = request_body)

pprint(vars(results))

```

### **map_field**
Map Custom Field
- HTTP Method: POST
- Endpoint: /field-mapping/map

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [MapFieldToProviderDto](/src/panorasdk/models/README.md#mapfieldtoproviderdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'attributeId': 'attributeId',
	'linked_user_id': 'linked_user_id',
	'source_custom_field_id': 'source_custom_field_id',
	'source_provider': 'source_provider'
}
results = sdk.field_mapping.map_field(request_input = request_body)

pprint(vars(results))

```

### **get_custom_provider_properties**
Retrieve Custom Properties
- HTTP Method: GET
- Endpoint: /field-mapping/properties

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| linked_user_id | str | Required |  |
| provider_id | str | Required |  |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.field_mapping.get_custom_provider_properties(
	linked_user_id = 'linkedUserId',
	provider_id = 'providerId'
)

pprint(vars(results))

```


### **get_events**
Retrieve Events
- HTTP Method: GET
- Endpoint: /events

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.events.get_events()

pprint(vars(results))

```


### **create_magic_link**
Create a Magic Link
- HTTP Method: POST
- Endpoint: /magic-link/create

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| request_input | [CreateMagicLinkDto](/src/panorasdk/models/README.md#createmagiclinkdto) | Required | Request body. |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'alias': 'alias',
	'email': 'email',
	'id_project': 'id_project',
	'linked_user_origin_id': 'linked_user_origin_id'
}
results = sdk.magic_link.create_magic_link(request_input = request_body)

pprint(vars(results))

```

### **get_magic_links**
Retrieve Magic Links
- HTTP Method: GET
- Endpoint: /magic-link

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.magic_link.get_magic_links()

pprint(vars(results))

```

### **get_magic_link**
Retrieve a Magic Link
- HTTP Method: GET
- Endpoint: /magic-link/single

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.magic_link.get_magic_link(id = 'id')

pprint(vars(results))

```


### **passthrough_request**
Make a passthrough request
- HTTP Method: POST
- Endpoint: /passthrough

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| request_input | [PassThroughRequestDto](/src/panorasdk/models/README.md#passthroughrequestdto) | Required | Request body. |

**Return Type**

[PassThroughResponse](/src/panorasdk/models/README.md#passthroughresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'data': {},
	'headers_': {},
	'method': 'PUT',
	'path': 'path'
}
results = sdk.passthrough.passthrough_request(
	request_input = request_body,
	integration_id = 'integrationId',
	linked_user_id = 'linkedUserId'
)

pprint(vars(results))

```


### **add_contact**
Create CRM Contact
- HTTP Method: POST
- Endpoint: /crm/contact

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional |  |
| request_input | [UnifiedContactInput](/src/panorasdk/models/README.md#unifiedcontactinput) | Required | Request body. |

**Return Type**

[AddContactResponse](/src/panorasdk/models/README.md#addcontactresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = {
	'email_addresses': [],
	'field_mappings': {},
	'first_name': 'first_name',
	'last_name': 'last_name',
	'phone_numbers': []
}
results = sdk.crm_contact.add_contact(
	request_input = request_body,
	integration_id = 'integrationId',
	linked_user_id = 'linkedUserId',
	remote_data = True
)

pprint(vars(results))

```

### **get_contacts**
Retrieve a batch of CRM Contacts
- HTTP Method: GET
- Endpoint: /crm/contact

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional |  |

**Return Type**

[GetContactsResponse](/src/panorasdk/models/README.md#getcontactsresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.crm_contact.get_contacts(
	integration_id = 'integrationId',
	linked_user_id = 'linkedUserId',
	remote_data = True
)

pprint(vars(results))

```

### **update_contact**
Update a CRM Contact
- HTTP Method: PATCH
- Endpoint: /crm/contact

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

Returns a dict object.

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.crm_contact.update_contact(id = 'id')

pprint(vars(results))

```

### **get_contact**
Retrieve a CRM Contact
- HTTP Method: GET
- Endpoint: /crm/contact/{id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |
| remote_data | bool | Optional |  |

**Return Type**

[GetContactResponse](/src/panorasdk/models/README.md#getcontactresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
results = sdk.crm_contact.get_contact(
	id = 'id',
	remote_data = True
)

pprint(vars(results))

```

### **add_contacts**
Add a batch of CRM Contacts
- HTTP Method: POST
- Endpoint: /crm/contact/batch

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional |  |
| request_input | [AddContactsRequest](/src/panorasdk/models/README.md#addcontactsrequest) | Required | Request body. |

**Return Type**

[AddContactsResponse](/src/panorasdk/models/README.md#addcontactsresponse) 

**Example Usage Code Snippet**
```Python
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK
sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))
request_body = [{},{}]
results = sdk.crm_contact.add_contacts(
	request_input = request_body,
	integration_id = 'integrationId',
	linked_user_id = 'linkedUserId',
	remote_data = True
)

pprint(vars(results))

```




