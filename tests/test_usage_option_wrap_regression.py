"""Usage help must keep hyphenated command-line option names intact."""

import unittest

from click.formatting import HelpFormatter, wrap_text


class TestUsageOptionWrapping(unittest.TestCase):
    def test_long_option_names_are_never_split_at_internal_hyphens(self):
        formatter = HelpFormatter(width=35)
        formatter.write_usage(
            "tool", "--enable-verbose-logging --output-file-path"
        )
        usage = formatter.getvalue()

        self.assertIn("--enable-verbose-logging", usage)
        self.assertIn("--output-file-path", usage)
        self.assertEqual(usage.count("\n"), 2)

    def test_long_command_name_keeps_options_intact_on_following_lines(self):
        formatter = HelpFormatter(width=25)
        formatter.write_usage(
            "extraordinarily-long-tool", "--enable-verbose-logging --output-file-path"
        )
        usage = formatter.getvalue()

        self.assertIn("--enable-verbose-logging", usage)
        self.assertIn("--output-file-path", usage)

    def test_general_prose_wrapping_keeps_existing_hyphen_behavior(self):
        self.assertEqual(wrap_text("alpha-beta gamma", width=8), "alpha-\nbeta\ngamma")


if __name__ == "__main__":
    unittest.main()
