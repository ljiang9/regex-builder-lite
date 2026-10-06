# regex-builder-lite

自然语言意图 → 正则模板：内置邮箱/手机号/日期/URL/邮编，返回正则与说明。
零第三方依赖。

## 功能简介

- `build("邮箱")` → `{pattern, desc, example}`；
- 每个模板都给出示例，正则可直接匹配示例；
- 未识别意图返回 `pattern=None`。

## 快速开始

```bash
python3 regex_builder.py 邮箱
python3 regex_builder.py 手机号
```

## 无 API key 如何运行

纯模板，**不需要任何 API key**。

## 目录结构

```
regex-builder-lite/
├── regex_builder.py
├── tests/test_regex_builder.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
