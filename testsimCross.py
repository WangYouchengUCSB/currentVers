simType ='sym_file'
simProps = [
  {
    "name": "transitive_dax",
    "RBs": [
      {
        "pred_name": "dax",
        "pred_sem": [["action1", 1.0, None, None, None], ["action2", 1.0, None, None, None], ["action3", 1.0, None, None, None]],
        "higher_order": False,
        "object_name": "toy",
        "object_sem": [["toy1", 1.0, None, None], ["toy2", 1.0, None, None], ["toy3", 1.0, None, None]],
        "P": "non_exist"
      },
      {
        "pred_name": "agent",
        "pred_sem": [["human1", 1.0, None, None, None], ["human2", 1.0, None, None, None], ["human3", 1.0, None, None, None]],
        "higher_order": False,
        "object_name": "she",
        "object_sem": [["she1", 1.0, None, None], ["she2", 1.0, None, None], ["she3", 1.0, None, None]],
        "P": "non_exist"
      }
    ],
    "set": "memory",
    "analog": 0
  },
  {
    "name": "intransitive_dax",
    "RBs": [
      {
        "pred_name": "dax",
        "pred_sem": [["action1", 1.0, None, None, None], ["action2", 1.0, None, None, None], ["action3", 1.0, None, None, None]],
        "higher_order": False,
        "object_name": "she",
        "object_sem": [["she1", 1.0, None, None], ["she2", 1.0, None, None], ["she3", 1.0, None, None]],
        "P": "non_exist"
      }
    ],
    "set": "memory",
    "analog": 0
  }
]




