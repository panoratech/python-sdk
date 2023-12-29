# PanoraSDK Python SDK 1.0.0
A Python SDK for PanoraSDK.

The Panora API description

- API version: 1.0.0
- SDK version: 1.0.0

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
    - [Dependencies](#dependencies)
- [Authentication](#authentication)
    - [Access Token Authentication](#bearer-authentication)
- [API Endpoint Services](#api-endpoint-services)
- [API Models](#api-models)
- [Testing](#testing)
- [Configuration](#configuration)
- [Sample Usage](#sample-usage)
- [PanoraSDK Services](#panorasdk-services)
- [License](#license)

## Installation
```bash
pip install panorasdk
```

### Dependencies

This SDK uses the following dependencies:
- requests 2.28.1
- http-exceptions 0.2.10
- pytest 7.1.2
- responses 0.21.0

## Authentication

To see whether an endpoint needs a specific type of authentication check the endpoint's documentation.

### Access Token Authentication
The PanoraSDK API uses bearer tokens as a form of authentication.You can set the bearer token when initializing the SDK through the constructor: 

```py
sdk = PanoraSDK('YOUR_BEARER_TOKEN')
```

Or through the `set_access_token` method:
```py
sdk = PanoraSDK()
sdk.set_access_token('YOUR_BEARER_TOKEN')
```

You can also set it for each service individually:
```py
sdk = PanoraSDK()
sdk.main.set_access_token('YOUR_BEARER_TOKEN')
```

## API Endpoint Services

All URIs are relative to https://api-demo.panora.dev.

Click the service name for a full list of the service methods.

| Service |
| :------ |
|[Main](./services/README.md#main)|
|[Protected](./services/README.md#protected)|
|[Auth](./services/README.md#auth)|
|[Connections](./services/README.md#connections)|
|[Webhook](./services/README.md#webhook)|
|[LinkedUsers](./services/README.md#linkedusers)|
|[Organisations](./services/README.md#organisations)|
|[Projects](./services/README.md#projects)|
|[FieldMapping](./services/README.md#fieldmapping)|
|[Events](./services/README.md#events)|
|[MagicLink](./services/README.md#magiclink)|
|[Passthrough](./services/README.md#passthrough)|
|[CrmContact](./services/README.md#crmcontact)|
|[TicketingTicket](./services/README.md#ticketingticket)|

## API Models
[A list documenting all API models for this SDK](./models/README.md#panorasdk-models).

## Testing

Run unit tests with this command:

```sh
python -m unittest discover -p "test*.py" 
```

## Sample Usage

```py
from os import getenv
from pprint import pprint
from panorasdk import PanoraSDK

sdk = PanoraSDK()
sdk.set_access_token(getenv("PANORASDK_ACCESS_TOKEN"))

results = sdk.main.app_controller_get_hello()

pprint(vars(results))
```


# PanoraSDK Services
A list of all services and services methods.
- Services

    - [Main](#main)

    - [Protected](#protected)

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

    - [TicketingTicket](#ticketingticket)
- [All Methods](#all-methods)


## Main

| Method    | Description|
| :-------- | :----------| 
| [app_controller_get_hello](#app_controller_get_hello) |  |


## Protected

| Method    | Description|
| :-------- | :----------| 
| [app_controller_get_hello2](#app_controller_get_hello2) |  |


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
| [get_connections](#get_connections) | List Connections |


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
| [get_contacts](#get_contacts) | List a batch of CRM Contacts |
| [update_contact](#update_contact) | Update a CRM Contact |
| [get_contact](#get_contact) | Retrieve a CRM Contact |
| [add_contacts](#add_contacts) | Add a batch of CRM Contacts |


## TicketingTicket

| Method    | Description|
| :-------- | :----------| 
| [add_ticket](#add_ticket) | Create a Ticket |
| [get_tickets](#get_tickets) | List a batch of Tickets |
| [update_ticket](#update_ticket) | Update a Ticket |
| [get_ticket](#get_ticket) | Retrieve a Ticket |
| [add_tickets](#add_tickets) | Add a batch of Tickets |




## All Methods


### **app_controller_get_hello**

- HTTP Method: GET
- Endpoint: /

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.



### **app_controller_get_hello2**

- HTTP Method: GET
- Endpoint: /protected

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.



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


### **get_users**
Get users
- HTTP Method: GET
- Endpoint: /auth/users

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


### **get_api_keys**
Retrieve API Keys
- HTTP Method: GET
- Endpoint: /auth/api-keys

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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


### **get_connections**
List Connections
- HTTP Method: GET
- Endpoint: /connections

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.



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


### **get_webhooks_metadata**
Retrieve webhooks metadata 
- HTTP Method: GET
- Endpoint: /webhook

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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


### **get_linked_users**
Retrieve Linked Users
- HTTP Method: GET
- Endpoint: /linked-users

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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



### **get_organisations**
Retrieve Organisations
- HTTP Method: GET
- Endpoint: /organisations

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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



### **get_projects**
Retrieve projects
- HTTP Method: GET
- Endpoint: /projects

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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



### **get_field_mappings_entities**
Retrieve field mapping entities
- HTTP Method: GET
- Endpoint: /field-mapping/entities

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


### **get_field_mappings**
Retrieve field mappings
- HTTP Method: GET
- Endpoint: /field-mapping/attribute

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


### **get_field_mapping_values**
Retrieve field mappings values
- HTTP Method: GET
- Endpoint: /field-mapping/value

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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



### **get_events**
Retrieve Events
- HTTP Method: GET
- Endpoint: /events

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.



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


### **get_magic_links**
Retrieve Magic Links
- HTTP Method: GET
- Endpoint: /magic-link

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 

**Return Type**

Returns a dict object.


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



### **add_contact**
Create CRM Contact
- HTTP Method: POST
- Endpoint: /crm/contact

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required | The integration ID |
| linked_user_id | str | Required | The linked user ID |
| remote_data | bool | Optional | Set to true to include data from the original CRM software. |
| request_input | [UnifiedContactInput](/src/panorasdk/models/README.md#unifiedcontactinput) | Required | Request body. |

**Return Type**

Returns a dict object.


### **get_contacts**
List a batch of CRM Contacts
- HTTP Method: GET
- Endpoint: /crm/contact

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional | Set to true to include data from the original CRM software. |

**Return Type**

Returns a dict object.


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


### **get_contact**
Retrieve a CRM Contact
- HTTP Method: GET
- Endpoint: /crm/contact/{id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required | id of the `contact` you want to retrive. |
| remote_data | bool | Optional | Set to true to include data from the original CRM software. |

**Return Type**

Returns a dict object.


### **add_contacts**
Add a batch of CRM Contacts
- HTTP Method: POST
- Endpoint: /crm/contact/batch

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional | Set to true to include data from the original CRM software. |
| request_input | [AddContactsRequest](/src/panorasdk/models/README.md#addcontactsrequest) | Required | Request body. |

**Return Type**

Returns a dict object.



### **add_ticket**
Create a Ticket
- HTTP Method: POST
- Endpoint: /ticketing/ticket

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required | The integration ID |
| linked_user_id | str | Required | The linked user ID |
| remote_data | bool | Optional | Set to true to include data from the original Ticketing software. |
| request_input | [UnifiedTicketInput](/src/panorasdk/models/README.md#unifiedticketinput) | Required | Request body. |

**Return Type**

Returns a dict object.


### **get_tickets**
List a batch of Tickets
- HTTP Method: GET
- Endpoint: /ticketing/ticket

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional | Set to true to include data from the original Ticketing software. |

**Return Type**

Returns a dict object.


### **update_ticket**
Update a Ticket
- HTTP Method: PATCH
- Endpoint: /ticketing/ticket

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required |  |

**Return Type**

Returns a dict object.


### **get_ticket**
Retrieve a Ticket
- HTTP Method: GET
- Endpoint: /ticketing/ticket/{id}

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| id | str | Required | id of the `ticket` you want to retrive. |
| remote_data | bool | Optional | Set to true to include data from the original Ticketing software. |

**Return Type**

Returns a dict object.


### **add_tickets**
Add a batch of Tickets
- HTTP Method: POST
- Endpoint: /ticketing/ticket/batch

**Parameters**
| Name    | Type| Required | Description |
| :-------- | :----------| :----------| :----------| 
| integration_id | str | Required |  |
| linked_user_id | str | Required |  |
| remote_data | bool | Optional | Set to true to include data from the original Ticketing software. |
| request_input | [AddTicketsRequest](/src/panorasdk/models/README.md#addticketsrequest) | Required | Request body. |

**Return Type**

Returns a dict object.






## License

License: MIT. See license in LICENSE.
