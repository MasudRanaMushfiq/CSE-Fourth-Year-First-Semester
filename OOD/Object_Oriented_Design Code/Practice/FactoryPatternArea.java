public class FactoryPatternArea {

    public static void main(String[] args) {

        ShapeFactory factory = new ShapeFactory();

        Shape circle = factory.getShape("circle");
        Shape rectangle = factory.getShape("rectangle");
        Shape triangle = factory.getShape("triangle");

        circle.draw();
        System.out.println("Area = " + circle.getArea());
        System.out.println();

        rectangle.draw();
        System.out.println("Area = " + rectangle.getArea());
        System.out.println();

        triangle.draw();
        System.out.println("Area = " + triangle.getArea());
    }
}


/* ================= FACTORY ================= */

class ShapeFactory {

    public Shape getShape(String type) {

        if (type == null) return null;

        switch (type.toLowerCase()) {

            case "circle":
                return new Circle();

            case "rectangle":
                return new Rectangle();

            case "triangle":
                return new Triangle();

            default:
                System.out.println("Invalid shape type");
                return null;
        }
    }
}


/* ================= INTERFACE ================= */

interface Shape {
    void draw();
    double getArea();
}


/* ================= CIRCLE ================= */

class Circle implements Shape {

    private double radius = 1;   // default value

    @Override
    public void draw() {
        System.out.println("Circle");
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
}


/* ================= RECTANGLE ================= */

class Rectangle implements Shape {

    private double width = 2;
    private double height = 1.5;

    @Override
    public void draw() {
        System.out.println("Rectangle");
    }

    @Override
    public double getArea() {
        return width * height;
    }
}


/* ================= TRIANGLE ================= */

class Triangle implements Shape {

    // default sides
    private double a = 3;
    private double b = 4;
    private double c = 5;

    @Override
    public void draw() {
        System.out.println("Triangle");
    }

    // Heron's formula
    @Override
    public double getArea() {
        double s = (a + b + c) / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}
