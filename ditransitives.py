simType = 'sym_file'

symProps = [
    {
        "name": "giveJohnMaryBook",
        "RBs": [
            {
                "pred_name": "giver",
                "pred_sem": ["giver1", "giver2", "giver3", "giver4"],
                "higher_order": False,
                "object_name": "John",
                "object_sem": ["john1", "john2", "john3", "john4"],
                "P": "non_exist"
            },
            {
                "pred_name": "recipient",
                "pred_sem": ["recipient1", "recipient2", "recipient3", "recipient4"],
                "higher_order": False,
                "object_name": "Mary",
                "object_sem": ["mary1", "mary2", "mary3", "mary4"],
                "P": "non_exist"
            },
            {
                "pred_name": "theme",
                "pred_sem": ["theme1", "theme2", "theme3", "theme4"],
                "higher_order": False,
                "object_name": "Book",
                "object_sem": ["book1", "book2", "book3", "book4"],
                "P": "non_exist"
            }
        ],
        "set": "memory",
        "analog": 0
    }
]
