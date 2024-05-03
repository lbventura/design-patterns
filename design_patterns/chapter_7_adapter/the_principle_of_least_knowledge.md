Given an object (`a`), the principle of least knowledge focuses on 1) the number of objects `a` interacts with and 2) how it interacts. 
This prevents the user from creating designs where a large number of objects are coupled together.

The principle provides some guidelines: take any object—from any method *in that object*, the principle suggests invoking only methods that belong to:

* The object itself;
* Objects passed in as a parameter to the method; -> *These two guidelines suggest not calling methods on objects that were returned from calling other methods.*
* Any object the method creates or instantiates;
* Any components of the object -> Component means any object that is referenced by an instance variable (i.e, an HAS-A relationship). For the example of `MovieWatcher` object, think of `home_theater_facade`.