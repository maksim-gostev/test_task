CUSTOM_LISTS_TEMPLATE = { "customcards":         {
        "options":{
          "search_enabled":True,
          "save_position":True
        },

        "layout": {
        "type": "LinearLayout",
        "orientation": "vertical",
        "height": "match_parent",
        "width": "match_parent",
        "weight": "0",
        "Elements": [
        {
            "type": "LinearLayout",
            "orientation": "horizontal",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
            "type": "Picture",
            "show_by_condition": "",
            "Value": "@pic1",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "16",
            "TextColor": "#DB7093",
            "TextBold": True,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "wrap_content",
            "weight": 2
            },
            {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "wrap_content",
            "width": "match_parent",
            "weight": "1",
            "Elements": [
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@string1",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": ""
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@string2",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": ""
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@string3",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": ""
            }
            ]
            },
            {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@val",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "16",
            "TextColor": "#DB7093",
            "TextBold": True,
            "TextItalic": False,
            "BackgroundColor": "",
            "width": "match_parent",
            "height": "wrap_content",
            "weight": 2
            }
            ]
        },
        {
            "type": "TextView",
            "show_by_condition": "",
            "Value": "@descr",
            "NoRefresh": False,
            "document_type": "",
            "mask": "",
            "Variable": "",
            "TextSize": "-1",
            "TextColor": "#6F9393",
            "TextBold": False,
            "TextItalic": True,
            "BackgroundColor": "",
            "width": "wrap_content",
            "height": "wrap_content",
            "weight": 0
        }
        ]
    }

}
}
