"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from panora_sdk.activities import Activities
from panora_sdk.applications import Applications
from panora_sdk.attachments import Attachments
from panora_sdk.candidates import Candidates
from panora_sdk.departments import Departments
from panora_sdk.eeocs import Eeocs
from panora_sdk.interviews import Interviews
from panora_sdk.jobinterviewstages import Jobinterviewstages
from panora_sdk.jobs import Jobs
from panora_sdk.offers import Offers
from panora_sdk.offices import Offices
from panora_sdk.panora_ats_users import PanoraAtsUsers
from panora_sdk.panora_tags import PanoraTags
from panora_sdk.rejectreasons import Rejectreasons
from panora_sdk.scorecards import Scorecards


class Ats(BaseSDK):
    activities: Activities
    applications: Applications
    attachments: Attachments
    candidates: Candidates
    departments: Departments
    interviews: Interviews
    jobinterviewstages: Jobinterviewstages
    jobs: Jobs
    offers: Offers
    offices: Offices
    rejectreasons: Rejectreasons
    scorecards: Scorecards
    tags: PanoraTags
    users: PanoraAtsUsers
    eeocs: Eeocs

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.activities = Activities(self.sdk_configuration)
        self.applications = Applications(self.sdk_configuration)
        self.attachments = Attachments(self.sdk_configuration)
        self.candidates = Candidates(self.sdk_configuration)
        self.departments = Departments(self.sdk_configuration)
        self.interviews = Interviews(self.sdk_configuration)
        self.jobinterviewstages = Jobinterviewstages(self.sdk_configuration)
        self.jobs = Jobs(self.sdk_configuration)
        self.offers = Offers(self.sdk_configuration)
        self.offices = Offices(self.sdk_configuration)
        self.rejectreasons = Rejectreasons(self.sdk_configuration)
        self.scorecards = Scorecards(self.sdk_configuration)
        self.tags = PanoraTags(self.sdk_configuration)
        self.users = PanoraAtsUsers(self.sdk_configuration)
        self.eeocs = Eeocs(self.sdk_configuration)
