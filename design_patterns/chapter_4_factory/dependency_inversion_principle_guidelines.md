## Dependency inversion principle guidelines
* No variable should hold a reference of a concrete class. Use a factory instead;
* No class should derive from a concrete class. If you derive from a concrete class, you depend on a concrete class. *Derive from an abstraction, like an interface or an abstract class;*
* No method should override an *implemented* method of any of its base classes. If you override an implemented method, then the base class was not really an abstraction to begin with. Those methods implemented in the base class are meant to be shared by all the subclasses;