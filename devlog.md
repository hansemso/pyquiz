# devlog

## ML Bayes theorem pyquiz-cpymos exercise feature

Created lab.json pyquiz and cpymos can use to pass data to each other. 

#1000 Bayes theorem review


## Bayes' Theorem – Posterior Density


            Bayes' Theorem                     Posterior Density

            P(B | A) P(A)                      p(x | θ) π(θ)
P(A | B) = ---------------      p(θ | x) = -------------------------
                P(B)                        ∫ p(x | t) π(t) dt   from -∞ to ∞


> Posterior = Likelihood × Prior / Evidence
p(θ | x) = Posterior distribution  
> Updated belief about parameter θ after observing data x.
p(x | θ) = Likelihood
Probability of observing data x assuming θ is true.
> π(θ) = Prior distribution
Belief about θ before seeing the data.
> ∫ p(x | t) π(t) dt = Evidence (normalizing constant)
  Ensures the posterior distribution integrates to 1.
  Represents the overall probability of observing the data.



        Set-Theoretic View                                 Outcome View

+--------------------------------------+      +--------------------------------------+
|              All Coins               |      |              All Coins               |
|         Ω = {H,T} = 2 elements       |      |         Ω = {H,T} = 2 elements       |
|      +------------------+            |      |                                      |
|      |        B         |            |      |      +------------------------+      |
|      |    Fair Coin     |            |      |      |           B            |      |
|      |                  |            |      |      |       Fair Coin        |      |
|      |    +------+      |            |      |      |                        |      |
|      |    | A∩B  |      |            |      |      |  +---------+--------+  |      |
|      |    |Heads |      |            |      |      |  |  A∩B    |        |  |      |
|      |    +------+      |            |      |      |  | Heads   | Tails  |  |      |
|      |                  |            |      |      |  |   H     |   T    |  |      |
|      +------------------+            |      |      |  +---------+--------+  |      |
|                                      |      |      |                        |      |
+--------------------------------------+      |      +------------------------+      |
                                              |                                      |
                                              +--------------------------------------+

B = Fair Coin = property/description of model, not a subset of Ω
A∩B or A|B = Heads AND Fair Coin = 1/2 = 1 out of 2 elements/outcomes

For a single fair coin, there really isn't a natural Bayes-theorem Venn diagram because there's no hidden variable to update. That's why our earlier diagram felt forced. You were noticing a real mathematical issue, not just a drawing issue.


### *** Bayes' Theorem ***  
+--------------------------------------+   
|              All Coins               |                   P(B | A) P(A)  
|         Ω = {H,T} = 2 elements       |       P(A | B) = ---------------      
|                                      |                       P(B)
|      +------------------------+      |       
|      |           B            |      |       B = Fair Coin = property/description of model,
|      |       Fair Coin        |      |                       not a subset of Ω
|      |                        |      |     
|      |  +---------+--------+  |      |       A∩B or A|B = Heads AND Fair Coin = 1/2 
|      |  |  A∩B    |  A∩B   |  |      |                  = 1 out of 2 elements/outcomes
|      |  | Heads   | Tails  |  |      |     
|      |  |   H     |   T    |  |      |                       p(D | θ) π(θ)
|      |  +---------+--------+  |      |       p(θ | D) = -------------------------
|      |                        |      |                  ∫ p(x | t) π(t) dt   from -∞ to ∞
|      +------------------------+      |     
|                                      |       D = dataset        θ = parameter      
+--------------------------------------+

