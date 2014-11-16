from Yowsup.structs import ProtocolTreeNode
from .clean_iq import CleanIqProtocolEntity
from Yowsup.layers.protocol_iq.protocolentities.test_iq import IqProtocolEntityTest

class CleanIqProtocolEntityTest(IqProtocolEntityTest):
    def setUp(self):
        super(CleanIqProtocolEntityTest, self).setUp()
        self.ProtocolEntity = CleanIqProtocolEntity
        cleanNode = ProtocolTreeNode("clean", {"type": "groups"})
        self.node.addChild(cleanNode)