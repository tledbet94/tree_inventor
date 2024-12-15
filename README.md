![image](https://github.com/user-attachments/assets/6b867a05-a45a-4ad8-914d-57da99e2a98a)

color palette: https://lospec.com/palette-list/cc-29 CC29 by Alpha6

Treeinventor is an application that works with Directed Acyclic Graph (DAG) style "trees". Dash cytoscape is the framework used to represent DAG trees. Features include saving and loading trees in JSON format, adding / deleting / renaming nodes, modifying weights (to the structure given in the app), setting custom field labels and values (values at node level), traversal, eight template trees to view, and visual theme options. 

The goal of treeinventor is to provide a flexible, user-friendly, and customizable method to create and view "trees". The integration of custom fields and weights should allow for a wide range of tree types. Dash cytoscape provides a natural interface to view and modify trees. 

From a code standpoint, treeinventor centers around the callback function to the cytoscape elements (tree) itself. Given the scale of the app, a system is used where each major function e.g. the tree "editor" (add, remove, rename) works on its own copy of elements and returns the copy to elements itself. Seperate from cytoscape callback functions are all non-cytoscape callbacks which are more straightforward to isolate. Overall, a modular approach is used - there are five main sections: switch view, control panel, cytoscape, info-panel, and button-row (at the bottom). All the modes of the app center around the control panel changing - simular to dividing and conquering on the cytoscape, the control panel is split up into its various modes which are selected in button row. A style.css file is primarily used to style the app, with some style overrides present. Searching in the IDE is essential to navigating the styles.css. There is an approach taken in styles.css and outside of it to help manage different screen sizes and especially small screen sizes. The file structure aggregates the highest level aspects of the app and works down, forking in areas like callback vs layout elements. 

As mentioned above and the app credit to Cytoscape.js-dagre, Cytoscape.js, Dash Cytoscape, and python Dash itself. Also to Alpha6 and the CC29 palette which supplied every color used in treeinventor. 

