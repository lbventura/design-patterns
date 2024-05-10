# design-patterns
Python adaptation of the Head First Design Patterns (HFDP) book by Freeman, Robson, Bates and Sierra.

## What is a (design) pattern?
A solution to a problem in context. In detail [HFDP]:
* The context is the situation in which the pattern applies, which should be a recurring situation;
* The problem refers to the objective, together with any constraints;
* The solution is the end goal: a general design that anyone can apply;

## Summary of the design principles
The parentheses identify the chapter on which the principle was first applied, i.e (1) = chapter 1.

1. (1) Identify the aspects of your application that vary and separate them from what stays the same - i.e, *encapsulate what varies*;
2. (1) *Program to an interface, not an implementation*;
3. (1) *Favor composition over inheritance*;
4. (2) *Strive for loosely coupled designs* between objects which can interact;
5. (3) **Open-closed principle**: Classes should be open for extension but closed for modification;
6. (4) **Dependency inversion principle**: Depend on abstractions, do not depend on concrete classes. See `chapter_4` for more details;
7. (7) **Principle of least knowledge**: Talk only to your immediate friends. See `chapter_7` for more details;
8. (8) **The Hollywood principle**: Do not call us, we call you! See `chapter_8` for more details;
9. (9) **The principle of single responsibility**: A class should only have one reason to change;

For more details, see the Markdown files in Chapters 4, 7 and 8.