# T2 Index Evaluation
## Description

This Python script generates a grouped bar chart visualising the development of the T2 index over time after surgery, based on the cartilage zones ("deep," "global," and "superficial") as described by Trattnig et al. (2015). The T2 index provides insights into cartilage repair quality, with a 95% confidence interval (CI) as a measure of uncertainty.
The data used includes post-surgery measurements at various time points (e.g., 12, 18, and 24 months) with an early post-surgery reference at 1 week. Error bars represent the 95% CI for the mean T2 index values, and the number of observations per category is displayed directly on the bars.
The chart is divided into three cartilage zones for comparison, using distinct colors to differentiate between them, facilitating the assessment of cartilage repair outcomes over time.

**PLEASE NOTE:** THIS CODE IS FOR EDUCATIONAL PURPOSES ONLY.

Datasource:
Trattnig, S., Ohel, K., Mlynarik, V., Juras, V., Zbyn, S., & Korner, A. (2015). Morphological and compositional monitoring of a new cell-free cartilage repair hydrogel technology – GelrinC by MR using semi-quantitative MOCART scoring and quantitative T2 index and new zonal T2 index calculation. Osteoarthritis and Cartilage, 23(12), 2224–2232. https://doi.org/10.1016/j.joca.2015.07.007

## Application Overview
![picture_1](https://github.com/user-attachments/assets/99afb8ba-646c-41ed-832d-f59b9a845990)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and the provided requirments.txt file to install this script.

```bash
pip install -r /path/to/requirements.txt
`````

## Usage

1. Download of all necessary files (main.py, requirements.txt)
2. Install necessary libraries on your local environment or virtual environment via the requirement.txt
3. Run application

## Contributing

Pull requests are welcome! For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Licenses
This script uses the [MIT](https://choosealicense.com/licenses/mit/) License.
