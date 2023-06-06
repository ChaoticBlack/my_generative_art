## What I did:
- Using perlin noise, I first created a vector field of angles. 
- Then, I drop points randomly in this field.
- The path that the point takes next is decided by the angle nearest toit. Basically it will try to move in the direction of that angle.
- Make sure that no point collides with another point. Or in other words, no two paths intersect. 
- One way of doing this is to implement an algorithm that detects when two curves come within a certain distance of each other. But I couldn't implement an efficient algorithm for this and the brute force method was incredibly slow.
- Hence instead, I implement a 2D grid on top of the canvas that stores all the points in a particular cell that have been drawn. And when a new point comes in that cell, the distance with all exisiting points is calculated.
- Draw circles, play with numsteps, play with colours, play with different ways of creating a vector field to get diverse results.


## Outputs
![cFF2](https://github.com/ChaoticBlack/my_generative_art/assets/55967429/3b0b105a-e2c2-4ca5-885b-c03047492078)
![cff3](https://github.com/ChaoticBlack/my_generative_art/assets/55967429/14323192-b314-4b46-bf2e-c98b5732d192)
![cff4](https://github.com/ChaoticBlack/my_generative_art/assets/55967429/63687eb4-89f7-4cc3-a0de-5fb36bc1f062)

Some circles intersect but i'm too lazy to fix it.
