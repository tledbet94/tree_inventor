default_elements = [
    # Nodes with additional properties
    {
        'data': {
            'id': 'root',
            'label': 'Wake up',
            'weight': 25,
            'level': 1,
            'children': 2,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1':
                {'field_name': 'Productive?',
                 'field_value': 'Yes'},
            'custom2':
                {'field_name': 'Mood Impact',
                 'field_value': 'Boost'},
            'custom3':
                {'field_name': 'Fun Level',
                 'field_value': 10},
        }
    },
    {
        'data': {
            'id': 'two',
            'label': 'Check Phone',
            'weight': 25,
            'level': 2,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1':
                {'field_name': 'Productive?',
                 'field_value': 'Yes'},
            'custom2':
                {'field_name': 'Mood Impact',
                 'field_value': 'Boost'},
            'custom3':
                {'field_name': 'Fun Level',
                 'field_value': 10},
        }
    },
    {
        'data': {
            'id': 'three',
            'label': 'Take Shower',
            'weight': 100,
            'children': 0,
            'level': 2,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1':
                {'field_name': 'Productive?',
                 'field_value': 'Yes'},
            'custom2':
                {'field_name': 'Mood Impact',
                 'field_value': 'Boost'},
            'custom3':
                {'field_name': 'Fun Level',
                 'field_value': 10},
        }
    },
    {
        'data': {
            'id': 'four',
            'label': 'Drink Coffee',
            'weight': 100,
            'children': 0,
            'level': 3,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1':
                {'field_name': 'Productive?',
                 'field_value': 'Yes'},
            'custom2':
                {'field_name': 'Mood Impact',
                 'field_value': 'Boost'},
            'custom3':
                {'field_name': 'Fun Level',
                 'field_value': 10},

        }
    },
    {
        'data': {
            'id': 'five',
            'label': 'Stretch',
            'weight': 100,
            'children': 0,
            'level': 3,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1':
                {'field_name': 'Productive?',
                 'field_value': 'Yes'},
            'custom2':
                {'field_name': 'Mood Impact',
                 'field_value': 'Boost'},
            'custom3':
                {'field_name': 'Fun Level',
                 'field_value': 10},
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
            'weight': 37.5,
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
            'weight': 37.5,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    }
]
