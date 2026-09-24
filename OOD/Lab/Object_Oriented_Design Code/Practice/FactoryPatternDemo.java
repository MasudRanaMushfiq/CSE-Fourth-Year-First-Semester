public class FactoryPatternDemo {
    public static void main(String[] args) {

        ShapeFactory shapeFactory = new ShapeFactory();

        Shape shape1 = shapeFactory.getShape("circle", 2);

        shape1.draw();
        System.out.println("Area = " + shape1.area());
    }
}

class ShapeFactory {

    public Shape getShape(String shapeType, double radius) {

        if (shapeType == null) return null;

        if (shapeType.equalsIgnoreCase("circle")) {
            return new Circle(radius);
        }

        return null;
    }
}

interface Shape {
    void draw();
    double area();
}

class Circle implements Shape {

    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public void draw() {
        System.out.println("Circle");
    }

    @Override
    public double area() {
        return Math.PI * 2 * radius;
    }
}
