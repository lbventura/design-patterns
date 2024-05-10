The model-view-controller pattern is composed of three separate patterns:

* Strategy: The view is configured with a strategy provided by the controller. The view focuses on the visual aspects, while the controller handles interface behavior decisions.
* Composite: The view is a hierarchical structure where components are organized in a tree-like manner. The controller notifies the top-level component for updates, and the Composite pattern manages further updates internally.
* Observer: The model remains independent of views and controllers (i.e., the observers). It updates relevant objects when changes occur, ensuring separation of concerns.