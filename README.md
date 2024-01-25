# De-Casteljau-Bezier-curve-drawer
A simple Bezier curve drawer made by utilizing De Casteljau's algorithm on tkinter. Using it is easy, just left click where you want the control points to be and the curve will be drawn based on that. Click space to restart.

![SharedScreenshot](https://github.com/Gatito7218/De-Casteljau-Bezier-curve-drawer/assets/156482606/b3256aa8-b299-4823-a762-643f5d27e0c8)

![Bernstein](https://github.com/Gatito7218/De-Casteljau-Bezier-curve-drawer/assets/156482606/deec2bf7-70af-40c0-b6ad-d8f166e94384)

(Formulas are straight from the wikipedia page for De Casteljau's algo)
First formula is for calculating the curve, with beta being the control points and n being the degrees.
Second formula is the Bernstein basis polynomial, which gets multiplied by beta and summed.

Information for implementing binomial coefficient into python pulled form here: https://stackoverflow.com/questions/26560726/python-binomial-coefficient
