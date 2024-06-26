# Fast-Dynamic-Type-Tree
This repository attempts to present a new, fast, scalable, programming-only type system.
It allows you to add a type system to the most complex parts of your existing code, which you can extend as your code becomes more complex.
This system does not depend on any programming language, but the lower level programming languages use it the greater the benefit should be.
We shouldn't tie ourselves to the "shoulds" of functional programming, object-oriented programming, and so on; all specifications are in the service of programming.

Initiatives such as forcing additional type annotations and safety checks on objects are often a huge drag on performance rather than helping us. In this code, I've tried to provide a "top-down" (rather than the traditional "bottom-up") approach, where you only need to draw the most complex and desirable parts.
You can always introduce multivariate functions into it if you want, and higher-order functions --- just types and arrows will do everything --- while maintaining good performance.
In this Python example I can create 300,000 types and arrows to them per second.
I've been reading some type theory papers and have been inspired by them. whereas HoTT treats elements as points, and the programming trend in recent years has been to think "everything of type is an object," I think of elements as subspaces, but the parent space can be thought of as a point, and "everything of type is an object. I see elements as subspaces, but the parent space can be seen as points instead, and "everything is a type".
I don't like PhD theses that are more and more mathematical (they're just trying to graduate or get famous, but there are a lot of uninformed people who actually try those things), and I don't like things that are more and more industrialized, and programming isn't an appendage of mathematics or some obscure "truth", and I hate structuralism, so I wrote this little thing .

God knows when I'll want to expand it, I'm just presenting an idea for now --- maybe I'll use it for some future project.
