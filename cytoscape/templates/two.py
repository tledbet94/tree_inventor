default_elements = [
    # Nodes with additional properties
    # commenting to explain functionality
    # comments on first node and first edge
    # overall - using cytoscape dag structure
    # on weights - weights are based on a node and edges belonging to that node
    # if node is leaf, weight is 100% because there is nowhere else to go
    # if node is branch, weight is non-100% because there are potential paths other than the node
    # paths are defined as child edges that lead to new nodes
    # root logic is similar to paths
    # the weight in the node is the % chance that it is the terminal node
    # the weight in the edges is the % chance that the edge transfers the current node to the next node
    # this is built for traversals to take place starting from the root or a branch
    # weights must follow these rules and add up to 100% in the "system" of the node
    # weights cannot be below 0% or above 100%
    {
        'data': {
            # Node
            # id, label standard for dash cytoscape
            'id': 'root',
            'label': 'Wake up',
            # custom entries below
            # weights have been explained - stored inside element
            'weight': 25,
            # stores the level that the node resides on (root is 0, first branch from root is 1)
            'level': 1,
            # stores the number of children that the node has
            'children': 2,
            # selector styles
            # styles are used viusally to guide the user
            # traversed style indicates a node has been traversed - begins false
            'traversed': 'False',
            # common indicates that the node was the most common in a series of traversals - begins false
            'common': 'False',
            # this style is used to visually guide the user when updating weights manually - begins false
            'invalid_weight': 'False',
            # is True when node is last clicked - begins false
            'last_clicked': 'False',
            # these are "custom fields" which the user gets to define the app
            # they should be in line with the concept of the tree overall
            # for example the tree is a taxonomy of animals - lays eggs: (yes/no), avg. weight (a number),
            # average family size (number of average children)
            # custom fields may or may not be parallel to concepts embedded in the tree e.g. you are in a decision
            # tree for american football where each level represents a series of downs, a custom field for yards to
            # go would likely get shorter on later downs or yards to goal would get shorter - plays on previous
            # downs would be expected to gain yards
            # The data structure needs to remain the same as shown here for the app to work
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
            # edge id follows the convention of "(parent's)id_(parent's child node)id" or (source)id_(target_id)
            'id': 'root_two',
            'source': 'root',
            'target': 'two',
            # weights have been explained earlier, again for edges the weight is the chance that the selected
            # node moves from being 'source' to 'target'
            'weight': 37.5,
            # below are used to sync with selector styles, same as nodes and always begin as false
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
