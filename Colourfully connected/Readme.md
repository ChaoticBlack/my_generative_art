## The Thought

Starting with the background, it's randomly generated everytime. The inspiration comes from the work of [Piet Mondrian](https://en.wikipedia.org/wiki/Piet_Mondrian) who was an abstract artist. If you look at the edges of the rectangles you'll see that they seem as if someone has drawn the same line over and over again. So it's not a uniform line and bulges out a bit. Coming to the foreground, the circles are all uniquely imperfect. I wanted to give a hand drawn feeling to them. Also the edges connecting them are not entirely straight. The colours are also randomized but it is a control randomization. The edges have a different set of colours, the circles.have a different set of colours and the background also has a different set of colours that the algorithm can choose from to draw.

For each aspect of the sketch there is separate set of colours. For example the circles aspect has 14 different colours. So while drawing a circle the program has a choice of 14 colours. But the choice is not entirely random, I have programmed some conditions to give it some structure but at the same time the conditions are loose enough that each output produced by the program will be different and non deterministic

The background works by recursively subdividing rectangles. So initially the entire window is one rectangle, that we divide into two rectangles then each of those two rectangles are further divided in two rectangles and so on. So the condition I'm giving is that the two subdivided parts of the rectangle cannot have the same colour no matter what.

I wanted to showcase the connections that we have as social animals. They are vibrant, varied and limited. They form under different circumstances and can mean different things. 

## Outputs

![op1](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/8615.5703125.png)

![op2](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/485.282531738.png)

![op3](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/298.520935059.png)


## Walking through the process

### The graph

First I wanted to get a feel of how graphs look and how they can be made to look. I wanted to understand what are the different parameters I can play. So I started by writing a simple program that randomly generates nodes and then draws the edges by picking two nodes at random. 

![A simple graph](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/ge1.png)
**A simple graph**

- This is pretty cool but there are way too many edges and a lot of overlapping. Also nodes farther apart connecting leads to longer edges which have a chance of passing through other unrelated nodes. The diagram is too noisy which made me think that I should have isolated groups of nearby nodes connecting.

![Second Iteration](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/ge2.png)
**Iteration Two**

- This is what I get after writing the logic for creating nearby clusters. The way I implemeted this was by assigning a proability to wach node which decided how many other nodes it was connected to. Any node could be connect to at least 0 nodes and at most 4 nodes. I also added some basic code for randomly colouring the nodes and drawing concentric circles. This is closer to the vision I have in mind. While working on this sketch I was taking a Social Network Analysis course. So in the back of my head I was thinking about the networks that an individual is part of. In my experince at leaset, the people that you are really connect to are limited.

- Next I wanted to add some imperfections to the graph. Make it seem sort of hand drawn. This meant that the lines couldn't be straight and the circles couldn't be round. As you can see below, I went a little overboard with my first iteration. I gradually understood the parameters involved after a lot of reading online. I also made sure that my code to draw imperfect shapes was generalized enough that it could be later reused if needed.

![imperfect](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/badOP.png)
**Imperfections are hard**

### The Background

- I wasn't sure where I was going with the graph. It did not look good on its own even after investing in colouring it. Something was missing. It needed a complimenting background. With nothing particular in mind I let this sketch stagnate for a while as I worked on other experiments. I was reading about subdivision and wondered if I could do something interesting with it. I started with triagnle subdivision and came up with the output below. It wasn't interesting on its own and I couldn't think of much to innovate in it.

![triangle subdiv](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/tsd3.png)
**Irregular triangle subdivision with colours inspired by the four elements of Avatar: The Last Airbender

- While working on Rectangle Subdivision, I felt that it had some flavour to it. I added the code to draw imperfect lines and liked the outputs. The colour choices below are terrible and the rectangles have been subdivided way too many times but you can see that it has potential!

![rect subdiv](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/rs3.png)
**Imperfect rectangle subdivision**

- I came across the [Art](https://en.wikipedia.org/wiki/Composition_with_Red,_Blue_and_Yellow) by Piet Mondrian which was pretty interesting. Its cool how at first glance it appears uniform and bland but looking closely you see how the lines are of different thicknesses, the colours are imperfectly filled in the rectangles and so on. Also the colours are so striking! Using this as a reference I came up with the foloowing output.

  ![rect_sub](https://github.com/ChaoticBlack/my_generative_art/blob/main/Colourfully%20connected/rect_sub_div_op.png)
  **Clean**

  ## The Final Step

  - Combining these two, I was happy. It wan't all that straightforward, a lot of tweaking was required. Making sure the nodes were uniformly distributed, the edges were clean and choose the appropriate colour combinations took quite a while. I am happy with the end result!
