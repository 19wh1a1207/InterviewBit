void Solution::merge(vector<int> &a, vector<int> &b) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int i=0,j=0;
    vector<int> result;
        while(i<a.size() && j<b.size()){
            if(a[i] < b[j]){
                cout<<a[i]<<" ";
                i++;
            }
            else{
                cout<<b[j]<<" ";
                j++;
            }
        }
        while(i<a.size()){
            cout<<a[i]<<" ";
            i++;
        }
        while(j<b.size()){
             cout<<b[j]<<" ";
             j++;
        }
        a.clear();
}
