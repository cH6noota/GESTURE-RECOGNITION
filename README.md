

<h1>GESTURE RECOGNITION </h1>

<h2>1. Execution environment</h2>

macOS High Sierra 10.13.6<br>
Python　3.6.0<br>
LOGICOOL Webcamera<br>
Google Colaboratory<br>
Raspbian GNU/Linux9<br>

<h2>2. Data creation</h2>
<p>python testdata_get.py<br>
About labels</p>
<table>
  <tr>
    <td>label name</td>
    <td>number</td>
  </tr>
  <tr>
    <td>Go to the left</td>
    <td>1</td>
  </tr>
  <tr>
    <td>Go to the right</td>
    <td>2</td>
  </tr>
  <tr>
    <td>Counterclockwise</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Clockwise</td>
    <td>4</td>
  </tr>
  <tr>
    <td>Error</td>
    <td>5</td>
  </tr>
</table>
<p>Image padding　... generator.py<br>
  Make label ... make_label.py </p>

<h2>3. Learning</h2>
<p>python svc.py</p>

<h2>4. Predictive execution</h2>
<p>example ... pred.py <br>
  On the device ... main.py </p>


