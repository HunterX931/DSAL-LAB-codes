#include <iostream>
#include <cstring>   // for strcmp
#include <algorithm> // for max()
using namespace std;

typedef struct student {
    int roll_num;
    char name[20];
    float marks;
} stud;

void create(stud s[20], int n);
void display(stud s[20], int n);
void bubble_sort(stud s[20], int n);
void insertionSort(stud s[20], int n);
void quick_sort(stud s[20], int, int);
int partition(stud s[20], int, int);
void search(stud s[20], int n, float key);
int bsearch(stud s[20], char x[20], int low, int high);

int main() {
    stud s[20];
    int ch, n = 0, result;
    float key;
    char x[20];

    do {
        cout << "\n\n--- Student Database Menu ---";
        cout << "\n 1) Create Student Database";
        cout << "\n 2) Display Student Records";
        cout << "\n 3) Bubble Sort (by Roll No)";
        cout << "\n 4) Insertion Sort (by Name)";
        cout << "\n 5) Quick Sort (by Marks)";
        cout << "\n 6) Linear Search (by Marks)";
        cout << "\n 7) Binary Search (by Name)";
        cout << "\n 8) Exit";
        cout << "\n Enter Your Choice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cout << "\n Enter the number of records: ";
                cin >> n;
                create(s, n);
                break;

            case 2:
                display(s, n);
                break;

            case 3:
                bubble_sort(s, n);
                cout << "\nRecords Sorted by Roll Number:\n";
                display(s, n);
                break;

            case 4:
                insertionSort(s, n);
                cout << "\nRecords Sorted by Name:\n";
                display(s, n);
                break;

            case 5:
                quick_sort(s, 0, n - 1);
                cout << "\nTop Students by Marks:\n";
                cout << "\tRoll No\tName\t\tMarks";
                for (int i = n - 1; i >= max(0, n - 10); i--) {
                    cout << "\n\t" << s[i].roll_num << "\t" << s[i].name << "\t\t" << s[i].marks;
                }
                break;

            case 6:
                cout << "\n Enter the marks to search: ";
                cin >> key;
                search(s, n, key);
                break;

            case 7:
                cout << "\n Enter the name to search: ";
                cin >> ws; // consume whitespace
                cin.getline(x, 20);
                insertionSort(s, n); // ensure sorted by name before searching
                result = bsearch(s, x, 0, n - 1);
                if (result == -1) {
                    cout << "\n Name not found!";
                } else {
                    cout << "\n Student found:\n";
                    cout << "\tRoll No: " << s[result].roll_num;
                    cout << "\n\tName: " << s[result].name;
                    cout << "\n\tMarks: " << s[result].marks;
                }
                break;

            case 8:
                cout << "\nExiting program.\n";
                return 0;

            default:
                cout << "\n Invalid choice! Please try again.";
        }
    } while (ch != 8);

    return 0;
}

//-------------------------------------
void create(stud s[20], int n) {
    for (int i = 0; i < n; i++) {
        cout << "\nEnter details for student " << i + 1 << ":";
        cout << "\n Roll number: ";
        cin >> s[i].roll_num;
        cout << " Name: ";
        cin >> ws;
        cin.getline(s[i].name, 20);
        cout << " Marks: ";
        cin >> s[i].marks;
    }
}

//-------------------------------------
void display(stud s[20], int n) {
    cout << "\n\tRoll No\tName\t\tMarks";
    cout << "\n\t--------------------------------";
    for (int i = 0; i < n; i++) {
        cout << "\n\t" << s[i].roll_num << "\t" << s[i].name << "\t\t" << s[i].marks;
    }
    cout << "\n";
}

//-------------------------------------
void bubble_sort(stud s[20], int n) {
    stud temp;
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            if (s[j].roll_num > s[j + 1].roll_num) {
                temp = s[j];
                s[j] = s[j + 1];
                s[j + 1] = temp;
            }
        }
    }
}

//-------------------------------------
void insertionSort(stud s[20], int n) {
    stud key;
    int j;
    for (int i = 1; i < n; i++) {
        key = s[i];
        j = i - 1;
        while (j >= 0 && strcmp(s[j].name, key.name) > 0) {
            s[j + 1] = s[j];
            j--;
        }
        s[j + 1] = key;
    }
}

//-------------------------------------
void quick_sort(stud s[20], int l, int u) {
    int j;
    if (l < u) {
        j = partition(s, l, u);
        quick_sort(s, l, j - 1);
        quick_sort(s, j + 1, u);
    }
}

int partition(stud s[20], int l, int u) {
    stud v = s[l], temp;
    int i = l, j = u + 1;

    do {
        do { i++; } while (i <= u && s[i].marks < v.marks);
        do { j--; } while (s[j].marks > v.marks);

        if (i < j) {
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    } while (i < j);

    s[l] = s[j];
    s[j] = v;
    return j;
}

//-------------------------------------
void search(stud s[20], int n, float key) {
    bool found = false;
    cout << "\n\tRoll No\tName\t\tMarks";
    for (int i = 0; i < n; i++) {
        if (s[i].marks == key) {
            found = true;
            cout << "\n\t" << s[i].roll_num << "\t" << s[i].name << "\t\t" << s[i].marks;
        }
    }
    if (!found) {
        cout << "\n No student found with marks = " << key;
    }
}

//-------------------------------------
int bsearch(stud s[20], char x[20], int low, int high) {
    int mid;
    while (low <= high) {
        mid = (low + high) / 2;
        int cmp = strcmp(x, s[mid].name);
        if (cmp == 0)
            return mid;
        else if (cmp < 0)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}

