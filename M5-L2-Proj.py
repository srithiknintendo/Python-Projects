class Circle {
    float r;
public:
    Circle(float radius) { r = radius; }
    float area() { return 3.14f * r * r; }
    float perimeter() { return 2 * 3.14f * r; }
};