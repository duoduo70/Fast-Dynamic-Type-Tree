# Fast-Dynamic-Type-Tree
This repository attempts to present a new, fast, scalable, programming-only type system.
It allows you to add a type system to the most complex parts of your existing code, which you can extend as your code becomes more complex.
This system does not depend on any programming language, but the lower level programming languages use it the greater the benefit should be.
We shouldn't tie ourselves to the "shoulds" of functional programming, object-oriented programming, and so on; all specifications are in the service of programming.

这个存储库尝试提出一种新型的、快速的、可扩展的、仅服务于编程的类型系统。
它允许你为现有代码的最复杂部分添加类型系统，随着你的代码越来越复杂，你可以拓展这个系统。
这个系统不依赖于任何编程语言，但越低级的编程语言使用它应该能带来更大的收益。
我们不应该用函数式编程、面向对象编程等等的“应该”束缚自己，因为一切规范都应该是为编程本身服务的。

Initiatives such as forcing additional type annotations and safety checks on objects are often a huge drag on performance rather than helping us. In this code, I've tried to provide a "top-down" (rather than the traditional "bottom-up") approach, where you only need to draw the most complex and desirable parts.
You can always introduce multivariate functions into it if you want, and higher-order functions --- just types and arrows will do everything --- while maintaining good performance.
In this Python example I can create 300,000 types and arrows to them per second.
I've been reading some type theory papers and have been inspired by them. whereas HoTT treats elements as points, and the programming trend in recent years has been to think "everything of type is an object," I think of elements as subspaces, but the parent space can be thought of as a point, and "everything of type is an object. I see elements as subspaces, but the parent space can be seen as points instead, and "everything is a type".
I don't like PhD theses that are more and more mathematical (they're just trying to graduate or get famous, but there are a lot of uninformed people who actually try those things), and I don't like things that are more and more industrialized, and programming isn't an appendage of mathematics or some obscure "truth", and I hate structuralism, so I wrote this little thing .

诸如为对象强制提供附加类型标注和安全检查的举措在很多时候不仅不能帮助我们，反而会极大的拖慢性能。在这些代码中，我则尝试提供一种“从上到下”（而非传统的“从下到上”）刻画的方式，你只需要刻画最复杂的、最值得刻画的部分。
如果你想的话你可以随时为其引入多元函数，高阶函数——仅通过 types 和 arrows 便可以做到一切——在保持较好的性能的基础上。
在这个 Python 示例中我可以每秒创建三十万个类型和连接到它们的 arrow 。
我看了一些类型论的论文，并从中得到了启发。HoTT 将元素看作一个个的点，近几年的编程潮流觉得“一切类型皆对象”，我则与它们相反，我将元素看作一个个子空间，但父空间反而可以看作点，同时“一切对象皆类型”。
我不喜欢那些越来越数学的博士论文（他们只是想毕业或者出名，但是有很多不明真相的人真的去尝试那些东西），我也不喜欢那些越来越工业化的东西，编程不是数学或某种晦涩“真理”的附庸，我讨厌结构主义，所以我编写了这个小东西。

God knows when I'll want to expand it, I'm just presenting an idea for now --- maybe I'll use it for some future project.

天知道我什么时候会想要拓展它，我暂且只是提出了一种思想——或许我未来的某个项目会用到它。
