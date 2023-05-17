"""Unit test for erd_diagram_generator"""

import unittest
from unittest.mock import MagicMock, patch

from aind_data_schema.utils.erd_generator import ErdGenerator


class ErdGeneratorTests(unittest.TestCase):
    """Class for testing ErdGenerator"""

    @patch("aind_data_schema.utils.erd_generator.ErdGenerator")
    def test_erd_generator_object(self, mock_generator: MagicMock):
        """Tests the object constructor for ErdDiagramGenerator"""

        self.assertFalse(mock_generator.called)
        mock_generator([])
        mock_generator.assert_called_with([])
        mock_generator(["BehaviorRig", "OphysSession"])
        mock_generator.assert_called_with(["BehaviorRig", "OphysSession"])

    @patch.object(ErdGenerator, "generate_aind_core_model_diagrams")
    def test_generate_ACM_erds(self, mock_generator: MagicMock):
        """
        Tests that erdgenerator is being called properly

        TODO: Add test that checks for path write attempt
        """

        ErdGenerator.generate_aind_core_model_diagrams()
        self.assertTrue(mock_generator.called)

    @patch.object(ErdGenerator, "generate_erd_diagram")
    def test_generate_single_erd(self, mock_generator: MagicMock):
        """
        Tests that erdgenerator is being called properly

        TODO: Add test that checks for path write attempt
        """

        ErdGenerator.generate_erd_diagram(ErdGenerator)
        mock_generator.assert_called_with(ErdGenerator)


if __name__ == "__main__":
    unittest.main()
