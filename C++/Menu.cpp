#include <iostream>
using std::cin;
using std::cout;
using std::endl;
int main(void)
{
    int num1;

    while (true)
    {
        cout << "--------<Menu>--------" << endl;
        cout << "1.  Menu item1" << endl;
        cout << "2.  Menu item2" << endl;
        cout << "3.  Menu item3" << endl;
        cout << "0.  Exit" << endl;
        cout << "----------------------" << endl;
        cout << "Your choice>>";
        cin >> num1;

        switch (num1)
        {
        case 1:
            cout << "Menu item1 is selected" << endl;
            break;
        case 2:
            cout << "Menu item2 is selected" << endl;
            break;
        case 3:
            cout << "Menu item3 is selected" << endl;
            break;
        case 0:
            return 0;
        default:
            cout << "no such menu item" << endl;
        }
    }
    return 0;
}