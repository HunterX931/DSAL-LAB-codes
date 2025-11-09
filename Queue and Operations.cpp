#include <iostream>
using namespace std;

int cqueue[5];
int front = -1, rear = -1, n = 5;

//===================================================================
// INSERT ELEMENT INTO CIRCULAR QUEUE
void insertCQ(int val) {
    if ((front == 0 && rear == n - 1) || (front == rear + 1)) {
        cout << "Queue Overflow\n";
        return;
    }
    if (front == -1) {  // First element
        front = 0;
        rear = 0;
    } else if (rear == n - 1)
        rear = 0;
    else
        rear++;

    cqueue[rear] = val;
    cout << "Inserted: " << val << endl;
}

//===================================================================
// DELETE ELEMENT FROM CIRCULAR QUEUE
void deleteCQ() {
    if (front == -1) {
        cout << "Queue Underflow\n";
        return;
    }
    cout << "Element deleted from queue is: " << cqueue[front] << endl;

    if (front == rear) {
        // Queue becomes empty
        front = -1;
        rear = -1;
    } else if (front == n - 1)
        front = 0;
    else
        front++;
}

//===================================================================
// DISPLAY ELEMENTS IN FORWARD DIRECTION
void displayCQ_forward() {
    if (front == -1) {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Queue elements (forward): ";
    int f = front;
    if (front <= rear) {
        while (f <= rear)
            cout << cqueue[f++] << " ";
    } else {
        while (f <= n - 1)
            cout << cqueue[f++] << " ";
        f = 0;
        while (f <= rear)
            cout << cqueue[f++] << " ";
    }
    cout << endl;
}

//===================================================================
// DISPLAY ELEMENTS IN REVERSE DIRECTION
void displayCQ_reverse() {
    if (front == -1) {
        cout << "Queue is empty\n";
        return;
    }

    cout << "Queue elements (reverse): ";
    int r = rear;
    if (front <= rear) {
        while (r >= front)
            cout << cqueue[r--] << " ";
    } else {
        while (r >= 0)
            cout << cqueue[r--] << " ";
        r = n - 1;
        while (r >= front)
            cout << cqueue[r--] << " ";
    }
    cout << endl;
}

//===================================================================
// MAIN FUNCTION WITH MENU
int main() {
    int ch, val;

    cout << "1) Insert\n";
    cout << "2) Delete\n";
    cout << "3) Display Forward\n";
    cout << "4) Display Reverse\n";
    cout << "5) Exit\n";

    do {
        cout << "\nEnter choice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cout << "Input value to insert: ";
                cin >> val;
                insertCQ(val);
                break;

            case 2:
                deleteCQ();
                break;

            case 3:
                displayCQ_forward();
                break;

            case 4:
                displayCQ_reverse();
                break;

            case 5:
                cout << "Exiting program.\n";
                break;

            default:
                cout << "Invalid choice! Try again.\n";
        }
    } while (ch != 5);

    return 0;
}

