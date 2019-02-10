#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>


using namespace cv;
using namespace std;

Mat& Average(Mat& I, int th);


int main( int argc, char* argv[]) {

  if (argc < 2) {
    cout << "Not enough parameters" << endl;
    return -1;
  }

  Mat I;
  Mat O(1005, 7707, CV_8UC3, Scalar(0,0,0));

  ifstream file_names;
  file_names.open (argv[1]);
  string line;

  int i = 0;
  if (file_names.is_open()) {

    while ( getline (file_names,line) ) {

      I = imread("./T152_Full/"+line, IMREAD_COLOR);
    
      if (!I.data) {
        cout << "The image: " << "/T152_Full/"+line << " could not be loaded." << endl;
        return -1;
      }
      // cout << I.cols << "\n";
      // cout << O.cols << "\n";

      I.row(1200).copyTo(O.row(i));

      i++;
      
    }
    file_names.close();
  imwrite("./slice/test.tif", O);

  }

  // int th = stoi(argv[1]);


  
  
  // imwrite("./slice/"+string(argv[2]), O);

 
  return 0;
}

/*
  Iterates over binary image (0 or 255)
  stops at any 255 pixel and begins search for neighbors
  if number of neighbors is below a threhsold will set pixel to 0
*/
Mat& GenerateSlices(Mat& I, int th) {

  
}

