

## slide 1
add GB10 NVIDIA DGX Spark somewhere appropriate in the title so the panel knows right away what we are talking about

The question on the slide should more relate to how we could effectively leverage a relatively affordable platform for building a compute cluster, and the challenges that come with pushing the limits of a new architecture 


## slide 3

reframe to a slide about why the dgx spark. the answer being that the next step up in a desktop architecture with FP4 Tensor Cores is the GB300, and while it has much higher memory bandwidth and PFLOPS, it only offers around 52 GB of additional memory while being priced 18x to 20x higher and taking up a much larger physical footprint.

## slide 4
Let's rephrase slide four has this two-node testbed is more of some preliminary groundwork for our research target of 10, 20, 30 nodes rather than making it seem like we just haven't done it yet. Because we haven't done it yet, but we're doing preliminary work to ensure that it's viable

## slide 5
An important distinction is that each node has two physical ports and four logical devices because here it looks like you are saying that we have two nodes, two total ports, and four logical devices total. We are investigating whether utilizing all four interfaces can help bandwidth under network-heavy inter-node communications, but we haven't obtained results for that yet. This explains why we are using two cables instead of one even though we can technically only achieve maximum bandwidth equivalent to what one cable can provide

## slide 6
We should add the actual bandwidth capabilities of each individiual piece of the graphic to their respective boxes. Also the arrows are not good, the arrow head should be smaller, and the top pcie arrow doesn't have a head while the blue line connecting connectx-7 nic to the qsfp port 1 has it. NO ARROW heads or have small bidirectional arrowheads if the data can flow both ways

    
## slide 7
we should mention the source of the ib verbs. We should add to the slide the estimated transmission time (with the methodology explained) as well as the differences between the write, send, read, isolated and concurrnet meanings.


## slide 8
scale the graph up to take up it's alloted space

## slide 11
Add arrows should the all gather / reduces or whatever the operations are that spreads the weights and then brings them together at the layer boundaries.

## slide 12

the arrows are kind of messy and we could do with a bit more for the diagram. Again, don't AI generate anything but we could come up with something a bit better than what we have currently.

## slide 13
remove the cable count discrepency. It is not important. It doesn't give us more bandwidth

## slide 14
this slide is relying on the data too much. We know the theory that RoCEv2 is better regardless of wheterh you take advantage of the IP routing or not, we can state that. Let's get some sources first and get a good thing going. The MTU stuff we aren't claiming any performance boost yet, it is mostly to answer the question of why we aren't using jumbo frames.we can gather more info about this, but I just don't want the slide to seem so unsure.

## slide 15
we need to mention what model we are looking at here. 
we also need to not mention why the plots stop at 64 concurrent requests.

## slide 20
In the current graphic, it looks like there isn't actually a conflict withe the serving and cleanup. The graphic should show what the failure looked like, and then insert one more slide after that is the same exact format with the locking and checking in place. the one that portrays the crash should visually look like a crash with an X or something of the sort

Let's drop the current slide 21, the hardware issue doesn't demonstrate anything cool I did and just adds clutter.


## New ending content slide

Let's add a new final content slide describing next steps. We can show a picture of our two sparks we have currently attached to a 400Gb/s network switch and show that if we get reliable results, we will have the current standalone sparks join the switched sparks.

## New true ending slide

Let's add a final slide that just says thank you and prompts for questions.


## general rules of thumb

clean up the wording to be a bit more formal and informative, even if we don't increase the technical rigor. Some of the language is still very AI like


