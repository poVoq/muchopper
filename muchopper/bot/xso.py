import enum

import aioxmpp
import aioxmpp.forms
import aioxmpp.rsm.xso
import aioxmpp.xso

from aioxmpp.utils import namespaces

from muchopper.common.model import AnonymityMode


namespaces.net_zombofant_muclumbus_search = \
    "https://xmlns.zombofant.net/muclumbus/search/1.0"


class StateTransferV1_0Namespaces(enum.Enum):
    MUCS = "https://xmlns.zombofant.net/muclumbus/state-transfer/1.0/mucs"
    DOMAINS = "https://xmlns.zombofant.net/muclumbus/state-transfer/1.0/domains"


namespaces.net_zombofant_muclumbus_state_transfer_1_0_mucs = \
    StateTransferV1_0Namespaces.MUCS.value

namespaces.net_zombofant_muclumbus_state_transfer_1_0_domains = \
    StateTransferV1_0Namespaces.DOMAINS.value


class SearchForm(aioxmpp.forms.Form):
    FORM_TYPE = namespaces.net_zombofant_muclumbus_search + "#params"

    query = aioxmpp.forms.TextSingle(
        var="q",
        label="Search for",
        required=False,
    )

    search_name = aioxmpp.forms.Boolean(
        var="sinname",
        label="Search in name",
        default=True,
    )

    search_description = aioxmpp.forms.Boolean(
        var="sindescription",
        label="Search in description",
        default=True,
    )

    search_address = aioxmpp.forms.Boolean(
        var="sinaddr",
        label="Search in address",
        default=True,
    )

    min_users = aioxmpp.forms.TextSingle(
        var="min_users",
        label="Minimum number of users",
        type_=aioxmpp.xso.Integer(),
        required=False,
        default=1,
    )

    order_by = aioxmpp.forms.ListSingle(
        var="key",
        label="Sort results by",
        default="nusers",
        options=[
            ("nusers", "Number of online users"),
            ("address", "Address"),
        ]
    )

    LAYOUT = [
        query,
        search_name,
        search_description,
        search_address,
        min_users,
        order_by,
    ]


@aioxmpp.IQ.as_payload_class
class Search(aioxmpp.xso.XSO):
    TAG = (namespaces.net_zombofant_muclumbus_search,
           "search")

    rsm = aioxmpp.xso.Child([
        aioxmpp.rsm.xso.ResultSetMetadata
    ])

    form = aioxmpp.xso.Child([
        aioxmpp.forms.Data,
    ])


class SearchResultItem(aioxmpp.xso.XSO):
    TAG = (namespaces.net_zombofant_muclumbus_search,
           "item")

    address = aioxmpp.xso.Attr(
        "address",
        type_=aioxmpp.xso.JID(),
    )

    name = aioxmpp.xso.ChildText(
        (namespaces.net_zombofant_muclumbus_search, "name"),
        default=None,
    )

    description = aioxmpp.xso.ChildText(
        (namespaces.net_zombofant_muclumbus_search, "description"),
        default=None,
    )

    language = aioxmpp.xso.ChildText(
        (namespaces.net_zombofant_muclumbus_search, "language"),
        default=None,
    )

    nusers = aioxmpp.xso.ChildText(
        (namespaces.net_zombofant_muclumbus_search, "nusers"),
        type_=aioxmpp.xso.Integer(),
        default=None,
    )

    is_open = aioxmpp.xso.ChildFlag(
        (namespaces.net_zombofant_muclumbus_search, "is-open"),
    )

    anonymity_mode = aioxmpp.xso.ChildText(
        (namespaces.net_zombofant_muclumbus_search, "anonymity-mode"),
        type_=aioxmpp.xso.EnumCDataType(AnonymityMode),
        default=None,
    )


@aioxmpp.IQ.as_payload_class
class SearchResult(aioxmpp.xso.XSO):
    TAG = (namespaces.net_zombofant_muclumbus_search,
           "result")

    items = aioxmpp.xso.ChildList([
        SearchResultItem,
    ])

    rsm = aioxmpp.xso.Child([
        aioxmpp.rsm.xso.ResultSetMetadata,
    ])


@aioxmpp.pubsub.xso.as_payload_class
class SyncItemMUC(aioxmpp.xso.XSO):
    TAG = (
        StateTransferV1_0Namespaces.MUCS.value,
        "muc"
    )

    address = aioxmpp.xso.Attr(
        "address",
        type_=aioxmpp.xso.JID(),
    )

    name = aioxmpp.xso.ChildText(
        (StateTransferV1_0Namespaces.MUCS.value, "name"),
        default=None,
    )

    description = aioxmpp.xso.ChildText(
        (StateTransferV1_0Namespaces.MUCS.value, "description"),
        default=None,
    )

    language = aioxmpp.xso.ChildText(
        (StateTransferV1_0Namespaces.MUCS.value, "language"),
        default=None,
    )

    nusers = aioxmpp.xso.ChildText(
        (StateTransferV1_0Namespaces.MUCS.value, "nusers"),
        type_=aioxmpp.xso.Float(),
        default=None,
    )

    is_open = aioxmpp.xso.ChildFlag(
        (StateTransferV1_0Namespaces.MUCS.value, "is-open"),
    )

    anonymity_mode = aioxmpp.xso.ChildText(
        (StateTransferV1_0Namespaces.MUCS.value, "anonymity-mode"),
        type_=aioxmpp.xso.EnumCDataType(AnonymityMode),
        default=None,
    )
