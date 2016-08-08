---
layout: page
title: How to write scripts in Spotfire 7.6.0
---
* What you will need: Spotfire 7.6.0, [sample.csv](/extra/sample.csv/)
* What you should know: basic Python
* Duration: 30 mins
* Difficulty: beginner

Spotfire is a business intelligence tool that allows users to do rapid data visualization and analytics. Not surprisingly, for a high level program like this, we lose flexibility, whilst, the power users can still try to make it up by writing Python or Javascript. We should keep in mind that, Spotfire is not designed for low level manipulation so the customization will require more work than what is needed if you are using Python alone.

In fact writing a script in Spotfire is not difficult. Once we introduce the general architecture and go through a few examples, you should be ready to start off the journey on your own.

-------------------------
<sub> Note that: All the functions we use in this tutorial can be found at [TIBCO Spotfire 7.5 API Reference](https://docs.tibco.com/pub/doc_remote/spotfire/7.5.0/doc/api/Index.aspx). I think the APIs remain unchanged from 7.5.0 to 7.6.0. You should appreciate the value of this manual because there are not many Sportfire scripts out there, and thus the most effective way to do what you want is via trial and error with the help of this documentation.
</sub>

-------------------------
We are going to use a simple data wich only has two variables `x` and `y`. Download sample.csv [here](/extra/sample.csv/), alternatively you can copy and paste the following into a csv file.

```
x,y
1,3
3,9
5,15
7,21
9,27
11,33
13,39
15,45
17,51
19,57
21,63
```
Afterwards, we will want to load the `sample.csv` into Spotfire and create a y vs x barchart. Now you should see something similar to firgure I.

asdf

![Firgure 1](/blog/spotfire/1.png/)

lkasdf

```python
from Spotfire.Dxp.Application.Visuals import BarChart

viz = visual.As[BarChart]()

viz.XAxis.ShowAxisSelector = 0
viz.YAxis.ShowAxisSelector = 0

from Spotfire.Dxp.Application.Visuals import VisualContent

Document.ActivePageReference.Title = "First Bashboard"

min = 0 
max = 10000
myRange = viz.XAxis.Range
```

![myImg](/img/capture.png/)
