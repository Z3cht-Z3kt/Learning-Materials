# \#Python Diary



> Day ?

I think it's about time I try documenting my progress in Python. For the last couple of days, I've been using a free course to learn Python from the ground up, and so far, it's been quite easy?  Having only tried Java and a tiny bit of C++, the syntax for Python was definitely easier. For a second, you'd think you're making something similar to pseudocode. But I digress. I guess after this initial entry, I'd label the days as \[1, 2, 3...] and so on. Kind of like an index. 


So far, I've learned the basics so far, data types, loops, dictionaries, lists, and exceptions. To learn these, I use a website called freeCodeCamp, they have other courses as well, so after I finish Python, I might go to C++ and finally finish it. There are instances where the automatic checker for the code doesn't agree with you, despite being logically correct but I don't know, I'm no expert, maybe it's just because of the fact that I'm still learning. Nonetheless, it does great at teaching you the basics. There are sections called 'lab' where they guide you through a coding session function-by-function, but I don't agree with the logic sometimes. It's great, don't get me wrong, but I can't seem to wrap my head around some of them. Anyways, tomorrow, I'll begin my lessons on Classes and Objects. 


> Day 2

Just finished my first part of four lessons about Classes and Methods. Suffice to say, it just got a whole lot confusing. The first part of the lesson tackled Classes, Attributes, and Objects; so it discussed things like __init__ and the 'self' keyword. As I understand it, the term 'Blueprint' is used to define Classes, where you have attributes that you can change by calling the Class. And in that class, you define a function for that Class. Essentially, Class --> Attribute --> Object. 

The 'self' constructor or parameter stumped me for a while. I thought it created an instance of a value, which is why you can have two values for the same name. But actually, it's completely different; it's used to refer to the current object, and you create multiple instances of that object by assigning a variable to call that specific class. So, in a class with (self, name) parameters, you can use student1 = ClassName(argument), and it creates an object called student1 with that argument as its value. 

The second lesson consisted of the difference between Instance Attributes and Class Attributes, as well as Methods inside a Class. This was fairly easy to digest. I guess all you need to know is that an Instance Attribute requires creating an object or an instance of that class. I suppose it's similar to initializing a variable, while Class Attributes are accessible throughout the whole Class, think of it like a global variable. And methods are just what you want the Class to do, for example, describing or output.

Working with Classes just got a whole lot confusing, because what do you mean, the usual functions I use aren't working anymore? So I'm now on Special Methods, and apparently, using the usual methods like add() or len() on an object doesn't work anymore, and you need to use Special Methods or Dunder Methods (Fun fact: Dunder is derived from the words: double and underscore). Python only knows how to use your functions/methods when it's a Class Attribute or a Global Variable; otherwise, it becomes an error. I guess it does make sense, though, how does Python know what to do with an attribute you're just now declaring, right?

After that slightly annoying detour, I'm now learning about dynamic attributes and the functions I can use to manipulate the attributes without changing the object itself. Functions such as getatrr(), setattr(), hasattr(), delattr(). You can concur what each does based on the name alone, but in short, getattr() takes in three arguments similar to all of them, (object, nameofattr, defaultattr). The same goes with setattr() with three arguments, (object, nameofattr, whattochangeinto). The hasattr() takes in only two arguments, (object, nameofattr), it's basically just a check. And lastly, delattr(), similar to hasattr() with two arguments, (object, nameofattrtodelete). There's also a function called dir(), which essentially just pertains to the whole object.

Right, I suppose I learned a lot today. Overall, I think it was fairly understandable. It is a bit frustrating that traditional functions won't work on objects, but I think there are alternatives. Well, there are; you can create your own functions in classes to do what a base function does.

> Day 3

Right, so I just finished the Classes and Objects section from freeCodeCamp. Well, I meant not in one day, of course, nonetheless, the Planet Class lab and Email Simulator Workshop tested my patience sooo much. The output is correct, but the checker won't let me pass, as you'd expect, it made me so frustrated. But anyway, time for a reflection. So, today was just an application of what I learned yesterday. Attributes, Classes, Objects, Instances, etc. What interested me the most is the Email Simulator, you can send, receive, read, check your inbox, and delete 'emails', which is essentially just data stored on a list. The entirety of that project was honestly similar to CRUD, or I think it is CRUD? It taught me how to apply theoretical knowledge to creating a neat, niche program. Overall, it was fun, although frustrating at most.
