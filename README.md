Andrew S. Messecar, 2023

This repository contains the training data and code used for the study published as "Machine learning-based investigation of optimal synthesis parameters for epitaxially-grown III-nitride semiconductors".

All training data sets are included as comma-separated value (CSV) files with identifying names inside of the "Data" folder.

Each row in every training data CSV file contains conventional plasma-assisted molecular beam epitaxy operating parameter values recorded during the epitaxial synthesis of either GaN or InN - depending on the data set - along with either a determination of crystallinity or a Bragg-Williams measure of lattice disorder (S^2) measured from each resulting sample. In this way, each row in the training data describes an individual III-nitride growth experiment, all performed inside of a single Perkin-Elmer 430 molecular beam epitaxy system. Included in the conventional operating parameter data are values for substrate temperature, solid metal (either gallium or indium) source effusion cell temperature, forward power applied to the radio frequency nitrogen plasma source, and the initial pressure of the nitrogen atmosphere within the growth chamber at the onset of deposition. The temperature values were measured from thermocouples and the initial nitrogen pressure values were measured from an ion gauge fixated inside of the growth chamber. Each sample was grown on a substrate attached to a solid molybdenum block; for the substrate temperature measurements, the thermocouple makes physical contact with the backside of the molybdenum block during growth. For the values of the metal source effusion cell temperatures, the thermocouple makes physical contact with the backside of a crucible containing the raw elemental material.

Crystallinity was determined by visually inspecting reflection high-energy electron diffraction (RHEED) patterns acquired of the surface of the grown sample at the end of deposition. Growth experiments yielding RHEED patterns that displayed clear, prominent, parallel streaks indicative of monocrystallinity were given a value of "1" in the "Crystal" axis of the training data. RHEED patterns including dominating arch features characteristic of a polycrystalline surface warranted a "Crystal" value of "0" for the growth trial. Growth experiments resulting in amorphous samples were not included in this study. Measurements of the Bragg-Williams order parameter (S^2) for studying the lattice disorder of epitaxially-grown GaN samples were obtained from ex-situ scanning electron micrographs. The values for S^2 result from measurements performed in the style of Makin et al. (2020).

Every code script can be found organized in the "Code" directory.

The R scripts used for the calculation of p-values, the fitting and plotting of decision trees, and random forest algorithm design are saved in the "R" folder within "Code".

The Python scripts are organized into folders that identify the training data set that the scripts are written to be used for.

Included are the Python scripts used for generating the test data sets as well as the programs for training the random forest algorithms on the experimental data before making and plotting predictions using the previously generated test data.
