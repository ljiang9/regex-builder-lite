import re
import unittest

from regex_builder import build, TEMPLATES


class TestBuilder(unittest.TestCase):
    def test_email(self):
        r = build("我想匹配邮箱")
        self.assertIsNotNone(r["pattern"])
        self.assertRegex("user@example.com", r["pattern"])

    def test_phone(self):
        r = build("手机号")
        self.assertTrue(re.search(r["pattern"], "联系 13800138000 我"))

    def test_date(self):
        r = build("日期格式")
        self.assertRegex("2026-10-06", r["pattern"])

    def test_url(self):
        r = build("url")
        self.assertRegex("visit https://example.com now", r["pattern"])

    def test_unknown(self):
        r = build("量子引力")
        self.assertIsNone(r["pattern"])

    def test_all_templates_match_example(self):
        for key, (pat, _) in TEMPLATES.items():
            r = build(key)
            self.assertRegex(r["example"], pat)


if __name__ == "__main__":
    unittest.main()
