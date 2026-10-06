#!/usr/bin/env python3
"""regex_builder —— 自然语言意图 -> 正则模板。

内置常见模板：邮箱、中国大陆手机号、日期、URL、邮编。
根据意图名返回 (正则, 中文说明)。零第三方依赖。

用法：
    from regex_builder import build
    pat, desc = build("邮箱")
"""
from __future__ import annotations

import argparse
import re
import sys

TEMPLATES = {
    "邮箱": (r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "匹配电子邮箱地址"),
    "手机号": (r"1[3-9]\d{9}", "匹配中国大陆 11 位手机号"),
    "日期": (r"\d{4}[-/]\d{1,2}[-/]\d{1,2}", "匹配 YYYY-MM-DD 或 YYYY/M/D 日期"),
    "url": (r"https?://[^\s]+", "匹配 http/https 链接"),
    "邮编": (r"\d{6}", "匹配 6 位邮政编码"),
}


def build(intent: str) -> dict:
    key = None
    for k in TEMPLATES:
        if k in intent or k.lower() in intent.lower():
            key = k
            break
    if not key:
        return {"pattern": None, "desc": "未识别的意图", "example": None}
    pat, desc = TEMPLATES[key]
    return {"pattern": pat, "desc": desc, "example": _example(key)}


def _example(key: str) -> str:
    return {
        "邮箱": "user@example.com",
        "手机号": "13800138000",
        "日期": "2026-01-01",
        "url": "https://example.com",
        "邮编": "100000",
    }[key]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="自然语言 -> 正则")
    p.add_argument("intent", nargs="?", help="如：邮箱 / 手机号 / 日期")
    args = p.parse_args(argv)
    intent = args.intent or sys.stdin.read()
    r = build(intent)
    if not r["pattern"]:
        print(r["desc"])
        return 1
    print(f"说明：{r['desc']}")
    print(f"正则：{r['pattern']}")
    print(f"示例：{r['example']}")
    m = re.search(r["pattern"], r["example"])
    print(f"示例匹配：{bool(m)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
