"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from panora_sdk.bankinfos import Bankinfos
from panora_sdk.benefits import Benefits
from panora_sdk.dependents import Dependents
from panora_sdk.employeepayrollruns import Employeepayrollruns
from panora_sdk.employees import Employees
from panora_sdk.employerbenefits import Employerbenefits
from panora_sdk.employments import Employments
from panora_sdk.groups import Groups
from panora_sdk.locations import Locations
from panora_sdk.panora_companies import PanoraCompanies
from panora_sdk.paygroups import Paygroups
from panora_sdk.payrollruns import Payrollruns
from panora_sdk.timeoffbalances import Timeoffbalances
from panora_sdk.timeoffs import Timeoffs

class Hris(BaseSDK):
    bankinfos: Bankinfos
    benefits: Benefits
    companies: PanoraCompanies
    dependents: Dependents
    employeepayrollruns: Employeepayrollruns
    employees: Employees
    employerbenefits: Employerbenefits
    employments: Employments
    groups: Groups
    locations: Locations
    paygroups: Paygroups
    payrollruns: Payrollruns
    timeoffs: Timeoffs
    timeoffbalances: Timeoffbalances
    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()
    
    def _init_sdks(self):
        self.bankinfos = Bankinfos(self.sdk_configuration)
        self.benefits = Benefits(self.sdk_configuration)
        self.companies = PanoraCompanies(self.sdk_configuration)
        self.dependents = Dependents(self.sdk_configuration)
        self.employeepayrollruns = Employeepayrollruns(self.sdk_configuration)
        self.employees = Employees(self.sdk_configuration)
        self.employerbenefits = Employerbenefits(self.sdk_configuration)
        self.employments = Employments(self.sdk_configuration)
        self.groups = Groups(self.sdk_configuration)
        self.locations = Locations(self.sdk_configuration)
        self.paygroups = Paygroups(self.sdk_configuration)
        self.payrollruns = Payrollruns(self.sdk_configuration)
        self.timeoffs = Timeoffs(self.sdk_configuration)
        self.timeoffbalances = Timeoffbalances(self.sdk_configuration)
    