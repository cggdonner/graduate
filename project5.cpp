// Catherine Donner
// DSA 5005
// Project 5

#include <iostream>
#include <stack>
#include <vector>
using namespace std;

template <class DT>
class ArrayBTNode
{
protected:
    // Instance Variables
    DT* _info;
    int _left;
    int _right;
public:
    // TODO: Overloaded Ostream Operator - Uses display method to output ArrayBTNode contents
    //template <class DT>
    friend ostream& operator << (ostream& s, ArrayBTNode<DT>& g) { // displays BTNode using ostream
        s << g.display();
        return s;
    } // could not have template <class DT>, debugging for autograder, same for ostream in ArrayBST
    // Constructors and Destructor
    ArrayBTNode(); // default
    ArrayBTNode(DT& info); // non default
    ~ArrayBTNode();
    // getter Methods
    DT* getinfo();
    int getleft();
    int getright();
    // setter Methods
    void setInfo(DT& info);
    void setInfoNull(); // Sets _info to Null
    void setLeft(int left);
    void setRight(int right);
    // Display Method
    // Outputs data in _info, _left, _right
    void display();
    // Overloaded Comparison Operators
    // Used for comparing _info field with other ArrayBTNodes
    bool operator<(ArrayBTNode<DT>& x); // no consts
    bool operator>(ArrayBTNode<DT>& x);
    bool operator==(ArrayBTNode<DT>& x);
    bool operator>=(ArrayBTNode<DT>& x);
    bool operator<=(ArrayBTNode<DT>& x);
    bool operator!=(ArrayBTNode<DT>& x);
};

//template <class DT>
//ostream& operator<< (ostream& s, ArrayBTNode<DT>& g) {
//    s << g.display();
//    return s;
//}

template <class DT>
ArrayBTNode<DT>::ArrayBTNode() {
    _info = NULL;
    _left = -1;
    _right = -1;
}

template <class DT>
ArrayBTNode<DT>::ArrayBTNode(DT &info) {
    _info = new DT(info);
    _left = -1;
    _right = -1;
}

template <class DT>
ArrayBTNode<DT>::~ArrayBTNode() {
    _info = NULL;
    _left = -1;
    _right = -1;
}

template <class DT>
DT* ArrayBTNode<DT>::getinfo() {
    return _info;
}

template <class DT>
int ArrayBTNode<DT>::getleft() {
    return _left;
}

template <class DT>
int ArrayBTNode<DT>::getright() {
    return _right;
}

template <class DT>
void ArrayBTNode<DT>::setInfo(DT& info) {
    delete _info;
    _info = new DT(info);
}

template <class DT>
void ArrayBTNode<DT>::setInfoNull() {
    _info = NULL;
}

template <class DT>
void ArrayBTNode<DT>::setLeft(int left) {
    _left = left;
}

template <class DT>
void ArrayBTNode<DT>::setRight(int right) {
    _right = right;
}

template <class DT>
void ArrayBTNode<DT>::display() {
    cout << "Info: " << *_info << ", Left : " << _left << ", Right : " << _right;
    //ArrayBTNode<DT> temp;
    //cout << "Info: " << *getinfo() << ", Left : " << getleft() << ", Right : " << getright();
}

template <class DT>
bool ArrayBTNode<DT>::operator<(ArrayBTNode<DT>& x) {
    return ((*_info) < *(x.getinfo()));
}

template <class DT>
bool ArrayBTNode<DT>::operator>(ArrayBTNode<DT>& x) {
    return ((*_info) > *(x.getinfo()));
}

template <class DT>
bool ArrayBTNode<DT>::operator==(ArrayBTNode<DT>& x) {
    return ((*_info) == *(x.getinfo()));
}

template <class DT>
bool ArrayBTNode<DT>::operator>=(ArrayBTNode<DT>& x) {
    return ((*_info) >= *(x.getinfo()));
}

template <class DT>
bool ArrayBTNode<DT>::operator<=(ArrayBTNode<DT>& x) {
    return ((*_info) <= *(x.getinfo()));
}

template <class DT>
bool ArrayBTNode<DT>::operator!=(ArrayBTNode<DT>& x) {
    return ((*_info) != *(x.getinfo()));
}

template <class DT>
class ArrayBST
{
protected:
    // Instance Variables
    vector<ArrayBTNode<DT>> _tree;    // Vector of ArrayBTNodes used to create a tree
    int _rootIndex;            // Index of the root node in _tree
    int _numNodes;             // Number of nodes in the tree
    int _size;                 // Maximum size of the _tree array
    stack<int> _freeLocations; // Stack containing indexes of freeLocations in the _tree array
public:
    // TODO: Overridden ostream operator for ArrayBST - this will call the pre order and in order methods
    //template <class DT>
    friend ostream& operator << (ostream& s, ArrayBST<DT>& t) { // displays pre order and in order methods
        t.display(s);
        return s;
    } 
    // Constructors and Destructor
    ArrayBST(); // default
    ArrayBST(int k); // initialize the vector with NULL nodes and fill the stack
    ~ArrayBST();
    // Accessor Methods
    bool isEmpty();
    int Height();
    int Size();
    int rootIndex(); // returns index of the root of the tree
    int maxSize();
    // Mutator Methods
    void setData(int index, DT& value);
    void setLeft(int index, int value);
    void setRight(int index, int value);
    // Display methods and traversals
    void display(ostream& os);
    void displayPreOrder(ostream& os); // displays root, left, right
    void _preOrder(int pos);
    void displayInOrder(ostream& os); // displays left, root, right
    void _inOrder(int pos);
    void printRaw(); // Display the array and all of its contents
    // BST Specific Methods
    void insert(DT& object); // inserts input node
    bool find(DT& object); // searches for input node
    bool _find(DT& object, int pos);
    int findIndex(DT& object); // finds index of the searched for node
    void remove(DT& object); // extra credit
};

//template <class DT>
//ostream& operator<< (ostream& s, ArrayBST<DT>& t) {
//    
//}

template <class DT>
ArrayBST<DT>::ArrayBST() {
    //_tree = 0;
    _rootIndex = -1;
    _numNodes = 0;
    _size = 0;
    //freeLocations = 0;
}

template <class DT>
ArrayBST<DT>::ArrayBST(int k) {
    _tree.reserve(k);
    _rootIndex = k - 1;
    _numNodes = 0;
    _size = k;
    for (int i = 0; i < k; i++) {
        _freeLocations.push(i);
        _tree.push_back(ArrayBTNode<DT>());
    }
}

template <class DT>
ArrayBST<DT>::~ArrayBST() {
    //_tree = NULL;
    _rootIndex = -1;
    _numNodes = 0;
    _size = 0;
    //freeLocations = NULL;
}

template <class DT>
bool ArrayBST<DT>::isEmpty() {
    return _tree.empty(); // returns if _tree is empty or not, debugging for autograder
}

template <class DT>
int ArrayBST<DT>::Height() {
    int intheight = 0;
    int leftheight;
    int height;

    for (int i = 0; i < _size; i++) {
        if (!isEmpty()) {
            if (_tree[i].getleft() == NULL) {
                leftheight = 0;
            }
            else {
                leftheight = _tree.Height(); //[i].getleft()
            }
            if (_tree[i].getright() == NULL) {
                height = 1 + leftheight;
            }
            else {
                height = 1 + max(leftheight, _tree.Height()); //[i].getright()
            }
        }
    }
    return height;
}

template <class DT>
int ArrayBST<DT>::Size() {
    int size = 0;
    int leftsize;
    
    for (int i = 0; i < _size; i++) {
        if (!isEmpty()) {
            if (_tree[i].getleft() == NULL) {
                leftsize = 0;
            }
            else {
                leftsize = _tree.Size(); //[i].getleft()
            }
            if (_tree[i].getright() == NULL) {
                size = 1 + leftsize;
            }
            else {
                size = 1 + leftsize + _tree.Size(); //[i].getright()
            }
        }
    }
    return size;
}

template <class DT>
int ArrayBST<DT>::rootIndex() {
    return _rootIndex; // returns the index of the root, debugging for autograder
}

template <class DT>
int ArrayBST<DT>::maxSize() {
    return _tree.Size();
}

template <class DT>
void ArrayBST<DT>::setData(int index, DT& value) {
    _tree[index].setInfo(value);
}

template <class DT>
void ArrayBST<DT>::setLeft(int index, int value) {
    _tree[index].setLeft(value);
}

template <class DT>
void ArrayBST<DT>::setRight(int index, int value) {
    _tree[index].setRight(value);
}

template <class DT>
void ArrayBST<DT>::display(ostream& os) {
    os << "Information in Tree:" << endl;
    displayPreOrder(os);
    cout << "\n";
    displayInOrder(os);
    cout << "\n";
}

template <class DT>
void ArrayBST<DT>::_preOrder(int pos) {
    cout << *(_tree[pos].getinfo()) << " ";
    if (_tree[pos].getleft() != -1) {
        _preOrder(_tree[pos].getleft());
    }
    if (_tree[pos].getright() != -1) {
        _preOrder(_tree[pos].getright());
    } 
}

template <class DT>
void ArrayBST<DT>::displayPreOrder(ostream& os) {
    os << "Pre Order Traversal:" << endl;
    _preOrder(_rootIndex);
}

template <class DT>
void ArrayBST<DT>::_inOrder(int pos) {
    if (_tree[pos].getleft() != -1) {
        _inOrder(_tree[pos].getleft());  
    }
    cout << *(_tree[pos].getinfo()) << " ";
    if (_tree[pos].getright() != -1) {
        _inOrder(_tree[pos].getright());
    }
}

template <class DT>
void ArrayBST<DT>::displayInOrder(ostream& os) {
    os << "In Order Traversal:" << endl;
    _inOrder(_rootIndex);
}

template <class DT>
void ArrayBST<DT>::printRaw() {
    cout << "Raw Data:" << endl;
    for (int i = 0; i < _size; i++) {
        if (_tree[i].getinfo() == NULL) {
            continue;
        }
        else {
            cout << "Index " << i << ": ";
            _tree[i].display();
        }
        cout << "\n";
    }
    stack<int> tempStack = _freeLocations; // to prevent code from crashing
    cout << "Free Indexes:" << endl;
    if (!(tempStack.empty())) {
        while (!(tempStack.empty()) && tempStack.top() >= 1) {
            cout << tempStack.top() << ", ";;
            tempStack.pop();
        }
        cout << "0"; // could not print comma after 0, debugging for autograder
    }
    else {
        cout << "None" << endl;
        return;
    }
    cout << "\n";
}

template <class DT>
void ArrayBST<DT>::insert(DT& object) {
    //Check size and numNodes
    if (_numNodes >= _size) {
        cout << "Cannot insert data, BST Full." << endl;
    }
    
    else {
        int freeIndex = _freeLocations.top();
        _freeLocations.pop();
        _numNodes++;
        _tree[freeIndex].setInfo(object);

        int curIndex = _rootIndex;
        if (_rootIndex != freeIndex) {
            while (true) {
                if (_tree[curIndex] > _tree[freeIndex]) {
                    if (_tree[curIndex].getleft() == -1) {
                        _tree[curIndex].setLeft(freeIndex);
                        break;
                    }
                    else {
                        curIndex = _tree[curIndex].getleft();
                    }
                }
                else {
                    if (_tree[curIndex].getright() == -1) {
                        _tree[curIndex].setRight(freeIndex);
                        break;
                    }
                    else {
                        curIndex = _tree[curIndex].getright();
                    }
                }
            }
        }
    }
}

template <class DT>
bool ArrayBST<DT>::find(DT& object) {
    return _find(object, rootIndex());
}

template <class DT>
bool ArrayBST<DT>::_find(DT& object, int pos) {
    if (*(_tree[pos].getinfo()) == object) { return true; }
    if (*(_tree[pos].getinfo()) < object) {
        if (_tree[pos].getright() != -1) {
            return _find(object, _tree[pos].getright());
        }
        return false;
    }
    else {
        if (_tree[pos].getleft() != -1) {
            return _find(object, _tree[pos].getleft());
        }
        return false;
    }
}

template <class DT>
int ArrayBST<DT>::findIndex(DT& object) {
    int findIndex = _rootIndex;  
    while (findIndex != -1) {
        if (*(_tree[findIndex].getinfo()) == object) {
            return findIndex;
        }
        if (*(_tree[findIndex].getinfo()) < object) {
            findIndex = _tree[findIndex].getright();
        }
        if (*(_tree[findIndex].getinfo()) > object) {
            findIndex = _tree[findIndex].getleft();
        }
    }
    return findIndex; // had to return a value, debugging for autograder
}

template <class DT>
void ArrayBST<DT>::remove(DT& object) {
    /*int pos;
    if (_tree.setLeft(pos, object).isEmpty()) {
        delete _tree.setLeft(pos, object);
        ArrayBST<DT> temp = _tree.setRight(pos, object);
        _tree.copyTree(temp);
        temp.setNull();
        delete temp;
    }
    else if (_tree.setRight(pos, object).isEmpty()) {
        delete _tree.setRight(pos, object);
        ArrayBST<DT> temp = _tree.setLeft(pos, object);
        _tree.copyTree(temp);
        temp.setNull();
        delete temp;
    }
    else {
        ArrayBST<DT> temp = _tree.setRight(pos, object);
        while (!temp.setLeft(pos, object).isEmpty()) temp = temp.setLeft(pos, object);
        _tree.setInfo(pos, object) = temp.setInfo(pos, object);
        delete temp.setLeft(pos, object);
        if (temp.setRight(pos, object).isEmpty()) {
            delete temp.setRight(pos, object);
            temp.setNull();
        }
        else {
            ArrayBST<DT> temp2 = temp.setRight(pos, object);
            temp.copyTree(temp.setRight(pos, object));
            temp2.setNull();
            delete temp2;
        }
    }*/
}

int main()
{
    // Get input for the size of the tree
    int inputSize;
    int rootInfo;
    cin >> inputSize;
    cout << "Number of maximum nodes: " << inputSize << endl;
    cout << "\n";
    // Create a BST of the size inputSize
    ArrayBST<int> myBST = ArrayBST<int>(inputSize);
    // TODO: input loop for commands
    char command;
    cin >> command;
    while (!cin.eof()) {
        switch (command) {
        case 'I': {
            cin >> rootInfo;
            cout << "Inserting " << rootInfo << endl;
            myBST.insert(rootInfo); // insert the input node
            cout << "\n";
            break;
        }
        //case 'R': {
        //    cin >> rootInfo;
            //cout << "Removing " << rootInfo << endl;
            //myBST.remove(rootInfo);
        //    break;
        //}
        case 'F': {
            cin >> rootInfo;
            cout << "Finding " << rootInfo << endl;
            if (myBST.find(rootInfo) == true) { // if the node found is true, then output the index where it is found
                cout << "Number found at index " << myBST.findIndex(rootInfo) << "." << endl;
            }
            else {
                cout << "Number not found." << endl;
            }
            cout << "\n";
            break;
        }
        case 'O': {
            cout << myBST; // overriden ostream to display the tree
            cout << "\n";
            break;
        }
        case 'A': {
            myBST.printRaw(); // prints raw data including index, info, left, and right
            cout << "\n";
            break;
        }
        default:
            cout << "Hello World" << endl;
            break;
        }
        cin >> command;
    }
    return 0;
}
