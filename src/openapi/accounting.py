"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from openapi.addresses import Addresses
from openapi.balancesheets import Balancesheets
from openapi.cashflowstatements import Cashflowstatements
from openapi.companyinfos import Companyinfos
from openapi.creditnotes import Creditnotes
from openapi.expenses import Expenses
from openapi.incomestatements import Incomestatements
from openapi.invoices import Invoices
from openapi.items import Items
from openapi.journalentries import Journalentries
from openapi.payments import Payments
from openapi.phonenumbers import Phonenumbers
from openapi.purchaseorders import Purchaseorders
from openapi.sdk_accounting_contacts import SDKAccountingContacts
from openapi.sdk_accounts import SDKAccounts
from openapi.sdk_attachments import SDKAttachments
from openapi.taxrates import Taxrates
from openapi.trackingcategories import Trackingcategories
from openapi.transactions import Transactions
from openapi.vendorcredits import Vendorcredits

class Accounting(BaseSDK):
    accounts: SDKAccounts
    addresses: Addresses
    attachments: SDKAttachments
    balancesheets: Balancesheets
    cashflowstatements: Cashflowstatements
    companyinfos: Companyinfos
    contacts: SDKAccountingContacts
    creditnotes: Creditnotes
    expenses: Expenses
    incomestatements: Incomestatements
    invoices: Invoices
    items: Items
    journalentries: Journalentries
    payments: Payments
    phonenumbers: Phonenumbers
    purchaseorders: Purchaseorders
    taxrates: Taxrates
    trackingcategories: Trackingcategories
    transactions: Transactions
    vendorcredits: Vendorcredits
    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.accounts = SDKAccounts(self.sdk_configuration)
        self.addresses = Addresses(self.sdk_configuration)
        self.attachments = SDKAttachments(self.sdk_configuration)
        self.balancesheets = Balancesheets(self.sdk_configuration)
        self.cashflowstatements = Cashflowstatements(self.sdk_configuration)
        self.companyinfos = Companyinfos(self.sdk_configuration)
        self.contacts = SDKAccountingContacts(self.sdk_configuration)
        self.creditnotes = Creditnotes(self.sdk_configuration)
        self.expenses = Expenses(self.sdk_configuration)
        self.incomestatements = Incomestatements(self.sdk_configuration)
        self.invoices = Invoices(self.sdk_configuration)
        self.items = Items(self.sdk_configuration)
        self.journalentries = Journalentries(self.sdk_configuration)
        self.payments = Payments(self.sdk_configuration)
        self.phonenumbers = Phonenumbers(self.sdk_configuration)
        self.purchaseorders = Purchaseorders(self.sdk_configuration)
        self.taxrates = Taxrates(self.sdk_configuration)
        self.trackingcategories = Trackingcategories(self.sdk_configuration)
        self.transactions = Transactions(self.sdk_configuration)
        self.vendorcredits = Vendorcredits(self.sdk_configuration)
    
