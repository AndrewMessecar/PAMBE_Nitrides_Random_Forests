Andrew S. Messecar, 2023

This repository contains the training data and code used for the study published as "Machine learning-based investigation of optimal synthesis parameters for epitaxially-grown III-nitride semiconductors".

All training data sets are included as comma-separated value (CSV) files with identifying names inside of the "Data" folder.

Each row in every training data CSV file contains conventional plasma-assisted molecular beam epitaxy operating parameter values recorded during the epitaxial synthesis of either GaN or InN - depending on the data set - along with either a determination of crystallinity or a Bragg-Williams measure of lattice disorder (S^2) measured from each resulting sample. In this way, each row in the training data describes an individual III-nitride growth experiment, all performed inside of a single Perkin-Elmer 430 molecular beam epitaxy system. Included in the conventional operating parameter data are values for substrate temperature, solid metal (either gallium or indium) source effusion cell temperature, forward power applied to the radio frequency nitrogen plasma source, and the initial pressure of the nitrogen atmosphere within the growth chamber at the onset of deposition. The temperature values were measured from thermocouples and the initial nitrogen pressure values were measured from an ion gauge fixated inside of the growth chamber. Each sample was grown on a substrate attached to a solid molybdenum block; for the substrate temperature measurements, the thermocouple makes physical contact with the backside of the molybdenum block during growth. For the values of the metal source effusion cell temperatures, the thermocouple makes physical contact with the backside of a crucible containing the raw elemental material. During growth, the substrate is positioned 20cm away from the openings of the effusion cells. For the data included in this study, gallium was deposited from an effusion cell with a volume of 60 cubic centimeters.

Crystallinity was determined by visually inspecting reflection high-energy electron diffraction (RHEED) patterns acquired of the surface of the grown sample at the end of deposition. Growth experiments yielding RHEED patterns that displayed clear, prominent, parallel streaks indicative of monocrystallinity were given a value of "1" in the "Crystal" axis of the training data. RHEED patterns including dominating arch features characteristic of a polycrystalline surface warranted a "Crystal" value of "0" for the growth trial. Growth experiments resulting in amorphous samples were not included in this study. Measurements of the Bragg-Williams order parameter (S^2) for studying the lattice disorder of epitaxially-grown GaN samples were obtained from ex-situ scanning electron micrographs. The values for S^2 result from measurements performed in the style of Makin et al. (2020).

Every code script can be found organized in the "Code" directory.

The R scripts used for the calculation of p-values, the fitting and plotting of decision trees, and random forest algorithm design are saved in the "R" folder within "Code".

The Python scripts are organized into folders that identify the training data set that the scripts are written to be used for.

Included are the Python scripts used for generating the test data sets as well as the programs for training the random forest algorithms on the experimental data before making and plotting predictions using the previously generated test data.

Data points included in the training data for this study have also appeared in the following publications:

Anderson, P A, Kendrick, C. E., Kinsey, R. J., Kennedy, V. J., Markwitz, A., Reeves, R. J., &amp; Durbin, S. M. (2005). Optical and compositional properties of indium nitride grown by plasma assisted molecular beam epitaxy. Smart Materials and Structures, 15(1). https://doi.org/10.1088/0964-1726/15/1/014

Anderson, P. A., Kendrick, C. E., Kinsey, R. J., Asadov, A., Gao, W., Reeves, R. J., &amp; Durbin, S. M. (2005). (111) and (100) YSZ as substrates for indium nitride growth. Physica Status Solidi (c), 2(7), 2320–2323. https://doi.org/10.1002/pssc.200461336

Anderson, P. A., Reeves, R. J., &amp; Durbin, S. M. (2006). RF plasma sources for III‐nitrides growth: Influence of operating conditions and device geometry on active species production and InN film properties. Physica Status Solidi (a), 203(1), 106–111. https://doi.org/10.1002/pssa.200563502

Anderson, Phillip A. (2006). Indium nitride: An investigation of growth, electronic structure and doping (dissertation). University of Canterbury, Christchurch, New Zealand.

Christie, V. A., Liem, S. I., Reeves, R. J., Kennedy, V. J., Markwitz, A., &amp; Durbin, S. M. (2004). Characterisation of polycrystalline gallium nitride grown by plasma-assisted evaporation. Current Applied Physics, 4(2–4), 225–228. https://doi.org/10.1016/j.cap.2003.11.015

Kendrick, C. E. (2008). Revisiting nitride semiconductors: Epilayers, P-type doping and nanowires (dissertation). University of Canterbury, Christchurch, New Zealand.

Kennedy, J., Markwitz, A., Trodahl, H. J., Ruck, B. J., Durbin, S. M., &amp; Gao, W. (2007). Ion beam analysis of amorphous and Nanocrystalline Group III-V nitride and ZnO thin films. Journal of Electronic Materials, 36(4), 472–482. https://doi.org/10.1007/s11664-006-0051-y

Kinsey, R. J., Anderson, P. A., Kendrick, C. E., Reeves, R. J., &amp; Durbin, S. M. (2004). Characteristics of InN thin films grown using a PAMBE technique. Journal of Crystal Growth, 269(1), 167–172. https://doi.org/10.1016/j.jcrysgro.2004.05.046

Markwitz, A., Kennedy, V. J., Durbin, S. M., Johnson, P. B., Mücklich, A., &amp; Dytlewski, N. (2004). Depth profiling of light elements in pambe‐grown GaN and helium‐implanted titanium with heavy ion time‐of‐flight elastic recoil detection. Surface and Interface Analysis, 36(4), 317–322. https://doi.org/10.1002/sia.1691

Soldatov, A. V., Guda, A., Kravtsova, A., Petravic, M., Deenapanray, P. N. K., Fraser, M. D., Yang, Y.-W., Anderson, P. A., &amp; Durbin, S. M. (2006). Nitrogen Defect Levels in InN: Xanes study. Radiation Physics and Chemistry, 75(11), 1635–1637. https://doi.org/10.1016/j.radphyschem.2005.07.021
