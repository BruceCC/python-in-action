import json

# 示例 JSON 数据
data = {
    "workflowKey": "",
    "formItemDirection": "row",
    "dataSource": "",
    "dataSourceName": "",
    "dbTable": "",
    "dbTableName": "",
    "columns": "2",
    "fields": [
        {
            "label": "姓名",
            "parameter": "name",
            "type": "input",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True,
            "placeholderType": "static",
            "placeholderStatic": "请输入",
            "validate": "return /^[a-zA-Z\u4e00-\u9fa5]{2,20}$/.test(val)"
        },
        {
            "label": "手机号",
            "parameter": "phone",
            "type": "input",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True,
            "placeholderType": "static",
            "placeholderStatic": "请输入",
            "validate": "return /^[1][3,4,5,6,7,8,9][0-9]{9}$/.test(val)"
        },
        {
            "label": "性别",
            "parameter": "gender",
            "type": "radio",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True,
            "options": [
                {
                    "value": "男",
                    "label": "男"
                },
                {
                    "value": "女",
                    "label": "女"
                }
            ]
        },
        {
            "label": "出生日期",
            "parameter": "birthday",
            "type": "date",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True
        },
        {
            "label": "身份证号",
            "parameter": "idCard",
            "type": "input",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True,
            "placeholderType": "static",
            "placeholderStatic": "请输入",
            "validate": "return /^[1-8]\\d{5}(18|19|20)\\d{2}(0\\d|10|11|12)([0-2]\\d|30|31)\\d{3}(\\d|X|x)$/.test(val)"
        },
        {
            "label": "邮箱",
            "parameter": "email",
            "type": "input",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True,
            "placeholderType": "static",
            "placeholderStatic": "请输入",
            "validate": "return /^(([^<>()\\[\\]\\.,;:\\s@\"]+(\\.[^<>()\\[\\]\\.,;:\\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/.test(val)"
        },
        {
            "label": "预约日期",
            "parameter": "appointmentDate",
            "type": "date",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True
        },
        {
            "label": "预约时间",
            "parameter": "appointmentTime",
            "type": "time",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True
        },
        {
            "label": "服务项目",
            "parameter": "service",
            "type": "checkbox",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ],
            "required": True,
            "options": [
                {
                    "value": "剪发",
                    "label": "剪发"
                },
                {
                    "value": "洗发",
                    "label": "洗发"
                },
                {
                    "value": "烫发",
                    "label": "烫发"
                },
                {
                    "value": "染发",
                    "label": "染发"
                },
                {
                    "value": "造型",
                    "label": "造型"
                }
            ]
        },
        {
            "label": "备注",
            "parameter": "remark",
            "type": "textarea",
            "edits": [
                {
                    "nodeKey": "new",
                    "nodeName": "new"
                }
            ],
            "displays": [
                {
                    "nodeKey": "all",
                    "nodeName": "all"
                }
            ]
        }
    ]
}

# 格式化输出JSON数据到控制台
# 将 JSON 数据格式化并在控制台输出（支持中文打印）
formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
print(formatted_json)

# 将 JSON 数据格式化并写入文件
# 将 JSON 数据写入 .json 文件（支持中文写入）
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

