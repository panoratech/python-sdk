"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from panora_sdk.types import BaseModel
from typing import TypedDict


class EventResponseType(str, Enum):
    r"""Scope of the event"""
    CRM_CONTACT_CREATED = "crm.contact.created"
    CRM_CONTACT_PULLED = "crm.contact.pulled"
    CRM_COMPANY_CREATED = "crm.company.created"
    CRM_COMPANY_PULLED = "crm.company.pulled"
    CRM_DEAL_CREATED = "crm.deal.created"
    CRM_DEAL_PULLED = "crm.deal.pulled"
    CRM_ENGAGEMENT_CREATED = "crm.engagement.created"
    CRM_ENGAGEMENT_PULLED = "crm.engagement.pulled"
    CRM_NOTE_CREATED = "crm.note.created"
    CRM_NOTE_PULLED = "crm.note.pulled"
    CRM_STAGE_PULLED = "crm.stage.pulled"
    CRM_TASK_PULLED = "crm.task.pulled"
    CRM_TASK_CREATED = "crm.task.created"
    CRM_USER_PULLED = "crm.user.pulled"
    TICKETING_TICKET_CREATED = "ticketing.ticket.created"
    TICKETING_TICKET_PULLED = "ticketing.ticket.pulled"
    TICKETING_COMMENT_CREATED = "ticketing.comment.created"
    TICKETING_COMMENT_PULLED = "ticketing.comment.pulled"
    TICKETING_ATTACHMENT_CREATED = "ticketing.attachment.created"
    TICKETING_ATTACHMENT_PULLED = "ticketing.attachment.pulled"
    TICKETING_COLLECTION_PULLED = "ticketing.collection.pulled"
    TICKETING_ACCOUNT_PULLED = "ticketing.account.pulled"
    TICKETING_CONTACT_PULLED = "ticketing.contact.pulled"
    TICKETING_TAG_PULLED = "ticketing.tag.pulled"
    TICKETING_TEAM_PULLED = "ticketing.team.pulled"
    TICKETING_USER_PULLED = "ticketing.user.pulled"
    ATS_ACTIVITY_CREATED = "ats.activity.created"
    ATS_ACTIVITY_PULLED = "ats.activity.pulled"
    ATS_APPLICATION_CREATED = "ats.application.created"
    ATS_APPLICATION_PULLED = "ats.application.pulled"
    ATS_ATTACHMENT_CREATED = "ats.attachment.created"
    ATS_ATTACHMENT_PULLED = "ats.attachment.pulled"
    ATS_CANDIDATE_CREATED = "ats.candidate.created"
    ATS_CANDIDATE_PULLED = "ats.candidate.pulled"
    ATS_DEPARTMENT_PULLED = "ats.department.pulled"
    ATS_EECOS_PULLED = "ats.eecos.pulled"
    ATS_INTERVIEW_CREATED = "ats.interview.created"
    ATS_INTERVIEW_PULLED = "ats.interview.pulled"
    ATS_JOB_PULLED = "ats.job.pulled"
    ATS_JOBINTERVIEWSTAGE_PULLED = "ats.jobinterviewstage.pulled"
    ATS_OFFER_CREATED = "ats.offer.created"
    ATS_OFFICE_PULLED = "ats.office.pulled"
    ATS_REJECTREASON_PULLED = "ats.rejectreason.pulled"
    ATS_SCORECARD_PULLED = "ats.scorecard.pulled"
    ATS_TAG_PULLED = "ats.tag.pulled"
    ATS_USER_PULLED = "ats.user.pulled"
    FILESTORAGE_FILE_PULLED = "filestorage.file.pulled"
    FILESTORAGE_FOLDER_PULLED = "filestorage.folder.pulled"
    FILESTORAGE_GROUP_PULLED = "filestorage.group.pulled"
    FILESTORAGE_USER_PULLED = "filestorage.user.pulled"
    FILESTORAGE_DRIVE_PULLED = "filestorage.drive.pulled"
    FILESTORAGE_PERMISSION_PULLED = "filestorage.permission.pulled"
    FILESTORAGE_SHAREDLINK_PULLED = "filestorage.sharedlink.pulled"
    CONNECTION_CREATED = "connection.created"

class EventResponseStatus(str, Enum):
    r"""Status of the event"""
    SUCCESS = "success"
    FAIL = "fail"

class Method(str, Enum):
    r"""HTTP method used for the event"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class EventResponseTypedDict(TypedDict):
    id_event: str
    r"""Unique identifier for the event"""
    id_connection: str
    r"""Connection ID associated with the event"""
    id_project: str
    r"""Project ID associated with the event"""
    type: EventResponseType
    r"""Scope of the event"""
    status: EventResponseStatus
    r"""Status of the event"""
    direction: str
    r"""Direction of the event"""
    method: Method
    r"""HTTP method used for the event"""
    url: str
    r"""URL associated with the event"""
    provider: str
    r"""Provider associated with the event"""
    timestamp: datetime
    r"""Timestamp of the event"""
    id_linked_user: str
    r"""Linked user ID associated with the event"""
    

class EventResponse(BaseModel):
    id_event: str
    r"""Unique identifier for the event"""
    id_connection: str
    r"""Connection ID associated with the event"""
    id_project: str
    r"""Project ID associated with the event"""
    type: EventResponseType
    r"""Scope of the event"""
    status: EventResponseStatus
    r"""Status of the event"""
    direction: str
    r"""Direction of the event"""
    method: Method
    r"""HTTP method used for the event"""
    url: str
    r"""URL associated with the event"""
    provider: str
    r"""Provider associated with the event"""
    timestamp: datetime
    r"""Timestamp of the event"""
    id_linked_user: str
    r"""Linked user ID associated with the event"""
    
