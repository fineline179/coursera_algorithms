// TODO: finish
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  ifstream inFile("knapsack1.txt", ios::in);

  // read in header data
  int knapSize;
  int numItems;
  cout << "KnapSize " << "NumItems" << endl;
  inFile >> knapSize >> numItems;
  cout << knapSize << " " << numItems;
  cout << endl << endl;

  // read in value/weight data
  vector<int> values;
  vector<int> weights;
  
  int currVal;
  int currWeight;

  while (inFile >> currVal >> currWeight)
  {
    values.push_back(currVal);
    weights.push_back(currWeight);
    cout << currVal << " " << currWeight << endl;
  }

  return 0;
}
