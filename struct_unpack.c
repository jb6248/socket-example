#include <stdio.h>

// define an equivalent struct as in python
typedef struct Point {
    double x;
    double y;
    // note timestamp time.
    // assuming you want sub-second measurements you'll need a floating point type
    // of some sort
    double timestamp;
} point;

int main () {
    // define an example point
    point x = {
        .x = 230.,
        .y = 50.,
        .timestamp = 20000123.02,
    };
    // cast the data to a void pointer! (this discards the type association)
    void* vp = &x;
    // since you'll be receivinig some sort of buffer of data, you'll have an array
    // of `sizeof(point)` bytes containinig this data
    // then you can cast the array identifier to void*
    // the point is, you can cast any reference to void*

    // cast as a point (this merely re-interprets the bytes as if it occupied
    // the same space as an actual point object)
    point y = (point)(*vp);

    // print the values
    printf("%f, %f, %f\n", y.x, y.y, y.timestamp);

    // prints "230.000000, 50.000000, 20000123.020000" in this case
}
