# devlog for pyquiz.py

# Development (Most recent at top):

8.26.26 Added pyquiz\repl folder to store Python 3 exercises user can follow from flashcard. Added repl_1.py loss.backward() exercise for ml cards.
8.6.26 Added note attachment feature to tkinter popup. Now when user inputs answer, answer explanation shows in popup to go with answer check. Can be edited in 3. Edit mode. So now there is an enlargeable popup of the question and an attachable note for the answer. 
7.20.26 Added pyquiz_demo.gif to repo showing pyquiz features. 
6.25.26: Adding truthy flag + payload means to Type I cards so diagram pops up in tkinter automatically only if it exists. Otherwise works normally as single-line qa's after multi-line problem display as usual for Type I. User can in Edit Mode input the unicode diagram into existing cards. 
6.10.26: Finally got Tkinter to work with pyquiz. Trick was to start over by attaching a relay as it were called "display" then to toggle on/off popup window per question by adding it to Edit Mode as, t = toggle. Defensive development as it were. So user will see Type I card question in terminal window and at once zoomed up as desired in Tkinter popup window. Then added g = toggle gui as well for the whole card so user can zoom up all questions on Tkinter display at once instead of toggling each one.
6.11.26: Decided not to for Type II cards put multi-line question on Tkinter as with Type I single-line questions. Because since mline question allows unicode diagrams there is no point of blowing it up in size using Tkinter display which is for zooming up single-line question input by user. 



## ML Bayes theorem pyquiz-cpymos exercise feature

#1000 Bayes theorem review

# Bayes' Theorem – Posterior Density

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


For Type I cards. Use gui toggle feature. 

* Coin fairness p ∈ [0,1]  

Ω = {H, T} = theoretical sample space = all possible outcomes
│             (dataset for one toss: D = {H} or {T})
│
├── ω = H or T        (one observed outcome)
│
├── subsets (events)
│     │
│     ├── A = {H} ⊆ Ω
│     ├── B = {T} ⊆ Ω
│     └── Ω = {H,T}
│
└── 𝔽 = P(Ω)
      │
      ├── ∅
      ├── {H} = A
      ├── {T} = B
      └── {H,T} = Ω



### *** Bayes' Theorem ***  
+----------------------------------+---------------------------------------------+
|                Ω                 |               P(B | A) P(A)                 |  
|     theoretical sample space     |   P(A | B) = ---------------                |  
|          (not dataset)           |                   P(B)                      |  
|    +------------+-----------+    |                                             |  
|    | B = new Ω(subset of Ω) |    |  (Ω,𝔽,P) where P:𝔽 → [0,1] and 𝔽 ⊆ P(Ω)    |  
|    |                        |    |                                             |  
|    |                        |    |                                             |       
|    |  +---------+--------+  |    |                                             |        
|    |  |  A∩B    |  A∩B   |  |    |                                             |   	  
|    |  | Heads   | Tails  |  |    |                                             |        
|    |  |   H     |   T    |  |    |                   p(D | θ) π(θ)             |        
|    |  +---------+--------+  |    |   p(θ | D) = -------------------------      |        
|    |                        |    |              ∫ p(x | t) π(t) dt  (-∞ to ∞)  |        
|    +------------------------+    |                                             |        
|                                  |   D = dataset        θ = parameter          |
+----------------------------------+---------------------------------------------+


pyquiz card # 1000:

### *** Bayes' Theorem (cancer) ***
+----------------------------------+--------------------------------------+
|                Ω                 |            Bayes' Theorem            |
|     theoretical sample space     |                                      |
|          (not dataset)           |      P(A | B) = P(B | A) P(A)        |
|                                  |                 -----------          |
| Ω = {(C,+),(C,-),                |                    P(B)              |
|      (NC,+),(NC,-)}              |                                      |
|                                  |  A  = Patient has cancer             |
| +----------------------------+   |  Aᶜ = Patient has no cancer          |
| | B = Positive Tests         |   |  B  = Patient tests positive         |
| |                            |   |                                      |
| | +---------+-------------+  |   |  P(A)     = Cancer prevalence        |
| | | A∩B     |   B∩Aᶜ      |  |   |  P(B|A)   = Sensitivity (TPR)        |
| | | (TP)    |   (FP)      |  |   |  P(B|Aᶜ)  = False Positive Rate      |
| | +---------+-------------+  |   |  P(Bᶜ|Aᶜ) = Specificity (TNR)        |
| +----------------------------+   |                                      |
|                                  |  P(B)=P(B|A)P(A)+P(B|Aᶜ)P(Aᶜ)        |
| (C,-) = FN    (NC,-) = TN        |                                      |
|                                  |  P(A|B) = Cancer given positive      |
| TPR = TP/(TP+FN)                 |                                      |
| FPR = FP/(FP+TN)                 |  D = {ω¹,ω²,…,ω¹⁰⁰⁰}, ωⁱ∈Ω           |
+----------------------------------+--------------------------------------+

Q:  In the venn diagram, which region represents false positives? a) A∩B  b) B|Aᶜ  
A:  b
Q:  B _ A∩B + B|Aᶜ  (Type in < = or >)
A:  =
Q:  False positives are included in B because they received a  ____  test result.
A:  positive
Q:  Does a false positive contribute to P(B)? (y/n)
A:  y
Q: False positives reduce P(C|+) because they ____ the number of + tests without increasing the number of cancer cases.
A:  increase
Q:  A patient has cancer and tests positive. Given a cancer prevalence of 0.01 and a false positive rate of 0.15, calculate P(B) and P(A|B). (Type both as 0.___ separated by comma,space)
A: 0.1575, 0.057
Q: False positive are outside A because those patients ___ have cancer. (do/do not)
A:  do not
Q: Does a false positive contribute to P(A)?  (y/n)
A:  n
Q: Sensitivity is the probability that the test is ____ given that the disease is actually present.
A: positive
Q: The rarer the disease, the greater the probability of ___ positives.
A: false
Q: Sensitivity measures performance on ___ patients, while false positives occur among ___ patients. (comma,space)
A: diseased, healthy


Q: What does sensitivity measure?
A: The fraction of actual cancer patients who test positive.
Q: What does the false positive rate measure?
A: The fraction of healthy patients who test positive.
Q: Can a test have high sensitivity and still produce many false positives?
A: Yes



Actual Cancer Patients              Actual Healthy Patients
┌─────────────────────┐             ┌─────────────────────┐
│ TP       │ FN       │             │ FP       │ TN       │
└─────────────────────┘             └─────────────────────┘
      ↑                                    ↑
  Sensitivity                    False Positive Rate

Q: How does a statistician calculate false positives?

A: By comparing each patient's test result with the patient's true disease status. Healthy patients who test positive are counted as false positives.




P(+)=P(+∣D)P(D)+P(+∣¬D)P(¬D) where + = A as false positive
P(B|A) 

- theoretical sample space does not include the dataset, such as 1000 cases of something, as 1000 is not theoretical, it is not conditionable
- 

group 1:
Q: Theoretical sample space 

Q: For one patient: If sample space Ω = {(C,+),(C,−),(NC,+),(NC,−)}, and B = {positive test}, then  B = {(C,+), (NC,+)} ⊆ Ω. 





Q:  Sample space Ω is the complete set of mutually exclusive and collectively exhaustive outcomes of a random experiment.
A:  
Q:  All possible data you could have observed before you actually collected any data.(For ML)
A:
Q:  The sample space (Ω) is the complete set of all possible data (outcomes) that a random experiment can produce. An outcome is one possible piece of data, and an event is any collection of those outcomes.
A: 
Q:  Experiment E ──► Ω = {all possible data/outcomes} ──► ω ∈ Ω ──► A,B ⊆ Ω ──► P(A|B)
This is the entire Bayesian workflow in one line:

E = random experiment
Ω = sample space (all possible data/outcomes)
ω = the actual observed data
A, B = events (subsets of Ω)
P(A|B) = probability of event/hypothesis A given observed event/data B
A:  
You don’t put Ω into Bayes because Bayes already operates entirely inside a fixed Ω; it is the background space, not a variable in the formula.

Ω = all possible outcomes (theoretical model space)
D = realized outcomes(positives) drawn from Ω (observed data--not data size such as 1000 patients). Data = a collection of observed values or measurements about one or more entities. Once you attach measurements, then it becomes data:

Data D → empirical probabilities on Ω → Bayes theorem → posterior P(A|B)



Q:  Sets are unordered, but tuples have o___, a___, and r___.  (comma,space)
A:  order, arity, repetition
Q: Events 𝔽 are ______ of outcomes; ordered sequences of outcomes are ______. (commas, space)
A: sets, tuples
Q:  A|B means 

Q: Prevalence = cases​ per population.  




group 2:  



Q: B is a subset(proper + improper) of Ω; B ⊆ Ω
 (t/f)
A: t
Q:  B is an event/condition (t/f)
A: t
Q:  Fair coin is a model, not an event/condition.  (t/f)
A:  t
Q:  An event is an outcome  (t/f)
A:  f
Q:  An event is a subset/collection of possible outcomes.  (t/f)
A:  t

Q: Outcomes are ___, events are ___ (subsets of sample spaces). (comma, space)
A: results, conditions
Q:  Sample spaces are sets/collections of all ___ outcomes of experiments.
A:  possible  

Q:  B is a model (t/f)
A:  f
Q:  H and T are subsets of 

Q:  B is the conditioning(known) event (t/f)
A:  t
Q:  P(A|B) is the posterior probability of A given B  (t/f)
A:  t
Q:  B is the prior event  (t/f)
A:  f

Q: A ⊆ B ⟺ A = B or A ⊂ B are 3 types of what set relation for A with B? (commas,space)
A: subset, improper, proper 
Q: Bayes operates on events(sets), not ___ outcomes.
A:  ordered
Q: “I know how A overlaps B but I want to know how B overlaps A” 
A: 


Event = subset means </= , not proper subset which is always less than sample space S . Improper subset is the whole set. 


A parameter is a fixed quantity that characterizes a model relative to a family of possible models.  M={P_θ​:θ∈Θ}

So Bayes is moving a point distribution over a curved parameter space


                 Θ  (parameter space)
                 │
                 │  θ ↦ P_θ   (model map)
                 ▼
        ┌──────────────────────┐
        │ 𝓜 = {P_θ : θ ∈ Θ}   │   (model family)
        └──────────────────────┘
                 │
                 │ induces
                 ▼
        ┌──────────────────────┐
        │ (Ω, 𝔽, P_θ)          │   (probability model)
        └──────────────────────┘



Q: How many outcomes are in the Ω set for 1 toss? (type in number) 
A: 2
Q: How many outcomes are in the Ω set for 2 tosses? (type in number)
A: 4

Q: Probabilities are ___ assigned to outcomes or to ___ (sets of elements). (comma, space) 
A: numbers, events
Q: Probability is a function of events. 


Q:  Probabilities are real numbers in [0,1] assigned to events (and thus to outcomes via singleton events).

F ⊆ P(Ω)  

(Ω,F,P) where P:F→[0,1] and F⊆P(Ω).

a field (algebra) of events, i.e., a collection of subsets of Ω on which probability is defined.

Outcome:            H

Sample space:       Ω = {H, T}

Events:             𝔽 = {∅, {H}, {T}, {H,T}}

Probability:        P : 𝔽 → [0,1]

Probability is a function that takes a set of outcomes (an event) and returns a number between 0 and 1, measuring how likely that event is.


A Venn diagram works only for:

subsets of the SAME universe

But:

Ω = outcomes
Θ = parameters

So they are different universes

That’s why:

you cannot directly draw θ inside Ω

unless you artificially build a combined space:




        θ (parameter)
              ↓ generates
        distribution over Ω
              ↓ produces
        observed event D ∈ Ω
              ↓ feeds into
        Bayes rule
              ↓ updates
        belief over θ
		



Joint space: Θ × Ω

Observe D in Ω
        ↓
Take slice at Ω = D
        ↓
Evaluate height along Θ using likelihood
        ↓
Renormalize along Θ
        ↓
Get posterior over Θ





Bayesian inference is geometry in the product space Θ × Ω, where observed outcomes in Ω define slices, and those slices reshape probability distributions over Θ.


outcome space Ω  versus  parameter space θ



Fair Coin                 60 Hz Signal
---------                 ------------
θ = 1/2                   f = 60 Hz
   |                          |
Defines probabilities     Defines oscillation rate
   |                          |
H or T observed           Voltage observed




The key insight

The Gambler's Fallacy incorrectly updates the probability of the next event while assuming the model (a fair coin) stays the same.

Bayes correctly updates the probability of the model or hypothesis when new evidence arrives.

So:

Gambler's Fallacy: "Ten heads means tails is due."
Bayes: "Ten heads makes me wonder whether the coin is actually fair."


Let A = {H} = "The toss is heads."        
B = {H,T} = "The outcome is either heads or tails." 
Then P(B∣A) =

"The probability of the outcome being heads of tails, given that the coin is heads." is an example how not to use Bayes because B is what you observe.

A is a hypothesis.  
Bayes works whenever: P(B)>0
B is only useful if it restricts the sample space for A. Thus for Bayes to work sample space must be :

Bayes requires:
a fixed sample space Ω
events A and B with P(B) > 0
a probability measure


P(B∣A)/P(B) is the Bayesian update ratio. It tells you how much more (or less) likely A becomes after seeing B

1. The real foundation (Kolmogorov view)

You start with a fixed probability space:

Ω = all possible worlds (coin outcomes, patient states, etc.)
Events A and B are subsets of Ω
Probability is a measure on Ω

Nothing moves or mutates.




Probability Model
────────────────────────────────────────────────────────

Parameter
│
├── p = P(H),  0 ≤ p ≤ 1
│      │
│      ├── p = 0.5  → fair coin
│      └── p ≠ 0.5  → biased coin
│
▼
Probability Space (Ω, 𝔽, P)
│
├── Ω = {H, T}
│     = theoretical sample space
│
├── ω ∈ Ω
│     = one observed outcome
│
├── Events (subsets of Ω)
│     │
│     ├── A = {H} ⊆ Ω
│     ├── B = {T} ⊆ Ω
│     └── Ω = {H,T}
│
└── 𝔽 = P(Ω)
      │
      ├── ∅
      ├── {H} = A
      ├── {T} = B
      └── {H,T} = Ω

────────────────────────────────────────────────────────

Observed Data
│
├── One toss:
│      D = {H}  or  {T}
│
└── n tosses:
       D = {ω¹, ω², …, ωⁿ}

────────────────────────────────────────────────────────

Bayesian Inference
│
├── Prior:        P(p)
├── Data:         D
└── Posterior:    P(p | D)



=======================MARKOV====================


      PRESENT    ×    TRANSITION      =     FUTURE
	  
                        H     T  
      ┌      ┐      ┌             ┐        ┌      ┐
 If H │ 0.60 │      │ 0.70  0.30  │      H │ 0.58 │
 If T │ 0.40 │      │ 0.40  0.60  │      T │ 0.42 │
      └      ┘      └             ┘        └      ┘


Heads (0.60) × 0.70 = 0.42 ───┐
                              ├── (+) ──▶ Heads (0.58)
Tails (0.40) × 0.40 = 0.16 ───┘


Heads (0.60) × 0.30 = 0.18 ───┐
                              ├── (+) ──▶ Tails (0.42)
Tails (0.40) × 0.60 = 0.24 ───┘



Bayes ≈ infer causes/hypotheses from evidence. 

Markov ≈ predict future states from current states. 

Markov:
P(Rain tomorrow | Sunny today)

Bayes:
P(It rained | Ground is wet)

Bayes:
Evidence → Hypothesis

Markov:
State → Next State

Bayes:
"What is the hidden cause given what I observed?"

Markov:
"What happens next given the current state?"

Bayes → inference (update beliefs from evidence)
Markov → transitions (how states change)

Q: Is Bayes discrete and Markov continuous?

A: No. Both can be discrete or continuous.

Bayes describes inference.
Markov describes state transitions.

Q: Is Bayes discrete and Markov continuous?

A: No. Both can be discrete or continuous.

Bayes describes inference.
Markov describes state transitions.


A transition matrix in a Markov chain:

A transition matrix is a matrix that contains the probabilities of moving from one state to another.

Formula:
Pᵢⱼ = P(Xₜ₊₁ = j | Xₜ = i)

Meaning:
"The probability of being in state j next, given the current state i."

Example:

P = [
  0.9  0.1
  0.2  0.8
]

Row = current state
Column = next state

Rules:
- Each value is between 0 and 1.
- Each row adds up to 1.

Key idea:
Current state → Transition matrix → Next state


Past affects Present:

P(X_t | X_{t-1}, X_{t-2}, ...)

P(X_{t+1} | X_t, X_{t-1}, ...)
=
P(X_{t+1} | X_t)

Chess Analogy for Markov Processes

The entire history of chess moves matters because it created the current board position.

However, once you know the exact current board position, you usually do not need to know every previous move to determine the possible next moves.

Similarly, in a Markov process:

Past → Present State → Future

The past influences the present, but the current state summarizes all relevant information needed to predict the future.

Example:

P(X_{t+1} | X_t, X_{t-1}, ..., X_0)
=
P(X_{t+1} | X_t)

Meaning:
"Given the current state, the past adds no additional predictive information."


                Tomorrow
             B     S     R
Today B   [0.8   0.15  0.05]
Today S   [0.3   0.40  0.30]  ← Sideways row
Today R   [0.2   0.20  0.60]

#==============================================================
# pyquiz card #1005 in 1000 series for machine learning:
*** ML 101 qa's ***


| Observed sequence | Probability of (n+1) |  P(n heads in a row) = (1/2)^n
| ----------------- | -------------------- |  n consecutive heads = 2^(n+1) − 2
| `1`               |                 50%* |  (2^(n+1) - 1) - 1 = 2^(n+1) - 2
| `1,2`             |              **90%** |
| `1,2,3`           |           **98.78%** |
| `1,2,3,4`         |           **99.86%** |

| Process      | Next outcome          | Does past change next probability? |
| ------------ | --------------------- | ---------------------------------- |
| Fair coin    | H or T                | **No**                             |
| Known (aₙ=n) | (n+1)                 | **No**                             |
| Unknown rule | User's guess of (n+1) | **Uncertainty is about the rule**  |

* Prob of fitting the model increases
Where it is n + 1 for natural sequence of (1/n)^p for fair coin toss variation. As number of terms grow, computer can calculate fit to model. 
So if you get 10 heads in a row, then you know it corresponds to a p. So the more heads you get, p increases proportionately. But gambler's fallacy states next prob is still 1/2 for fair coin. It suggests some derivative exists. The prob of 1/6 is obviously a lot greater. With p increasing even faster. With n + q for integers, what outcomes would fit model as q increase? Or a more complex model, where q can be a noninteger. Obviously, n + prime is not guessable, as no formula has been found for finding prime numbers. Or is there? prime + 1?  

**Q:** Does the order of observations always matter in probability? (y/n)
**A:** n
**Q:** Order Of Observations matters when the model uses the r____s or t_____s between observations. (comma,space)
A: relationships, transitions
 
Q: A list is a finite ______ collection. A _____ is a function whose domain is an ordered index set. (comma,space)
A: ordered, sequence
Q: P(10 consecutive heads) = 2^(10+1) - 2 = 2046. P(head) for next toss is __%
A: 50
Q: P(aₙ₊₁ = n+1 | 1,2,…,n)
A: 


# Predicting the Next Whole Number

Given:1, 2, 3, …, n  What is the probability, P(aₙ₊₁ = n+1 ∣ 1,2,…,n), that the next term is n+1?



**Question:**
What is the probability that the next term is n+1?

**Answer:**

**P(aₙ₊₁ = n+1 ∣ 1,2,…,n)**

The probability depends on the model used for possible rules.

As more consecutive terms match the pattern, confidence in **aₙ = n** can increase, but it does not necessarily reach 100% at any finite n.

**Key idea:**

**More matching terms → greater confidence in aₙ = n**

**But:** the exact probability requires assumptions about the possible underlying rules.







# Predicting the Next Whole Number

**Computer's rule:**

**aₙ = n**

**Computer knows:**

**aₙ₊₁ = n+1**

**User sees only:**

**1, 2, 3, …, n**

**Question:**
What is the probability that the user correctly guesses **n+1**?

**Answer:**

**P(user guesses n+1 ∣ 1,2,…,n)**

The probability is determined **empirically** by observing the user's guesses:

**Confidence = correct guesses / total guesses**

For example:

**80 correct guesses / 100 attempts = 80%**

The computer knows the answer with certainty, but the user's confidence depends on their ability to infer the pattern.

**Key idea:**

**Computer: 100% certain**

**User: probability measured from guessing behavior**




| Process      | Next outcome          | Does past change next probability? |
| ------------ | --------------------- | ---------------------------------- |
| Fair coin    | H or T                | **No**                             |
| Known (aₙ=n) | (n+1)                 | **No**                             |
| Unknown rule | User's guess of (n+1) | **Uncertainty is about the rule**  |




=================================================












### 4. Probability vs. model

**Q:** Does probability itself determine whether sequence matters?

**A:** No. **The probability model determines whether sequence is relevant.**

### 5. Bayesian inference

**Q:** In Bayesian inference, what determines whether sequence matters?

**A:** The **likelihood model** determines whether the order of observations contributes information about the hypothesis.

These are better separated because each card tests **one idea** rather than putting all five ideas into one card.




========================== pytorch section ==============================================
# card # 1100

*** pytorch differentiation lesson ***

import torch

x = torch.tensor(3.0, requires_grad=True)

loss = x ** 2

loss.backward()

print(x.grad)

Q: What is the output?  (C&P Py3 answer)
A: tensor(6.)
Q: In the code, what is the PyTorch tensor object? 
A: loss
Q: Calling y.backward() tells PyTorch to calculate the gradients by working backward through the operations that produced `y`.
* The resulting gradients are stored in the `.grad` attributes of tensors that require gradients.

# PyTorch `.backward()` Method

**Question:**
In PyTorch, what are `y` and `.backward()` in:

```python
y.backward()
```

**Answer:**

* **`y`** is a PyTorch **tensor object**.
* **`.backward()`** is a **method** belonging to that tensor.
* Calling `y.backward()` tells PyTorch to calculate the gradients by working backward through the operations that produced `y`.
* The resulting gradients are stored in the `.grad` attributes of tensors that require gradients.

Example:

```python
x = torch.tensor(3.0, requires_grad=True)
y = x ** 2

y.backward()

print(x.grad)
```

Output:

```text
tensor(6.)
```

because:

**y = x² → dy/dx = 2x → dy/dx at x = 3 is 6**



Loss
  ↑
25│ ●                 ●
  │  ╲             ╱
16│    ●         ●
  │      ╲     ╱
 9│        ● ●
  │         ╲╱
 4│          ●
  │
 0│──────────●────────────→ Prediction
            10

             ↑
          true value
		  
		  
import torch

# True value
y = torch.tensor(10.0)

# Prediction
ŷ = torch.tensor(7.0, requires_grad=True)

# Loss
L = (ŷ - y) ** 2

# Calculate derivative
L.backward()

print("Prediction:", ŷ.item())
print("Difference:", (ŷ - y).item())
print("Loss:", L.item())
print("Gradient:", ŷ.grad.item())

Prediction: 7.0
Difference: -3.0
Loss: 9.0
Gradient: -6.0
		  
		  
		  
		  
		  
		  
# input  → model → prediction → loss → .backward() → gradient → update → parameters → repeat

# pyquiz card 1101 stored in repl folder as repl_1.py

import torch

x = torch.tensor(3.0)  # input
y = torch.tensor(10.0)  # target(correct answer used to evaluate)

w = torch.tensor(2.0, requires_grad=True)  # model parameter, what it learns

learning_rate = 0.01

for i in range(100):
    prediction = w * x  # y' or prediction = 6
    loss = (prediction - y) ** 2  # = 16 or how wrong the prediction is

    w.grad = None  # Tells how to change w
    loss.backward()  # calculates how param w should change

    with torch.no_grad():
        w -= learning_rate * w.grad

print("w:", w.item())
print("prediction:", (w * x).item())
print("loss:", loss.item())





---------------------

|                           | NumPy            | PyTorch |
| ------------------------- | ---------------- | ------- |
| Arrays/tensors            | ✓                | ✓       |
| Mathematical operations   | ✓                | ✓       |
| Automatic differentiation | ✗                | ✓       |
| `.backward()`             | ✗                | ✓       |
| GPU computation           | Limited/indirect | ✓       |
