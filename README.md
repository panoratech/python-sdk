# panora

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=<no value>&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasy.com/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasy.com/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install panora-sdk
```

Poetry
```bash
poetry add panora-sdk
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.hello()

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from panora_sdk import Panora

async def main():
    s = Panora(
        bearer=os.getenv("BEARER", ""),
    )
    await s.hello_async()
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [Panora SDK](docs/sdks/panora/README.md)

* [hello](docs/sdks/panora/README.md#hello)
* [health](docs/sdks/panora/README.md#health)

### [webhook](docs/sdks/webhook/README.md)

* [list](docs/sdks/webhook/README.md#list) - List webhooks 
* [create](docs/sdks/webhook/README.md#create) - Add webhook metadata
* [delete](docs/sdks/webhook/README.md#delete) - Delete Webhook
* [update_status](docs/sdks/webhook/README.md#update_status) - Update webhook status
* [verify_event](docs/sdks/webhook/README.md#verify_event) - Verify payload signature of the webhook


### [ticketing.tickets](docs/sdks/tickets/README.md)

* [list](docs/sdks/tickets/README.md#list) - List  Tickets
* [create](docs/sdks/tickets/README.md#create) - Create Tickets
* [retrieve](docs/sdks/tickets/README.md#retrieve) - Retrieve Tickets

### [ticketing.users](docs/sdks/users/README.md)

* [list](docs/sdks/users/README.md#list) - List  Users
* [retrieve](docs/sdks/users/README.md#retrieve) - Retrieve Users

### [ticketing.accounts](docs/sdks/accounts/README.md)

* [list](docs/sdks/accounts/README.md#list) - List  Accounts
* [retrieve](docs/sdks/accounts/README.md#retrieve) - Retrieve Accounts

### [ticketing.contacts](docs/sdks/contacts/README.md)

* [list](docs/sdks/contacts/README.md#list) - List all Contacts
* [retrieve](docs/sdks/contacts/README.md#retrieve) - Retrieve Contacts

### [ticketing.collections](docs/sdks/collections/README.md)

* [list](docs/sdks/collections/README.md#list) - List  Collections
* [retrieve](docs/sdks/collections/README.md#retrieve) - Retrieve Collections

### [ticketing.comments](docs/sdks/comments/README.md)

* [list](docs/sdks/comments/README.md#list) - List  Comments
* [create](docs/sdks/comments/README.md#create) - Create Comments
* [retrieve](docs/sdks/comments/README.md#retrieve) - Retrieve Comments

### [ticketing.tags](docs/sdks/tags/README.md)

* [list](docs/sdks/tags/README.md#list) - List  Tags
* [retrieve](docs/sdks/tags/README.md#retrieve) - Retrieve Tags

### [ticketing.teams](docs/sdks/teams/README.md)

* [list](docs/sdks/teams/README.md#list) - List  Teams
* [retrieve](docs/sdks/teams/README.md#retrieve) - Retrieve Teams

### [ticketing.attachments](docs/sdks/panoraticketingattachments/README.md)

* [list](docs/sdks/panoraticketingattachments/README.md#list) - List  Attachments
* [create](docs/sdks/panoraticketingattachments/README.md#create) - Create Attachments
* [retrieve](docs/sdks/panoraticketingattachments/README.md#retrieve) - Retrieve Attachments

### [sync](docs/sdks/sync/README.md)

* [status](docs/sdks/sync/README.md#status) - Retrieve sync status of a certain vertical
* [resync](docs/sdks/sync/README.md#resync) - Resync common objects across a vertical


### [crm.companies](docs/sdks/companies/README.md)

* [list](docs/sdks/companies/README.md#list) - List  Companies
* [create](docs/sdks/companies/README.md#create) - Create Companies
* [retrieve](docs/sdks/companies/README.md#retrieve) - Retrieve Companies

### [crm.contacts](docs/sdks/panoracontacts/README.md)

* [list](docs/sdks/panoracontacts/README.md#list) - List CRM Contacts
* [create](docs/sdks/panoracontacts/README.md#create) - Create Contacts
* [retrieve](docs/sdks/panoracontacts/README.md#retrieve) - Retrieve Contacts

### [crm.deals](docs/sdks/deals/README.md)

* [list](docs/sdks/deals/README.md#list) - List  Deals
* [create](docs/sdks/deals/README.md#create) - Create Deals
* [retrieve](docs/sdks/deals/README.md#retrieve) - Retrieve Deals

### [crm.engagements](docs/sdks/engagements/README.md)

* [list](docs/sdks/engagements/README.md#list) - List  Engagements
* [create](docs/sdks/engagements/README.md#create) - Create Engagements
* [retrieve](docs/sdks/engagements/README.md#retrieve) - Retrieve Engagements

### [crm.notes](docs/sdks/notes/README.md)

* [list](docs/sdks/notes/README.md#list) - List  Notes
* [create](docs/sdks/notes/README.md#create) - Create Notes
* [retrieve](docs/sdks/notes/README.md#retrieve) - Retrieve Notes

### [crm.stages](docs/sdks/stages/README.md)

* [list](docs/sdks/stages/README.md#list) - List  Stages
* [retrieve](docs/sdks/stages/README.md#retrieve) - Retrieve Stages

### [crm.tasks](docs/sdks/tasks/README.md)

* [list](docs/sdks/tasks/README.md#list) - List  Tasks
* [create](docs/sdks/tasks/README.md#create) - Create Tasks
* [retrieve](docs/sdks/tasks/README.md#retrieve) - Retrieve Tasks

### [crm.users](docs/sdks/panorausers/README.md)

* [list](docs/sdks/panorausers/README.md#list) - List  Users
* [retrieve](docs/sdks/panorausers/README.md#retrieve) - Retrieve Users

### [linked_users](docs/sdks/linkedusers/README.md)

* [create](docs/sdks/linkedusers/README.md#create) - Add Linked User
* [list](docs/sdks/linkedusers/README.md#list) - Retrieve Linked Users
* [import_batch](docs/sdks/linkedusers/README.md#import_batch) - Add Batch Linked Users
* [retrieve](docs/sdks/linkedusers/README.md#retrieve) - Retrieve a Linked User
* [remote_id](docs/sdks/linkedusers/README.md#remote_id) - Retrieve a Linked User From A Remote Id

### [field_mappings](docs/sdks/fieldmappings/README.md)

* [define](docs/sdks/fieldmappings/README.md#define) - Define target Field
* [create](docs/sdks/fieldmappings/README.md#create) - Create Custom Field
* [map](docs/sdks/fieldmappings/README.md#map) - Map Custom Field

### [passthrough](docs/sdks/passthrough/README.md)

* [request](docs/sdks/passthrough/README.md#request) - Make a passthrough request


### [hris.bankinfos](docs/sdks/bankinfos/README.md)

* [list](docs/sdks/bankinfos/README.md#list) - List  Bankinfos
* [retrieve](docs/sdks/bankinfos/README.md#retrieve) - Retrieve Bank Infos

### [hris.benefits](docs/sdks/benefits/README.md)

* [list](docs/sdks/benefits/README.md#list) - List  Benefits
* [retrieve](docs/sdks/benefits/README.md#retrieve) - Retrieve Benefits

### [hris.companies](docs/sdks/panoracompanies/README.md)

* [list](docs/sdks/panoracompanies/README.md#list) - List  Companys

### [hris.dependents](docs/sdks/dependents/README.md)

* [list](docs/sdks/dependents/README.md#list) - List  Dependents
* [retrieve](docs/sdks/dependents/README.md#retrieve) - Retrieve Dependents

### [hris.employeepayrollruns](docs/sdks/employeepayrollruns/README.md)

* [list](docs/sdks/employeepayrollruns/README.md#list) - List  EmployeePayrollRuns
* [retrieve](docs/sdks/employeepayrollruns/README.md#retrieve) - Retrieve Employee Payroll Runs

### [hris.employees](docs/sdks/employees/README.md)

* [list](docs/sdks/employees/README.md#list) - List  Employees
* [create](docs/sdks/employees/README.md#create) - Create Employees
* [retrieve](docs/sdks/employees/README.md#retrieve) - Retrieven Employees

### [hris.employerbenefits](docs/sdks/employerbenefits/README.md)

* [list](docs/sdks/employerbenefits/README.md#list) - List  EmployerBenefits
* [retrieve](docs/sdks/employerbenefits/README.md#retrieve) - Retrieve Employer Benefits

### [hris.employments](docs/sdks/employments/README.md)

* [list](docs/sdks/employments/README.md#list) - List  Employments
* [retrieve](docs/sdks/employments/README.md#retrieve) - Retrieve Employments

### [hris.groups](docs/sdks/groups/README.md)

* [list](docs/sdks/groups/README.md#list) - List  Groups
* [retrieve](docs/sdks/groups/README.md#retrieve) - Retrieve Groups

### [hris.locations](docs/sdks/locations/README.md)

* [list](docs/sdks/locations/README.md#list) - List  Locations
* [retrieve](docs/sdks/locations/README.md#retrieve) - Retrieve Locations

### [hris.paygroups](docs/sdks/paygroups/README.md)

* [list](docs/sdks/paygroups/README.md#list) - List  PayGroups
* [retrieve](docs/sdks/paygroups/README.md#retrieve) - Retrieve Pay Groups

### [hris.payrollruns](docs/sdks/payrollruns/README.md)

* [list](docs/sdks/payrollruns/README.md#list) - List  PayrollRuns

### [hris.timeoffs](docs/sdks/timeoffs/README.md)

* [list](docs/sdks/timeoffs/README.md#list) - List  Timeoffs
* [create](docs/sdks/timeoffs/README.md#create) - Create Timeoffs
* [retrieve](docs/sdks/timeoffs/README.md#retrieve) - Retrieve Timeoffs

### [hris.timeoffbalances](docs/sdks/timeoffbalances/README.md)

* [list](docs/sdks/timeoffbalances/README.md#list) - List  TimeoffBalances
* [retrieve](docs/sdks/timeoffbalances/README.md#retrieve) - Retrieve Time off Balances


### [marketingautomation.actions](docs/sdks/actions/README.md)

* [list](docs/sdks/actions/README.md#list) - List  Actions
* [create](docs/sdks/actions/README.md#create) - Create Action
* [retrieve](docs/sdks/actions/README.md#retrieve) - Retrieve Actions

### [marketingautomation.automations](docs/sdks/automations/README.md)

* [list](docs/sdks/automations/README.md#list) - List  Automations
* [create](docs/sdks/automations/README.md#create) - Create Automation
* [retrieve](docs/sdks/automations/README.md#retrieve) - Retrieve Automations

### [marketingautomation.campaigns](docs/sdks/campaigns/README.md)

* [list](docs/sdks/campaigns/README.md#list) - List  Campaigns
* [create](docs/sdks/campaigns/README.md#create) - Create Campaign
* [retrieve](docs/sdks/campaigns/README.md#retrieve) - Retrieve Campaigns

### [marketingautomation.contacts](docs/sdks/panoramarketingautomationcontacts/README.md)

* [list](docs/sdks/panoramarketingautomationcontacts/README.md#list) - List  Contacts
* [create](docs/sdks/panoramarketingautomationcontacts/README.md#create) - Create Contact
* [retrieve](docs/sdks/panoramarketingautomationcontacts/README.md#retrieve) - Retrieve Contacts

### [marketingautomation.emails](docs/sdks/emails/README.md)

* [list](docs/sdks/emails/README.md#list) - List  Emails
* [retrieve](docs/sdks/emails/README.md#retrieve) - Retrieve Emails

### [marketingautomation.events](docs/sdks/events/README.md)

* [list](docs/sdks/events/README.md#list) - List  Events
* [retrieve](docs/sdks/events/README.md#retrieve) - Retrieve Events

### [marketingautomation.lists](docs/sdks/lists/README.md)

* [list](docs/sdks/lists/README.md#list) - List  Lists
* [create](docs/sdks/lists/README.md#create) - Create Lists
* [retrieve](docs/sdks/lists/README.md#retrieve) - Retrieve Lists

### [marketingautomation.messages](docs/sdks/messages/README.md)

* [list](docs/sdks/messages/README.md#list) - List  Messages
* [retrieve](docs/sdks/messages/README.md#retrieve) - Retrieve Messages

### [marketingautomation.templates](docs/sdks/templates/README.md)

* [list](docs/sdks/templates/README.md#list) - List  Templates
* [create](docs/sdks/templates/README.md#create) - Create Template
* [retrieve](docs/sdks/templates/README.md#retrieve) - Retrieve Templates

### [marketingautomation.users](docs/sdks/panoramarketingautomationusers/README.md)

* [list](docs/sdks/panoramarketingautomationusers/README.md#list) - List  Users
* [retrieve](docs/sdks/panoramarketingautomationusers/README.md#retrieve) - Retrieve Users


### [ats.activities](docs/sdks/activities/README.md)

* [list](docs/sdks/activities/README.md#list) - List  Activities
* [create](docs/sdks/activities/README.md#create) - Create Activities
* [retrieve](docs/sdks/activities/README.md#retrieve) - Retrieve Activities

### [ats.applications](docs/sdks/applications/README.md)

* [list](docs/sdks/applications/README.md#list) - List  Applications
* [create](docs/sdks/applications/README.md#create) - Create Applications
* [retrieve](docs/sdks/applications/README.md#retrieve) - Retrieve Applications

### [ats.attachments](docs/sdks/attachments/README.md)

* [list](docs/sdks/attachments/README.md#list) - List  Attachments
* [create](docs/sdks/attachments/README.md#create) - Create Attachments
* [retrieve](docs/sdks/attachments/README.md#retrieve) - Retrieve Attachments

### [ats.candidates](docs/sdks/candidates/README.md)

* [list](docs/sdks/candidates/README.md#list) - List  Candidates
* [create](docs/sdks/candidates/README.md#create) - Create Candidates
* [retrieve](docs/sdks/candidates/README.md#retrieve) - Retrieve Candidates

### [ats.departments](docs/sdks/departments/README.md)

* [list](docs/sdks/departments/README.md#list) - List  Departments
* [retrieve](docs/sdks/departments/README.md#retrieve) - Retrieve Departments

### [ats.interviews](docs/sdks/interviews/README.md)

* [list](docs/sdks/interviews/README.md#list) - List  Interviews
* [create](docs/sdks/interviews/README.md#create) - Create Interviews
* [retrieve](docs/sdks/interviews/README.md#retrieve) - Retrieve Interviews

### [ats.jobinterviewstages](docs/sdks/jobinterviewstages/README.md)

* [list](docs/sdks/jobinterviewstages/README.md#list) - List  JobInterviewStages
* [retrieve](docs/sdks/jobinterviewstages/README.md#retrieve) - Retrieve Job Interview Stages

### [ats.jobs](docs/sdks/jobs/README.md)

* [list](docs/sdks/jobs/README.md#list) - List  Jobs
* [retrieve](docs/sdks/jobs/README.md#retrieve) - Retrieve Jobs

### [ats.offers](docs/sdks/offers/README.md)

* [list](docs/sdks/offers/README.md#list) - List  Offers
* [retrieve](docs/sdks/offers/README.md#retrieve) - Retrieve Offers

### [ats.offices](docs/sdks/offices/README.md)

* [list](docs/sdks/offices/README.md#list) - List Offices
* [retrieve](docs/sdks/offices/README.md#retrieve) - Retrieve Offices

### [ats.rejectreasons](docs/sdks/rejectreasons/README.md)

* [list](docs/sdks/rejectreasons/README.md#list) - List  RejectReasons
* [retrieve](docs/sdks/rejectreasons/README.md#retrieve) - Retrieve Reject Reasons

### [ats.scorecards](docs/sdks/scorecards/README.md)

* [list](docs/sdks/scorecards/README.md#list) - List  ScoreCards
* [retrieve](docs/sdks/scorecards/README.md#retrieve) - Retrieve Score Cards

### [ats.tags](docs/sdks/panoratags/README.md)

* [list](docs/sdks/panoratags/README.md#list) - List  Tags
* [retrieve](docs/sdks/panoratags/README.md#retrieve) - Retrieve Tags

### [ats.users](docs/sdks/panoraatsusers/README.md)

* [list](docs/sdks/panoraatsusers/README.md#list) - List  Users
* [retrieve](docs/sdks/panoraatsusers/README.md#retrieve) - Retrieve Users

### [ats.eeocs](docs/sdks/eeocs/README.md)

* [list](docs/sdks/eeocs/README.md#list) - List  Eeocss
* [retrieve](docs/sdks/eeocs/README.md#retrieve) - Retrieve Eeocs


### [accounting.accounts](docs/sdks/panoraaccounts/README.md)

* [list](docs/sdks/panoraaccounts/README.md#list) - List  Accounts
* [create](docs/sdks/panoraaccounts/README.md#create) - Create Accounts
* [retrieve](docs/sdks/panoraaccounts/README.md#retrieve) - Retrieve Accounts

### [accounting.addresses](docs/sdks/addresses/README.md)

* [list](docs/sdks/addresses/README.md#list) - List  Addresss
* [retrieve](docs/sdks/addresses/README.md#retrieve) - Retrieve Addresses

### [accounting.attachments](docs/sdks/panoraattachments/README.md)

* [list](docs/sdks/panoraattachments/README.md#list) - List  Attachments
* [create](docs/sdks/panoraattachments/README.md#create) - Create Attachments
* [retrieve](docs/sdks/panoraattachments/README.md#retrieve) - Retrieve Attachments

### [accounting.balancesheets](docs/sdks/balancesheets/README.md)

* [list](docs/sdks/balancesheets/README.md#list) - List  BalanceSheets
* [retrieve](docs/sdks/balancesheets/README.md#retrieve) - Retrieve BalanceSheets

### [accounting.cashflowstatements](docs/sdks/cashflowstatements/README.md)

* [list](docs/sdks/cashflowstatements/README.md#list) - List  CashflowStatements
* [retrieve](docs/sdks/cashflowstatements/README.md#retrieve) - Retrieve Cashflow Statements

### [accounting.companyinfos](docs/sdks/companyinfos/README.md)

* [list](docs/sdks/companyinfos/README.md#list) - List  CompanyInfos
* [retrieve](docs/sdks/companyinfos/README.md#retrieve) - Retrieve Company Infos

### [accounting.contacts](docs/sdks/panoraaccountingcontacts/README.md)

* [list](docs/sdks/panoraaccountingcontacts/README.md#list) - List  Contacts
* [create](docs/sdks/panoraaccountingcontacts/README.md#create) - Create Contacts
* [retrieve](docs/sdks/panoraaccountingcontacts/README.md#retrieve) - Retrieve Contacts

### [accounting.creditnotes](docs/sdks/creditnotes/README.md)

* [list](docs/sdks/creditnotes/README.md#list) - List  CreditNotes
* [retrieve](docs/sdks/creditnotes/README.md#retrieve) - Retrieve Credit Notes

### [accounting.expenses](docs/sdks/expenses/README.md)

* [list](docs/sdks/expenses/README.md#list) - List  Expenses
* [create](docs/sdks/expenses/README.md#create) - Create Expenses
* [retrieve](docs/sdks/expenses/README.md#retrieve) - Retrieve Expenses

### [accounting.incomestatements](docs/sdks/incomestatements/README.md)

* [list](docs/sdks/incomestatements/README.md#list) - List  IncomeStatements
* [retrieve](docs/sdks/incomestatements/README.md#retrieve) - Retrieve Income Statements

### [accounting.invoices](docs/sdks/invoices/README.md)

* [list](docs/sdks/invoices/README.md#list) - List  Invoices
* [create](docs/sdks/invoices/README.md#create) - Create Invoices
* [retrieve](docs/sdks/invoices/README.md#retrieve) - Retrieve Invoices

### [accounting.items](docs/sdks/items/README.md)

* [list](docs/sdks/items/README.md#list) - List  Items
* [retrieve](docs/sdks/items/README.md#retrieve) - Retrieve Items

### [accounting.journalentries](docs/sdks/journalentries/README.md)

* [list](docs/sdks/journalentries/README.md#list) - List  JournalEntrys
* [create](docs/sdks/journalentries/README.md#create) - Create Journal Entries
* [retrieve](docs/sdks/journalentries/README.md#retrieve) - Retrieve Journal Entries

### [accounting.payments](docs/sdks/payments/README.md)

* [list](docs/sdks/payments/README.md#list) - List  Payments
* [create](docs/sdks/payments/README.md#create) - Create Payments
* [retrieve](docs/sdks/payments/README.md#retrieve) - Retrieve Payments

### [accounting.phonenumbers](docs/sdks/phonenumbers/README.md)

* [list](docs/sdks/phonenumbers/README.md#list) - List  PhoneNumbers
* [retrieve](docs/sdks/phonenumbers/README.md#retrieve) - Retrieve Phone Numbers

### [accounting.purchaseorders](docs/sdks/purchaseorders/README.md)

* [list](docs/sdks/purchaseorders/README.md#list) - List  PurchaseOrders
* [create](docs/sdks/purchaseorders/README.md#create) - Create Purchase Orders
* [retrieve](docs/sdks/purchaseorders/README.md#retrieve) - Retrieve Purchase Orders

### [accounting.taxrates](docs/sdks/taxrates/README.md)

* [list](docs/sdks/taxrates/README.md#list) - List  TaxRates
* [retrieve](docs/sdks/taxrates/README.md#retrieve) - Retrieve Tax Rates

### [accounting.trackingcategories](docs/sdks/trackingcategories/README.md)

* [list](docs/sdks/trackingcategories/README.md#list) - List  TrackingCategorys
* [retrieve](docs/sdks/trackingcategories/README.md#retrieve) - Retrieve Tracking Categories

### [accounting.transactions](docs/sdks/transactions/README.md)

* [list](docs/sdks/transactions/README.md#list) - List  Transactions
* [retrieve](docs/sdks/transactions/README.md#retrieve) - Retrieve Transactions

### [accounting.vendorcredits](docs/sdks/vendorcredits/README.md)

* [list](docs/sdks/vendorcredits/README.md#list) - List  VendorCredits
* [retrieve](docs/sdks/vendorcredits/README.md#retrieve) - Retrieve Vendor Credits


### [filestorage.drives](docs/sdks/drives/README.md)

* [list](docs/sdks/drives/README.md#list) - List  Drives
* [retrieve](docs/sdks/drives/README.md#retrieve) - Retrieve Drives

### [filestorage.files](docs/sdks/files/README.md)

* [list](docs/sdks/files/README.md#list) - List  Files
* [create](docs/sdks/files/README.md#create) - Create Files
* [retrieve](docs/sdks/files/README.md#retrieve) - Retrieve Files

### [filestorage.folders](docs/sdks/folders/README.md)

* [list](docs/sdks/folders/README.md#list) - List  Folders
* [create](docs/sdks/folders/README.md#create) - Create Folders
* [retrieve](docs/sdks/folders/README.md#retrieve) - Retrieve Folders

### [filestorage.groups](docs/sdks/panoragroups/README.md)

* [list](docs/sdks/panoragroups/README.md#list) - List  Groups
* [retrieve](docs/sdks/panoragroups/README.md#retrieve) - Retrieve Groups

### [filestorage.users](docs/sdks/panorafilestorageusers/README.md)

* [list](docs/sdks/panorafilestorageusers/README.md#list) - List  Users
* [retrieve](docs/sdks/panorafilestorageusers/README.md#retrieve) - Retrieve Users
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from panora.utils import BackoffStrategy, RetryConfig
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.hello(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

# Use the SDK ...

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from panora.utils import BackoffStrategy, RetryConfig
from panora_sdk import Panora

s = Panora(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bearer=os.getenv("BEARER", ""),
)


s.hello()

# Use the SDK ...

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

### Example

```python
import os
from panora_sdk import Panora, models

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


try:
    s.hello()

except models.SDKError as e:
    # handle exception
    raise(e)

# Use the SDK ...

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.panora.dev` | None |
| 1 | `https://api-sandbox.panora.dev` | None |
| 2 | `https://api-dev.panora.dev` | None |

#### Example

```python
import os
from panora_sdk import Panora

s = Panora(
    server_idx=2,
    bearer=os.getenv("BEARER", ""),
)


s.hello()

# Use the SDK ...

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import os
from panora_sdk import Panora

s = Panora(
    server_url="https://api.panora.dev",
    bearer=os.getenv("BEARER", ""),
)


s.hello()

# Use the SDK ...

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from panora_sdk import Panora
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Panora(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from panora_sdk import Panora
from panora_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Panora(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name        | Type        | Scheme      |
| ----------- | ----------- | ----------- |
| `bearer`    | http        | HTTP Bearer |

To authenticate with the API the `bearer` parameter must be set when initializing the SDK client instance. For example:
```python
import os
from panora_sdk import Panora

s = Panora(
    bearer=os.getenv("BEARER", ""),
)


s.hello()

# Use the SDK ...

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=<no value>&utm_campaign=python)
