# star-track

### Addressing Track The Stardust

### Created by star-track
* Zak Aroui: ZakAroui
* Matt Casey: MattMCasey
* Max Gribov: mgribov
* Emma Jablonski: emmajab
* Sarah Mathew: sarahmathew
* Michael Saunders: pluto8195
* Madelyne Xiao: madelyne

### Solution Description

In order to calculate the metrics for the stardust, we needed to generate accurate trails. At first we tried to binarize the data but there was too much noise. This issue also affected our attempt to find edges in the picture. We then decided to denoise the data through multiple steps. We used a blue threshold filter, a standard deviation filter, and an average filter. These filters, used in order, work well to reduce noise in the first data set. The second data set still has background noise so the thresholds/parameters could be tweaked more. We then created two kinds of resulting data. One is a 2D stack (a single 2D picture) of the data to calculate some desired metrics. The other is the slices of data with their trails filled in. To create filled trails, we extracted points in the data and then connected them to form an outline. Future work includes using a GPU for some image processing functions because the data has ~12 million points per picture. It also includes generating image slices from the x and y directions to get a better view for some metrics such as the radius of entry area.

### Installation Instructions

You must list by name all software packages, APIs, frameworks, databases, or any other tools or libraries you used.

You must also provide any step-by-step instructions for installation of your solution.

The following steps are for MacOS systems
* Step one - install Xcode, OpenCV for C++ and Python3, pkg-config (through homebrew), Python's numpy library (through pip)
* Step two - 
    1. <https://www.learnopencv.com/install-opencv-4-on-macos/> -- follow this to install the most recent packages for OpenCV on MacoS
    2. <https://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/> -- use this to link OpenCV to python3
    3. <https://medium.com/@jaskaranvirdi/setting-up-opencv-and-c-development-environment-in-xcode-b6027728003> -- how to compile OpenCV with C++ on MacOS
* Step three - system administration notes ????
* Step four - 
    * To compile the C++ average filter code:
        1. g++ $(pkg-config --cflags --libs opencv4) -std=c++11 average.cpp -o average
        2. ./average
    * scripts in order
        1. blueChannelReduction.py
        2. stdBinarization.py
        3. averageFilter.py
        4. fill-image.py
        5. kmeans_centroids.py /path/to/clean/images

[track_the_stardust]: https://github.com/amnh/HackTheSolarSystem/wiki/Track-The-Stardust
