import tap_zendesk_chat
import unittest


class BaseMetadata:
    """
    creates a Base class for metadata
    """
    metadata = [{"breadcrumb": [], "metadata": {"valid-replication-keys": [],
                "table-key-properties": ["id"], "selected": True}}, {"breadcrumb": ["properties", "create_date"],
                "metadata": {"inclusion": "available"}}]


class Departments(BaseMetadata):
    """
    Class for Departments stream
    inherits BaseMetadata class
    """
    stream = 'departments'
    schema = {}
    properties = ['description', 'name', 'id', 'enabled', 'members', 'settings']


class Account(BaseMetadata):
    """
    Class for Account stream
    inherits BaseMetadata class
    """
    stream = 'account'
    properties = ['create_date', 'account_key', 'status', 'billing', 'plan']


class Bans:
    """
    Class for Bans stream
    has its own metadata attribute
    """
    stream = 'bans'
    properties = []
    metadata = [{"breadcrumb": [], "metadata": {"valid-replication-keys": [],
                "table-key-properties": ["id"], "selected": False}}, {"breadcrumb": ["properties", "create_date"],
                "metadata": {"inclusion": "available"}}]


class TestMetadataFunctions(unittest.TestCase):
    """
    Used to test metadata functions defined in tap_zendesk_chat/__init__.py file
    """
    POSITIVE_TEST_STREAMS = [Account, Departments]
    NEGATIVE_TEST_STREAM = [Bans]

    def test_is_selected(self):
        """
        tests is_selected fn in tap_zendesk_chat/__init__.py file
        checks if selected field is set as true in metadata
        """
        for stream in self.POSITIVE_TEST_STREAMS:
            self.assertEqual(True, tap_zendesk_chat.is_selected(stream))

        for stream in self.NEGATIVE_TEST_STREAM:
            self.assertEqual(False, tap_zendesk_chat.is_selected(stream))

    def test_load_schema(self):
        """
         tests load_schema fn in tap_zendesk_chat/__init__.py file
         checks if length of properties attr equals with size of properties in loaded schema using load_schema fn
        """
        for stream in self.POSITIVE_TEST_STREAMS:
            self.assertEquals(len(stream.properties), len(tap_zendesk_chat.load_schema(stream.stream)['properties']))

        for stream in self.NEGATIVE_TEST_STREAM:
            self.assertNotEqual(len(stream.properties), len(tap_zendesk_chat.load_schema(stream.stream)['properties']))



