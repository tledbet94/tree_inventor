default_elements = [
    # Nodes with additional properties
    {'data':
         {'id': 'one',
          'label': 'Wake up',
          'weight': 5,
          'Productive?': 'Yes',
          'Mood Impact': 'Increase',
          'Fun Level': '6'}},

    {'data':
         {'id': 'two',
          'label': 'Check Phone',
          'weight': 3,
          'Productive?': 'Yes',
          'Mood Impact': 'Increase',
          'Fun Level': '6'}},

    {'data':
         {'id': 'three',
          'label': 'Take Shower',
          'weight': 4,
          'Productive?': 'Yes',
          'Mood Impact': 'Increase',
          'Fun Level': '6'}},

    {'data':
         {'id': 'four',
          'label': 'Drink Coffee',
          'weight': 2,
          'Productive?': 'Yes',
          'Mood Impact': 'Increase',
          'Fun Level': '6'}},

    {'data':
         {'id': 'five',
          'label': 'Stretch',
          'weight': 1,
          'Productive?': 'Yes',
          'Mood Impact': 'Increase',
          'Fun Level': '6'}},

    # Edges with additional properties
    {'data':
         {'source': 'one',
          'target': 'two',
          'weight': 10}},

    {'data':
         {'source': 'one',
          'target': 'three',
          'weight': 8}},

    {'data':
         {'source': 'two',
          'target': 'four',
          'weight': 6}},

    {'data':
         {'source': 'two', 'target':
             'five', 'weight': 7}}
]
