---
layout: page
title: Intelligence - Can machines really be intelligent?
---
*** Abstract
Gordon Moore predicted that the number of transistors or the processing speed of computers will double every two years ( Moore's law) and it has been true over the last a few decades. Equipped with the fast growing computing power, brain inspired methods such as artificial neural network are able to accomplish many tasks that are considered almost impossible without certain degree of intelligence. Nowadays, the machines can even outperform the best of human minds in playing go and jeopardy. In this essay, I will try to address whether the machines we have today are truly intelligent and whether the kind of intelligence that many computer scientists are building the same kind of the intelligence that humans have.

  The ideas of this essay primarily stem from Jeff Hawkins' On Intelligence and Alan Turing's Computing Machinery and Intelligence.
  
%----------------------------------------------------------------------------------------
%	ESSAY BODY
%----------------------------------------------------------------------------------------
 
*** Introduction
Earlier this year, a group of computer scientists and neuroscientists came up with AlaphaGo, a program that plays go. Go is an ancient Chinese board game that is played on a 19 * 19 grid. One player places white stones and the other places black stones. The winning strategy is to capture as much area as one can. The difficulty for computers to play this game is the number of the possibilities that this game has. Especially in the beginning of the game, if a computer wants to find the best move, it will need to simulate all the possible scenarios of go and there are about $2 * 10^{170}$ different scenarios. We should keep in mind that the number of atoms in the universe is estimated to be around $10^{80}$. For computer scientists, go is an EXPTIME-complete game. For the others, it means go is a really hard game and we cannot find a proper solution by somply by simulating all the possibilities. For games that have small sample spaces, the computers can easily simulate all the possible situations to evaluate which move is the best however for go this is not possible, and, thus people use neural network instead so that some good strategies can be found without searching through the whole sample space. With the help of neural network and large computing power, AlaphaGo is able to become better by playing against itself and by playing many games at the same time. To many people's surprises, it beat Lee Sedol, a go world champion, with a score of four to one.

After Deep Blue won aganist the chess world champion Garry Kasparov in 1997, another defense line of human intellect was annihilated. AlaphaGo is just one example of many applications of current artificial intelligence research.

Not long after AlphaGo obtained the trophy in the game between humans and machines, hadlines advocating machines will someday surpass human intelligence have gone viral. It is true that this worrisome apocalypse is possible, and yet if the journalists really know about what happens behind the scene, they will realize that day probably won't come anytime soon.

*** Neurla Network
Regardless the origin of neural network techniques used in machine learning, most of them nevertheless are not trying to simulate what the brain really does. There are certainly similarities between these two: our brain has many small units called neurons that interact with each other via electrical signals. Neural networks are also made of neurons which typically spread across many layers. We feed inputs into the first layer and then based on some rules, some of the neurons in this layer become active and the others remain the same and then the activated neurons will transmit this information further down the road.

Whilst, there are several reasons why the neural network is not doing what the brain does.

* For computers to do tasks such as object recognition. A computer will need to do millions of the computation steps behind the scene. As you know a computer is nothing other than zeros and ones. The way to facilitate this process is to have parallel computing which essentially means having many computers working at the same time. Even though we have parallel machines that can compute quickly, adding one cluster of computers to another to accelarate the process, and even though our brain is also parallel, different regions processing the inputs at the same time, brain surely can still finish object recognition faster than the computers. Think of recognition of a cat. We can easily identify if an object is a cat or not within seconds, whereas, for computers, recognizing a cat is a challenging task which will require millions of computation steps. On the other hand, for a brain, it only needs a serveral seconds to carry out a few hundred computations but are able to recgonize a cat. This can be explained by the fact that our brains store the invariant representation of a cat in the brain and when we see a pattern, the representation is summoned and thus we don't need extra computation steps that the computers need.
* Today, we have a wide range of neural networks that are either descriptive or normative and yet there exists no such a network that tries to explain the overall architecture of the human brain.
* I think Hawkins' primary argument of machines being different from the brain is the fact that people put too much weight on the behavior of the program, meaning the program mimicking what we do under different situations, and they don't care if the program really ``understands'' or not.

The emphasis on the output and the behavior of programs comes from the father of computation Alan Turing. To him, intelligence is not easy to define, and therefore, he proposes the imitation game, in which there are three participants, two men and one machine. Of course, the physical aspect of the machine is eliminated as we only want to deal with the pure intelligence. During the game, one man serves as the arbitrator to ask both the machine and the other man questions without knowing who is who. If the arbitrator is not able to identify which subject is machine, then it means the program passes the Turing test, signaling the program has real intelligence. Otherwise, the program does not have intelligence. 

According to Hawkins, Turing's view on intelligence is not entirely correct. To understand Hawkins' perspective, we will need to know another old story from John Searle who first used the Chinese room to think about artificial intelligence. Searle himself doesn't know any Chinese at all, but imagine a room where he has abundant references to look up. The resources he has will enable him to respond to any Chinese message in Chinese and can even convince native speakers that he knows Chinese well.

The centerpiece of Searle's argument is the behavior equivalence is not the true intelligence. Indeed he can get a Chinese message and use the proper references to devise a response in Chinese and send it out. However, you wouldn't say Searle understands any Chinese at all, although he can act as if he speak Chinese fluently. Purely producing the wanted behavior without understanding invalidates the intelligence defined by the Turing test. 

*** So what is intelligence?
The true intelligence is prediction as proposed in Hawkins' On Intelligence, but why prediction you might ask?

Let's look at the following examples. Next time after you take a shower, pay attention to the way that you wipe off the water. Most of us will do that in the same order every single time. Our sensory inputs feed the completion of shower signal to our brain, and our brain recalls the memory stored in the past and talks to the motor cortex which moves our body to wipe off the water. The new-born babies aren't able to do this, not because their brain structure is any different from ours but they just have formed the corresponding memories yet. This explains why understanding memory is important to understand intelligence.

Another example will be when solving a math problem that one has never met before, a mathematician will look at the problems from different ways and perhaps in a sudden he/she will find out, ``Oh I have seen this before. Perhaps this method will work.`` Although, this problem is completely new, the mathematician solves the problem by identifying the old patterns and recalls the stored methods to solve the unsolved. 

Our visual perception will also prove that prediction is the sign of intelligence. Many people don't know that there are blind spots for our eyes. The reasons are:

* the blind spot for each eye is different, so when we have both eyes open, the blind spot of one eye is covered by the other eye.
* when only one eye is open, our brain will fill in the blind spot, and thus we see a complete image.

The fill-in effect is the prediction that the neocortex is making from stored patterns. When there is a hole in a stick, and that hole at our blind spot's position, what we will see is a smooth stick rather than a stick with a hole in it.

Our brains are constantly making predictions. If I say, ``president Barack'', you will know ``Obama'' is coming next. Or if I say, ``what do you want to eat for'', depending on the time of the day, ``breakfast``, ``lunch``, or ``dinner`` might pop up.

The major differences between our brains and those of other species, are the bigger brains we have and our neocortices' ability to make predictions. A dolphin also has a large brain as well as a neocortex. Like a human, it probably can memorize lots of things, but, its brain doesn't make as many predictions as we do. Our cortex is developed in two ways, one is that we can store a large amount of past experiences in complicated ways, and based on those memories we can predict what we will see, hear, and sense so to make appropriate actions. Memory along with prediction is the new framework for intelligence that Hawkins claims.
