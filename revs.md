# general revisions 
We shouldn't add any lines or callbacks to the other files in the repo or the revisions document. the audience has no idea what any of this is and will never see it. Boxes that hold text should have slight padding, but only a few pixels. Currently some text is pushed all the way up to border or overflowing. THis should involve making the boxes bigger, not the text smaller. Ensure that other elements are not then broken. Each 'Research question' or 'Hypothesis' should have the yellow bar in front of it, similar to slide 2

# slide 2 

expand the Two desktop systems box to fit the RoCEv2 carries synchronization and activations sentence

# slide 3
we should explicitly state the memory to cost ratio. so how many times more memory do we get in a single gb300 compared to a spark, compared to how many times more in cost the gb300 is.

# slide 4

add the transparent png of the sparks to this slide in place of the blank boxes we currently have in the preliminary testbed graphic. place the sparks inside the current boxes

# slide 5
move the 'Two cables expose all four interfaces...' Down so it is in the middle of the Research Question and Hypothesis

# slide 10
mention that we are using the Hockney model for estimating transmission time

# slide 11
the word 'activations' should be yellow on the pipeline parallelism graphic

# slide 12
the 'request' word is overlapping the head node box, causing the word to be slightly obscured. It should be outside the box entirely. The same idea with the 'place workers' text and the 'NCCL over RoCEv2' text.

# slide 13
scale the graph up so that it is larger. Add a note centered underneath the graph explaining how at larger message sizes we were capped around 2.3 GB/s with TCP sockets, and achieve near line rate speeds of around 23 GB/s with RoCEv2 

# slide 14
we should include what the method for measuring gpu power should be. We should state that we imposed an 80% memory cap for the inference to reserve some memory for the cpu, and that future tests will raise this budget as far as we can. We should state what the total memory budget for one node and both are now

# slide 21
the next test should be using the interfaces bonded as failover and comparing how bandwidth under heavy traffic is affected, if at all
