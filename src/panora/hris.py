"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from panora.bankinfos import Bankinfos
from panora.benefits import Benefits
from panora.dependents import Dependents
from panora.employeepayrollruns import Employeepayrollruns
from panora.employees import Employees
from panora.employerbenefits import Employerbenefits
from panora.employments import Employments
from panora.groups import Groups
from panora.locations import Locations
from panora.panora_companies import PanoraCompanies
from panora.paygroups import Paygroups
from panora.payrollruns import Payrollruns
from panora.timeoffbalances import Timeoffbalances
from panora.timeoffs import Timeoffs

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
    
