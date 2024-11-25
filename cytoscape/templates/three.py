# Meal Decision Tree Template
default_elements = [
    # Root Node
    {
        'data': {
            'id': 'root',
            'label': 'Meal Time',
            'weight': 25,  # Chance that the decision ends at this node
            'level': 1,
            'children': 3,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Time of Day', 'field_value': 'Any'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Any'},
            'custom3': {'field_name': 'Dietary Preference', 'field_value': 'Any'}
        }
    },
    # Level 2 Nodes
    {
        'data': {
            'id': 'breakfast',
            'label': 'Breakfast',
            'weight': 25,
            'level': 2,
            'children': 3,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Time of Day', 'field_value': 'Morning'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Continental'},
            'custom3': {'field_name': 'Dietary Preference', 'field_value': 'Any'}
        }
    },
    {
        'data': {
            'id': 'lunch',
            'label': 'Lunch',
            'weight': 25,
            'level': 2,
            'children': 3,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Time of Day', 'field_value': 'Afternoon'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Any'},
            'custom3': {'field_name': 'Dietary Preference', 'field_value': 'Any'}
        }
    },
    {
        'data': {
            'id': 'dinner',
            'label': 'Dinner',
            'weight': 25,
            'level': 2,
            'children': 3,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Time of Day', 'field_value': 'Evening'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Any'},
            'custom3': {'field_name': 'Dietary Preference', 'field_value': 'Any'}
        }
    },
    # Breakfast Options
    {
        'data': {
            'id': 'pancakes',
            'label': 'Pancakes',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Sweetness', 'field_value': 'High'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'American'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '15 mins'}
        }
    },
    {
        'data': {
            'id': 'omelette',
            'label': 'Omelette',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Protein Rich', 'field_value': 'Yes'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'French'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '10 mins'}
        }
    },
    {
        'data': {
            'id': 'cereal',
            'label': 'Cereal',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Quick Meal', 'field_value': 'Yes'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Any'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '5 mins'}
        }
    },
    # Lunch Options
    {
        'data': {
            'id': 'sandwich',
            'label': 'Sandwich',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Vegetarian', 'field_value': 'Optional'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Any'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '10 mins'}
        }
    },
    {
        'data': {
            'id': 'salad',
            'label': 'Salad',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Healthy', 'field_value': 'Yes'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Mediterranean'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '15 mins'}
        }
    },
    {
        'data': {
            'id': 'soup',
            'label': 'Soup',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Warm Meal', 'field_value': 'Yes'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Various'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '20 mins'}
        }
    },
    # Dinner Options
    {
        'data': {
            'id': 'steak',
            'label': 'Steak',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Protein Rich', 'field_value': 'High'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'American'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '30 mins'}
        }
    },
    {
        'data': {
            'id': 'pasta',
            'label': 'Pasta',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Comfort Food', 'field_value': 'Yes'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Italian'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '25 mins'}
        }
    },
    {
        'data': {
            'id': 'stirfry',
            'label': 'Stir-fry',
            'weight': 100,
            'level': 3,
            'children': 0,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False',
            'custom1': {'field_name': 'Quick Meal', 'field_value': 'Yes'},
            'custom2': {'field_name': 'Cuisine', 'field_value': 'Asian'},
            'custom3': {'field_name': 'Preparation Time', 'field_value': '15 mins'}
        }
    },
    # Edges from Root
    {
        'data': {
            'id': 'root_breakfast',
            'source': 'root',
            'target': 'breakfast',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'root_lunch',
            'source': 'root',
            'target': 'lunch',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'root_dinner',
            'source': 'root',
            'target': 'dinner',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    # Edges from Breakfast
    {
        'data': {
            'id': 'breakfast_pancakes',
            'source': 'breakfast',
            'target': 'pancakes',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'breakfast_omelette',
            'source': 'breakfast',
            'target': 'omelette',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'breakfast_cereal',
            'source': 'breakfast',
            'target': 'cereal',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    # Edges from Lunch
    {
        'data': {
            'id': 'lunch_sandwich',
            'source': 'lunch',
            'target': 'sandwich',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'lunch_salad',
            'source': 'lunch',
            'target': 'salad',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'lunch_soup',
            'source': 'lunch',
            'target': 'soup',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    # Edges from Dinner
    {
        'data': {
            'id': 'dinner_steak',
            'source': 'dinner',
            'target': 'steak',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'dinner_pasta',
            'source': 'dinner',
            'target': 'pasta',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    },
    {
        'data': {
            'id': 'dinner_stirfry',
            'source': 'dinner',
            'target': 'stirfry',
            'weight': 25,
            'traversed': 'False',
            'common': 'False',
            'invalid_weight': 'False',
            'last_clicked': 'False'
        }
    }
]
