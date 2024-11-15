default_elements = [
    # Nodes with additional properties
    {
        'data': {
            'id': 'root',
            'label': 'Wake up',
            'weight': 25,
            'level': 1,
            'children': 2,
            'Productive?': 'Yes',
            'Mood Impact': 'Increase',
            'Fun Level': '6',
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'two',
            'label': 'Check Phone',
            'weight': 25,
            'level': 2,
            'Productive?': 'Yes',
            'Mood Impact': 'Increase',
            'Fun Level': '6',
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'three',
            'label': 'Take Shower',
            'weight': 100,
            'children': 0,
            'level': 2,
            'Productive?': 'Yes',
            'Mood Impact': 'Increase',
            'Fun Level': '6',
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'four',
            'label': 'Drink Coffee',
            'weight': 100,
            'children': 0,
            'level': 3,
            'Productive?': 'Yes',
            'Mood Impact': 'Increase',
            'Fun Level': '6',
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'five',
            'label': 'Stretch',
            'weight': 100,
            'children': 0,
            'level': 3,
            'Productive?': 'Yes',
            'Mood Impact': 'Increase',
            'Fun Level': '6',
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    # Edges with additional properties
    {
        'data': {
            'id': 'root_two',
            'source': 'root',
            'target': 'two',
            'weight': 37.5,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'root_three',
            'source': 'root',
            'target': 'three',
            'weight': 37.5,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'two_four',
            'source': 'two',
            'target': 'four',
            'weight': 75,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'two_five',
            'source': 'two',
            'target': 'five',
            'weight': 75,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    }
]
